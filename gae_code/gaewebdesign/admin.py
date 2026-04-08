import os
from google.appengine.ext.webapp import template

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from google.appengine.api import urlfetch

import urllib
import re,cgi,calendar,string,types
import datetime,time

import datastore,library

from google.appengine.api import users


def monday( m,d, y):
   return datetime.date(m,d,y) - datetime.timedelta( datetime.date(m,d,y).weekday())

class Hours(object):
  def __init__(self,hr):
     self.hr = hr
     if( hr < 12):
         self.p = str(hr) + "am"
     elif( hr == 12) :
         self.p = "12 noon"
     else:
         self.p = str(hr-12)+"pm"


class Days(object):
  def __init__(self,d):
     self.day = d
     self.selected = ""

class Months(object):
  def __init__(self,n,m):
     self.number = n
     self.month = m

class Captains:
     fname=""     
     lname=""     
     user=""     
     team=""
     password=""
     count=0
     key=""

class DeleteHandler(webapp.RequestHandler):
    def get(self ):
        print("delete schedules")
        query="select __key__ from CourtTime "
        keys =  db.GqlQuery( query)
        for k in keys:
          p = db.get(k)
          print("delete", p.date, p.weekday)
          db.delete(k)

class OpenHandler(webapp.RequestHandler):

    def Writeln(self,t):
        self.response.out.write(t+"\n")

    def post(self):

        _month = cgi.escape(self.request.get('open_month'))
        _hour = cgi.escape(self.request.get('open_hour'))
        _day = cgi.escape(self.request.get('open_day'))
        _year = cgi.escape(self.request.get('open_year'))

        self.Writeln('<center>')
        self.Writeln( str(_month)+'/'+str(_day) + '/'+str(_year) )

        key_id =  "key_opendate"
        g = datastore.OpenDate( key_name=key_id )
        g.openingdate= datetime.datetime(year=int(_year), month=int(_month), day=int(_day),hour=int(_hour),minute=0)
        db.put( g )

class AddCaptHandler(webapp.RequestHandler):

    def Writeln(self,t):
        self.response.out.write(t)
        self.response.out.write("\n")

    def post(self):

        fname = cgi.escape(self.request.get('fname'))    
        lname = cgi.escape(self.request.get('lname'))    
        user = cgi.escape(self.request.get('user'))    
        team = cgi.escape(self.request.get('team'))    
        password = cgi.escape(self.request.get('password'))    


        key_id =  "key_"+ fname + "_" + lname  + "_" + team
        g = datastore.Captain( key_name=key_id )
        g.count = 0
        g.fname = fname
        g.lname = lname
        g.user = user
        g.password = password
        g.team = team
        print( fname,lname,user,team,password )
#       print( g.fname,g.lname,g.user,g.team,g.password )

        db.put( g )



class EditCaptHandler(webapp.RequestHandler):

    def Writeln(self,t):
        self.response.out.write(t)
        self.response.out.write("\n")

    def post(self):
        self.Writeln("posted<br>")
        _arg = self.request.arguments() 
#       self.Writeln( str(len( _arg )) )
#       self.Writeln( str( _arg ) )

        for e in _arg:
           _rest = self.request.get_all(e)
           keyname  = _rest[0]
           password = str(_rest[1])
           count    = int(_rest[2])
           self.Writeln( str(keyname) + " " + str(password) + " " + str(count) + "<br>" )
           user = datastore.Captain.get_by_key_name( keyname )
           user.password = password
           user.count    = count
           db.put(user)



class CaptainHandler(webapp.RequestHandler):

    def Writeln(self,t):
        self.response.out.write(t+"\n")

    def create(self):
        captains = []


        captains.append( ("Lionel", "Fors" ,"lionel", "fors","M3.0A", ) )
        captains.append( ("Kevin", "Brown" ,"kevin", "brown" ,"M3.5B") )
        captains.append( ("Robert", "Jones" ,"robert", "jones" ,"M3.5A") )
        captains.append( ("Carlos", "Lee" ,"carlos", "lee" ,"M3.5C") )
        captains.append( ("Kirt", "Ong" ,"kirt", "ong" ,"M4.0A") )
        captains.append( ("Steve", "Hayes" ,"steve", "hayes" ,"M4.0B") )

        captains.append( ("Teresa", "Arakaki" ,"teresa", "arakaki" ,"W3.0A") )
        captains.append( ("Emi", "Sato" ,"emi", "sato" ,"W3.5B") )
        captains.append( ("Linda", "Chen" ,"linda", "chen" ,"W3.5B") )
        captains.append( ("Melinda", "Won" ,"melinda", "won","W3.0D" ) )
        captains.append( ("Suzy", "Chu" ,"suzy", "chu" ,"W4.0A") )
        captains.append( ("Melissa", "Lee" ,"melissa", "lee" ,"W4.0B") )
        captains.append( ("Maureen", "Moore" ,"maureen", "moore" ,"W4.0C") )
        captains.append( ("Elizabeth", "Koo" ,"elizabeth", "koo" ,"W4.0D") )
        captains.append( ("Fe", "Baum" ,"fe", "baum" ,"W4.0A") )
        captains.append( ("Susan", "Reynold" ,"susan", "reynold" ,"W4.0A") )



        captainlist = []
        for e in captains:
          fname = e[0]
          lname = e[1]
          user = e[2]
          password = e[3]  
          team= e[4]


          key_id =  "key_"+ fname + "_" + lname  + "_" + team
          g = datastore.Captain( key_name=key_id )
          g.count = 0
          g.fname = fname
          g.lname = lname
          g.user = user
          g.password = password
          g.team = team
          captainlist.append(g)
          print( e )

        db.put(captainlist)
 


    def list(self):

        self.Writeln('<style type = "text/css">') 
        self.Writeln('<!--')
        self.Writeln('@import url("assets/css/sctc.css");')
        self.Writeln('@import url("assets/css/library.css");')
        self.Writeln('-->')
        self.Writeln('</style>')

        query="select __key__ from Captain order by team"
        keys =  db.GqlQuery( query)
        self.Writeln('<div align="center"><br>')
        self.Writeln('<table>')
        self.Writeln( '<tr>')
        self.Writeln( '<th scope="col">First Name</th>')
        self.Writeln( '<th scope="col">Last Name</th>')
        self.Writeln( '<th scope="col">User</th>')
        self.Writeln( '<th scope="col">Password</th>') 
        self.Writeln( '<th scope="col">Team</th>') 
        self.Writeln( '</tr>')


        for k in keys:
          p = db.get(k)
          self.Writeln('<tr>')
          self.Writeln('<td>' + p.fname + '</td>')
          self.Writeln('<td>' + p.lname + '</td>')
          self.Writeln('<td>' + p.user+ '</td>')
          self.Writeln('<td>' + p.password +'</td>')
          self.Writeln('<td>' + p.team + '</td>')
          self.Writeln('</tr>')

        self.Writeln('</table>')
        self.Writeln("</html>")

    def delete(self):
        query="select __key__ from Captain"
        keys =  db.GqlQuery( query)
        for k in keys:
          p = db.get(k)
          self.Writeln( p.fname + " " +  p.lname + " " + p.user + "<br>")
          p = db.delete(k)

        self.Writeln("</html>")

    def clear(self):
        query="select __key__ from Captain"
        keys =  db.GqlQuery( query)
        for k in keys:
          p = db.get(k)
          p.count=0
          self.Writeln("Set " +  p.fname + " " +  p.lname + " to " + str(p.count) + "<br>")
          db.put(p)

        query="select __key__ from CourtTime "
        keys =  db.GqlQuery( query)
        for k in keys:
          p = db.get(k)
          if( type(p.owner) is not types.NoneType):
           self.Writeln("set " +  p.weekday + " " + str(p.date)  + " to None <br>")
           p.owner=None
           db.put(p)


    def get(self, pick ):
        if( pick == "capt"):
          self.list()
        elif( pick == "ccapt"):
          self.create()
        elif( pick == "clear"):
          self.clear()



class ScheduleHandler(webapp.RequestHandler):

    def Write(self,t):
     self.response.out.write(t)

    def Writeln(self,t):
     self.response.out.write(t)
     self.response.out.write("<br>")

    def get(self):

        dayofmonth = []
        for d in range(1,32):
          _d =  Days(d) 
          if( d == 9 ) : _d.selected="selected"
          dayofmonth.append( _d )

        m = ["Jan","Feb","Mar","Apr","May","June","July","Aug","Sept","Oct","Nov","Dec"]
        mon=[]
        for d in range(0,len(m)):
          mon.append( Months(d+1,m[d]) )


        hlist = []
        for d in range(8,23):
          hlist.append( Hours(d) )

        p = datastore.OpenDate.get_by_key_name( "key_opendate" )


        opendate = None
        opentime = None

        if( p ):
         opendate = p.openingdate
         opentime = library.ctime(p.openingdate)

#       Get all the Captains
        query="select __key__ from Captain order by team"

        clist=[]
        Captainkeys =  db.GqlQuery( query)
        for key in Captainkeys:
           c = Captains()
           k = db.get(key)
           c.fname = k.fname
           c.lname = k.lname
           c.user = k.user
           c.team = k.team
           c.password = k.password
           c.key = k.key().name()
           c.count = k.count
           clist.append(c)

#       g.date= datetime.datetime(year=int(_year), month=int(_month), day=int(_day),hour=20,minute=0)

        site = library.Host()
        template_values = {
             'Site': site,
             'Hours': hlist,
             'Days': dayofmonth,
             'Months': mon,
             'opendate': opendate,
             'opentime': opentime,
             'Captains' : clist

        }
        path = os.path.join(os.path.dirname(__file__), 'administer.html')
        self.response.out.write(template.render(path, template_values))

    def post(self):

        weekday = [ "Mon","Tues","Wed", "Thurs", "Fri", "Sat","Sun"]

        weeks = cgi.escape(self.request.get('weeks'))            #  weeks
        days4 = cgi.escape(self.request.get('days4'))            #  either 0 or 4 (Mon-Thurs)

        description = cgi.escape(self.request.get('desc'))

        start_hr = cgi.escape(self.request.get('start_hr'))
        t = start_hr.split(":")
        start_hr = int(t[0])
        start_min="0"
        if( len(t)>1): start_min = t[1]
        start_min = int(start_min)


        start_len = int(cgi.escape(self.request.get('start_len')))
        courtlist = self.request.get_all('courts')
        month =  self.request.get('m') 
        day   =  self.request.get('d') 
        year  =  self.request.get('y') 

        courts=[]
        court_str = ""
        for c in courtlist:   
           court_str = court_str + "_" + c
           courts.append( c)

# TODO  STOP IF NO COURTS SELECTED!

        try:
         start= datetime.datetime(year= int(year) , month=int(month) ,day=int(day))
        except:
         self.Writeln("EXCEPTION: date error" )
         return

        if( int(days4) > 1):
         self.Writeln("convert to Monday since days4=" + str(days4) )
         start = start - datetime.timedelta( start.weekday())


        reservelist=[]
        for w in range(0 , int(weeks)):
          self.Writeln("week  " + str(w))
          for d in range(0,int(days4)):
            reserve= start + datetime.timedelta(days = w*7 + d)
            rstart = reserve + datetime.timedelta(hours= start_hr, minutes=start_min)
            rend = reserve + datetime.timedelta(hours= start_hr + start_len,minutes=start_min)



            key_id =  "_"+ string.replace(str(rstart) ," " ,"_") + court_str + "_" + weekday[reserve.weekday()]

            g = datastore.CourtTime( key_name=key_id )
            g.date = reserve
            g.start = rstart
            g.end = rend
            g.courts = courts
            g.desc = description
            g.weekday  = weekday[ reserve.weekday() ]
            g.owner = None
            reservelist.append(g)

            self.Writeln(" append " + key_id )


        db.put( reservelist )


application = webapp.WSGIApplication(
                                     [('/admin', ScheduleHandler ),
                                     ('/doschedule', ScheduleHandler ),
                                     ('/doopen', OpenHandler),
                                     ('/doeditcapt', EditCaptHandler),
                                     ('/doaddcapt', AddCaptHandler),
                                     ('/delete', DeleteHandler ),
                                     ('/(capt)', CaptainHandler),
                                     ('/(ccapt)', CaptainHandler),
                                     ('/(clear)', CaptainHandler),
                                     ],


                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":

#   print __file__
#   print __name__

    main()

