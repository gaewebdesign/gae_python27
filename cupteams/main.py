import webapp2

from google.appengine.api import urlfetch
from google.appengine.api.urlfetch import urllib2

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
         Writeln(self, str(team) + " ")
#         Write(self, team[0] + " ")
#         Write(self, team[1] + " ")
#         Writeln(self, team[2] + " ")


         idx = team[0]
         o = Team.get_by_id(int(idx))
         Writeln(self, "Look for team " + str(idx) )
         if( o != None):
            Writeln(self, "Team Found")
            Writeln(self, "DELETE FROM DATA BASE")
#           o.key.delete()

         else:
            Writeln(self, "Cant find Team ")



class CronAddTeamHandler( webapp2.RequestHandler):
   def get(self):
      Writeln(self,"GetTeamHandler")

      idx = "463"   # Sunnyvale Tennis Center
      idx = "113"   # Cupertino Sports Center

      url = "http://www.ustanorcal.com/organization.asp?id=" + idx

      print("CronAddTeamHandler"*10)

      result = urlfetch.fetch(url,payload=None, method=urlfetch.GET)
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
      regLevel = r"([\d]{2}[\w]{2}[\d\w\.\+]{0,5})"    # DOESNT INCLUDE COMBO

      regLevel = r"([CMS\d]{0,2}[\w]{2}[\d\w\.\+]{0,5})"   # [\d\w]{0,2} , zero to 2 18Mx, CM , S70

# fix for 18-39N8.5A
      regLevel = r"([CMS\d]{0,2}[\w]{2}[\-\d\w\.\+]{0,8})"   # [\d\w]{0,2} , zero to 2 18Mx, CM , S70


      for i,team in enumerate(match):

#        Write(self, '<br>' + str(i) + " " +  str(team) )
#        Write(self, '<br>' + team[1] + "<br>" )

#        Write(self, 'TEAM ' + str(i)  + "<br>" )

#        0: team id 1: teamname  3: captain
#        Writeln(self,   team[0] + " *  " + team[1] + " * " + team[3] )
         teamid = team[0]
         name = team[1]
        
#        Clear out CUPERTINO from the name, in order to extract the level (18M vs CM messes up)
         level = name
         level = re.sub("CUPERTINO TC","",name)
         level = re.sub("CUPERTINO SC","",level)
           
         m = re.search(regLevel , level )
#        if (m  is  None ): continue

         level = m.group(1)

         print("****"+ name + " " + level + " ****** " )

         m = re.search(regCaptain , team[3])
         fname = m.group(2)
         lname = m.group(1)

         teamKey = ndb.Key(Team, int(teamid) )

         g = Team.get_by_id( int(teamid) )

         if( g != None):
           Writeln( self, "Team exists " )
           Writeln( self, g )
         else:
           g = Team( key=teamKey)
           Writeln( self, "Team created " )
           Writeln( self, g )

#        g = Team( key= teamKey )
         g.position = i
         g.captain = fname + " " + lname
         g.teamid = int(teamid)
         g.name = name
         g.level = level[:-1]    # TAKE OUT TEAM A,B,C,D,E,
         g.timestamp = datetime.datetime.now()
         r = g.put()

         Writeln(self,str(g.position) + ")" +str(g.teamid) + " " + g.name  + " -- " + g.captain + " " + g.level + " " + str(r)  )

class GetTeamRosterHandler( webapp2.RequestHandler):
   def get(self):

       idx = 63393  #M4.0
       idx = 63568  #M4.5
       g = Team.get_by_id( int(idx) )

       if( g != None):
         Writeln( self, "Team exists " )
         Writeln( self, g )
       else:
         teamKey = ndb.Key(Team, int(idx) )
         g = Team( key=teamKey)
         Writeln( self, "Team created " )
         Writeln( self, g )

       roster = GetTeamRoster(self, idx )
       Writeln(self, roster )
       g.timestamp = datetime.datetime.now()
       g.roster = roster
       g.put()



def GetTeamRoster(self,idx):

      url = "https://www.ustanorcal.com/teaminfo.asp?id=" + str(idx)

      url = "https://www.ustanorcal.com/teaminfo.asp?id=" + str(idx)
      url = "http://www.sctennisclub.org/tcloud/tcloud.php?id=" + str(idx)

#      print(" ***  "*23 )
#      print("URL = " + url )
#      print(" ***  "*23 )


# TO FIX PROBLEM WITH reading https:
# This  works! August 20,2018 
      print ("FETCHING... " + url )

#      result = urllib2.urlopen( url )
#      scraped = result.read() 
#      self.response.out.write(  "fetching ... " + url  )

#      self.response.out.write(  result.headers )

      req = urllib2.Request( url )
      response = urllib2.urlopen( req )
      scraped = response.read()
#     self.response.out.write(  scraped )

#  This doesn't work any more
#     result = urlfetch.fetch(url)
#     scraped = result.content
# ******************************

#      print result.status_code
#      self.response.out.write(  url + "<br>" )
#      self.response.out.write(  str(result.status_code) +  "<br>")
#      self.response.out.write(  result.content  + "<br>")


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


      regName = r"([ \d\w\-\'\.]*),([ \d\w\-\'\.]*)"
      regCity = r"nowrap>([ \d\w\-\']*)"

      regNTRP = r">([\d\.\w]{0,5})"


      teamPlayerList=[]
      rosterKey = ndb.Key(RosterList, int(idx) )
      g = RosterList( key= rosterKey )

# Go through player list and create a roster
      city=""
      ntrp=""
      for i,team in enumerate(player):
         playerid = team[0]

         m = re.search(regName , team[1])
         fname = m.group(2)
         lname = m.group(1)

         m = re.search(regCity , team[2])
         if(m != None): 
             city = m.group(1)
#            print(city)

         m = re.search(regNTRP , team[4])
         if(m != None): 
             ntrp = m.group(1)
#            print(ntrp)


         rDate = roster[i]
# team ->  0: id 1:lname,fname 2:city 3:gender 4:rating 


#        print(team)
#        Writeln(self, str(i) + ")" + playerid + " " + fname + " " + lname + " " + rDate)

         rl = RosterList()
         rl.fname = fname 
         rl.lname = lname 
         rl.city = city 
         rl.ntrp = ntrp
         rl.rdate = rDate

         d = rDate.split('/')
         rl.timestamp = datetime.date( 2000+int(d[2]),int(d[0]),int(d[1]) )


         teamPlayerList.append(rl)

#     -------OUTSIDE LOOP ---------------------
# return the ROSTER list
      return teamPlayerList



# Add Rostered players players to active teams
class CronAddRosterHandler( webapp2.RequestHandler):
   def get(self):


       past = datetime.datetime.now() - datetime.timedelta(hours = 72,minutes=30)
#      query = Team.query().order(Team.timestamp).filter(Team.timestamp < past).fetch(5)
       query = Team.query().order(Team.timestamp).fetch(3)

       for p in query:
          Writeln(self, " " )
          Writeln( self, str(p.key.id()) + "  " + p.name + " " + p.captain)
          print( p.name ,p.captain)
          p.timestamp = datetime.datetime.now()

          roster = GetTeamRoster(self, p.key.id() )
#         print( roster )
          p.roster = roster
          p.put()


app = webapp2.WSGIApplication(
                                     [
                                      ('/getroster', GetTeamRosterHandler),
                                      ('/cronaddteams', CronAddTeamHandler),
                                      ('/crondelteams', CronDeleteTeamHandler),
                                      ('/cronaddroster', CronAddRosterHandler),
                                      ('/cron', CronAddRosterHandler)
                                     ],
                                      debug=True)



