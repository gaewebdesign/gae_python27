from google.appengine.ext.webapp import template
# new Python 2.7 imports
import webapp2    # Python 2.7
from google.appengine.ext import ndb

import urllib
import os,re,cgi,calendar,string,types
import datetime,time

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


# Admin
class AdminHandler( webapp2.RequestHandler):
   def get(self):

      TeamList=[]
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
          TeamList.append(u)

      template_values = {'Teams' : TeamList }

      path = os.path.join(os.path.dirname(__file__), 'templates','admin.html')
      self.response.out.write(template.render(path, template_values))


app = webapp2.WSGIApplication(
                                     [
                                      ('/admin', AdminHandler),

                                     ],
                                      debug=True)

