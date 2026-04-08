from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from google.appengine.ext.webapp import template
from google.appengine.ext import db

import os,re,datetime,sys, calendar,cgi,types

import datastore,library
from appengine_utilities.sessions import Session

class Reservation:
   fname=""              # Captain name
   lname=""              # Captain name
   team=""               # team
   count=0               # count
   courts=[]             # court list 


class Court:
   weekday=""            # day of week
   date=""               # date of reservation

   courts=""             # courts (string)
   start=""              # start time   (converted to am/pm)
   end=""                # end time     (converted to am/pm)
   desc=""               # description  


class UnReserveHandler(webapp.RequestHandler):
    def Writeln(self,t):
        self.response.out.write(t)
        self.response.out.write("\n")

    def Write(self,t):
        self.response.out.write(t)


    def post(self):

        sess = Session()
        if(not sess.get(keyname='user') ):
          self.Writeln("<p><br><p><br>")
          self.Writeln("<center>")
          self.Writeln("<h1>Please Login </h1>")
          self.Writeln("</center>")          
          return

#  Should only get to here is there's a session 
        fname = sess['fname'] 
        lname = sess['lname'] 
        captain_keyname = sess['keyname'] 


        self.Writeln("<html>")
        try:
          keyname = self.request.get('keyname')
          if( len(keyname) == 0):
            self.Writeln("<body bgcolor=#d2d2ee>")
            self.Writeln("<center><p><br><p><br>")
            self.Writeln("<h2>Please make a selection</h2>" )
            return
        except:
          self.Writeln("<h2>Please make a selection.</h2>" )
          return


#  Get the court and set the owner to None
        e = datastore.CourtTime.get_by_key_name( keyname )

        if( type(e.owner) is types.NoneType):
            self.Writeln("<body bgcolor=#d2d2ee>")
            self.Writeln("<center>")
            self.Writeln("<h2> Can't delete reservation </h2>")
            self.Writeln("<h2> Please go back and refresh the page </h2>")
            return


        e.owner = None
        db.put( e) 

#       use to return to calender month/year
#  TODO  decide if to  implement in captain_unreserve.html page
        Month = e.date.month
        Year = e.date.year

        g = datastore.Captain.get_by_key_name( captain_keyname )
        g.count = g.count - 1
        count = g.count
        db.put( g) 

        template_values = {
            'LoginForm' : library.LoginForm(),
            'Host'     : library.Host(),
            'Month'    : Month,
            'Year'     : Year,
            'Count'    : count,
            'Weekday'  : e.weekday,
            'Day'      : library.cday(e.start),
            'Start'    : library.ctime(e.start),
            'End'      : library.ctime(e.end),
            'Desc '    : e.desc
        }

        path = os.path.join(os.path.dirname(__file__), 'captain_unreserve.html')
        self.response.out.write(template.render(path, template_values))




class CaptainHandler(webapp.RequestHandler):


    def Writeln(self,t):
        self.response.out.write(t)
        self.response.out.write("\n")

    def Write(self,t):
        self.response.out.write(t)

    def get(self ):

        capt_keyname=""
        LoggedIn =  False
        sess = Session()
        CaptainReservation = Reservation()        
        if(sess.get(keyname='user') ):
           LoggedIn = True
           capt_keyname = sess['keyname'] 
           CaptainReservation.fname = sess['fname']
           CaptainReservation.lname = sess['lname']
           CaptainReservation.team = sess['team']
           g = datastore.Captain.get_by_key_name( capt_keyname )
           CaptainReservation.count = g.count

# TODO  more efficient db grab
           query="select __key__ from CourtTime where owner='" + capt_keyname + "'"
           keys =  db.GqlQuery( query)
           res = db.get(keys)
           courtlist = []
           for r  in res:
              c = Court()
              c.weekday = r.weekday
              c.date = library.cday(r.date)
              c.start = library.ctime(r.start)
              c.end = library.ctime(r.end)
              c.courts = library.listconv(r.courts)
              c.key = r.key().name()
              courtlist.append( c)

           CaptainReservation.courts = courtlist

# ---------------------------------------------------------------------------------
        template_values = {
             'LoginForm' : library.LoginForm(),
             'LoggedIn': LoggedIn,
             'Host': library.Host(),
             'CaptainReservation': CaptainReservation,
             'Site'      : library.Host() + "/unreserve",
        }

        path = os.path.join(os.path.dirname(__file__), 'captain.html')
        self.response.out.write(template.render(path, template_values))



def main():
    application = webapp.WSGIApplication(
          [  ('/captain', CaptainHandler),
             ('/unreserve', UnReserveHandler)
          ], debug=True)
    run_wsgi_app(application)

if __name__ == '__main__':
  main()
