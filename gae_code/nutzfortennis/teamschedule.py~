import os
from google.appengine.ext.webapp import template

import webapp2

#from google.appengine.ext import webapp
#from google.appengine.ext.webapp.util import run_wsgi_app

from google.appengine.ext import db

import urllib
from google.appengine.api import urlfetch

import re,sys,string,datetime
import datastore


class Player:
    fname=lname=usta_id=""
    teamid=0

class Date:
    day=month=""


# gets a player entire schedule, all active teams 
class PlayerSchedule(webapp2.RequestHandler):

    def get(self):

      playerid=11507   # GR
      self.getPlayerSchedule(playerid)

    def getPlayerSchedule( self,playerid):
      t = datetime.datetime(2013,7,4)

      self.response.headers['Content-Type'] = 'text/html'
      print "date<br>"
      print t.month,t.day,t.year, "<br>"

      url  = "http://www.ustanorcal.com/playermatches.asp?id="+str(playerid)
      result = urlfetch.fetch(url)
      scraped = result.content

      team = r'nowrap\"><a href="teaminfo\.asp\?id=([\d]*)">([ .\[\]\d\w\/]*)[<b>Captain</b>]*</a>'

      combine = team
      r = re.compile(combine ,re.IGNORECASE )
      match = r.findall( scraped )
 
      teams=[]
      for i, tuple in enumerate(match):      #returns i(ndex) and a 3-Tuple
        print tuple,"<br>"
        teams.append( tuple[0])
        if i>6 : break

      g = datastore.Player( key_name = str(playerid) )   #key_name prohibits dup entries
      g.playerid = playerid
      g.teams = teams
      db.put( g )

class TeamSchedule(webapp2.RequestHandler):

    def get(self):


      team=52981  # Cupertino
      team=53996  # SCTC
      team=52567  # GGP
      team=54054  # Hopkins

      self.getTeamInfomation( team )

    def getTeamInfomation(self,teamid):


      url  = "http://www.ustanorcal.com/teaminfo.asp?id="+str(teamid)
      result = urlfetch.fetch(url)
      scraped = result.content


      g = datastore.Team( key_name = str(teamid) )   #key_name prohibits dups

# ----Search for Team Name
      pattern = r"<title>([ \-\w\W\d]{0,100})<\/title>"
      m = re.search(pattern,scraped )
      name= ""
      nickname = ""


      if( m ):
        print m.group(1),self.translate(m.group(1)),"<br>"
        name=m.group(1)
        nickname = self.translate(m.group(1))

# ----Search for Completed Match Times

      pattern = r"<a href=scorecard\.asp\?id=([\d]*)&[:l=\d]*>"
      pattern +=  r"([\d]{2})\/([\d]{2})\/([\d]{2})"

      r = re.compile(pattern,re.IGNORECASE )
      match = r.findall( scraped )
      print "COMPLETED<br"
      completed=[]
      for i, d in enumerate(match):      #returns i(ndex) and a 3-Tuple
        month = int(d[1])
        day   = int(d[2])
        year  = int(d[3]) + 2000
        completed.append( datetime.date(year,month,day) )
        print d

      g.completed = completed

#.completed
#.dates


# ----Search for Match Times
      rexp = r"nbsp;([\d]{2})\/([\d]{2})\/([\d]{2})"
      r = re.compile(rexp,re.IGNORECASE )
      match = r.findall( scraped )


      dates=[]

      print "FUTURE<br>"
      for i,d in enumerate(match):      #returns i(ndex) and a 3-Tuple
           month = int(d[0])
           day   = int(d[1])
           year  = int(d[2]) + 2000
           dates.append( datetime.date(year,month,day) )
           print d,month,day,year
           print "<br>"

      g.dates = dates
      g.name = string.replace(name,"USTA NorCal - Team Information | ","",1)
      g.nickname = nickname

# ----Search for Players
      pattern = r"nowrap><a href=playermatches\.asp\?id=([\d]*)>([ \-\w\d\'\.]*)[, ]*([ \-\w\d\'\.]*)[ <>\w=#\d\/]*?nowrap>([ \w]*)"

      r = re.compile(pattern,re.IGNORECASE )
      match = r.findall( scraped )

      playerlist=[]
      for i, tuple in enumerate(match):      #returns i(ndex) and a 3-Tuple
        t = [ str(tuple[0]), str(tuple[1]) , str(tuple[2]) ]
        t =  str(tuple[0])+":"+str(tuple[1])+":"+str(tuple[2])
        print t,"<br>"
        playerlist.append(t)

#     print playerlist

      g.players=playerlist
      db.put ( g )                

# ---- All match dates
      print "Match Dates<br>"
      qr =  datastore.Team.get_by_key_name( str(teamid) )
      l = qr.dates
      for e in qr.completed:
         l.append( e)

      l.sort()

      for e in l:
        print e,"<br>"



    def getSchedule(self,teamid):

      self.response.headers['Content-Type'] = 'text/html'


      url  = "http://www.ustanorcal.com/teaminfo.asp?id="+str(teamid)
      result = urlfetch.fetch(url)
      scraped = result.content

      pattern = r"<title>([\-\|\/\. \w\d]*)<\/title>"
      pattern = r"<title>( \w\d]*)"

      rexp = r"Register[ =#<\/>\d\w]*href=teaminfo\.asp\?id=([\d]*)>([ \+\d\w\/\.\(\)\-\\!']*)"
      rexp = r"nbsp;([\d]{2})\/([\d]{2})\/([\d]{2})"
#     rexp = r"([\d]{2})"


#Home facility: <a href=organization.asp?id=3483>Santa Clara Tennis Center at Central Park</a
      pattern = r"Home facility: <a href=organization\.asp\?id=[\d]*>([ \d\w]*)<"
      pattern = r"(Home facility: <a)"
      pattern = r"<a href=organization\.asp\?id=[\d]*>([ \d\w]*)"

      pattern = r"<title>([ \w\W]*>)"

      result = re.search( pattern,scraped,re.IGNORECASE )
      if result != None : print result.group()

      print "<br>"
      r = re.compile(rexp,re.IGNORECASE )
      match = r.findall( scraped )

      g = datastore.Team( key_name = str(teamid) )   #key_name prohibits dup entries
      dates=[]

      for i,d in enumerate(match):      #returns i(ndex) and a 3-Tuple
           month = int(d[0])
           day   = int(d[1])
           year  = int(d[2]) + 2000
           dates.append( datetime.date(year,month,day) )
           print d,month,day,year
           print "<br>"


      g.dates = dates
      g.name = "Cupertino Mx8.0"
      g.nickname = "Cup"
      db.put ( g )          

    def translate( self, name):

        t = { ("Santa Clara", "SC"),  ("Los Gatos", "LG")

        }

        for x in t: 
          if( x[0].lower() in name.lower() ): return x[1]

        return "L"

class Display(webapp2.RequestHandler):
    def get(self):

     teamid=52567  # GGPark
     teamid=54054  # Hopkins

     result =  datastore.Team.get_by_key_name( str(teamid) )
     self.response.headers['Content-Type'] = 'text/html'


# Get all the match dates  (combined completed with yet to be played)
     d=result.dates
     for e in result.completed:
        d.append(e)
     d.sort()

     datelist=[]
     for e in d:
         t = Date()
         t.day = e.day
         t.month = e.month
         datelist.append(t)        

# Get all the team players
     players = result.players
     playerlist=[]
     for p in players:
        t = Player()
        s = p.split(":")
        t.ustaid = s[0]
        t.lname  = s[1]
        t.fname  = s[2]
        playerlist.append(t)


#     for x in datelist:
#          print x.month,x.day,"<br>"     

#     for p in playerlist:
#        print p.ustaid, p.fname, p.lname,"<br>"     


     template_values = {
            'Player' : playerlist,
            'Dates' : datelist,
            'matches'   : len(datelist)
     }
     path = os.path.join(os.path.dirname(__file__), 'display.html')
     self.response.out.write(template.render(path, template_values))


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


class GetHome(webapp2.RequestHandler):

    def get(self):

      self.response.headers['Content-Type'] = 'text/html'
      teamid=54054  # Hopkins      
      teamid=54055  # Hopkins      
      url  = "http://www.ustanorcal.com/teaminfo.asp?id="+str(teamid)
      result = urlfetch.fetch(url)
      scraped = result.content



      pattern = r"(Home facility: <a)"
      pattern = r"<a href=organization\.asp\?id=([\d]*)>([ \d\w]*)"
      pattern = r"Home facility: <a href=organization\.asp\?id=([\d]*)"
      pattern = r"Home facility: <a href=organization\.asp\?id=([\d]*)"


      pattern = r"Home facility: <a href=organization\.asp\?id=([\d]*)>([ \d\w]*)<"

      result = re.search( pattern,scraped,re.IGNORECASE )
      if result != None : 
        print "id= " , result.group(1), "<br>"
        print "name= " , result.group(2), "<br>"

      print "<br>"


#>Home facility: <a href=organization.asp?id=1787>Golden Gate Park Tennis Complex</a>


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



 
#
#application = webapp.WSGIApplication(
#                                     [('/schedule', TeamSchedule),
#                                       ('/display', Display),
#                                       ('/player', PlayerSchedule),
#
#
#                                      ('/score', GetScorecard),
#                                      ('/home', GetHome),
#                                      ('/players', GetPlayers),
#                                      ('/team[s]', GetTeams)
#                                     ],
#                                     debug=True)

#def main():
#    run_wsgi_app(application)

#if __name__ == "__main__":


#    main()




class MainPage (webapp2.RequestHandler):
   def get(self):

    self.response.headers['Content-Type'] = 'text/html'
    print('Hello, WebApp World!')
    print('Hello, WebApp World!')


app =  webapp2.WSGIApplication(  [ ('/', MainPage) ] )

  
