import webapp2

from google.appengine.api import urlfetch

from google.appengine.ext import db
from google.appengine.ext import ndb

from datetime import timedelta

import urllib,re,datetime,string,sys,os

import mysession

from flights import *


# CLASSES FOR THIS PROJECT ARE IN ndbstore.py
# JUST REFERENCE BY THEIR NAME
from ndbstore import *
#import ndbstore


def Writeln( selfobj, *t):
   for x in t:
     selfobj.response.out.write(x )
     selfobj.response.out.write(" ")

   selfobj.response.out.write("<br>")

def Write( selfobj, *t):
   for x in t:
     selfobj.response.out.write(x )
     selfobj.response.out.write(" ")

def getTeams( leagueid ,limit):

      url  = "http://www.ustanorcal.com/standings.asp?l="+ str(leagueid)
      print "get teams at " + url

      result = urlfetch.fetch(url)
      s = result.content
      s = s.replace("\r","")      
      s = s.replace("\n","")      
      scraped = s.replace("\t","")      

#     print scraped

      pTeamName = r"([ ,.#\d\w\+\/\-\[\]\!\"\:\'\&\?\(\)]*)"
      pName = r"([ .\d\w\/\-']*)"

#      pattern = r"<td>[ ]*"   #bunch of spaces follow this first <td>
#      pattern = r'<span a href="TeamInfo.asp\?id=([\d]*)">'  + pTeamName   + "[ ]*</a>[ ]*</td>"
#      pattern = r'<span([^~]*?)</span>'   # position


      pattern = r'<span class="standing_position">' + "[\.\d]*" + '</span>' + '[ ]*'    # to prevent overflowing into playoffs

      pattern += r'<a href="TeamInfo.asp\?id=([\d]*)">'  + pTeamName   + "[ ]*</a>[ ]*</td>"

      pattern += r'<td([^~]*?)</td>'   #captain

      pattern += r'<td([^~]*?)</td>'   #send email
      pattern += r'<td([^~]*?)</td>'   #win

      pattern += r'<td([^~]*?)</td>'   #loss

      r = re.compile(pattern,re.IGNORECASE )
      match = r.findall( scraped )


      teams = []
      for i,m in enumerate(match):

         _teamid = m[0]
         _teamname = m[1]
         _captainid = m[2]
         _captain = m[2]
#        skip Email column
         _win = m[4]
         _loss = m[5]

         r1 = re.search(r"playermatches.asp\?id=([\d]*)>"+pName,_captainid)

         if( r1 != None ):
              _captainid = r1.group(1)
              _captain = r1.group(2)

         r3 = re.search(r">([\d]{1,3})",_win)

         r4 = re.search(r">([\d]{1,3})",_loss)

         if( r3 != None ):
              _win = r3.group(1)


         if( r4 != None ):
              _loss = r4.group(1)


#        print i,_teamid, _teamname ,_captainid, _captain , _won, _loss
#        teams.append([ i,_teamid, _teamname ,_captainid, _captain , _won, _loss] )
#         t = Team(i,_teamid , _teamname, _captainid,_captain, "area", _won, _loss,"playoff")
         t = Team()
         t.order = int(i)
         t.teamid = _teamid
         t.teamname = _teamname
         t.captainid = _captainid
         t.captain = _captain


         t.win = int(_win)
         t.loss = int(_loss)

         teams.append( t  )

      return teams


def saveTeams( flightid ,teams):
      print "save teams"
      flightKey = ndb.Key(Flight, str(flightid))
      o = flightKey.get()
      if o == None :
         print "flight doesnt exist "
         o = Flight( key = flightKey)
         o.teams = teams
         o.put()
         print "flight created "
         return


#     print teams

# ----  have a good flight ---- 
#  PUT the teams into a dictionary
      tdict = {}
      for t in o.teams:
        tdict[t.teamid]= t


# GO through teams and keep just current playoff information
      for t in teams:
         if tdict[ t.teamid] != None:
            d = tdict[ t.teamid]

            t.area = d.area
#           print t.area,t.playoff
#           t.win = d.win            
#           t.loss =  d.loss            

            t.playoff = d.playoff
            t.date =  datetime.datetime.now()  

         else:
            print( "didnt find" )

#     print( t )
      o.teams = teams
      o.put()

# Get flight teams, keep player records if available
class StandingHandler(webapp2.RequestHandler):
    def get(self,flightid):
      Writeln(self, "GetFlightHandler")

      limit = 300

      teams=getTeams(flightid, limit)  # do the url fetch
#     print teams

      saveTeams( flightid, teams)      # save to ndbstore 

      Writeln(self, "flight" + str(flightid) + " saved to ndb")


class StandingsHandler(webapp2.RequestHandler):
    def get(self):
      Writeln(self, "GetAll Flights")

      limit = 400
      for f in ActiveList:
        teams = getTeams(f.id, limit)   # do the url fetch
        saveTeams( f.id , teams)        # save to ndb
        print( "flight " + str(f.id) + " " + f.name + " saved to ndb")
        Writeln(self, "flight " + str(f.id) + " " + f.name + " saved to ndb")




app = webapp2.WSGIApplication(
                                     [
                                      ('/[get]{0,3}stand/([\w]*)', StandingHandler),
                                      ('/[get]{0,3}standings', StandingsHandler),

                                     ],
                                      debug=True,config=mysession.config)

