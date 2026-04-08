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

from google.appengine.ext.webapp import template


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
class MATCH:
   date = ""
   where = "Home"
   balls=0


class TEAM:
   teamid   = 0
   players  = 0
   team = fname = lname = ""
   matches = [] 

class PLAYERS:
    unique= {}   # Dictionary


uniquePlayers = {}

class PlayoffsHandler( webapp2.RequestHandler):


    def get(self):

      Writeln(self, "<p>")

      idx = "113"
      url = "http://www.ustanorcal.com/organization.asp?id=" + idx

      url = "https://www.ustanorcal.com/Organization.asp?id=113&archive=Y"


      result = urlfetch.fetch(url,payload=None, method=urlfetch.GET)
      scraped = result.content

      rexp = r"ref=teaminfo\.asp\?id=([\d]*)>([ \d\w\/\.\(\)\-\\!']*)"

#     this only takes team if Registration is still open
      rexp = r"Register[ =#<\/>\d\w]*href=teaminfo\.asp\?id=([\d]*)>([ \+\d\w\/\.\(\)\-\\!']*)"
      rexp += r"[<>\/\w#= ]*align=left>([-\w\d]*)[, ]*([-\w\d]*)"

# 11/3/14  FIX Area is a new column 
      rexp = r"Register[ =#<\/>\d\w]*href=teaminfo\.asp\?id=([\d]*)>"    # ID

#    Closed season to get playoffs 
      rexp = r"Closed[ =#<\/>\d\w]*href=teaminfo\.asp\?id=([\d]*)>"    # ID

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

      limit = 0
      balls = 0
      usta = 0
      players = 0
      count_cans = 0
      count_players = 0

      teamList=[]
      for i,team in enumerate(match):

         teamid = team[0]
         name = team[1]

         limit += 1

#        if( limit > 7): break
#        if( int(teamid) == 86084): break  # Combo (70M7.0 Sperinde )
#        if( int(teamid) == 82855): break  # A.Dolor 40W4.5
         if( limit > 23): break
         if( limit > 62): break

#        Clear out CUPERTINO from the name, in order to extract the level (18M vs CM messes up)
         level = name
         level = re.sub("CUPERTINO TC","",name)
         level = re.sub("CUPERTINO SC","",level)
           
         m = re.search(regLevel , level )
         level = m.group(1)
# https://www.ustanorcal.com/teaminfo.asp?id=85644

         c = re.search(regCaptain , team[3])
         fname = c.group(2)
         lname = c.group(1)

         link = "https://www.ustanorcal.com/teaminfo.asp?id="+str(teamid)
         link = '<a href=\"' + link + '">' + name + "</a>"

         inc = 3

         r = level.find("18A")
         if( r>=0): inc = 5

         r = level.find("40AM")
         if( r>=0): inc = 5

         r = level.find("40AW")
         if( r>=0): inc = 5


         _matchList,balls,mates = BallCount( self, teamid, balls ,inc)

#   ************************************

         cup = TEAM()
         
         cup.teamid = teamid
         cup.team = name
         cup.fname = fname 
         cup.lname = lname 
         cup.matches = _matchList
         cup.players = mates

         teamList.append( cup )
         usta += 1
         players += mates


#   ************************************
#     END of loop

      print(uniquePlayers)

      template_values = {
               'teamList' : teamList,
               'usta': usta,
               'players':  players,
               'cans':  balls,
               'unique':  len( uniquePlayers)

          }

      path = os.path.join(os.path.dirname(__file__), 'templates','team.html')
      self.response.out.write(template.render(path, template_values))



def BallCount( selfobj, idx, count,increment):


      url = "http://www.sctennisclub.org/tcloud/tcloud.php?id=" + str(idx)
      req = urllib2.Request( url )
      response = urllib2.urlopen( req )
      scraped = response.read()

#     Writeln(selfobj, scraped )
#     REMOVE return,newline,tab
# Remove Show/Hide Details

      scraped= re.sub("<div class=\"alert alert-info scheduled-block\">([^~]*?)<\/div>","",scraped)

      scraped = scraped.replace("\r","")       
      scraped = scraped.replace("\n","")       
      scraped = scraped.replace("\t"," ")       

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

      patternPlay = r"PlayOff"   #playoff is in Match column
      patternDist= r"District"   #playoff is in Match column
      patternSect = r"Sectional"   #playoff is in Match column

      match = re.findall(pattern,scraped )

      matchList=[]
      for i,m in enumerate(match):  # returns list 0->6 of each found item
           status = ""                             # (Week)/Playoff/District/Sectional
           date = datetime.datetime(2000, 1,1 )   # Sometimes no match date
           desc = ""                              # Description of match 'All 3 at'
           opponent_id = ""                       # Opponent's team id
           opponent = ""                          # Opponent's team name
           where = ""                             # Home/Away
           delta = timedelta(hours=0)             # Time of match hr:min 
           wonlost = ""
           scorecardID = ""
           where = ""                             # Home/Away

           playoff= ""

#          match = re.findall(pattern,scraped )
           d = re.search(patternPlay, m[1])
           if (d != None):           
                 playoff = "PLAYOFF"

           d = re.search(patternDist, m[1])
           if (d != None):           
                 playoff = "DISTRICTS"

           d = re.search(patternSect, m[1])
           if (d != None):           
                 playoff = "SECTIONALS"


           _date  = m[2] 
           d = re.search(patternDate, _date)
           if (d != None):
              try:
                  month = d.group(1)
                  day   = d.group(2)
                  year  = d.group(3)
                  date = datetime.datetime(2000+int(year), int(month),int(day) )
              except:
                 print "Match Date: Unexpected exception"

           _status  = m[0] 
           _date  = m[2] 
           _desc  = m[4] 
           _opponent = m[5]
           _where =  m[6]
           _wonlost = m[7]


           if(( _where == "Home" and playoff=="") or (_where=="Home" and playoff=="PLAYOFF")  ):
            count += increment

           date =  str(month) + "/" + str(day) + "/" + str(year) 
           m = MATCH()
           m.date = date
           m.where = _where
           m.playoff = playoff
           m.balls = count
           matchList.append( m )

#          Writeln(selfobj, "" + str(month) + "/" + str(day) + "/" + str(year)  + " " + _where + " " + playoff + " ( " + str(count) + ")" )

#     for i,m in enumerate(match):  # returns list 0->6 of each found item
      playercount = PlayerCount( scraped )


      return matchList,count,playercount
#     return date,_where, playoff, count

def PlayerCount(  scraped ):
      rexp = r"nowrap><a href=playermatches\.asp\?id=([\d]*)>"
      rexp += r"([^~]*?)</a></td>"

#      rexp += r"<td ([^~]*?)</td>"  #City
#      rexp += r"<td ([^~]*?)</td>"  # Gender
#      rexp += r"<td ([^~]*?)</td>"  # Rating
#      rexp += r"<td ([^~]*?)</td>"  # NP/SW
#      rexp += r"<td ([^~]*?)</td>"  # Expiration

#     rexp = r"nbsp;Playoff<"
     
      r = re.compile(rexp,re.IGNORECASE )
      player = r.findall( scraped )

#     print(  " " )
      for f in player:
       uniquePlayers[f[0] + " " + f[1] ] = 1
#      print( f[0] + " " + f[1]  )


      return len(player)

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

      rexp = r"nbsp;Playoff<"


      r = re.compile(rexp,re.IGNORECASE )
      player = r.findall( scraped )

      Writeln(self, player)

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



app = webapp2.WSGIApplication(
                                     [
                                      ('/playoffs', PlayoffsHandler)

                                     ],
                                      debug=True)



