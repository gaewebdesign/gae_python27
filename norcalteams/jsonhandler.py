import webapp2


from google.appengine.api import urlfetch

from google.appengine.ext import db
from google.appengine.ext import ndb

from google.appengine.api import mail

from datetime import timedelta
import time

import urllib,re,datetime,string,sys,os


import collections

from ndbstore import *

import mysession

import logging

#try:
import json                #Python 2.7 
import urllib2
#except ImportError:
#  import simplejson as json  #Python 2.5

def Writeln( selfobj, *t):
   for x in t:
     selfobj.response.out.write(x )
     selfobj.response.out.write(" ")

   selfobj.response.out.write("<br>")

def Write( selfobj, *t):
   for x in t:
     selfobj.response.out.write(x )
     selfobj.response.out.write(" ")

class UserHandler(webapp2.RequestHandler):

    def get(self):
      print("UserHandler")

      Writeln(self, "UserHandler")
      try:


#       req = urllib2.Request("http://www.jung4tennis.appspot.com/jsonrurl")
        req = urllib2.Request("http://www.jung4tennis.appspot.com/jsonuser")
        opener = urllib2.build_opener()
        f = opener.open(req)
        jDict = json.loads(f.read())
        Writeln(self,jDict)
  
        match = [item for item in jDict if item["user"] == "ken"]
        LoggedIn = False
        if( len(match) > 0):
            LoggedIn = True
            User = match[0]["user"] 
            Name = match[0]["name"]
            id = match[0]["id"]
            Writeln(self , "FOUND " + User + " " + Name + " " + id)

      except Exception as e: 
        Writeln(self,str(e) )
        print( str(e) )

app = webapp2.WSGIApplication(
                                     [

                                      ('/jsonruser', UserHandler)


                                     ],
                                     debug=True)

