import webapp2

from google.appengine.api import mail

from google.appengine.api import urlfetch

from google.appengine.ext.webapp import template
from google.appengine.ext import db
from google.appengine.ext import ndb

from datetime import timedelta

import urllib,re,datetime,string,sys,os

import operator # for sorting

import mysession

# CLASSES FOR THIS PROJECT ARE IN ndbstore.py
# JUST REFERENCE BY THEIR NAME
from ndbstore import *

from flights import *

class T:
   teamname=captain=area=playoff=""
   wins=loss=0

class F:
   name=""
   flight=0

   def __init__(self,n,f):
      self.name = n
      self.flight = f

class RedirectHandler(webapp2.RequestHandler):

    def get(self ):

      url = "http://" + os.environ["SERVER_NAME"]
      if (re.search("localhost",url )) : url="http://localhost:8080"

      self.redirect(url + "/18Mx8.0")



class DisplayHandler( mysession.BaseHandler ):

    def get(self ):

        template_values = {
#               'teams'     : teams,
#               'flightlist'    : flightList
        }

        print("DisplayHandler")

        path = os.path.join(os.path.dirname(__file__), 'templates','display.html')
        self.response.out.write(template.render(path, template_values))


    def get(self ,league):
        print("DisplayHandler")
        teams=[]

# go through flight list to get league id
# FlightList is defined in flight.py and imported here
        for f in FlightList:
           print(f.name + " ? " + str(league))
           if( f.name == league):
               leagueid = f.id
               print("league id = " + str(leagueid) )
               break

#       flightKey = ndb.Key(Flight, "1700" )
        flightKey = ndb.Key(Flight, str(leagueid) )
        o = flightKey.get()
        if( o == None):
           print("cant get Flight " + str(leagueid )  )
        else:
           print("Flight")
           teams = o.teams


# SORT by wins (descending, so team with the  most wins is at the top)   
        try:
          teams.sort( key = operator.attrgetter('win') ,reverse=True)
        except Exception as e:
          print("EXCEPTION " + str(e) + " likely no teams ")

# SESSION
        LoggedIn = False
        User = Team = ""
        path = os.environ['PATH_INFO']

#       for key in os.environ :
#          print( key + "->" + str(os.environ[key])  )
        try:
           user = self.session.get('user')
           name = self.session.get('name')
           id   = self.session.get('id')
           print("SESSION:" + user + " " + name + " " + id)
#          if user != None & user!="":
           if user != None :
              LoggedIn = True
              try:
                 mail.send_mail( sender="Roger <tennis.mutt@gmail.com>",
                        to = "Tennis Mutt <tennis.mutt@gmail.com>",
                        subject =  user+ " browsing " + self.request.url,
                        body =  user + " browsing " + self.request.url)

                 print("MAIL: " + user + " logged in (" + self.request.url + ")" )
              except:
                 print("EXCEPTION email!!")

           
           if user == "":
              LoggedIn = False


        except Exception as e:
           print("SESSION EXCEPTION -> " + str(e) )

# SESSION

        LoggedIn  = True
        template_values = {
               'LoggedIn' : LoggedIn,
               'Name'     : name,
               'Path'     : path,
               'teams'     : teams,
               'flightlist'    : FlightList
        }


        path = os.path.join(os.path.dirname(__file__), 'templates','display.html')
        self.response.out.write(template.render(path, template_values))



app = webapp2.WSGIApplication(
                                     [
                                      ('/', RedirectHandler),
                                      ('/([SAMWxC\d\.+]*)',DisplayHandler),
#                                      ('/([\d]*)', DisplayHandler),


                                     ],
                                      debug=True,config=mysession.config)

