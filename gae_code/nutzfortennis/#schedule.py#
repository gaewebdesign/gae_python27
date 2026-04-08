import os
from google.appengine.ext.webapp import template

import webapp2

#from google.appengine.ext import webapp
#from google.appengine.ext.webapp.util import run_wsgi_app

from google.appengine.ext import db

import urllib
from google.appengine.api import urlfetch

import json
from django.utils import simplejson

import re,sys,string,datetime,sets

import datastore


class Player:
    fname=lname=usta_id=""
    teamid=0

class Date:
    day=month=""

class Spam( db.Model):
   eggs = db.TextProperty()
     

def Writeln(selfobj,*t):
        for x in t:
          selfobj.response.out.write(x )
          selfobj.response.out.write(" ")

        selfobj.response.out.write("<br>")

def Write(selfobj,*t):
        for x in t:
          selfobj.response.out.write(x )
          selfobj.response.out.write(" ")

def translate(  name):

        t = { ("Santa Clara", "SC"),  ("Los Gatos", "LG")

        }

        for x in t: 
          if( x[0].lower() in name.lower() ): return x[1]

        return "L"

def getTeamFromDB( teamid):

      team_key = db.Key.from_path("Team",teamid)
      team = db.get(team_key)   # team exists

#     Create a team 
      if( team == None):
        team  = datastore.Team( key_name = str(teamid) )   #key_name prohibits dups     


      return team




# teaminfo:  get team info ( schedule, player list)
# playerinfo: gets a player entire schedule, all active teams 
class GetInformation(webapp2.RequestHandler):

    def get(self):

      player=11507   # GR
      player=20832   # CB


      team=52567  # GGP
      team=52981  # Cupertino
      team=54054  # Hopkins

      Writeln( self, self.request.path )
      path = self.request.path

      if ( "teaminfo" in path ):
         self.GetTeamInfo(team)
      elif ( "playerinfo" in path):
         self.playerinfo(player)



    def playerinfo( self,playerid, playername=""):

      t = datetime.datetime.now( ) - datetime.timedelta(hours=7)

      self.response.headers['Content-Type'] = 'text/html'
      Writeln(self, "date")
      Writeln(self, t.month,t.day,t.year,t.hour, t.minute,t.second)




class GetScorecard(webapp2.RequestHandler):

#<a href=scorecard.asp?id=328799&l=7640:1133>04/07/13</a>
    def get(self):

      teamid=52981  # Cup

      self.response.headers['Content-Type'] = 'text/html'

      url  = "http://www.ustanorcal.com/teaminfo.asp?id="+str(teamid)
      result = urlfetch.fetch(url)
      scraped = result.content

      pattern = r"<a href=scorecard\.asp\?id=([\d]*)&[:l=\d]*>"
      pattern +=  r"([\d]{2})\/([\d]{2})\/([\d]{2})"

      print "<p>"

      r = re.compile(pattern,re.IGNORECASE )
      match = r.findall( scraped )

      for i, tuple in enumerate(match):      #returns i(ndex) and a 3-Tuple
        print tuple
        print "<br>"


class GetPlayers(webapp2.RequestHandler):

    def get(self):

      self.response.headers['Content-Type'] = 'text/html'
      teamid=54054  # Hopkins      

      url  = "http://www.ustanorcal.com/teaminfo.asp?id="+str(teamid)
      result = urlfetch.fetch(url)
      scraped = result.content

#a href=playermatches.asp?id=20832>Bell, Carrie</b></a>
      rexp = r"<a href=playermatches.asp\?id=([\d]*)>([\w]*) ([\w]*)"

#     rexp = r"<a href=playermatches.asp\?id=([\d]*)>([\w]*]"
#     rexp = r"<a href=playermatches.asp\?id=([\d]*)>([\d\w]*])[ ,]*"
      rexp = r"nowrap><a href=playermatches\.asp\?id=([\d]*)>([ \-\w\d\'\.]*)[, ]*([ \-\w\d\'\.]*)[ <>\w=#\d\/]*?nowrap>([ \w]*)"


      r = re.compile(rexp,re.IGNORECASE )
      match = r.findall( scraped )

      for i, tuple in enumerate(match):      #returns i(ndex) and a 3-Tuple
#       print tuple,tuple[0],tuple[1]
        print tuple
        print "<br>"


class GetTeams(webapp2.RequestHandler):

    def conversion(self,club):

      c = {
              ("Cup","Cu"),("Palo","PA"),("Yello","Y")
      }

      return 'a'

    def get(self):

      self.response.headers['Content-Type'] = 'text/html'


      playerid=11507   # GR
      playerid=100472  # Roger
      playerid=58252   # CJ

      url  = "http://www.ustanorcal.com/playermatches.asp?id="+str(playerid)
      result = urlfetch.fetch(url)
      scraped = result.content


#    <td nowrap>2013 Mixed 18 & Over 8.0</td>
#>2012 Combo Mens League 8.5</a></td>
#<td nowrap="nowrap"><a href="teaminfo.asp?id=53996">SANTA CLARA TC/SANTA CLARA TENNIS C 18MX8.0A </a></td>


#<td nowrap="nowrap"><a href="teaminfo.asp?id=53996">SANTA CLARA TC/SANTA CLARA TENNIS C 18MX8.0A </a></td>
      team = r'nowrap\"><a href="teaminfo\.asp\?id=([\d]*)">([ .\[\]\d\w\/]*)(<b>Captain</b>)*</a>'

      team = r'nowrap\"><a href="teaminfo\.asp\?id=([\d]*)">([ .\[\]\d\w\/]*)[<b>Captain</b>]*</a>'


      rexp = r'<td nowrap>(2013[ &.\w\d]*)</td'

      rexp = r'>(2012[ &.\w\d]*)<'
      rexp = r'>(2012|2013[ &.\w\d]*)<'


#>2013 Mixed 18 & Over 8.0</td>
#>2013 Adult 18 & Over Mens 4.0</a></td>
      rexp12 = r'<td nowrap>(2012[ &.\w\d]*)</td>'
      rexp12a = r'match\">(2012[ &.\w\d]*)</a></td>'

      rexp13 = r'<td nowrap>(2013[ &.\w\d]*)</td>'
      rexp13a = r'match\">(2013[ &.\w\d]*)</a></td>'

#<a href="teaminfo.asp?id=53996">SANTA CLARA TC/SANTA CLARA TENNIS C 18MX8.0A </a

      rexp3 = r'nowrap\"><a href="teaminfo\.asp\?id=([\d]*)">([ .\[\]\d\w\/]*)(<b>Captain</b>)*</a>'


      r = re.compile(r'(rexp1) | (rexp2)' ,re.IGNORECASE )
      combine = rexp3
      combine = rexp13 + '|' + rexp13a + '|' +rexp12 + '|' +  rexp12a

      combine = rexp12 + '|' +  rexp12a
      combine = rexp13 + '|' + rexp13a 

      combine = rexp13 + '|' + rexp13a + '|' +rexp12 + '|' +  rexp12a

      combine = rexp13 + '|' + rexp12a + '|' + rexp12

      combine = rexp13 + '|' + rexp13a + '|' +rexp12 + '|' +  rexp12a + '|' + team

      combine = team + '|' + rexp12a

      r = re.compile(combine ,re.IGNORECASE )
      match = r.findall( scraped )

#     print match 
      print "<br>"

      dates = []
      for i, tuple in enumerate(match):      #returns i(ndex) and a 3-Tuple
#          print i,tuple, "  *<br>"
           print i,")",tuple[0]," , ",tuple[1], ", ", tuple[2], "  <-<br>"
           print type(i)
            
           if( "2012" in tuple[2]): 
               print "done <br>"
               break
           g = datastore.Player( key_name = str(playerid) )   #key_name prohibits dup entries
           g.playerid = playerid
           g.name = "Greta"
           g.teams = ["23133","23153" ]

           t = datetime.date(2013,7,4)
           dates.append( t )

           g.dates = dates
           db.put ( g )          

           if i> 10 : break

 
# ------------------------------------------------------#
class ScheduleInfo(webapp2.RequestHandler):

    def get(self):


        teamid= 53995  # SCTC
        teamid= 54054  # Hopkins
#       self.playerinfo( teamid)


        playerid = 122943  # Rochelle
        playerid = 100472 # Roger
        playerid = 140800 # Hovhannes
        playerid = 122284  # R Truong
        playerid = 100472 # Roger
        playerid = 113873  # Scheper


        playerid = 20832  # CBell
        playerid = 58252  # CJeung
        playerid = 145469   # KOng
        playerid = 94120  # JPineda

        playerid=114432   #GCaabay

#       p = self.findPlayerTeams( teamid)
#       Writeln( self, p )

        path = self.request.path
        path = path.lstrip("/")
        Writeln(self, path)

        if ( "roster" == path ):
           Writeln(self, "roster for team id =", teamid)
           self.roster(teamid)            # Creates  a Roster class for this teamid

        elif ( "rosterteams" == path ):
           Writeln(self, "rosterteams teamid=",teamid)
           self.rosterteams( teamid )     # update Roster.teams (requires existing Team )

        elif ( "createplayerteams" == path ):
           Writeln(self, "Create Teams for playerid=",playerid)
           self.CreatePlayerTeams( playerid )     # create Teams for playerid

        elif ( "createplayer" == path ):
           Writeln(self, "Create Player for playerid=",playerid)
           self.CreatePlayer( playerid )          # create Player for playerid, get teamIDs


        elif ( "scrap_teamids" in path ):

           playerid= 100472

           Writeln(self, "get teams for player id =", teamid)
           teams=self.scrap_teamIDs(playerid)   
           Writeln(self, teams)

        elif ( "scrap_teamdates" in path ):
           teamid= 53996  #SCTC
           teamid= 54054  #Hopkins
           teamid= 54103  #SCTC W55 4.0

           Writeln(self, "ScrapTeamDates for team id =", teamid)
           active=self.scrapTeamDates(teamid)         # Saves  a Roster class , info about this team
           Writeln(self, active)


        elif ( "teamplayerinfo" in path ):
           Writeln(self, "for team id =", teamid)
           self.teamplayerinfo(teamid)        # Saves Player classes for each player on this team

        elif ( "playerinfo" in path ):
           Writeln(self, "for player id =", playerid)
           self.playerinfo(playerid)        # return a list of team IDs for a player (Test)

        elif ( "test" in path ):
           Writeln(self, "TEST")
           self.test( )        # return a list of team IDs for a player (Test)


        elif ( "updateplayer" in path):
           self.playerinfo(player)       # DATASTORE uses playerteams, gets team IDs for each player
        elif ( "findplayerteams" in path):
           self.playerinfo(player)
        elif ( "teamdates" in path):
           player=100472  #roger
           self.findPlayerTeams(player)   # go through entire player team list and get dates
        elif ( "home" in path):
           player=100472  #roger
           self.findPlayerTeams(player)   # go through entire player team list and get dates


#  Gets all Team Information ( dates,teammates, etc.)


    def roster( self,teamid):

      url  = "http://www.ustanorcal.com/teaminfo.asp?id="+str(teamid)
      result = urlfetch.fetch(url)
      scraped = result.content

      g = datastore.Roster( key_name = str(teamid) )   #key_name prohibits dups

      Writeln(self ," teaminfo ")

# ----Search for Home Facility (id and name)
#>Home facility: <a href=organization.asp?id=1787>Golden Gate Park Tennis Complex</a>
      pattern = r"Home facility: <a href=organization\.asp\?id=([\d]*)>([ \d\w]*)<"
      result = re.search( pattern,scraped,re.IGNORECASE )
      if( result != None) : 
        Writeln(self, "home_id= " , result.group(1)    )
        Writeln(self, "home_name= " , result.group(2) )
        g.home_id = result.group(1)
        g.home_name = result.group(2)

# ----Search for Team Name
      pattern = r"<title>([ \-\w\W\d]{0,100})<\/title>"
      m = re.search(pattern,scraped )
      name= ""
      nickname = ""

      if( m ):
        Writeln(self, m.group(1) + translate(m.group(1)) )
        name=m.group(1)
        nickname = translate(m.group(1))

# ----Search for Completed Match Times

      pattern = r"<a href=scorecard\.asp\?id=([\d]*)&[:l=\d]*>"
      pattern +=  r"([\d]{2})\/([\d]{2})\/([\d]{2})"

      r = re.compile(pattern,re.IGNORECASE )
      match = r.findall( scraped )
      Writeln( self, "COMPLETED" )
      completed=[]
      for i, d in enumerate(match):      #returns i(ndex) and a 3-Tuple
        month = int(d[1])
        day   = int(d[2])
        year  = int(d[3]) + 2000
        completed.append( datetime.date(year,month,day) )
        Writeln(self, d )

      g.completed = completed

#.completed
#.dates


# ----Search for Match Times
      rexp = r"nbsp;([\d]{2})\/([\d]{2})\/([\d]{2})"
      r = re.compile(rexp,re.IGNORECASE )
      match = r.findall( scraped )


      active=[]

      Writeln(self, "ACTIVE MATCHES" )
      for i,d in enumerate(match):      #returns i(ndex) and a 3-Tuple
           month = int(d[0])
           day   = int(d[1])
           year  = int(d[2]) + 2000
           active.append( datetime.date(year,month,day) )
           Writeln( self, month, day,year )

      g.active = active
      g.name = string.replace(name,"USTA NorCal - Team Information | ","",1)
      g.nickname = nickname

# ----Search for Players
      pattern = r"nowrap><a href=playermatches\.asp\?id=([\d]*)>([ \-\w\d\'\.]*)[, ]*([ \-\w\d\'\.]*)[ <>\w=#\d\/]*?nowrap>([ \w]*)"

      r = re.compile(pattern,re.IGNORECASE )
      match = r.findall( scraped )

      Writeln(self, "PLAYERS ")
      playerlist=[]
      for i, tuple in enumerate(match):      #returns i(ndex) and a 3-Tuple
        t = [ str(tuple[0]), str(tuple[1]) , str(tuple[2]) ]
        t =  str(tuple[0])+":"+str(tuple[1])+":"+str(tuple[2])
        Writeln( self, t )
        playerlist.append(t)

      g.players=playerlist

      h = datastore.Player( key_name = str(teamid) )   #key_name prohibits dups


      db.put ( g )                

# ---- All match dates
      Writeln( self, "<br>All Match Dates")
      qr =  datastore.Roster.get_by_key_name( str(teamid) )
      l = qr.active
      for e in qr.completed:
         l.append( e)

      l.sort()

      for e in l:
        Writeln( self, e )



#   Returm a list of team IDs
    def playerinfo( self,playerid):
        url  = "http://www.ustanorcal.com/playermatches.asp?id="+str(playerid)
        result = urlfetch.fetch(url)
        scraped = result.content

        pattern_league = r'>(20[\d]{2}) (Mixed|Adult|Combo)'
        pattern_teamID = r'<a href=\"teaminfo\.asp\?id=([\d]*)">'

        pattern = pattern_league + "|" + pattern_teamID

        r = re.compile( pattern ,re.IGNORECASE )
        match = r.findall( scraped )

        teams=[]
        year = datetime.datetime.now().year
        Writeln( self, year )
        for i, found in enumerate(match):      #returns i(ndex) and Tuple
 
             stripped = [ s for s in found if len(s)>0 ]
             Writeln(self, i, stripped )

             if stripped[0] =="2012" : break
             if stripped[0] =="2011" : break

             if len(stripped[0])> 4 : 
               teams.append( stripped[0])
             if i > 25 : break


        Writeln( self, teams )
        return teams


# Update roster.teams
# Go through each player on a Roster and get their teams
    def rosterteams( self,teamid):

        roster_key = db.Key.from_path("Roster",str(teamid) )

        Writeln(self, roster_key)
        roster = db.get(roster_key)   # roster exists

        if( roster == None):
          Writeln(self, " roster doesnt exist ")
          return

        Writeln(self, "Proceeding")
        Writeln(self, roster.players)

        accumulated=[]
        for n in roster.players:

           t = n.split(":")
           playerid = t[0]
           lname    = t[1]
           fname    = t[2]

           teamlist = self.scrap_teamIDs( playerid)
           Writeln(self, playerid,fname, lname, teamlist)
           accumulated = accumulated +  teamlist 

# Gather all the teams and keep unique ones
        set = sets.Set( accumulated)
        lset = list(set)
        lset.sort( key = str.lower )

        Writeln(self, len(lset) , lset )

        Writeln(self, "done")

        roster.teams = lset
        db.put( roster )

# for a player go their home page and get team IDs
    def scrap_teamIDs( self,playerid):

        url  = "http://www.ustanorcal.com/playermatches.asp?id="+str(playerid)
        result = urlfetch.fetch(url)
        scraped = result.content

        pattern_league = r'>(20[\d]{2}) (Mixed|Adult|Combo)'
        pattern_teamID = r'<a href=\"teaminfo\.asp\?id=([\d]*)">'

        pattern = pattern_league + "|" + pattern_teamID

        r = re.compile( pattern ,re.IGNORECASE )
        match = r.findall( scraped )

        teams=[]

        year = datetime.datetime.now().year
#       Writeln( self, year )
        year="2013"
        for i, found in enumerate(match):      #returns i(ndex) and Tuple

             stripped = [ s for s in found if len(s)>0 ]
#            0 ['2013', 'Mixed'] 
#            1 ['53825'] 
#            2 ['2013', 'Mixed'] 
#            3 ['54054'] 
#            Writeln(self, i, stripped )

             if stripped[0] =="2012" : break
             if stripped[0] =="2011" : break
             if stripped[0] =="2010" : break
             if stripped[0] =="2009" : break

             if len(stripped[0])> 4 : 
               teams.append( stripped[0])
             if i > 25 : break


#       Writeln( self, teams )
        return teams


    def CreatePlayerTeams( self,playerid):

       teams = self.scrap_teamIDs( playerid )

       for teamid in teams:
          active = self.scrapTeamDates(  teamid )
          Writeln( self, "Create team here for id ",teamid )
          Writeln( self, "ACTIVE DATES\n",active )
#         g =  datastore.Team.get_by_key_name( str(teamid) )
          g = datastore.Team( key_name = str(teamid) )   #key_name prohibits dups
          g.active = active
          g.put()


    def CreatePlayer( self,playerid):
          Writeln( self, "Create Player for id ", playerid )


          g = datastore.Player.get_by_key_name( str(playerid) )
          if( g == None ):
             Writeln( self, "Player doesnt exist, so creating " )
             g = datastore.Player( key_name = str(playerid) )
             teams =  self.scrap_teamIDs( playerid )
             g.teams = teams
             Writeln(self, "IDs=", teams)
             g.put()
# STOPPING PT


# From a teamid, get and save each player and their teams (cron job)
    def ___teamplayerinfo( self,teamid):

        t = datastore.Team.get_by_key_name( str(teamid) )
        Writeln(self, t.name )

        length =  len(t.players)

        playerlist = []
        name = ""
        for n in t.players:
            t= n.split(":") 
            Writeln(self, t )
            playerid = t[0]
            name = t[2] + " " + t[1]
            g = datastore.Player( key_name = str(playerid) )
            g.name = name
            g.teams = self.playerinfo(  playerid )   # This one takes a while
            playerlist.append(g)

        db.put( playerlist )




#   return a list of all the match dates of this team
    def scrapTeamDates( self,teamid):

      url  = "http://www.ustanorcal.com/teaminfo.asp?id="+str(teamid)
      result = urlfetch.fetch(url)
      scraped = result.content

# ----Search for Match Times
      rexp = r"nbsp;([\d]{2})\/([\d]{2})\/([\d]{2})"
      r = re.compile(rexp,re.IGNORECASE )
      match = r.findall( scraped )

      active=[]
      for i,d in enumerate(match):      #returns i(ndex) and a 3-Tuple
           month = int(d[0])
           day   = int(d[1])
           year  = int(d[2]) + 2000
           active.append( datetime.date(year,month,day) )

      return active

    def scrapPlayerTeams( self,playerid,playername):
        Writeln( self, "Find teams for player id=", playerid,"Player = ",playername)      
        g = datastore.Player.get_by_key_name( str(playerid) )

        for teamid in g.teams:
             active=self.researchTeamDates( teamid )
             Writeln(self, teamid, dates )
             if( active == None ): return
      


# Go through players on a team, and the schedule of get each team they're on
    def findPlayerTeams( self,teamid):

        Writeln(self, "findPlayerTeams from team",teamid )

        t = datastore.Team.get_by_key_name( str(teamid) )
        for p in t.players: 
              playerinfo = p.split(":")

              self.scrapPlayerTeams( playerinfo[0] , playerinfo[2]+" " +playerinfo[1] )




class MainPage (webapp2.RequestHandler):
   def get(self):

    print('Hello, WebApp World!')


app =  webapp2.WSGIApplication(  [ ('/', MainPage),
#                                  ('/hopkins', ScheduleHandler),

                                   ('/roster', ScheduleInfo),        # cron job
                                   ('/rosterteams', ScheduleInfo),   # cron


                                   ('/playerinfo', ScheduleInfo),      # per id get player teams
                                   ('/teamplayerinfo', ScheduleInfo),  # helper (test)
                                   ('/createplayerteams', ScheduleInfo),  # helper (test)
                                   ('/createplayer', ScheduleInfo),    # Create a player (from playerid)


#------ Helper Methods
                                   ('/scrap_teamids', ScheduleInfo),  # helper (test)
                                   ('/scrap_teamdates', ScheduleInfo),  # helper (test)


                                   ('/updateplayer', ScheduleInfo),
                                   ('/findteams', ScheduleInfo),
                                   ('/teamdates', ScheduleInfo),

                                   ('/home', ScheduleInfo)


                                 ],debug=True )

  
