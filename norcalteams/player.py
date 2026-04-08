import webapp2

from google.appengine.api import urlfetch

from google.appengine.ext.webapp import template
from google.appengine.ext import db
from google.appengine.ext import ndb

from datetime import timedelta

import urllib,re,datetime,string,sys,os

import operator # for sorting
import random   # for shuffling


import mysession
from ndbstore import *
from flights import *



def Writeln( selfobj, *t):
   for x in t:
     selfobj.response.out.write(x )
     selfobj.response.out.write(" ")

   selfobj.response.out.write("<br>")

def Write( selfobj, *t):
   for x in t:
     selfobj.response.out.write(x )
     selfobj.response.out.write(" ")


def getRecord(sobj,playerid):

      url  = "http://www.ustanorcal.com/playermatches.asp?id=" + str(playerid)
      result = urlfetch.fetch(url)
      s = result.content
      s = s.replace("\r","")      
      s = s.replace("\n","")      
      scraped = s.replace("\t","")      


      pattern = r"(l=1698)([^~]*?)</tr>"   # Captain

      r = re.compile(pattern,re.IGNORECASE )
      match = r.findall( scraped )


      for i,m in enumerate(match):
         print str(i) + ") " + str(m)
         Writeln(sobj,  str(i) + ") " + str(m[0]) + " ^ " + str(m[1])   )
         print "\n"

         try:
            r1 = re.search(r"<td align=center>([ \d]*)/([ \d]*)<\/td>", m[1])
            if(r1 != None):
              w = r1.group(1)
              l = r1.group(2)     
              print "win/loss = " + str(w) + "/" + str(l)
              Writeln(sobj,  "win/loss = " + str(w) + "/" + str(l) )

         except Exception as e:
             print "EXCEPTION: -> " + str(e)


def getTeam(sobj,teamid):

      url  = "http://www.ustanorcal.com/teaminfo.asp?id=" + str(teamid)
      result = urlfetch.fetch(url)
      s = result.content
      s = s.replace("\r","")      
      s = s.replace("\n","")      
      scraped = s.replace("\t","")      

      pName = r"([ \d\w\'\-]*)"

      pattern = r"(playermatches\.asp?id=[\d]*)"   
      pattern = r"<a href=(playermatches.asp\?id=[\d]*)>" + pName + "[ ,]*" + pName  + "[ ]*</a></td>"
      pattern += r"<td ([^~]*?)</td>"   # City
      pattern += r"<td ([^~]*?)</td>"   # Gender
      pattern += r"<td ([^~]*?)</td>"   # Rating
      pattern += r"<td ([^~]*?)</td>"   # NP/SW
      pattern += r"<td ([^~]*?)</td>"   # Expiration
      pattern += r"<td ([^~]*?)</td>"   # Win,Loss

      r = re.compile(pattern,re.IGNORECASE )
      match = r.findall( scraped )

      print( "*"*40 )

#     0: id  1: lname 2:fname 3:city  4: Gender 5:Rating 8:Win,Loss
      _city = _gender = _rating = _win = _loss ="xxx"

      playerList=[]
      for i,m in enumerate(match):
       
         r1 = re.search(r"id=([\d]*)", m[0])
         if( r1 != None):
              _id =  r1.group(1)

         _lname = m[1]
         _fname = m[2]

         r3 = re.search(r"nowrap>" +pName , m[3])
         if( r3 != None):
              _city =  r3.group(1)

         r4 = re.search(r"(M|F)" , m[4])
         if( r4 != None):
              _gender =  r4.group(1)
              if _gender=="F": _gender="W"

         r5 = re.search(r">([ \.\d\w]*)" , m[5])
         if( r5 != None):
              _rating =  r5.group(1)

         r8 = re.search(r">([\d]*)[ \/]*([\d]*)" , m[8])
         if( r8 != None):
              _win  =  r8.group(1)
              _loss =  r8.group(2)


         p = Player()
#        p.teamid = str(teamid)
#        p.id = int(_id)
         p.id = str(teamid)+"_"+_id

         p.name = _fname + " " + _lname
         p.rating = _gender+_rating
         p.winloss = _win+"-"+_loss
         playerList.append(p)
#        Writeln(sobj,  _id, _lname, _fname ,_city, _gender, _rating, _win , _loss)
#        print( _id, _lname, _fname ,_city,_gender, _rating, _win , _loss )

      return playerList


class PlayerHandler(webapp2.RequestHandler):


    def get(self):
      Writeln(self, "PlayerHandler")

      getRecord( self,  83240 )
      getRecord( self,  100901 )

class TeamHandler(webapp2.RequestHandler):


    def get(self):
      Writeln(self, "TeamHandler")

#      getTeam( self,  66419 )
#      getTeam( self,  66432 )

#Combo 1698 - 1701 , 1690-1693
#MX 1791-94
#40 1780-83  , 1786-1790


      flightid = 1780
      flightid = 1700

      flightKey = ndb.Key(Flight, str(flightid) )
      o = flightKey.get()
      if( o == None):
         print("cant find flight")
         return
          
      pdict = {}
# Get current players
      for p in o.players:
         pdict[p.id]= p

      start = 0
      limit = start + 5
      for i,t in enumerate(o.teams):
         if i<start: continue
         players = getTeam( self,  t.teamid )
         print( str(t.teamid), t.teamname)
         Writeln(self, str(t.teamid), t.teamname)
#        Writeln(self,players)
         if  i> limit: break

# update
         for q in players:
           pdict[q.id]= q

#     outside loop
      pList=[]
      for i,v in enumerate(pdict):
        pList.append(pdict[v])

      for p in pList:
        print p.id, p.name, p.rating,p.winloss

      print("Players to add ")
      print(pList)

      o.players=pList
      o.put()

class P:
    name=rating=playerid=""
    win=loss=0

class DisplayHandler( mysession.BaseHandler ):

    def get(self ):
        flightid = 1700
        flightKey = ndb.Key(Flight, str(flightid) )
        o = flightKey.get()
        if( o!= None):
            print(" got flight ")

        players = o.players
        print(players)

        playerDict={}
        for i,p in enumerate(players):
              if( i > 25): break
              q = P()
              q.name = p.name
              q.rating = p.rating

              try:
#               print "try = " + p.winloss
                r1 = re.search(r"([\d]*)-([\d]*)", p.winloss)
                if(r1 != None):
                    w = r1.group(1)
                    l = r1.group(2)     
                    print "win/loss = " + (w) + "/" + l 
                    q.win = int(w)
                    q.loss = int(l)
#                   print("w/l = " + str(w) + "/" + str(l) )
              except Exception as e:
                print "EXCEPTION: -> " + str(e)

              try:
                r2 = re.search(r"([\d]*)_([\d]*)", p.id)
                if(r2 != None):
                    playerid = r2.group(2)     
                    q.playerid = playerid
                    print("id = " + playerid )
              except Exception as e:
                print "EXCEPTION: -> " + str(e)

              print(q.name,q.playerid)
#             playerList.append(q)




class DisplayHandler_( mysession.BaseHandler ):

    def get(self ):

        flightid = 1700
        flightKey = ndb.Key(Flight, str(flightid) )
        o = flightKey.get()
        if( o!= None):
            print(" got flight ")

        players = o.players
        print(players)

        playerList=[]
        for i,p in enumerate(players):
#             if( i > 25): break
              q = P()
              q.name = p.name
              q.rating = p.rating

              try:
#               print "try = " + p.winloss
                r1 = re.search(r"([\d]*)-([\d]*)", p.winloss)
                if(r1 != None):
                    w = r1.group(1)
                    l = r1.group(2)     
                    print "win/loss = " + (w) + "/" + l 
                    q.win = int(w)
                    q.loss = int(l)
#                   print("w/l = " + str(w) + "/" + str(l) )
              except Exception as e:
                print "EXCEPTION: -> " + str(e)

              try:
                r2 = re.search(r"([\d]*)_([\d]*)", p.id)
                if(r2 != None):
                    playerid = r2.group(2)     
                    q.playerid = playerid
                    print("id = " + playerid )
              except Exception as e:
                print "EXCEPTION: -> " + str(e)

              print(q.name,q.playerid)
              playerList.append(q)


        playerList.sort( key = operator.attrgetter('win') , reverse=True)



        template_values = {
                'players'     : playerList
#               'flightlist'    : flightList
        }

        print("DisplayHandler")

        path = os.path.join(os.path.dirname(__file__), 'templates','player.html')
        self.response.out.write(template.render(path, template_values))


app = webapp2.WSGIApplication(
                                     [
#                                     ('/player', PlayerHandler),
                                      ('/team', TeamHandler),
                                      ('/player', DisplayHandler)


                                     ],
                                      debug=True,config=mysession.config)


