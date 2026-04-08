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



# CLASSES FOR THIS PROJECT ARE IN ndbstore.py
# JUST REFERENCE BY THEIR NAME
from ndbstore import *


def Writeln( selfobj, *t):
   for x in t:
     selfobj.response.out.write(x )
     selfobj.response.out.write(" ")

   selfobj.response.out.write("<br>")

def Write( selfobj, *t):
   for x in t:
     selfobj.response.out.write(x )
     selfobj.response.out.write(" ")


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

        scraped = None
        n=gc.collect()
        print("gc.collect = " + str(n))

      except Exception as e:
        print("EXCEPTION: record.py " + str(e) )
        w = 0
        l = 0


      return [w,l]


def getTeams( flight, limit):
      teams = None
      flightKey = ndb.Key(Flight, str(flight))

      o = flightKey.get()
      if( o == None):
         print( "cant find flight")
         return None
      else:
         print( "GOOD: found flight " + str(flight) )

      updatedteams = []
      try:
        teams = o.teams
        teams.sort( key = operator.attrgetter('date') )
#       teams.sort( key = operator.attrgetter('date') , reverse=True)

        for i,t in enumerate(teams):
          if( i > limit): 
              print("breaking at limit= " + str(limit))
              break
          record = getRecord(t.teamid)

          t.win = int(record[0])
          t.loss = int(record[1])
          t.date = datetime.datetime.now()  
          updatedteams.append(t)
#         print(t.win,t.loss,t.date )

      except Exception as e:
         print("EXCEPTION: " + str(e) )

      return updatedteams

# save just the updated teams returned from getTeams
def saveTeams( flightid, updatedteams):
      print("saveTeams")
      flightKey = ndb.Key(Flight, str(flightid))
      o = flightKey.get()
      if o == None :
         print "flight doesnt exist "
         return

      try:
# ----  have a good flight ---- 
#  PUT the teams into a dictionary for quick access
          tdict = {}
          for t in o.teams:
             tdict[t.teamid]= t


          for d in updatedteams:
             print("update " + d.teamname )
             uTeam = tdict[d.teamid]
             uTeam.win = d.win
             uTeam.loss = d.loss
             uTeam.date = datetime.datetime.now()  

# sneaky way of doing this... o.teams updated on the fly in memory (above)
          o.put()

      except Exception as e:
        print("EXCEPTION: " + str(e) )

class RecordHandler(webapp2.RequestHandler):
    def get(self, flightid):
      Writeln(self, "RecordHandler")
      limit = 50
      teams = getTeams( flightid , limit)   # from the db

      Writeln(self, teams )
      saveTeams( flightid , teams)



class RecordsHandler(webapp2.RequestHandler):
    def get(self):
      Writeln(self, "RecordsHandler")

#     getRecord( flightid , limit)

      tempList = list(ActiveList)
      random.shuffle(tempList)

      max = 4
      limit = 24
      for i,f in enumerate(tempList):
           if( i > max):
                print("breaking at " + str(i) )
                break


           flightid = f.id
           teams = getTeams( flightid , limit)

           Writeln(self, "updateFlight " +  f.name + " id=" +str(f.id) )
           Writeln(self, teams )

           print("updateFlight " +  f.name + " id=" +str(f.id) )
           print( teams )

           saveTeams( flightid , teams)


class TestHandler(webapp2.RequestHandler):

    def get(self):

      TempList = list(FlightList)
      random.shuffle(TempList)

      print("shuffled")
      for f in TempList:
           print(  f.name + " id=" +str(f.id) )



app = webapp2.WSGIApplication(
                                     [
                                      ('/getrecord/([\d]*)', RecordHandler),
                                      ('/getrecords', RecordsHandler),


                                      ('/test', TestHandler)


                                     ],
                                      debug=True,config=mysession.config)



