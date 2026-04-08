from appengine_utilities.sessions import Session

import urllib,sys,re,string,datetime,os
import datastore

months= ("January", "January", "February", "March", "April", "May", "June", "July","August", "September","October", "November", "December")

def getDate( d ):
   year= str(d.year)
   month=months[(d.month)]
   day=str(d.day)

   return  month + " " + day + ", " + year


# Convert from military to standard time
def stime( d ):
 hour = d.hour
 minute = d.minute

 z =""
 if( minute<10): z="0"
 if( hour > 12):    hour = hour - 12
 r = str(hour) + ":" + z + str(minute)
 return r


def ctime( d ):
 hour = d.hour
 minute = d.minute

 z =""
 if( minute<10): z="0"

 pm = " am"
 if( hour == 12):
       pm = " pm"
 elif( hour > 12):
       pm= " pm"
       hour = hour - 12

 r = str(hour) + ":" + z + str(minute) + str(pm)
 return r



def cday( d ):
   year= str(d.year)
   month=str(d.month)
   day=str(d.day)

   return  month + "-" + day + "-" + year


def Host():
# HTTP_HOST also works
#        url = os.environ["SERVER_NAME"]
#        for e in os.environ:
#           self.Writeln(e + " " + os.environ[e] + "<br>")

    url = "http://"+os.environ["SERVER_NAME"]
    if (re.search("localhost",url )): url = "http://localhost:8080"

    return url


def LoginForm(  ):

    sess = Session()
    if( sess.get(keyname='user') ):
        site = Host() + "/logout"
        form = '<form name="logout" action="'+site +'" method="POST">'

        form = form + '<input type="hidden" name="path" value ="'+ os.environ["PATH_INFO"] +'">'
        form = form + '<input type="submit" value="Logout">'
        form = form + '&nbsp;'
        form = form + sess['fname'] + " " +  sess['lname']  + " logged in"
        form = form + " for " +  sess['team']
        form = form + '</form>'
        return form

    site = Host() + "/login"
    form = '<form name="login" action="'+site +'" method="POST">'
    form = form +'&nbsp;'
    form = form + '<input type="hidden" name="path" value ="'+ os.environ["PATH_INFO"] +'">'
    form = form +'<input type="submit" value="Login">'
    form = form +'<input type="text" id="e50"  size="7" name="username">' 
    form = form +'&nbsp;'
    form = form +'<input type="password" id="e50" size="7" name="password">'
    form = form +'&nbsp;'
    form = form +'</form>'
#   form = form +'</div>'

    return form


def listconv( alist ):
   r=""
   for a in alist: r = r + a + ","

   if( r != ""): r = r.rstrip(",")

   return r


def GetReservationStart ( ):

        g = datastore.OpenDate.get_by_key_name(  "key_opendate" )
        if( g == None):
          return None

        start = g.openingdate

        StartDate    = getDate(g.openingdate)
        StartTime    = ctime(g.openingdate)

        return [ StartDate, StartTime ]
