import webapp2

from google.appengine.api import urlfetch


from google.appengine.ext import db
from google.appengine.ext import ndb

from datetime import timedelta

import urllib,re,datetime,string,sys,os

#import mysession
#import logging

#import user

#import library

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

# delete Closed teams 
class CronDeleteTeamHandler( webapp2.RequestHandler):

   def get(self):
      Writeln(self, "Cron Delete Team ")


      idx = "113"   # Cupertino Sports Center
      url = "http://www.ustanorcal.com/organization.asp?id=" + idx

      result = urlfetch.fetch(url)
      scraped = result.content

#     this doesn't account for closed season
      rexp = r"ref=teaminfo\.asp\?id=([\d]*)>([ \d\w\/\.\(\)\-\\!']*)"

#     this only takes team if Registration is still open
      rexp = r"Closed[ =#<\/>\d\w]*href=teaminfo\.asp\?id=([\d]*)>([ \+\d\w\/\.\(\)\-\\!']*)"
      r = re.compile(rexp,re.IGNORECASE )
      match = r.findall( scraped )

      for i,team in enumerate(match):
         Write(self, team)
         Writeln(self, "delete " + team[0])

         idx = team[0]
         o = Team.get_by_id(int(idx))
         Writeln(self, "Look for team " + str(idx) )
         if( o != None):
            Writeln(self, "Team Found")
            Writeln(self, "DELETE FROM DATA BASE")
            o.delete()
         else:
            Writeln(self, "Cant find Team ")



class CronAddTeamHandler( webapp2.RequestHandler):
   def get(self):
      Writeln(self,"GetTeamHandler")

      idx = "113"   # Cupertino Sports Center
      url = "http://www.ustanorcal.com/organization.asp?id=" + idx

      result = urlfetch.fetch(url)
      scraped = result.content

#     this doesn't account for closed season
      rexp = r"ref=teaminfo\.asp\?id=([\d]*)>([ \d\w\/\.\(\)\-\\!']*)"

#     this only takes team if Registration is still open
      rexp = r"Register[ =#<\/>\d\w]*href=teaminfo\.asp\?id=([\d]*)>([ \+\d\w\/\.\(\)\-\\!']*)"
      rexp += r"[<>\/\w#= ]*align=left>([-\w\d]*)[, ]*([-\w\d]*)"

# 11/3/14  FIX Area is a new column 
      rexp = r"Register[ =#<\/>\d\w]*href=teaminfo\.asp\?id=([\d]*)>"    # ID
      rexp += r"([ \+\d\w\/\.\(\)\-\\!']*)<\/a><\/td>"     # team
      rexp += r"<td([^`]*?)<\/td>"                         # Area ( not needed)
      rexp += r"<td([^`]*?)<\/td>"                         # Captain

      r = re.compile(rexp,re.IGNORECASE )
      match = r.findall( scraped )

      teamlist=[]
      count=-1

      regCaptain = r"([ \w\d]*),([ \w\d]*)"
      regLevel = r"([\d]{2}[\w]{2}[\d\w\.]{0,4})"

      for i,team in enumerate(match):

#        Write(self, '<br>' + str(i) + " " +  team )
#        0: team id 1: teamname  3: captain
#        Writeln(self,   team[0] + " *  " + team[1] + " * " + team[3] )
         teamid = team[0]
         name = team[1]

         m = re.search(regLevel , team[1])
         level = m.group(1)

         m = re.search(regCaptain , team[3])
         fname = m.group(2)
         lname = m.group(1)

         teamKey = ndb.Key(Team, int(teamid) )
         g = Team( key= teamKey )
         g.position = i
         g.captain = fname + " " + lname
         g.teamid = int(teamid)
         g.name = name
         g.level = level
         g.timestamp = datetime.datetime.now()
         Writeln(self,str(g.teamid) + " " + g.name  + " -- " + g.captain + " " + g.level)
         g.put()

def GetTeamRoster(self,idx):
      Writeln(self,"GetTeamRoster")
      url = "http://www.ustanorcal.com/teaminfo.asp?id=" + str(idx)

      result = urlfetch.fetch(url)
      scraped = result.content

#     REMOVE return,newline,tab
      scraped = scraped.replace("\r","")       
      scraped = scraped.replace("\n","")       
      scraped = scraped.replace("\t"," ")       

      rexp = r"nowrap><a href=playermatches\.asp\?id=([\d]*)>"
      rexp += r"([^~]*?)</a></td>"
      rexp += r"<td ([^~]*?)</td>"  #City
      rexp += r"<td ([^~]*?)</td>"  # Gender
      rexp += r"<td ([^~]*?)</td>"  # Rating
      rexp += r"<td ([^~]*?)</td>"  # NP/SW
      rexp += r"<td ([^~]*?)</td>"  # Expiration

      r = re.compile(rexp,re.IGNORECASE )
      player = r.findall( scraped )

#     Get the roster date (go to the end of the line)
      rexp2 = r"center>([\d]{1,2}\/[\d]{1,2}\/[\d]{2})<\/td>"
      r2 = re.compile( rexp2, re.IGNORECASE)
      roster = r2.findall( scraped )

#     Number of players equals number of roster dates
      plen = len(player)
      rlen = len(roster)
      Writeln(self, '<br>' + str(idx) + " " +  " ROSTERED= " + str(rlen) + ' PLAYERS= ' + str(plen) + '<br>')

      if( plen != rlen):
         Writeln(self, 'STOP ')
         Writeln(self, 'len of player != roster ')
         return


      regName = r"([ \d\w\-\']*),([ \d\w\-\']*)"

      teamPlayerList=[]
      rosterKey = ndb.Key(RosterList, int(idx) )
      g = RosterList( key= rosterKey )

# Go through player list and create a roster
      for i,team in enumerate(player):
         playerid = team[0]

         m = re.search(regName , team[1])
         fname = m.group(2)
         lname = m.group(1)

         rDate = roster[i]
#        Writeln(self, str(i) + ")" + playerid + " " + fname + " " + lname + " " + rDate)

         rl = RosterList()
         rl.fname = fname 
         rl.lname = lname 
         rl.rdate = rDate

         d = rDate.split('/')
         rl.timestamp = datetime.date( 2000+int(d[2]),int(d[0]),int(d[1]) )


         teamPlayerList.append(rl)

#     -------OUTSIDE LOOP ---------------------
# TEAM already created
# so just need to add roster of players
#     teamKey = ndb.Key(Team, int(idx) )
#     o = Team.get_by_id(int(idx))

      return teamPlayerList
#
#     Writeln(self, "Look for team " + str(idx) )
#      if( o != None):
#            Writeln(self, "Team Found")
#            o.roster =  teamPlayerList
#            Writeln(self, "STORE INTO DATA BASE")
#            o.put()
#      else:
#            Writeln(self, "Cant find Team ")




class GetRosterHandler( webapp2.RequestHandler):
   def get(self):


      idx=63052
      idx=63294
      idx=62553  #Roger

      url = "http://www.ustanorcal.com/teaminfo.asp?id=" + str(idx)

      result = urlfetch.fetch(url)
      scraped = result.content

#     REMOVE return,newline,tab
      scraped = scraped.replace("\r","")       
      scraped = scraped.replace("\n","")       
      scraped = scraped.replace("\t"," ")       

      rexp = r"nowrap><a href=playermatches\.asp\?id=([\d]*)>"
      rexp += r"([^~]*?)</a></td>"
      rexp += r"<td ([^~]*?)</td>"  #City
      rexp += r"<td ([^~]*?)</td>"  # Gender
      rexp += r"<td ([^~]*?)</td>"  # Rating
      rexp += r"<td ([^~]*?)</td>"  # NP/SW
      rexp += r"<td ([^~]*?)</td>"  # Expiration

      r = re.compile(rexp,re.IGNORECASE )
      player = r.findall( scraped )

#     Get the roster date (go to the end of the line)
      rexp2 = r"center>([\d]{1,2}\/[\d]{1,2}\/[\d]{2})<\/td>"
      r2 = re.compile( rexp2, re.IGNORECASE)
      roster = r2.findall( scraped )

#     Number of players equals number of roster dates
      plen = len(player)
      rlen = len(roster)
      Writeln(self, '<br>' + str(idx) + " " +  " ROSTERED= " + str(rlen) + ' PLAYERS= ' + str(plen) + '<br>')

      if( plen != rlen):
         Writeln(self, 'STOP ')
         Writeln(self, 'len of player != roster ')
         return


      regName = r"([ \d\w\-\']*),([ \d\w\-\']*)"

      teamPlayerList=[]
      rosterKey = ndb.Key(RosterList, int(idx) )
      g = RosterList( key= rosterKey )

# Go through player list and create a roster
      for i,team in enumerate(player):
         playerid = team[0]

         m = re.search(regName , team[1])
         fname = m.group(2)
         lname = m.group(1)

         rDate = roster[i]
         Writeln(self, str(i) + ")" + playerid + " " + fname + " " + lname + " " + rDate)

         rl = RosterList()
         rl.fname = fname 
         rl.lname = lname 
         rl.rdate = rDate

         d = rDate.split('/')
         rl.timestamp = datetime.date( 2000+int(d[2]),int(d[0]),int(d[1]) )


         teamPlayerList.append(rl)

#     -------OUTSIDE LOOP ---------------------
# TEAM already created
# so just need to add roster of players
#     teamKey = ndb.Key(Team, int(idx) )
      o = Team.get_by_id(int(idx))

      Writeln(self, "Look for team " + str(idx) )
      if( o != None):
            Writeln(self, "Team Found")
            o.roster =  teamPlayerList
            Writeln(self, "STORE INTO DATA BASE")
            o.put()
      else:
            Writeln(self, "Cant find Team ")




# Add Rostered players players to active teams
class CronAddRosterHandler( webapp2.RequestHandler):
   def get(self):
       Writeln(self, "Cron Add Roster ")

       past = datetime.datetime.now() - datetime.timedelta(hours = 72,minutes=30)
       query = Team.query().order(Team.timestamp).filter(Team.timestamp < past).fetch(5)
       query = Team.query().order(Team.timestamp).fetch(2)

       for p in query:
          Writeln( self, str(p.key.id()) + "  " + p.name )
          p.timestamp = datetime.datetime.now()

          roster = GetTeamRoster(self, p.key.id() )
          Writeln(self, roster )

          p.put()


app = webapp2.WSGIApplication(
                                     [
                                      ('/getroster', GetRosterHandler),
                                      ('/cronaddteams', CronAddTeamHandler),
                                      ('/crondelteams', CronDeleteTeamHandler),
                                      ('/cronaddroster', CronAddRosterHandler)

                                     ],
                                      debug=True)



