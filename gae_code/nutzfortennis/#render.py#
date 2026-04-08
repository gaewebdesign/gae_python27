import os

import webapp2
from google.appengine.ext.webapp import template

import os,re,datetime,sys, calendar,cgi,types

import library

class Day:
    year=2012    
    month=1    
    day=1    
    classtype=""
    holiday = ""
    courts = ""

class Courts:
    time=""
    cts = ""
    owner= ""
    mine = False



class BaseHandler(webapp2.RequestHandler):
  def render_template(self, filename, **template_args):
        path = os.path.join(os.path.dirname(__file__), 'templates', filename)
        self.response.write(template.render(path, template_args))

class RenderHandler(BaseHandler):
  def get(self,month,year):
        m = ["Jan","January","February","March","April","May","June","July","August","September","October","November","December"]

        month=int(month)
        year=int(year)

# Figure next month/year    
        next_month = month + 1
        next_year = year 
        if( next_month > 12):
               next_month = 1
               next_year = year + 1

# Figure previous month/year    
        prev_month = month - 1
        prev_year  = year 
        if( prev_month < 1):
               prev_month = 12
               prev_year = year - 1

# Calculate the few days before/after this month
        offdays=[]
        cal = calendar.Calendar()
        for d in cal.itermonthdates(year , month ):
            if( not re.search(str(year)+"-[0]*"+str(month) ,str(d) ) ):
                   offdays.append( d)   # list of datetime objects

# -----------------------------------------------------------------------
        thismonth = calendar.monthcalendar(year, month ) 
        nweeks = len(thismonth) 

        index=0
        Reservations=[]                 # Array of weeks
        for w in range(0,nweeks):       # 0,1,2,3,4
            week = thismonth[w]             # list of days of each week (0,0,0,0,1,2,3), (4,5,6,7,8,9,10)
            wk = []
            for x in week:   # either 0 (days before) or current day (1..31)
                 d  = Day()
                 d.day = x

                 d.classtype = "weekday"
                 if( x==0 ): 
                    d.classtype = "previous"
                    t = offdays[index]
                    d.day= t.day
                    d.month = t.month
                    d.year  =  t.year
                    index   = index + 1
                 else:
                    _d = calendar.weekday(year,month,x)
                    if( _d == 5 or _d == 6):  d.classtype = 'weekend' 
                    d.day = x
                    d.month = month
                    d.year = year


                 d.holiday = library.Holiday(d.year,d.month,d.day)
#                d.courts = FindCourts(d.year , d.month , d.day)
                 wk.append(d)

            Reservations.append(wk)           
            StartDate = StartTime = None;
            Start =  library.GetReservationStart ( )
            if(Start != None):
               StartDate = Start[0]
               StartTime = Start[1]

        template_values = {
               'monthname'     : m[month],
               'month'     : month,
               'year'      : year,
               'LoginForm' : library.LoginForm(),
               'Host'      : library.Host(),

               'StartDate' : StartDate,
               'StartTime' : StartTime,

               'Next_month'     : next_month,
               'Next_year'      : next_year,
               'Prev_month'     : prev_month,
               'Prev_year'      : prev_year,
               'Month'            : Reservations,

        }



        self.render_template('render.html', name=self.request.get('name'))

app = webapp2.WSGIApplication([
    ('/month/([\d]*)/([\d]*)', RenderHandler),



], debug=True)
