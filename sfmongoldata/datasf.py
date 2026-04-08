import webapp2
import logging

import collections
import datetime,re, random,time

from google.appengine.ext import ndb
import json   #Python 2.7


import urllib2

from datastore import  *

#from dataimportggtc import *

class Player ( ):
   fname = lname = address = city = ntrp = ip = ""
   year=2019


   phone="(408) 992-2123"
   src = "src"
   help = "CB"
   other = "other"

   def __init__( self,u,year, fname, lname, email, city ,ntrp, address,zip,ip):

        self.unix = u


        self.fname = fname
        self.lname = lname

        self.email = email

        self.city = city
        self.ntrp = ntrp
        self.address = address

        self.year = year

        self.zip = zip
        self.ip = ip



        self.phone = self.phone
        self.other = self.other
        self.src = self.src
        self.help = self.help


class AddHandler(webapp2.RequestHandler):
   def get (self ):

# Anne Kavanaugh , annekava@gmail.com , SF
# David Kim , davidckim@poundsine.com, SF
# Moris Levin , morelevin55@gmail.com , SF
# Francis Parchaso , parchaso@usgs.gov , Menlo Park
# Herman Singh , herman.p.singh@gmail.com , SF
# Mary Jo Tierney , tierneymaryjo@gmail.com , SF
# Charlene Tuchman , chartuch@gmail.com , SF
# Jonathan Waxman , jmwaxman@gmail.com , NY
# Toni Wilson , jmwaxman@gmail.com , San Rafael
# https://www.epochconverter.com/

#      self.response.write("nothing <br>")


       self.response.write("me <br>")
       g = GGTC(key=ndb.Key(GGTC,"1547064304"))
       g.year=2019
       g.fname="Roger"
       g.lname="Okamoto"
       g.address=""
       g.city="San Francisco"
       g.zip="95126"
       g.phone="(408) 800-7646"
       g.email="tennis.mutt@gmail.com"
       g.ntrp="M3.5"
#      g.put()

       "95014","10.0.0.1"

       allPlayers = []
       unix = 172324212

       allPlayers.append( Player( unix ,2018,"Anne", "Kavanaugh" , "annekava@gmail.com" , "San Francisco", "W4.0","2415 Van Ness #304",95014,"10.0.0.1"))
       unix = unix + 1
       allPlayers.append( Player( unix ,2018,"David", "Kim" , "davidckim@poundsine.com" , "San Francisco","M","1263 Plymouth Ave " ,95014,"10.0.0.1")) 
       unix = unix + 1
       allPlayers.append( Player( unix ,2018,"Moris", "Levin" , "morlevin55@gmail.com" , "San Francisco","M3.5","2129 15th Ave" ,95014,"10.0.0.1"))
       unix = unix + 1
       allPlayers.append( Player( unix ,2018,"Francis", "Parchaso" , "parchaso@usgs.gov" , "Menlo Park","M4.0", "345 Middlefield Rd MS 496",95014,"10.0.0.1"))

#repeat for 2019
       unix = unix + 1

       allPlayers.append( Player( unix ,2019,"Anne", "Kavanaugh" , "annekava@gmail.com" , "San Francisco", "W4.0","2415 Van Ness #304",95014,"10.0.0.1"))
       unix = unix + 1
       allPlayers.append( Player( unix ,2019,"David", "Kim" , "davidckim@poundsine.com" , "San Francisco","M","1263 Plymouth Ave " ,95014,"10.0.0.1")) 
       unix = unix + 1
       allPlayers.append( Player( unix ,2019,"Moris", "Levin" , "morlevin55@gmail.com" , "San Francisco","M3.5","2129 15th Ave" ,94125,"10.0.0.1"))
       unix = unix + 1
       allPlayers.append( Player( unix ,2019,"Francis", "Parchaso" , "parchaso@usgs.gov" , "Menlo Park","M4.0", "345 Middlefield Rd MS 496",95014,"10.0.0.1"))

       allPlayers.append( Player( unix ,2019,"Herman", "Singh" , "herman.p.singh@gmail.com" , "San Francisco" ,"M4.5", "1690 Broadway Street #608" ,95014,"10.0.0.1"))
       unix = unix + 1
       allPlayers.append( Player( unix ,2019,"Mary Jo", "Tierney" , "tierneymaryjo@gmail.com" , "San Francisco" ,"W3.5","554- 7th Ave" ,95014,"10.0.0.1"))
       unix = unix + 1
       allPlayers.append( Player( unix ,2019,"Charlene", "Tuchman" , "chartuch@gmail.com" , "San Francisco" ,"W3.5","25 Heather Ave" ,95014,"10.0.0.1"))
       unix = unix + 1
       allPlayers.append( Player( unix ,2019,"Jonathan", "Waxman" , "jmwaxman@gmail.com" , "New York" ,"M", "600 West End Ave 12B", 95014,"10.0.0.1"))
       unix = unix + 1
       allPlayers.append( Player( unix ,2019,"Toni", "Wilson" , "toni.wilson@yahoo.com" , "San Rafael" ,"W4.0","9 Safebrush Ct " ,95014,"10.0.0.1"))

#
       unix = unix + 1
       allPlayers.append( Player( unix ,2019,"Patty", "O'Kelly" , "pattii@gmail.com" , "San Francisco" ,"W4.0","39 - 4th Ave" ,95014,"10.0.0.1"))


       allPlayers.sort(key = lambda x: x.lname, reverse=False)

       for p in allPlayers:

          epoch = int(time.time())
          epoch = epoch + random.randint(1,1000)

#         g = GGTC(key=ndb.Key(GGTC,str(epoch)) )
          g = GGTC(key=ndb.Key(GGTC,str(p.unix)) )

          g.year = p.year
          g.fname= p.fname
          g.lname= p.lname
          g.email= p.email
          g.address= p.address
          g.ntrp= p.ntrp
          g.city= p.city
          g.zip= str(p.zip)

          g.phone= p.phone

          g.ip= p.ip

          g.help= p.help
          g.src= p.src
          g.other= p.other

          self.response.write( g )
          self.response.write( "<br>" )

          g.put()


# jimtoni@aol.com





class TwilightHandler(webapp2.RequestHandler):
   def get (self ):


#15
       self.response.write("wade shang <br>")
       g = TWILIGHT(key=ndb.Key(TWILIGHT,"1537196755"))
       g.year=2018
       g.fname="Sherman"
       g.lname="Wagner"
       g.address="351 Parker St"
       g.city="SF"
       g.zip="94120"
       g.phone="(650) 232-1232"
       g.email="wade.shang@gmail.com"
       g.ntrp="M3.5s"
       g.put()


#16
       self.response.write("Spencer Tracey<br>")
       g = TWILIGHT(key=ndb.Key(TWILIGHT,"1537159946"))
       g.year=2018
       g.fname="Spender"
       g.lname="Tracey"
       g.address="351 Parker St"
       g.city="SF"
       g.zip="94120"
       g.phone="(650) 232-1232"
       g.email="spencer@gmail.com"
       g.ntrp="M3.5s"
       g.put()


#17
       self.response.write("Anthony Jones <br>")
       g = TWILIGHT(key=ndb.Key(TWILIGHT,"1537227076"))
       g.year=2018
       g.fname="Anthony"
       g.lname="Jones"
       g.address="351 Parker St"
       g.city="SF"
       g.zip="94120"
       g.phone="(650) 232-1232"
       g.email="anthony@gmail.com"
       g.ntrp="M4.0s"
       g.put()


#18
       self.response.write("Janet Jones <br>")
       g = TWILIGHT(key=ndb.Key(TWILIGHT,"1537099589"))
       g.year=2018
       g.fname="Janet"
       g.lname="Jones"
       g.address="351 Parker St"
       g.city="SF"
       g.zip="94120"
       g.phone="(650) 232-1232"
       g.email="janet@gmail.com"
       g.ntrp="F4.0C"
       g.put()



       g.ntrp="M3.5s"
       g.put()


#26
       self.response.write("Kevin Gough <br>")
       g = GGTC(key=ndb.Key(GGTC,"1537236951"))
       g.year=2016
       g.fname="Kevin"
       g.lname="Gough"
       g.address="351 Parker St"
       g.city="SF"
       g.zip="94120"
       g.phone="(650) 232-1232"
       g.email="kevin.gough@gmail.com"
       g.ntrp="M3.5C"
       g.put()


#27
       self.response.write("Lawrence Henriquez <br>")
       g = GGTC(key=ndb.Key(GGTC,"1537220500"))
       g.year=2017
       g.fname="Lawrence"
       g.lname="Henriquez"
       g.address="351 Parker St"
       g.city="SF"
       g.zip="94120"
       g.phone="(650) 232-1232"
       g.email="lawrence.henriquez@gmail.com"
       g.ntrp="M4.0C"
       g.put()


#28
       self.response.write("Wilbur Houston <br>")
       g = GGTC(key=ndb.Key(GGTC,"1537167027"))
       g.year=2017
       g.fname="Wilbur"
       g.lname="Houston"
       g.address="351 Parker St"
       g.city="SF"
       g.zip="94120"
       g.phone="(650) 232-1232"
       g.email="wilbur.houston@gmail.com"
       g.ntrp="M3.5s"
       g.put()


from  data import dataGG2018
from  data import dataGG2019

class DataHandler(webapp2.RequestHandler):
   def get (self ):

#      dataGG2018.ggtc2018( self )
       dataGG2019.ggtc2019( self )


app = webapp2.WSGIApplication(
                                     [

                                      ('/fakedatasf', AddHandler)
#                                       ('/datasf', DataHandler)
#                                      ('/datasf', DataHandler2)
#                                      ('/datasf', TwilightHandler)


                                     ],
                                     debug=True)
