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


def location( where):
       loc="LP"
       if( re.search("Mg",where,re.IGNORECASE)): loc="Mango"
       if( re.search("Cu",where,re.IGNORECASE)): loc="Cuesta"
       return loc


def Holiday( y,m,d):

  if(y==2012 and m==6 and d==25): return os.environ['HOMECOURTS']

  if(y==2012 and m==2 and d==14): return 'Valentines Day'   
  if(y==2012 and m==5 and d==13): return "Mother's Day"   
  if(y==2012 and m==7 and d==4): return "4th of July"

  if(y==2012 and m==8 and d==10): return "Adult"
  if(y==2012 and m==8 and d==11): return "Districts"
  if(y==2012 and m==8 and d==12): return "Weekend"



  if(y==2012 and m==7 and d==2): return 'Week 1'   
  if(y==2012 and m==7 and d==30): return 'Week 5'   
  if(y==2012 and m==9 and d==3): return 'Week 10'   

  if(y==2012 and m==8 and d==24): return 'South'   
  if(y==2012 and m==8 and d==25): return 'Bay'   
  if(y==2012 and m==8 and d==26): return 'NTRP'   



  return ''

