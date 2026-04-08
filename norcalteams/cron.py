import webapp2

from google.appengine.api import urlfetch

from google.appengine.ext import db
from google.appengine.ext import ndb

from datetime import timedelta

import urllib,re,datetime,string,sys,os

import operator # for sorting
import random   # for shuffling


import mysession
from flights import *

#garbage collector ------
import gc
import pprint
# -----------------------

#import logging

#import user

#import library

# CLASSES FOR THIS PROJECT ARE IN ndbstore.py
# JUST REFERENCE BY THEIR NAME
from ndbstore import *
#import ndbstore

# NOTES
# standings per flight
# https://www.ustanorcal.com/standings.asp?l=1811

# NOTES


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
#     teamid = ndb.StringProperty()
#     desc = ndb.StringProperty()
#     leagueid = ndb.StringProperty()    
#     area = ndb.StringProperty()    
#     captain = ndb.StringProperty()
#     win = ndb.StringProperty()    
#     loss = ndb.StringProperty()    

class RecordHandler(webapp2.RequestHandler):
    def get(self):
      Writeln(self, "Main")



class TeamHandler(webapp2.RequestHandler):

    def get(self):
      Writeln(self, "Main")
      print "get"


      leagueid= "1793"   #40Mx8.0 2015
      leagueid= "1700"   #CW8.5 2015
      url  = "http://www.ustanorcal.com/listteams.asp?leagueid="+leagueid

# <a href=teaminfo.asp?id=67985>SANTA ROSA JC 40MX8.0A</a>

      result = urlfetch.fetch(url)
      s = result.content
      s = s.replace("\r","")      
      s = s.replace("\n","")      
      scraped = s.replace("\t","")      
#     print(scraped)

      pTeamName = r"([ .\d\w\/\-']*)"
      pName = r"([ .\d\w\/\-']*)"

      pattern = r"<td>[ ]*"   #bunch of spaces follow this first <td>
      pattern += r"<a href=teaminfo.asp\?id=([\d]*)>" + pTeamName + "[ ]*</a></td>"

      pattern += r"<td ([^~]*?)</a></td>"   # Captain

      pattern += r"<td ([^~]*?)</td>"   # City (not used)

      pattern += r"<td ([^~]*?)</td>"   # Area (i.e. MP)

      r = re.compile(pattern,re.IGNORECASE )
      match = r.findall( scraped )
      for i,m in enumerate(match):
          if(i>20): return

          teamid = m[0]
          teamname = m[1]
          _captain = m[2]
          _city = m[3]
          _area = m[4]
#         Writeln( self, i, teamid, teamname, _captain, _area )
          print(_city)
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


          Writeln(self,teamid, teamname,id, lname,fname, city , area)
          print( teamid, teamname, id,lname,fname, city , area)

#
#     teamid = ndb.StringProperty()
#     desc = ndb.StringProperty()
#     leagueid = ndb.StringProperty()    
#     area = ndb.StringProperty()    
#     captain = ndb.StringProperty()
#     win = ndb.StringProperty()    
#     loss = ndb.StringProperty()    
          teamKey = ndb.Key(Team, str(teamid))
          o = teamKey.get()
          if( o == None):
             Writeln(self, "Team new")
             o = Team( key=teamKey)
          else:
             Writeln(self, "Team exists")


          o.teamid = teamid
          o.teamname = teamname

          o.captain = fname + " " + lname
          o.captainid = id

#         o.leagueid = leagueid
          o.area = area

# Get Win/Loss record
          record = getRecord( teamid)
          o.win = int(record[0])
          o.loss = int(record[1])

          o.put()


def ____getRecord( teamid):
      print(" getRecord() --")

      url  = "http://www.ustanorcal.com/Teaminfo.asp?id=" + teamid
      result = urlfetch.fetch(url)
      scraped = result.content

      pattern = r"valign=middle>([\d]{1,2})"


      r = re.compile(pattern,re.IGNORECASE )
      match = r.findall( scraped )

#  a series of valign=middle>Win (or Loss) contains the team's record
#  select the 2nd and 3rd ones for the Win/Loss values
      try:
       w = match[2]
       l = match[3]
      except Exception as e:
       print("EXCEPTION try to find match[2],match[3] ->" + str(e))
       print("cron.py Line 170 " )
       w=0
       l=0

      try:
        print("releasing memory ")
        del scraped
      except Exception as e:
        print("EXCEPTION: " + str(e))

      return [w,l]


def getTeams( leagueid ,limit):

      url  = "http://www.ustanorcal.com/listteams.asp?leagueid="+leagueid
      result = urlfetch.fetch(url)
      s = result.content
      s = s.replace("\r","")      
      s = s.replace("\n","")      
      scraped = s.replace("\t","")      

      pTeamName = r"([ .\d\w\/\-']*)"
      pName = r"([ .\d\w\/\-']*)"

      pattern = r"<td>[ ]*"   #bunch of spaces follow this first <td>
      pattern += r"<a href=teaminfo.asp\?id=([\d]*)>" + pTeamName + "[ ]*</a></td>"

      pattern += r"<td ([^~]*?)</a></td>"   # Captain

      pattern += r"<td ([^~]*?)</td>"   # City (not used)

      pattern += r"<td ([^~]*?)</td>"   # Area (i.e. MP)

      r = re.compile(pattern,re.IGNORECASE )
      match = r.findall( scraped )
      print("OK")
      teamList=[]
      for i,m in enumerate(match):
          if(i>limit): continue
          teamid = m[0]
          teamname = m[1]
          _captain = m[2]
          _city = m[3]
          _area = m[4]
#         Writeln( self, i, teamid, teamname, _captain, _area )
#         print(_city)
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
         
          t.win = win
          t.loss = loss
 
          print( teamid, teamname, id,lname,fname, city , area) #,win,loss)

          teamList.append(t)

#     for i,m in enumerate(match):
      return teamList

def getRecord( teamid):
      url  = "http://www.ustanorcal.com/Teaminfo.asp?id=" + teamid
      result = urlfetch.fetch(url)
      scraped = result.content

      pattern = r"valign=middle>([\d]{1,2})"

      r = re.compile(pattern,re.IGNORECASE )
      match = r.findall( scraped )
     
      try:
#  a series of valign=middle>Win (or Loss) contains the team's record
#  select the 2nd and 3rd ones for the Win/Loss values
        w = match[2]
        l = match[3]
      except Exception as e:
        print("EXCEPTION: has no win-loss record teamid= " + teamid )
        w = 0
        l = 0

      try:
        print("cron.py L295: releasing scraped memory ")
#       del scraped
        scraped = None
        n=gc.collect()
        print("gc.collect = " + str(n))
#       pprint.pprint(gc.get_objects()  )
#       pprint.pprint(gc.garbage)

      except Exception as e:
        print("EXCEPTION: " + str(e))


      return [w,l]


def updateRecord( flight ,limit):

      teams = None
      flightKey = ndb.Key(Flight, str(flight))

      o = flightKey.get()
      if( o == None):
         print( "cant find flight")
         return None
      else:
         print( "GOOD: found flight " + str(flight) )

      record=[]
      try:

        teams = o.teams
#       o.put()
        teams.sort( key = operator.attrgetter('date') )
#       teams.sort( key = operator.attrgetter('date') , reverse=True)

        count = len(teams)

        print("TEAMS in the flight = "+ str(count) )
        print("getrecord of  "+ str(limit) )

        start = 0
        for t in teams:
          start = start +1
          if( start > limit): 
              print("breaking..")
              break

#         print("calling getRecord("+t.teamid+")")
          record = getRecord(t.teamid)

          try:
            t.win = int(record[0])
            t.loss = int(record[1])
            t.date = datetime.datetime.now()  
          except Exception as e:
           print("EXCEPTION: updateRecord Line 327 ->" + str(e))

#         Writeln(self, t.teamid , t.teamname,t.win,t.loss,t.date )
          print(start, t.teamid , t.teamname,t.date,"(" + str(t.win) +"-"+ str(t.loss) +")")
      except Exception as e:
        print("EXCEPTION: cron.py trying to get teams ->" + str(e))

      try:
        if( teams != None):
           o.teams = teams
           o.put()
           del o
           print("cron.py L356 SAVED to DB, memory released")
      except Exception as e:
        print("EXCEPTION: cron.py trying to save teams ->" + str(e) )

      return teams

# update (get win/loss) of a single flight
class UpdateFlightHandler(webapp2.RequestHandler):

    def get(self,flightID):
      Writeln(self, "UpdateHandler")


      limit = 50
      teams=updateRecord(flightID,limit)
      Writeln(self,teams)
      print teams



class ActiveHandler(webapp2.RequestHandler):


    def get(self):
      Writeln(self, "ActiveHandler")
   

      TempList = list(ActiveList)

      random.shuffle(TempList)

      max=4
      i=0
      limit = 25
      print("get records of " + str(max) + " flights  " + str(limit) + " teams in each flight")
      for f in TempList:
           i = i + 1
           if( i > max):
                print("breaking at " + str(i) )
                break

           print("updateRecord " +  f.name + " id=" +str(f.id) )
           teams=updateRecord(f.id,limit)
           Writeln(self, teams)

           try:
#             del teams
              for t in teams:
                  t = None
              teams = None
              print("release teams")
           except Exception as e:
              print("EXCEPTION: " + str(e) )




class ShortHandler(webapp2.RequestHandler):


    def get(self):
      Writeln(self, "ShortHandler")
      print( "ShortHandler")
   
      TempList = list(ShortList)
      limit = 24
      limit = 224

#  

#

      random.shuffle(TempList)

      for f in TempList:
           print("updateRecord " +  f.name + " id=" +str(f.id) )
        
           teams=updateRecord(f.id,limit)
           Writeln(self, teams)

class _Team:
     order = won = loss = 0
     teamid=teamname=captainid=captain=""


     def __init__(self, order,teamid,teamname,captainid,captain,area,won,loss,playoff):
        self.order =  order
        self.teamid =  teamid

        self.teamname =  teamname
        self.captainid =  captainid
        self.captain =  captain

        self.playoff =  playoff
        self.won =  won
        self.loss =  loss


def standings(self,leagueid):

      url  = "http://www.ustanorcal.com/standings.asp?l="+ str(leagueid)

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
         _won = m[4]
         _loss = m[5]

         r1 = re.search(r"playermatches.asp\?id=([\d]*)>"+pName,_captainid)

         if( r1 != None ):
              _captainid = r1.group(1)
              _captain = r1.group(2)

         r3 = re.search(r">([\d]{1,3})",_won)
         r4 = re.search(r">([\d]{1,3})",_loss)

         if( r3 != None ):
              _won = r3.group(1)

         if( r4 != None ):
              _loss = r4.group(1)


#        print i,_teamid, _teamname ,_captainid, _captain , _won, _loss
#        teams.append([ i,_teamid, _teamname ,_captainid, _captain , _won, _loss] )
         t = _Team(i,_teamid , _teamname, _captainid,_captain, "area", _won, _loss,"playoff")
         teams.append( t  )

      return teams


class StandingsHandler(webapp2.RequestHandler):

    def get(self,flightid):


      teams = standings(self, flightid)

      for t in teams:
         Writeln( self, t.order,t.teamname ,t.captain ) 


      flightKey = ndb.Key(Flight, str(flightid))
      o = flightKey.get()
      if( o == None):
         print( "BAD: no  flight " + str(flightid) )
         return

# CONTINUE WITH A GOOD FLIGHT
# SAVE teams by teamid  into dictionary for quick access
      tdict = {}
      for t in o.teams:
          tdict[t.teamid]= t

# GO through teams and update order/win/loss
      for t in teams:
        if tdict[ t.teamid] != None:
                d = tdict[ t.teamid]
                t.order = d.order            
                t.win = d.win            
                t.loss = d.loss            
                print( t )
                Writeln( self, t )
        else:
                print( "didnt find" )


class TestHandler(webapp2.RequestHandler):

    def get(self):

      TempList = list(FlightList)
      random.shuffle(TempList)

      print("shuffled")
      for f in TempList:
           print(  f.name + " id=" +str(f.id) )


app = webapp2.WSGIApplication(
                                     [
                                      ('/active', ActiveHandler),
                                      ('/short', ShortHandler),

                                      ('/updateflight/([\d]*)', UpdateFlightHandler),

#                                     ('/standings/([\d]*)', StandingsHandler),

                                      ('/test', TestHandler)


                                     ],
                                      debug=True,config=mysession.config)


