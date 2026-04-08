from google.appengine.ext.webapp import template
# new Python 2.7 imports
import webapp2    # Python 2.7
from google.appengine.ext import ndb

import urllib
import os,re,cgi,calendar,string,types
import datetime,time

from operator import itemgetter

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


# 
class Cupertino:
   rdate=fname=lname=team=captain=position=""
   timestamp =""

class Level:
     position=0
     level=""

#  def __cmp__(self, other):
#   if hasattr(other,'getKey'):
#      return self.getKey().__cmp__(other.getKey() )

#   def getKey(self):
#        return self.rdate

class DisplayHandler( webapp2.RequestHandler):
   def get(self):



#     regGroup = "([\d]{2})([\w]{2})([\d\.\w]{4})"

#  Put leagues into dictionary (18M3.0,18M3.5,.... 18W3.5, ...40M3.0.. )
      levelDict={}
      q = Team.query().order(Team.position)

      print("put levels into dictionary")
      for p in q.fetch():
           levelDict[p.level] =  p.position   
           print(p.level + " : "  + str(p.position)   )

#  Put into array of Level()
      LevelList=[]
      for key in levelDict:
          l  = Level()
          l.position = levelDict[key]
          l.level = key
          LevelList.append(l)
          print(key , levelDict[key])

#  Want leagues in order
      LevelList.sort(key=lambda x: x.position, reverse=False)
      print("SORTED : t.position,t.level")
      for t in LevelList:
          print(t.position,t.level)

# -----------------------------------------------------------------------------
      PlayerList=[]
      q = Team.query().order(Team.timestamp)
#     Writeln(self, Player.kind() )
      for p in q.fetch():
          u = Team()
          u.name = p.name
          u.level = p.level
          u.captain = p.captain
          u.id = p.key.id()
          u.timestamp = p.timestamp - datetime.timedelta(hours=8)

#         Writeln(self, str(u.id) + " " + u.level + " " + u.name + " " +u.captain)
          if  p.roster:
#           Writeln(self, p.roster)
#           Writeln(self, "")

            for q in p.roster:

              cup = Cupertino()
# from the Roster
              cup.fname = q.fname
              cup.lname = q.lname            
              cup.rdate = q.rdate
              cup.timestamp = q.timestamp

#  from the Team
              cup.team = p.name
              cup.captain = p.captain

# Check
#              Write(self, cup.fname + " " + cup.lname + " " + cup.rdate )
#              Write(self, cup.name)
#              Writeln(self, cup.timestamp)

              PlayerList.append(cup)



      PlayerList.sort(key=lambda x: x.timestamp, reverse=True)
      template_values = {'PlayerList' : PlayerList,
                         'Levels' : LevelList
             }

      path = os.path.join(os.path.dirname(__file__), 'templates','display.html')
      self.response.out.write(template.render(path, template_values))


class LevelHandler( webapp2.RequestHandler):
   def get(self,level):

#     Writeln(self,level)
      query = Team.query(Team.level==level).order(Team.position)


#
#      for pTeam in query:
#           Writeln(self,pTeam.name + " " + pTeam.captain)
#           for r in pTeam.roster:
#             Write(self, r.fname + " " + r.lname + " " + r.city )
#             Writeln(self," " + r.ntrp + " " + r.rdate )

# pTeam  name,teamid,captain
# Roster fname,lname,city,ntrp,rdate

      template_values = {
                         'Levels' : query
             }

      path = os.path.join(os.path.dirname(__file__), 'templates','level.html')
      self.response.out.write(template.render(path, template_values))


app = webapp2.WSGIApplication(
                                     [
                                      ('/', DisplayHandler),
                                      ('/cupertino', DisplayHandler),
                                      ('/([SNAMWXC\d\.\-+]*)',LevelHandler)

                                     ],
                                      debug=True)

