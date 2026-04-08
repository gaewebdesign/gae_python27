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

#


def getRecord( teamid):
      url  = "http://www.ustanorcal.com/Teaminfo.asp?id=" + teamid
      result = urlfetch.fetch(url)
      scraped = result.content

      pattern = r"valign=middle>([\d]{1,2})"

      r = re.compile(pattern,re.IGNORECASE )
      match = r.findall( scraped )

#  a series of valign=middle>Win (or Loss) contains the team's record
#  select the 2nd and 3rd ones for the Win/Loss values
      w = match[2]
      l = match[3]

      return [w,l]


def getTeams( leagueid ,limit):


      url  = "http://www.ustanorcal.com/listteams.asp?leagueid="+str(leagueid)
      result = urlfetch.fetch(url)
      s = result.content
      s = s.replace("\r","")      
      s = s.replace("\n","")      
      scraped = s.replace("\t","")      


#     print(scraped)

# REMOVE
# tenniscloud/main.py line 440
      scraped = re.sub("[ ]*<span class=\"label label\-success\">Looking</span>[ ]*","", scraped)
# REMOVE


      pTeamName = r"([ .\d\w\/\-\+\:\&']*)"   #previous one, doenst get everything


      pTeamName = r"([ ,.#\d\w\+\/\-\[\]\!\"\:\'\&\?\(\)]*)"   # Get everything possible in a team name

      pName = r"([ .\d\w\/\-']*)"

      pattern = r"<td>[ ]*"   #bunch of spaces follow this first <td>
      pattern += r"<a href=teaminfo.asp\?id=([\d]*)>" + pTeamName + "[ ]*</a></td>"

      pattern += r"<td ([^~]*?)</a></td>"   # Captain

      pattern += r"<td ([^~]*?)</td>"   # City (not used)

      pattern += r"<td ([^~]*?)</td>"   # Area (i.e. MP)

      r = re.compile(pattern,re.IGNORECASE )
      match = r.findall( scraped )
      print("OK - enumerate")
      teamList=[]
      for i,m in enumerate(match):

          if(i>limit): 
                print("LIMIT = " + str(limit))
                break


          teamid = m[0]
          teamname = m[1]
          _captain = m[2]
          _city = m[3]
          _area = m[4]
#         Writeln( self, i, teamid, teamname, _captain, _area )
          print(  i, teamid, teamname, _captain, _area )

          try:
# align=left nowrap><a href=playermatches.asp?id=100472>Okamoto,Roger
# align=center>MP
# align=left nowrap>SANTA ROSA
             r1 = re.search(r"id=([\d]*)>"+pName+","+pName,_captain)
             r2 = re.search(r"center>([\w]{1,3})",_area)
             r3 = re.search(r"nowrap>" + pName ,_city)
             print("try")
          except:
             print("Exception")

          if( r1 != None ):
               id = r1.group(1)
               lname = r1.group(2)
               fname = r1.group(3)

          if( r2 != None ):
               area = r2.group(1)

          if( r3 != None ):
               city = r3.group(1)


          t = Team()
          t.teamid = teamid
          t.teamname = teamname
          t.captain = fname + " " + lname
          t.captainid = id
          t.area = area

          t.date = datetime.datetime.now()  
#         record = getRecord(teamid)
          win = 0  # int(record[0])
          loss = 0 # int(record[1])
         
          t.order = 0
          t.win = win
          t.loss = loss
 
          print( teamid, teamname, id,lname,fname, city , area) #,win,loss)

          teamList.append(t)

#     for i,m in enumerate(match):
      return teamList

def saveTeams(flightid, teams ):
      print "SAVING"
      flightKey = ndb.Key(Flight, str(flightid))
      o = flightKey.get()
      if o == None :
         print "flight doesnt exist "
         o = Flight( key = flightKey)
         o.teams = teams
         o.put()
         print "flight created "
         return

# ----  have a good flight ---- 

#  PUT the teams into a dictionary
      tdict = {}
      for t in o.teams:
        tdict[t.teamid]= t


# GO through teams and keep current order/win/loss/playoff information
      for t in teams:
         if tdict[ t.teamid] != None:
            d = tdict[ t.teamid]
            t.order = d.order            
            t.win = d.win            
            t.loss =  d.loss            
            t.playoff = d.playoff
            t.date =  datetime.datetime.now()  
            print( t )
         else:
            print( "didnt find" )

      o.teams = teams
      o.put()



# Get flight teams, keep player records if available
class GetFlightHandler(webapp2.RequestHandler):
    def get(self,flightid):
      Writeln(self, "GetFlightHandler")

      limit = 300

      teams=getTeams(flightid, limit)  # do the url fetch
      saveTeams( flightid, teams)      # save to ndbstore 

      Writeln(self, "flight" + str(flightid) + " saved to ndb")

# Get flight teams, keep player records if available
class GetFlightsHandler(webapp2.RequestHandler):
    def get(self):
      Writeln(self, "GetAll Flights")

      limit = 400
      for f in FlightList:
        teams = getTeams(f.id, limit)   # do the url fetch
        saveTeams( f.id , teams)        # save to ndb
        Writeln(self, "flight" + str(f.id) + " saved to ndb")


class TestHandler(webapp2.RequestHandler):
    def get(self):
      Writeln(self, "Test Handler")


app = webapp2.WSGIApplication(
                                     [

                                      ('/getflight/([\d]*)', GetFlightHandler),
                                      ('/getflights', GetFlightsHandler)

                                     ],
                                      debug=True,config=mysession.config)

#
#
#      getflight/1700   get a specific flight no records
#      getflights        get all flights with no records
#
#

