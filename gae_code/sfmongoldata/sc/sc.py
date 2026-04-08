# python -v -m my_scriptname.py

import urllib   # 
import urllib2
import random

# import datetime,re, random,time
# from google.appengine.api import urlfetch
# from datastore import  *

import urllib   # maybe not right , sleepy 9/26/19


def sendtosantaclara(self,year, unix, fname, lname, address, city, email, ntrp, zip, phone  ):

         url = "http://localhost/~roger/sc/ggtc/receive.php" 
         url = "http://www.sctennisclub.org/ggtc_/receive.php" 

         params = {
               'unix' : unix,
               'year' : year,

               'fname' : fname,
               'lname' : lname,
               'email' : email,

               'address' : address,
               'city' : city,
               'phone' : phone,
               'ntrp' : ntrp,
               'zip' : zip
         }

         data = urllib.urlencode( params )
         req = urllib2.Request( url , data )

         self.response.write( "sending to " + url + "<br>") 
         self.response.write( data )

         try:
           html = urllib2.urlopen( req )
         except :
           self.response.writet("HTTPEror exception")
           print("HTTPEror exception")

#   NOT NEEDED ANYMORE
         year = 2017
         fname = "Roger TS ";
         lname = "Federer";
         address = "20 Wimbledon Blvd";
         city = "Basel,Switzerland   ";
         email = "roger@gmail.com"
         ntrp = "M8.0";
         zip = "04121";
         phone = "(650)822-9412";
         unix = random.randrange(70000000,750000000)
         unix = 80000009;
