

from google.appengine.ext.webapp import template
from google.appengine.ext import db

import os,re,datetime,sys, calendar,cgi,string

from google.appengine.api import mail

import webapp2    # Python 2.7

#try:
import json                #Python 2.7 
import urllib2
#except ImportError:
#  import simplejson as json  #Python 2.5


from webapp2_extras import sessions
import mysession


#   http://www.fiveriversyoga.com/a-dedicated-life-practice



def Writeln( selfobj, *t):
   for x in t:
     selfobj.response.out.write(x )
     selfobj.response.out.write(" ")

   selfobj.response.out.write("<br>")

def Write( selfobj, *t):
   for x in t:
     selfobj.response.out.write(x )
     selfobj.response.out.write(" ")



class LoginHandler( mysession.BaseHandler):

    def Writeln(self,t):
        self.response.out.write(t+"\n")

    def User(self):
        return self.session['user']

    def ID(self):
        return self.session['id']

    def post(self):


        user = cgi.escape(self.request.get('user'))
        user = user.lower()


        LoggedIn = False
# JSON data from tenniscloud
        try:

           print("LoginHandler")

           req = urllib2.Request("http://www.tenniscloud.appspot.com/jsonuser")
#         req = urllib2.Request("http://www.jung4tennis.appspot.com/jsonuser")
           opener = urllib2.build_opener()
           f = opener.open(req)
           jDict = json.loads(f.read())
 
           print("got JSON data ")
           print(jDict)

           print("looking for " + user )

           match = [item for item in jDict if item["user"] == user]
           LoggedIn = False
           User = Name = ID = ""
           if( len(match) > 0):
            LoggedIn = True
            User = match[0]["user"] 
            Name = match[0]["name"]
            ID = match[0]["id"]
            print( "FOUND " + User + " " + Name + " " + str(id) )

        except Exception as e: 
           Writeln(self,str(e) )
           print( str(e) )


#SESSION
             

        if LoggedIn == True:
            self.session['user'] = User
            self.session['id'] = ID
            self.session['name'] = Name
        else: 
            LoggedIn == False               
            self.session['user'] = ""
            self.session['id'] = ""
            self.session['name'] = ""

#SESSION


        path = cgi.escape(self.request.get('path'))

#
        try:
            mail.send_mail( sender="Roger <tennis.mutt@gmail.com>",
                        to = "Tennis Mutt <tennis.mutt@gmail.com>",
                        subject =  user+ " logged in from " + self.request.url,
                        body =  user + " logged in from " + self.request.url)

            print("MAIL: " + user + " logged in (" + self.request.url + ")" )
        except:
            print("EXCEPTION email!!")
                          
#       path = os.environ['PATH_INFO']
        self.redirect(path)
#       self.redirect(site)





config = {}
config['webapp2_extras.sessions'] = {'secret_key' :  'superman' }



app = webapp2.WSGIApplication(
          [  

             ('/login', LoginHandler)


          ], debug=True,config=config)
    



