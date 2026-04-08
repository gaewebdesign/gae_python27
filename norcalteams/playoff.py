import webapp2

from google.appengine.api import urlfetch

from google.appengine.ext import db
from google.appengine.ext import ndb

from datetime import timedelta

import urllib,re,datetime,string,sys,os

import operator # for sorting

import mysession

from flights import *
from ndbstore import *


from random import randint

class MatchList :
     desc = ""
     date = "" #ndb.DateTimeProperty()

#  ADDED to match main.py description of MatchList
     status = ""           # Completed/Scheduled
     match  = ""           # Week/Playoff/Districts/Sectionals
     scorecard_id  = ""
     opponent    = ""
     opponent_id = ""
     where    = ""


def Writeln( selfobj, *t):
   for x in t:
     selfobj.response.out.write(x )
     selfobj.response.out.write(" ")

   selfobj.response.out.write("<br>")

def Write( selfobj, *t):
   for x in t:
     selfobj.response.out.write(x )
     selfobj.response.out.write(" ")

def getPlayoff(teamid):


      url  = "http://www.ustanorcal.com/teaminfo.asp?id="+ str(teamid)

      result = urlfetch.fetch(url)
      s = result.content
      s = s.replace("\r","")      
      s = s.replace("\n","")      
      scraped = s.replace("\t","")      
      scraped= re.sub("<div class=\"alert alert-info scheduled-block\">([^~]*?)<\/div>","",scraped)

      pattern = r"(Sectional S[ \-\d\w]{1,9})"      # 1: Match  (could be Playoffs/Districts/Sectionals or the week)
      pattern = r"(Playoff [ \-\d\w]{1,9})"      # 1: Match  (could be Playoffs/Districts/Sectionals or the week)

      pattern = r"(PlayOff[ \-\d]{1,9})"      # 1: Match  (could be Playoffs/Districts/Sectionals or the week)

      match = re.findall(pattern,scraped )

#     for i,m in enumerate(match):  # returns list 0->6 of each found item
#          print i,m,      len(match)

      return len(match)

class PlayoffHandler(webapp2.RequestHandler):


     def get(self, flightid):

      Writeln(self, "PlayoffHandler")

#      getPlayoff(flightid)
#      return

      flightKey = ndb.Key(Flight, str(flightid) )

      o = flightKey.get()
      if( o == None):
           print("cant get Flight " + str(leagueid )  )
      else:

           teams = o.teams


      n = randint(0,14)
      n=0
      if( n==0):
          teams.sort( key = operator.attrgetter('win') ,reverse=True)
          print( str(n) + ") sort by win ")
          Writeln(self, str(n) + ") sort by win")
      elif n==1:
         teams.sort( key = operator.attrgetter('win') ) # start w worst teams
         print(str(n) + ") sort by -win")
         Writeln(self, str(n) + ") sort by -win")
      elif n==2:
         teams.sort( key = operator.attrgetter('date') )
         print( str(n) + ") sort by date")
         Writeln(self,str(n) + ") sort by date")

      else: 
          teams.sort( key = operator.attrgetter('win') ,reverse=True)
          print(str(n) + ") sort by wins")
          Writeln(self, str(n) +  ") sort by wins")

#     TempList = list(ActiveList)
#     random.shuffle(TempList)


      i = 0
      limit = 25
      for t in teams:

        len = getPlayoff( t.teamid )

        d = t.date.strftime("%a %b %d") + " " + t.date.strftime("%I:%M %p") + ")"
        print( t.teamname, t.captain ,t.win,t.loss, d)
        if len == 1:
             t.playoff = "P"
        elif len == 2:
             t.playoff = "PP"

        i = i + 1
        if( i> limit): break

        t.date = datetime.datetime.now()  

      o.teams = teams
      print("save teams to db")
#     print(teams)

      o.put()

      Writeln(self, teams )
      Writeln(self, "done")

app = webapp2.WSGIApplication(
                                     [
                                       ('/[get]{0,3}playoff/([\d]*)', PlayoffHandler),

                                     ],
                                      debug=True,config=mysession.config)

