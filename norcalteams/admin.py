import webapp2

from google.appengine.api import urlfetch

from google.appengine.ext.webapp import template
from google.appengine.ext import db
from google.appengine.ext import ndb

from datetime import timedelta

import urllib,re,datetime,string,sys,os

import operator # for sorting
import random   # for shuffling

# CLASSES FOR THIS PROJECT ARE IN ndbstore.py
# JUST REFERENCE BY THEIR NAME
from ndbstore import *


import mysession
from flights import *

class F:
 flight = name = ""
 len = 0

 def __init__(self, id,name, len):
   self.id = id
   self.name = name
   self.len    = len

class AdminHandler(webapp2.RequestHandler):

    def get(self):

        flightList=[]
        xList  = ShortList + ActiveList

        for flight in xList:
            print flight.id , flight.name
            flightKey = ndb.Key(Flight, str(flight.id))
            o = flightKey.get()
            if( o != None):
               f =  F( flight.id, flight.name , len(o.teams) )
               flightList.append( f )
#              print flight.id, flight.name , len(o.teams)              

        print(flightList)

        LoggedIn = True
        template_values = {
               'Flights'    : flightList,
               'LoggedIn'    : LoggedIn
        }



        path = os.path.join(os.path.dirname(__file__), 'templates','admin.html')
        self.response.out.write(template.render(path, template_values))



app = webapp2.WSGIApplication(
                                     [
                                      ('/admin', AdminHandler)

                                     ],
                                      debug=True,config=mysession.config)


a
