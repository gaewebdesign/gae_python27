import os
from google.appengine.ext.webapp import template

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from google.appengine.ext import db

import urllib
from google.appengine.api import urlfetch

import re
import datastore
import datetime

import library

from google.appengine.api import users

#from google.appengine.dist import use_library
#use_library('django','1.2')

class Member:
    date=fname=lname=team=captain=""
    teamid=0

class Team:
    name=captain=""    

class TemplateDisplay(webapp.RequestHandler):

    def Write(self,t):
      self.response.out.write(t)

    def Writeln(self,t):
      self.response.out.write(t+"\n")

    def get(self,t):

     cup = "113"
     facilityid = cup

     tdict = {}
     query="select * from FacilityTeam"
     qr =  db.GqlQuery( query )          
     for e in qr:
       t = Team()
       t.name = e.name
       t.captain = e.captain
       tdict[e.teamid] = t
#      self.Writeln( str(e.teamid) + ", " + e.name + ", " + e.captain  + "<br>")

     query="select * from FacilityRoster where facility="+facilityid+" order by date desc , lname  limit 200"
     lastrostered =  db.GqlQuery( query )          
     mlist=[]

     for l in lastrostered:
          m = Member()
          m.date = l.date
          m.fname = l.fname
          m.lname = l.lname


          m.teamid = l.teamid
          m.team = tdict[l.teamid].name 
          m.captain = tdict[l.teamid].captain

#         skip if not Mx

          if( re.search("MX",m.team)):
            mlist.append(m)


     template_values = {

           'Member' : mlist
     }



     path = os.path.join(os.path.dirname(__file__), 'templatedisplay.html')
     self.response.out.write(template.render(path, template_values))

class Redirect(webapp.RequestHandler):

    def get(self):
      url = "http://"+os.environ["SERVER_NAME"]
      url = "http://"+os.environ["HTTP_HOST"]
      self.redirect(url+"/cupertino")
#      for u in os.environ:
#         self.response.out.write(u+" " + str(os.environ[u])+ "<br>")



class Display(webapp.RequestHandler):

    def Write(self,t):
      self.response.out.write(t)

    def Writeln(self,t):
      self.response.out.write(t+"\n")

    def Links(self,idx):
      library.Links(self,idx)       

    def CSSHeader(self):

#     self.Writeln('<LINK REL=StyleSheet HREF="css/style.css" TYPE="text/css"')

      self.Writeln('<style type = "text/css">') 
      self.Writeln('<!--')
      self.Writeln('@import url("assets/css/table.css");')
      self.Writeln('@import url("assets/css/library.css");')
      self.Writeln('-->')
      self.Writeln('</style>')

    def ScriptHeader( self ):   
       self.Write('<SCRIPT LANGUAGE="JavaScript" SRC="assets/javascript/sorttable.js"></SCRIPT>') 
       self.Write('<SCRIPT LANGUAGE="JavaScript" SRC="assets/javascript/library.js"></SCRIPT>') 

    def ScriptTester(self):
       self.Writeln( '<script>')
       self.response.out.write( 'function test()')
       self.Writeln( '{')
       self.Writeln( 'document.writeln("Javascript from inside py")')
       self.Writeln( '}')
       self.Writeln( 'test()')
       self.Writeln( 'hello()')
       self.Writeln( '</script>')

    def Table(self)  :
       self.Writeln( '<table align="center" class="sortable" >')

    def EndTable(self)  :
       self.Write( '</table>')

    def DoHeader(self):
       self.Write( '<tr>')
       self.Write( '<th scope="col">First Name</th>')
       self.Write( '<th scope="col">Last Name</th>')
       self.Write( '<th scope="col">City</th>')
       self.Write( '<th scope="col">NTRP</th>')
       self.Write( '<th scope="col">Roster</th>')
       self.Write( '</tr>')


    def DoLastRosteredHeader(self):
       self.Writeln( '<tr>')
       self.Write( '<th scope="col">Date</th>')
       self.Write( '<th scope="col">First Name</th>')
       self.Write( '<th scope="col">Last Name</th>')
       self.Write( '<th scope="col">Team</th>')
       self.Write( '<th scope="col">Captain</th>')
       self.Writeln( '</tr>')

    def TripleCell( self,data):
        self.response.out.write('<td valign="middle" colspan=8 width="500" ALIGN=LEFT>'+data+'&nbsp</td>')

    def TripleCellLink( self,id ,data):

        self.TripleCell('<a class="implink" style=text-decoration:none href="http://www.ustanorcal.com/teaminfo.asp?id='+ str(id) + '">' + str(data) + '</a>')

    def TeamCellLink( self,id ,data):

       self.Writeln('<a class="implink" style=text-decoration:none href="http://www.ustanorcal.com/teaminfo.asp?id='+ str(id) + '">' + str(data) + '</a>')
#      self.Writeln('<a class="implink" href="http://www.ustanorcal.com/teaminfo.asp?id='+ str(id) + '">' + str(data) + '</a>')

    def Cell( self,data):
       self.Write( '<td>' + str(data) + '</td>');

    def CellImage( self,data):
#      self.Write( '<td>' + str(data) + '</td>');
       self.Write( '<td>' + str(data) + '<img src="assets/images/sctc.jpeg" />'  '</td>');


    def CellLink( self,id , data):
       self.Cell('<a style=text-decoration:none href="http://www.ustanorcal.com/teaminfo.asp?id='+ str(id) + '">' + str(data) + '</a>')


    def CSS( self ):
       self.Write('<style type="text/css">\n')
       self.Write('table{\n')
       self.Write('font-family: "Tahoma", Verdana, Arial, Helvetica, sans-serif;\n')
       self.Write('font-size:  75%;\n')
       self.Write('border-collapse: collapse;\n')
       self.Write('}\n')

       self.Write('caption{\n')
       self.Write('background: url(title.png) no-repeat 50px;\n')
       self.Write('font-size: 400%;\n')
       self.Write('text-indent: -10000px;\n')
       self.Write('}\n')

       self.Write('tr{')
       self.Write('background-color: #EAFDFF;\n')
       self.Write('}\n')

       self.Writeln('thead th{')
       self.Writeln('      padding: 0.5em;')
       self.Writeln('      white-space: nowrap;')
       self.Writeln('}')
       self.Write('</style>\n')


    def get(self,fac):

        sctc="3483"
        cup = "113"
        laspalmas = "463"        

        if( fac == 'santaclara'):
             facilityid = sctc
             facilityname  = "Santa Clara "
        elif( fac == 'cupertino'):
             facilityid = cup
             facilityname  = "Cupertino"
        elif( fac == 'sunnyvale'):
             facilityid = laspalmas
             facilityname  = "Sunnyvale"
        elif( fac == ''):
             facilityid = cup
             facilityname  = "Cupertino"
        else:
             facilityid = cup
             facilityname  = "Cupertino"


        self.response.headers['Content-Type'] = 'text/html'

        self.Write('<html>\n')
        self.Write('<head>\n')
        self.Write('</head>\n')

        self.CSSHeader()
        self.ScriptHeader()

#       self.ScriptTester()

        self.Write('<center>\n')

        self.Write('<title>'+ facilityname + ' Players</title>\n')
        self.Write('<h1>'+ facilityname + '  USTA Rosters</h1>\n')
        self.Write('<body>\n')


        level =  self.request.get('level') 
        level = level.lower()
#
#       Show this for basic (nothing clicked)
        if( level == ''):
              level = 'last' # 's60m70'

        reg = "( M3.5)";
# Translate /?level=M35 to regular expression
#       dict = library.dict

        reg = "( " + level + ")"  # dict[level]

        self.Links(facilityid)

        if( re.search("last",reg)):
          query="select * from FacilityRoster where facility="+facilityid+" order by date desc , lname  limit 600"
          lastrostered =  db.GqlQuery( query )          

          self.Write('<center>Click on top row to sort </center>')
          self.Table()
#         self.TripleCell(" Last Rostered ")
          self.Write('<thead>\n')
          self.DoLastRosteredHeader()
          self.Write('</thead>\n')

          for l in lastrostered:
              query="select * from FacilityTeam where teamid=" + str(l.teamid) 
              if( l.date < datetime.date(2013,3,1)): break
              c =  db.GqlQuery( query )          
              self.Write( '<tr>')        
#             self.Cell(l.roster)
              self.Cell( l.date )
              self.Cell(l.fname)
              self.Cell(l.lname)
              self.CellLink(c[0].teamid , c[0].name )
              self.Cell(c[0].captain)
              self.Writeln( '</tr>')        

          self.EndTable()
          self.Writeln("</html>")
          return     # all below is for if not 'last' rostered
# ------------------------------------------------------------------------------

#  Search for selected team level from all teams 
        query="select __key__ from FacilityTeam where facility="+ facilityid + " order by position"

        keys =  db.GqlQuery( query )

        regexp = re.compile( reg, re.IGNORECASE)
        teams=[]
        for k  in keys:
           t = db.get(k)
           found = regexp.findall( t.name )
           if( found):
#              self.Write("found " + reg + "in " + t.name + "<br>" )
               teams.append(t)                

# Display the players from each team

        for t in teams:

#   Get the keys
           query="select __key__ from FacilityRoster where teamid="+ str(t.teamid) + " order by date desc"
           rosterkey =  db.GqlQuery( query)

           self.Write('<p>')


#          self.Write('\n<thead>')
           updated=''
           if( t.updated != None):
            updated = '('+  str(t.updated.month) + '/' + str(t.updated.day) + ' '
            min = t.updated.minute 
            if ( min < 10):
              min = '0' + str(min)

            updated += str(t.updated.hour) + ':' + str(min) + ')'

           name =  t.name + " " + t.captain 
           br = ' '
           if (len(name)> 40): br = '<br>'

# Team name, captain and last updated


           self.Writeln('<thead>')
#          self.TripleCellLink( t.teamid, name + updated )
           self.TeamCellLink( t.teamid, name + " " + updated )
           self.Writeln('</thead>')
           self.Table()

           self.Writeln('<thead>')
           self.DoHeader()
           self.Writeln('</thead>')

#          t.xrosterkey.sort(key=lambda k: db.get(k).date, reverse=True)

# Display each player on the roster
           for r in rosterkey:
               e = db.get(r )     

               if( e == None): continue
               self.Writeln( '<tr>')
               self.Cell(e.fname)
               self.Cell(e.lname)
               self.Cell(e.city)
               self.Cell(e.gender+ e.rating )
               self.Cell(e.roster)
#              self.Cell('ctc')
#              self.Cell('csc')
               self.Writeln( '</tr>')

           self.EndTable()  


        return





application = webapp.WSGIApplication(
                                     [('/(santaclara)', Display),
                                     ('/', Redirect),
                                     ('/(cupertino)', Display),
                                     ('/(cup)', TemplateDisplay),
                                     ('/(sunnyvale)', Display),
                                     ('/()', Display)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":

#   print __file__
#   print __name__

    main()


