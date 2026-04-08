import os
from google.appengine.ext.webapp import template

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from google.appengine.ext import db

import urllib
from google.appengine.api import urlfetch

import re,sys
import datastore
import datetime

import library

from google.appengine.api import users

#from google.appengine.dist import use_library
#use_library('django','1.2')



class GetTeams(webapp.RequestHandler):
    def get(self):

        self.response.headers['Content-Type'] = 'text/html'

        fac =  self.request.get('facility') 
        facilityid,facility = library.getfacilityNameID( fac)

        startposition =  self.request.get('start') 
        endposition =  self.request.get('end') 

        print("get teams")
        print("facility = " + facility  + "(" + facilityid + ")" )
        print("start = " + startposition  + ", end=" + endposition  )
        print("<br>"  )

        url  = "http://www.ustanorcal.com/organization.asp?id="+facilityid
        result = urlfetch.fetch(url)

        scraped = result.content

#       this doesn't account for closed season
        rexp = r"ref=teaminfo\.asp\?id=([\d]*)>([ \d\w\/\.\(\)\-\\!']*)"

#       this only takes team if Registration is still open
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
        for i,team in enumerate(match):
          count = count+1
#         if( count < int(startposition) ) : continue
          if( count > int(endposition) ) : break

          g = datastore.FacilityTeam( key_name= team[0] )
          g.position = int(i)
          g.facility = int(facilityid)
          g.teamid = int(team[0])   #0: id
          g.name = team[1]          #1: team name
                                    #2: area (new (11/5/14)                                  
                         
          captain = team[3]
          reName = r" \w\d\-\'"
          m = re.search(r"left>(["+ reName+ "]*)[ ,](["+ reName + "]*)" , captain)
          g.captain = team[2]+","+team[3]
          g.captain  = m.group(1) + "," + m.group(2)
          teamlist.append( g )


#   Put into db with a single call
        db.put( teamlist )
        print(" ")
        for t in teamlist:
         print(str(t.position)+ ") " + str(t.teamid) + " " +t.name +","+t.captain + "<br>")


class GetPlayers(webapp.RequestHandler):

   def Write(self,t):
       self.response.out.write(t)

   def get(self):

       facility = library.getfacility(self)

       startposition =  self.request.get('start') 
       endposition   =  self.request.get('end')
       if( startposition == '' or endposition==''):
           startposition= '0'
           endposition= '10'



#      query = 'select * from FacilityTeam where position>='+ startposition + ' and position<='+ endposition + ' order by position'
       query = 'select * from FacilityTeam where facility='+ facility + ' and position>='+ startposition + ' and position<='+ endposition + ' order by position'

       print query
       teams =  db.GqlQuery(query )


       for team in teams:
          self.scrapeteam( facility,team.teamid,team.name,team.captain)

   def scrapeteam(self, facility, idx,name, captain):

       url = "http://www.ustanorcal.com/teaminfo.asp?id=" + str(idx)

       self.Write( 20*'*>' )
       self.Write( '<br>' + str(url)  + '<br>')

       result = urlfetch.fetch(url)
       scraped = result.content
# <a href=playermatches.asp?id=15067>Lynch, Carl H 
#   print scraped   
#   Get id , lname,fname,city
       rexp = r"nowrap><a href=playermatches\.asp\?id=([\d]*)>([ \-\w\d\'\.]*)[, ]*([ \-\w\d\'\.]*)[ <>\w=#\d\/]*?nowrap>([ \w]*)"

#   Get id , lname,fname,city, place holder, rating
       rexp = r"nowrap><a href=playermatches\.asp\?id=([\d]*)>([ \-\w\d\'\.]*)[, ]*([ \-\w\d\'\.]*)[ <>\w=#\d\/]*?nowrap>([ \w]*)([ <>\/=#\d\w]*>)(\d\.\d)"


#                                                id        lname               fname                                city
       rexp = r"<a href=playermatches\.asp\?id=([\d]*)>([ \-\w\d\'\.]*)[, ]*([ \-\w\d\'\.]*)[ <>\w=#\d\/]*?nowrap>([ \w]*)"
#                                              gender                  rating
       rexp += r"([ <>\/=#\d\w]* align=center)>(M|F)<([ \/td<>=#\d\w]*)>(\d\.\d\w)*<"
#      0: id 1: lname 2: fname 3: city 4:  5: gender 6: 7: rating


#      Get the player name
       r = re.compile(rexp,re.IGNORECASE )
       player = r.findall( scraped )

#      Get the roster date
       rexp2 = r"align=center>([\d]{1,2}\/[\d]{1,2}\/[\d]{2})<\/td><\/tr>";
       r2 = re.compile( rexp2, re.IGNORECASE)
       roster = r2.findall( scraped )


#      Number of players equals number of roster dates
       plen = len(player)
       rlen = len(roster)
       self.Write( '<br>' + str(idx) + " " +  name + " " + captain + " " + str(rlen) + ' ' + str(plen) + '<br>')

#      Stop here if something is wrong
       if( plen != rlen):
          self.Write('STOP ')
          self.Write('len of player != roster ')
          return

       rlist=[]


       for id,name in enumerate(player):
#   name = (player_id, lname, fname )   
         url = "http://www.ustanorcal.com/playermatches.asp?id="+name[0]

         r = datastore.FacilityRoster( key_name= str(idx)+"_"+name[0] )   #key_name prohibits dup entries
         r.teamid = idx
#      0: id 1: lname 2: fname 3: city 4:  5: gender 6: 7: rating
         r.playerid = int(name[0])
         r.lname = name[1]
         r.fname = name[2]
         r.city   = name[3]      
         r.gender   = name[5]
         r.rating   = name[7].lower()
         r.roster= roster[id]
         r.facility = int(facility)
         d = r.roster.split('/')
         r.date = datetime.date( 2000+int(d[2]),int(d[0]),int(d[1]) )

         rlist.append(r)
         self.Write( str(r.playerid) + ') ' + r.fname+' '+ r.lname + ' ' + r.city + ' ' + r.gender + ' ' + r.rating + ' ' + r.roster + '<br>' )

#   Put into db in one call
       db.put(rlist)


# GetTeams    Gets all teams at a facility
# GetPlayers  ?start=1&end=10   Gets players on a team from start to end
application = webapp.WSGIApplication(
                                     [('/team', GetTeams),
                                     ('/player', GetPlayers)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":



#   print __file__
#   print __name__


    main()

