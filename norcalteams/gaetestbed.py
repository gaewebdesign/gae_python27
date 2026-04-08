import webapp2

from google.appengine.api import urlfetch

from google.appengine.ext import db
from google.appengine.ext import ndb

from datetime import timedelta

import urllib,re,datetime,string,sys,os

import mysession

from flights import *


#import logging

#import user

#import library

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


#     print("getTeams **************")
#     print(scraped)
#     print("getTeams **************")

# REMOVE
# tenniscloud/main.py line 440
      scraped = re.sub("[ ]*<span class=\"label label\-success\">Looking</span>[ ]*","", scraped)
# REMOVE


      pTeamName = r"([ .\d\w\/\-\+\:\&']*)"
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
         
          t.win = win
          t.loss = loss
 
          print( teamid, teamname, id,lname,fname, city , area) #,win,loss)

          teamList.append(t)

#     for i,m in enumerate(match):
      return teamList


class FlightHandler(webapp2.RequestHandler):
    def get(self,flightid):
      Writeln(self, "Main")
   
#     getTeams("1700", 20)
#     getTeams("1691", 20)  # CM7.5

      legal = [1693,1692,1691,1701,1700,1699,1690]  #Combo

      if int(flightid) in legal:
         Writeln(self, "legit flight")
      else:       
         Writeln(self, "Not Found")
         return


#      flightid = "1691"  # CM7.5
#      flightid = "1693"  # CM9.5
#      flightid = "1700"  # CW8.5


      limit = 10
      tlist=getTeams(flightid, limit)  # CM9.5
      print(tlist)

      flightKey = ndb.Key(Flight, str(flightid))

      o = flightKey.get()
      if( o == None):
         Writeln(self, "Flight new")
         o = Flight( key=flightKey)
      else:
         Writeln(self, "Flight exists")

      try:
        o.teams= tlist  
        o.put()
      except:
        print("Exception")

      Writeln(self, o.teams)


class AllFlightHandler(webapp2.RequestHandler):
    def get(self):
      Writeln(self, "GetAll Flights")

      limit = 400
      for f in FlightList:

           print(f.name + "- " + str(f.id)) 

           tlist=getTeams(f.id, limit)  

           Writeln(self,f.name + " - " + str(f.id)) 

#          print(tlist)
           flightKey = ndb.Key(Flight, str(f.id))
           o = flightKey.get()

           if( o == None):
             Writeln(self, "Flight new")
             o = Flight( key=flightKey)
           else:
             Writeln(self, "Flight exists")

           Writeln(self,"try ")
           try:
             o.teams= tlist  
             Writeln(self,tlist)
             Writeln(self,"Saving")
             o.put()
           except:
             print("Exception")


app = webapp2.WSGIApplication(
                                     [
                                      ('/team', TeamHandler),
                                      ('/record', RecordHandler),
                                      ('/flight/([\d]*)', FlightHandler),
                                      ('/allflight', AllFlightHandler)

#                                      ('/division', DivisionHandler)
#                                     ('/getrecord', GetRecordHandler)


                                     ],
                                      debug=True,config=mysession.config)


