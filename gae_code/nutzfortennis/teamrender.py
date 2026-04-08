import os
from google.appengine.ext.webapp import template

from google.appengine.ext import db
import webapp2

import re,sys,string,datetime
import datastore

class Player:
    fname=lname=usta_id=""
    teamid=0

class Date:
    day=month=""

class TeamRender(webapp2.RequestHandler):
    def get(self):


     teamid=54054  # Hopkins
     teamid=52567  # GGPark
     self.render(teamid)

    def render(self,teamid):

     result =  datastore.Team.get_by_key_name( str(teamid) )

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



app =  webapp2.WSGIApplication(  [ ('/team', TeamRender)

                                 ],debug=True )

