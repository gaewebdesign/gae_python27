import webapp2

#from datetime import timedelta
import datetime

import Cookie
import random
import os


import mysession

def Writeln( selfobj, *t):
   for x in t:
     selfobj.response.out.write(x )
     selfobj.response.out.write(" ")

   selfobj.response.out.write("<br>")

def Write( selfobj, *t):
   for x in t:
     selfobj.response.out.write(x )
     selfobj.response.out.write(" ")

class SetHandler(webapp2.RequestHandler):

    def get(self):
       print("set cookie")

       expiration = datetime.datetime.now() + datetime.timedelta(days=30)
       cookie = Cookie.SimpleCookie()
       cookie["gaewebdesign"] = "lori"

       cookie["session"] = 3700

       cookie["session"]["domain"] = "www.norcalteams.appspot.com"
       cookie["session"]["path"] = "/"
       cookie["session"]["expires"] =  expiration.strftime("%a, %d-%b-%Y %H:%M:%S PST") 

#       Writeln( self,  cookie.output()  )

       os.environ["USER_"] = "roger"

       print "Content-type: text/html\n"
       print cookie.output()
#       print cookie

#      print
#      print "Cookie set with: " + cookie.output()


class GetHandler(webapp2.RequestHandler):

    def get(self):


      if 'HTTP_COOKIE' in os.environ:
            cookie_string = os.environ.get('HTTP_COOKIE')
            Writeln(self,  "cookie ->" + str(cookie_string)  )
      else:
            Writeln(self,  "no cookie ->" )

      for key in os.environ :
         print( key + "->" + str(os.environ[key])  )
         Writeln(self, key + "->" + str(os.environ[key])  )


      print "Content-type: text/plain\n"
#      print("os.environ = " + os.environ["HTTP_COOKIE"])
      try:
             cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
             print "session = " + cookie["session"].value
             Writeln(self, "session = " + cookie["session"].value)
      except (Cookie.CookieError, KeyError):
             Writeln(self, "session cookie not set " )
             print "session cookie not set!"




app = webapp2.WSGIApplication(
                                     [
                                      ('/set', SetHandler),
                                      ('/get', GetHandler)


                                     ],
                                      debug=True,config=mysession.config)


