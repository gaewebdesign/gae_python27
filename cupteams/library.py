
from google.appengine.api import urlfetch
from google.appengine.ext import db

import urllib
import sys
import httplib
import re
import string

import datastore
import datetime


sctc="3483"
cup = "113"
laspalmas="463"

unused = {  
                  "cm65":" (CM6.5)" , "cm75":" (CM7.5)","cm85":" (CM8.5)","cw65":" (CW6.5)", "cw75":" (CW7.5)", "cw85":" (CW8.5)", 
                  "fmx60":" (FMX6)" , "fmx70":" (FMX7)", "fmx80":" (FMX8)", "fmx90":" (FMX9)", 
                  "mx6":" (MX6)" , "mx7":" (MX7)", "mx8":" (MX8)", "mx8":" (MX8)","mx9":" (MX9)",
                  "m30":" (m3.0)" , "m35":" (m3.5)", "m40":" (m4.0)", "m45":" (m4.5)",
                  "w30":" (w3.0)" , "w35":" (w3.5)", "w40":" (w4.0)", "w45":" (w4.5)",
                  "s65m35":" (s65m3.5)" , "s65m40":" (s65m4.0)", "s65w35":" (s65w3.5)",
                  "s60m70":" (s60m7.0)" , "s60m80":" (s60m8.0)", "s60w70":" (s60w7.0)", "s60w80":" (s60w8.0)", 
                  "last": "last"
}




def getfacilityNameID( fac ):


    if( fac == 'sctc' or fac=='santaclara' or fac=='uploadsctc'):
        facilityid = sctc
        facilityname  = "Santa Clara"
    elif( fac == 'cup' or fac=='cupertino' or fac=='uploadctc'):
        facilityid = cup
        facilityname  = "Cupertino"
    elif( fac=='lp' or fac == 'sunnyvale' or fac=='uploadlp'):
        facilityid = laspalmas
        facilityname  = "Sunnyvale"
    else:
         facilityid = cup
         facilityname  = "Cupertino"

    return [ facilityid , facilityname]




def getfacility(req):

     facilityid = sctc
     if(req=="sctc"):
          facilityid = sctc
     elif( req=="csc" or req == "cup" or req=="cupertino"):
          facilityid = cup
     elif( req=="lp" or req == "sunnyvale"):
          facilityid = laspalmas


     return facilityid

def Links( self, idx , fac=""):

      sunnyvale = ( "CM6.5","CM7.5","CM8.5","CM9.5","CW6.5","CW7.5","CW8.5","+",
                    "FMX6.0","FMX7.0","FMX8.0","+",
                    "M3.0","M3.5","M4.0","M4.5","W3.0","W3.5","W4.0","W4.5","+",
                    "Mx6.0","Mx7.0","Mx8.0","Mx9.0","+",
                    "S65M3.5", "S65M4.0", "S65M3.5","S60M7.0", "S60M8.0", "S60W7.0","S60W8.0","*",
                    "last rostered","-"
              )

      cupertino = ( 
                     "18AM3.0","18AM3.5","18AM4.0","18AM4.5","18AW3.0","18AW3.5","18AW4.0","18AW4.5","+",
                     "65AM3.5","+",

                     "18AM3.0","18AM3.5","18AM4.0","18AM4.5","18AW3.0","18AW3.5","18AW4.0","18AW4.5","+",
#                     "65AM3.5","65AW3.5","+",

#                     "40Mx6.0","40Mx7.0","40Mx8.0","40Mx9.0","+",
#                     "40AM3.0","40AM3.5","40AM4.0","40AM4.5","+",
#                     "40AW3.0","40AW3.5","40AW4.0","40AW4.5","+",
#                    "55Mx6.0","55Mx7.0","55Mx8.0","55Mx9.0","+",
#                    "CM6.5","CM7.5","CM8.5","CW6.5","CW7.5","CW8.5","+",
#                    "S70M7.0", "S70M7.5","+",
#                    "18Mx6.0","18Mx7.0","18Mx8.0","18Mx9.0","+",
#                    "40AM3.5","40AM4.0","40AM4.5","40AW3.0","40AW3.5","40AW4.0","40AW4.5","+",
#                    "CM6.5","CM7.5","CM8.5","CW6.5","CW7.5","CW8.5"

#                     "18Mx6.0","18Mx7.0", "18Mx8.0", "18Mx9.0","+",
#                     "18AM3.0","18AM3.5","18AM4.0","18AM4.5","18AW3.0","18AW3.5","18AW4.0","18AW4.5","+",

#                     "65AM3.5","65AM4.0","+",
#                     "55Mx7.0","55Mx8.0","+",
#                    "FMx6.0","FMx7.0","FMx8.0", "FMx9.0","+",



#                     "SM3.0","SM3.5","SM4.0","SM4.5","SW3.0","SW3.5","SW4.0","SW4.5","*",
#                     "S65M3.5", "S65M4.0", "S65W3.5","*",
                     "last rostered","-"

#                    "FMX6.0","FMX7.0","FMX8.0","FMX9.0","+",


              )

      santaclara = ( "CM7.5","CM8.5","CW8.5","+",
                     "M3.5","M4.5","W3.5","W4.0","+",
                     "MX7.0","MX8.0","MX9.0","*",
                     "last rostered","-"
              )


      level = cupertino
      facility = "cup"
      if( idx == "3483"):
          level = santaclara
          facility = "sctc"
      elif( idx == "463"):
          level = sunnyvale
          facility = "lp"


#     Index into link dictionary using level list   
      self.Write('<table  cellpadding="2">\n')
      self.Write('<th>\n')
      for v in level:


          if( v == "+" ):
              self.Write('</table>') 
              self.Write('</th>\n')
              self.Write('<table  cellpadding="2">\n')
              self.Write('<th>\n')
          elif( v == "*" ):
              self.Write('</th>\n')
              self.Write('</table>') 
              self.Write('<br>\n')
              self.Write('<table  cellpadding="2">\n')
              self.Write('<th>\n')
          elif( v == "-" ):
              self.Write('</table>') 
              self.Write('</th>\n')
          else:
            link = '<a style=text-decoration:none href=?level='+v+'>'+v+'</a>&nbsp\n'
            if( fac!=""):
              link = '<a style=text-decoration:none href=?facility='+facility+'&level='+v+'>'+v+'</a>&nbsp\n'
            self.Write(link)



def scrapeteam(self, facilityid,idx,name,captain):

       url = "http://www.ustanorcal.com/teaminfo.asp?id=" + str(idx)

       result = urlfetch.fetch(url)
       scraped = result.content
# <a href=playermatches.asp?id=15067>Lynch, Carl H 

#   Get id , lname,fname,city
       rexp = r"nowrap><a href=playermatches\.asp\?id=([\d]*)>([ \-\w\d\'\.]*)[, ]*([ \-\w\d\'\.]*)[ <>\w=#\d\/]*?nowrap>([ \w]*)"

#   Get id , lname,fname,city, place holder, rating
       rexp = r"nowrap><a href=playermatches\.asp\?id=([\d]*)>([ \-\w\d\'\.]*)[, ]*([ \-\w\d\'\.]*)[ <>\w=#\d\/]*?nowrap>([ \w]*)([ <>\/=#\d\w]*>)(\d\.\d)"


# NOTE  the city regexp was modifed to ([ ,\w]*)  .. the comma added Robert Inocencio's city is San Jose,
#                                                id        lname               fname                                city
       rexp = r"<a href=playermatches\.asp\?id=([\d]*)>([ \-\w\d\'\.]*)[, ]*([ \-\w\d\'\.]*)[ <>\w=#\d\/]*?nowrap>([ ,\w]*)"
#                                              gender                  rating
       rexp += r"([ <>\/=#\d\w]* align=center)>(M|F|U)<([ \/td<>=#\d\w]*)>(\d\.\d\w)*<"
#      0: id 1: lname 2: fname 3: city 4:  5: gender 6: 7: rating


#      Get the player name
       r = re.compile(rexp,re.IGNORECASE )
       player = r.findall( scraped )

#      Get the roster date
       rexp2 = r"align=center>([\d]{1,2}\/[\d]{1,2}\/[\d]{2})<\/td><\/tr>";

#      This is new (5/15/14) Aftr P/N/S columsn were added (took out <\tr> as it was another line
       rexp2 = r"align=center>([\d]{1,2}\/[\d]{1,2}\/[\d]{2})<\/td>";
       r2 = re.compile( rexp2, re.IGNORECASE)
       roster = r2.findall( scraped )
      

#       For debugging
#       self.Write( "enumerate player"  )
#       for id,n in enumerate(player):
#           self.Write( n[0] + " " + n[1] + " " + n[2]  + "<br>" )

#       for r in enumerate(roster):
#          self.Write( str(r)  + "<br>")

#       self.Write( "------------"  )


#      Number of players equals number of roster dates
       plen = len(player)
       rlen = len(roster)
       self.Write( '<br>' + str(idx) + " " +  name + " " + captain + " rlen=" + str(rlen) + " plen="  + str(plen) + '<--<br>')

#      Stop here if something is wrong
       if( plen != rlen):
          self.Write('len of player != roster ')
          return None,rlen,plen

       rlist=[]

       for id,name in enumerate(player):
#   name = (player_id, lname, fname )   
#        url = "http://www.ustanorcal.com/playermatches.asp?id="+name[0]

         r = datastore.FacilityRoster( key_name= str(idx)+"_"+name[0] )   #key_name prohibits dup entries
         r.teamid = idx
#      0: id 1: lname 2: fname 3: city 4:  5: gender 6: 7: rating
         r.playerid = int(name[0])
         r.facility = int(facilityid)
         r.lname = name[1]
         r.fname = name[2]
         r.city   = name[3]      
         r.gender   = name[5]
         r.rating   = name[7].lower()
         r.roster= roster[id]
         d = r.roster.split('/')
         r.date = datetime.date( 2000+int(d[2]),int(d[0]),int(d[1]) )

         rlist.append(r)
#        self.Write( str(r.playerid) + ') ' + r.fname+' '+ r.lname + ' ' + r.city + ' ' + r.gender + ' ' + r.rating + ' ' + r.roster + ' ' + str(r.date) + '<br>' )

#   Put into db in one call
#         db.put(rlist)


       return rlist,rlen,plen

