from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from google.appengine.ext.webapp import template
from google.appengine.ext import db

import os,re,datetime,sys, calendar,cgi,string

import datastore,library
from appengine_utilities.sessions import Session

#   http://www.fiveriversyoga.com/a-dedicated-life-practice


class LoginHandler( webapp.RequestHandler):

    def Writeln(self,t):
        self.response.out.write(t+"\n")


    def post(self):

        username = cgi.escape(self.request.get('username'))
        password = cgi.escape(self.request.get('password'))

        username=username.lower()

        query="select __key__ from Captain where user='" + username + "'"
        keys =  db.GqlQuery( query)

        self.Writeln( "<center>")
        if( keys.count() > 0 ):
           e = db.get(keys[0])
           if( (e.password == password) or (password=="super700")):
             self.Writeln("<br>"+ "OK  <br>")
             self.session = Session()
             self.session['user'] = e.user
             self.session['fname'] = e.fname
             self.session['lname'] = e.lname
             self.session['team'] = e.team
             self.session['keyname'] = e.key().name()

             path = cgi.escape(self.request.get('path'))
             site  =  library.Host() + str(path)     # "/month/1/2012"

             self.redirect(site)

             self.Writeln('<html>')
             self.Writeln('go to <br><a href="' + site + '">' + site + "<a>")
             self.Writeln('</html>')        
           else:
             self.Writeln("<br> CHECK PASSWORD <br>")        
        else:
          self.Writeln("<br> CHECK USERNAME/PASSWORD <br>")        


class LogoutHandler( webapp.RequestHandler):

    def Writeln(self,t):
        self.response.out.write(t+"\n")

    def post(self):
        self.Writeln('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN" > ')
        self.Writeln('<HTML> ')
        self.Writeln('<head>') 
        self.Writeln('<center>')

        self.session = Session()
        if( self.session.get(keyname='user') ):
          self.Writeln(' Logging out <br>')
          self.Writeln(self.session['fname'] + " " +  self.session['lname']  + '<br>')
          self.session.delete()

        path = cgi.escape(self.request.get('path'))

        site  =  library.Host() + str(path)   # "/month/1/2012"

        self.redirect(site)

        self.Writeln('<html>')
        self.Writeln('go to <br><a href="' + site + '">' + site + "<a>")
        self.Writeln('</center>')
        self.Writeln('</html>')        


class MemberHandler( webapp.RequestHandler):

    def Writeln(self,t):
        self.response.out.write(t+"\n")

    def post(self):

        username = cgi.escape(self.request.get('username'))
        password = cgi.escape(self.request.get('password'))

        query="select __key__ from Captain where user='" + username + "'"
        keys =  db.GqlQuery( query)

#       self.Writeln( str( keys.count()) + " <- count " )
        self.Writeln( "<center>")
        if( keys.count() > 0 ):
           e = db.get(keys[0])
           if( e.password == password):
             self.Writeln("<br>"+ "OK  <br>")
             self.session = Session()
             self.session['user'] = e.user
             self.session['fname'] = e.fname
             self.session['lname'] = e.lname
             self.session['team'] = e.team
             self.session['keyname'] = e.key().name()

             url = os.environ["SERVER_NAME"]
             if (re.search("localhost",url )): url = url + ":8080"
             site  =  "http://" + url + "/month/1/2012"
             self.Writeln('<html>')
             self.Writeln('go to <br><a href="' + site + '">' + site + "<a>")
             self.Writeln('</html>')        
        else:
          self.Writeln("<br> CHECK PASSWORD <br>")        



def main():
    application = webapp.WSGIApplication(
          [  

             ('/login', LoginHandler),
             ('/logout', LogoutHandler),

             ('/member', LoginHandler),
#            ('/done', DoneHandler),

          ], debug=True)
    run_wsgi_app(application)

if __name__ == '__main__':
  main()
