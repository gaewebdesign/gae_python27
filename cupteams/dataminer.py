import webapp2

from google.appengine.api import urlfetch


from google.appengine.ext import db
from google.appengine.ext import ndb

from datetime import timedelta

import urllib,re,datetime,string,sys,os

import mysession
import logging

import user

import library

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


def WantPlayer( self):
      Writeln( self, "WantPlaye ")

# Scrap this player, for  the team IDs
# TODO LIMIT BACK SEARCH, YEAR isnt working!
def scrap_teamIDs( self,URLContent):

        scraped = URLContent

        pattern_league = r'>(20[\d]{2}) (Mixed|Adult|Combo|Tri-Level)'
        pattern_teamID = r'<a href=\"teaminfo\.asp\?id=([\d]*)">'

        pattern = pattern_league + "|" + pattern_teamID

        r = re.compile( pattern ,re.IGNORECASE )
        match = r.findall( scraped )

        teams=[]

        year = datetime.datetime.now().year
        Writeln( self, year )
        year=year-1    # limit to last year
        for i, found in enumerate(match):      #returns i(ndex) and Tuple

             league = [ s for s in found if len(s)>0 ]
#            0 ['2013', 'Mixed'] 
#            1 ['53825'] 
#            2 ['2013', 'Mixed'] 
#            3 ['54054'] 
             Writeln(self, i, league )

             if int(league[0]) < year : break
             if league[0] =="2012" : break


             if len(league[0])> 4 : 
               teams.append( league[0])
             if i > 26 : break


#       Writeln( self, teams )
        return teams

# Just a one time hack
def login(self, pid):
        playerid = int(pid)
        if(playerid == 32778):
           username = "lori"
        elif(playerid == 58252):
           username = "cindy"
        elif(playerid == 167135):
           username = "cjarvis"
        elif(playerid == 20832):
           username = "carrie"
        elif(playerid == 100472):
           username = "roger"
        elif(playerid == 114432):
           username = "gary"
        elif(playerid == 94120):
           username = "jay"
        elif(playerid == 172141):
           username = "kelly"
        elif(playerid == 114432):
           username = "gary"
        elif(playerid == 48970):
           username= "stephen"
        elif(playerid == 21917):
           username = "suzanne"
        elif(playerid == 169090):
           username = "johnny"
        elif(playerid == 48970):
           username = "stephen"
        else:
           username = "roger"

        return username


def GetPlayer(self, playerid):
#     Writeln( self, "GetPlayer")

# Scrap the USTA player (do this once)
      url  = "http://www.ustanorcal.com/playermatches.asp?id="+str(playerid)
      result = urlfetch.fetch(url)
      scraped = result.content

      logging.info("Log info")
      logging.debug("Get player information")

      playerKey = ndb.Key(Player, str(playerid) )
      g = Player.get_by_id( str(playerid) )

      if( g != None):
         Writeln( self, "Player exists " )
         Writeln( self, g )
      else:
         g = Player( key=playerKey)
         Writeln( self, "Player created " )
         Writeln( self, g )

#     self.scrap_PlayerName(  playerid) # NO LONGER USED 1/7/15 
      pattern = 'bgcolor="white"><font size="3"><b>'
      pattern = '([ \w\d\-]*)'
      pattern += '</b>'
      r = re.compile( pattern ,re.IGNORECASE )
      match = r.findall( scraped )
      playername = match[0]

#  Set the Player's name in the model
      g.name = playername
      Writeln(self, g )
      Writeln(self,"g.login = "+ str(g.login) )
      g.login = g.login
      print("Player.login = " + str(g.login) )

# just a one time hack
#      g.login = login(self,playerid)

      Writeln( self, "Player is ", g.name )

# Get the teams
      teams =  scrap_teamIDs( self, scraped )

      Writeln(self, "ADD TEAMS TO DB " )
      tlist=[]
      for t in teams:
        d = IDList()
        d.desc = "-"
        d.id=t

        if( d.id == "55535"):
          Writeln(self, "SKIPPING ", d.id )
          continue

        if( d.id == "53864"):
          Writeln(self, "SKIPPING Walnut Creek 8.5", d.id )
          continue

        tlist.append(d)

      g.teams = tlist
      Writeln(self, "teams", g.teams )

      g.put()

def CreateTeam( self, teamid, ObjTeam):
      Writeln( self, "CreateTeam (" + str(teamid) +")" )      
      url  = "http://www.ustanorcal.com/teaminfo.asp?id="+str(teamid)
      result = urlfetch.fetch(url)
      s = result.content


#     REMOVE return,newline,tab
      s = s.replace("\r","")       
      s = s.replace("\n","")       
      s = s.replace("\t"," ")       

      scraped = s

# Remove Show/Hide Details
# <div class="alert alert-info scheduled-block">
# ......
# </div>
#<div class="alert alert-info scheduled-block">                    Last schedule update: 12/22/2014 8:48:30 PM                    <br>User:Perry R  Segal                </div>
      scraped= re.sub("<div class=\"alert alert-info scheduled-block\">([^~]*?)<\/div>","",scraped)

# Get the team name
      pattern = r"<title>([ \w\d-]*)\|([ \/\w\d\.]*)"
      m = re.search( pattern ,scraped)
      teamname=""
      if(m):
        teamname = m.group(2).lstrip().rstrip()
        Writeln(self,"group(1) = ", m.group(1).lstrip() )
        Writeln(self,"Team Name = ",teamname )

#   0 name=status> Status  </td>   
#   1   <td> Match       </d>      Unused (this is the week)
#   2   <td> Match date  </td>    
#   3   <td> Day         </td>     Unused 
#   4   <td  Match time </td>
#   5   <td> Opponent Team   </td>     Both  ID and team name
#   6   <td> Home/Away   </td>   


      pattern = r"<a name=status>(Scheduled|Confirmed|Verify)[^.]*?</td>"  #0: Status (Confirmed/Scheduled)
      pattern += r"<td([^.]*?)</td>"      # 1: Match  (could be Playoffs/Districts/Sectionals or the week)

      pattern += r"<td([^']*?)</td>"      # 2: Date
      pattern += r"<td([^.]*?)</td>"      # 3: Day (unused)
      pattern += r"<td>([^<]*?)</td>"      # 4: Match time
      pattern += r"<td([^~]*?)</td>"          # 5: Opposing Team (ID/Team)
      pattern += r"<td[^.]*?>(Home|Away)</td>"     # 6: Home/Away

      pattern += r"<td[^.]*?>([WonLost \d\-]*)</td>"     # 7: Win 4-1 or Lost 1-4 or -

#     PATTERN to extract information between <td>  </td>
      patternDate   =  r"([\d]{2})\/([\d]{2})\/([\d]{2})"
      patternDate   =  r"([\d]{1,2})\/([\d]{1,2})\/([\d]{1,2})"

      patternScorecard   =  r"id=([\d]*)"

      patternTime   = r"([\d]{1,2}):([\d]{1,2})[ ]([AM|PM]{2})"
      patternID = r"id=([\d]*)"  #extract teamid/team
      patternTeam = r"id=[\d]*>([^`]*?)<"  #extract teamid/team
      patternWonLost = r"([\d]-[\d])"   #won/lost


      match = re.findall(pattern,scraped )

      scheduledList=[]
      confirmedList=[]
      Writeln(self, "SEASON MATCHES = " + str(len(match)) )
      for i,m in enumerate(match):  # returns list 0->6 of each found item

#          Initial Conditons
           status = ""                             # (Week)/Playoff/District/Sectional
           date = datetime.datetime(2000, 1,1 )   # Sometimes no match date
           desc = ""                              # Description of match 'All 3 at'
           opponent_id = ""                       # Opponent's team id
           opponent = ""                          # Opponent's team name
           where = ""                             # Home/Away
           delta = timedelta(hours=0)             # Time of match hr:min 
           wonlost = ""

           scorecardID = ""

           _status  = m[0] 
#          1: Match column is unused
           _date  = m[2] 
#          3: Day column is unused
           _desc  = m[4] 


           _opponent = m[5]
           _where =  m[6]

           _wonlost = m[7]

           patternDate   =  r"([\d]{1,2})\/([\d]{1,2})\/([\d]{1,2})"
           m = re.search(patternDate, _date)
           if (m != None):
              try:
                  month = m.group(1)
                  day   = m.group(2)
                  year  = m.group(3)
                  date = datetime.datetime(2000+int(year), int(month),int(day) )
              except:
                 print "Match Date: Unexpected exception"

           # only gets run if the match is confirmed
           m = re.search(patternScorecard, _date)  
           _scorecardID = 0
           if(m!=None):
              _scorecardID = m.group(1)

           _desc = _desc.replace("&nbsp;"," ")
           _desc = _desc.rstrip(" ")
           _desc = _desc.lstrip(" ")


           m = re.search(patternTime ,  _desc)
           if( m != None ):
              try:
                 hr = m.group(1)
                 min = m.group(2)
                 am   = m.group(3)
                 delta = timedelta(hours=int(hr) , minutes=int(min) )
                 if( am=="PM" and int(hr)!=12): delta = delta + timedelta(hours=12)
              except:
                 print "Match Time: Unexpected Exception"


           m =re.search(patternID ,  _opponent)
           if( m != None ):
              try:
                 opponent_id = m.group(1)
              except:
                 print "Opponent id: Unexpected Exception"

           m = re.search(patternTeam, _opponent)
           if( m != None ):
              try:
                 opponent = m.group(1)
                 if( opponent[-1:]== "1" or opponent[-1:]== "2"): 
                   opponent = opponent[:-1] 
              except:
                 print "Opponent: Unexpected exception"

           Writeln(self, "")
           Writeln(self, "Match =", _status )
           Writeln(self, "Date = " ,date+delta)
           Writeln(self, "Time = " ,delta)
           Writeln(self, "Desc = ",_desc )
           Writeln(self, "Opponent ID = ",opponent_id)
           Writeln(self, "Opponent = ", opponent)
           Writeln(self, "Where = ",_where)
           Writeln(self, "Won/Lost = ",_wonlost)
           Writeln(self, "Scorecard ID = ",_scorecardID)

           m = MatchList()    
           m.status = _status
           m.desc = _desc
           m.date = date+delta
           m.opponent_id = opponent_id   
           m.opponent = opponent  
           m.where = _where
           m.match = _wonlost

           Writeln(self,"m.status = "+ m.status)
           if( m.status == "Scheduled"):
                Writeln(self, "ADD to Scheduled List")
                scheduledList.append(m)
                Writeln(self, m)
           elif( m.status == "Confirmed" ):
                Writeln(self, "ADD to Confirmed List")
                confirmedList.append( m)   
           elif( m.status == "Verify" ):
                Writeln(self, "ADD to Confirmed List (Verify)")
                confirmedList.append( m)   

           else:
                Writeln(self, "didnt match either")
          
# Players on this team (id,lname,fname)
#     ------ outside loop -------
      pattern = r"<a href=playermatches\.asp\?id=([\d]*)>([^.]*?)[,]([^.]*?)</a></td><td"

      r = re.compile(pattern,re.IGNORECASE )
      match = r.findall( scraped )
      Writeln(self, "PLAYERS (information only, not used)")
      for i, tuple in enumerate(match):      #returns i(ndex) and a 3-Tuple
            Writeln(self, i, tuple)

# Create the Team Object
      pteamKey = ndb.Key(ObjTeam, str(teamid) )
      o = pteamKey.get()
      if( o != None):
            Writeln(self, "Team exists")
      else:
            Writeln(self, "Team create")
            o = ObjTeam( key=pteamKey)
            o.name = teamname
            o.alias = library.Alias(teamname)

# Store into Db
      o.scheduled=scheduledList
      o.confirmed=confirmedList
      Writeln(self, "Store to DB *" + "*"*30)
      Writeln(self, o.scheduled)
      Writeln(self, o.confirmed)

#     Writeln(self, "Skipping store")
      Writeln(self, "STORE INTO DATA BASE")
      o.put()


# START from here to get the player teams (calls CreateTeam)
def GetPlayerTeams(self, playerid):
#     Writeln( self, "Create Team for id= ",teamid)
      g=Player.get_by_id( str(playerid) )


      tlist = g.teams
      limiting=0
      for t in tlist:
         limiting += 1
         logging.info("team id = " + str(t.id) )
         Writeln(self, "*"*25 )
         Writeln(self, str(limiting)+ ") CreateTeam(" + str(t.id) + ")")
         Writeln(self, "*"*25 )
         CreateTeam(self, t.id, PTeam)


class MainHandler(webapp2.RequestHandler):

    def get(self):

      url = "http://"+os.environ["SERVER_NAME"]
      if (re.search("localhost",url )): url = "http://localhost:8080"

      now = datetime.datetime.now()
      month = str(now.month) 
      year  = str(now.year) 

      self.redirect(url+"/month/"+month+"/"+year)


# Use session for browser update
class TeamHandler(mysession.BaseHandler):

    def get(self):

      playerid = 100472  #Roger
      user = self.session.get('user')        # USTA name
      id   = self.session.get('id')    # USTA id

      if(id):
          playerid=id
    
# Use this to call from another routine
      GetPlayerTeams( self,playerid)



class PlayerHandler(mysession.BaseHandler):

    def get(self):

#     path = self.request.path
#     logging.getLogger().setLevel(logging.DEBUG)

      playerid = 100472  #Roger

      user = self.session.get('user')  # USTA name
      id   = self.session.get('id')    # USTA id

      if(id):
          playerid=id

# Use this to call from another routine
      GetPlayer( self, playerid)

class CronHandler(mysession.BaseHandler):

    def get(self):
      Writeln(self,"CRON Jobber")

#     Skip if player updated within last 2 days
      past = datetime.datetime.now() - datetime.timedelta(hours = 48,minutes=30)

#     Switch these around to test
      query = Player.query().order(Player.timestamp).fetch(3)
      query = Player.query().order(Player.timestamp).filter(Player.timestamp < past).fetch(3)

      for p in query:
          Writeln( self, p.key.id() + "  " + str(p.timestamp))
          print(self, "CRON " + p.name + " id=" + p.key.id() + " time=" + str(p.timestamp))
          ustaID = str(p.key.id())

          GetPlayer( self, ustaID )
          GetPlayerTeams( self,ustaID)


app = webapp2.WSGIApplication(
                                     [
                                      ('/', MainHandler),
                                      ('/main', MainHandler),
                                      ('/getplayer', PlayerHandler),
                                      ('/getplayerteams', TeamHandler),
                                      ('/cron', CronHandler)
                                     ],
                                      debug=True,config=mysession.config)



