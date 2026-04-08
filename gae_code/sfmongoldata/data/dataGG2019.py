#GGTC
import webapp2 
from datastore import  *


def ggtc2019(selfobj):

	selfobj.response.write("Henry Brodkin 45 Graystone Terrace henrybrodkin@sbcglobal.net M3.5") 
	selfobj.response.write("<br>") 
	g =GGTC(key=ndb.Key(GGTC,"1539591102")) 
	g.fname = "Henry" 
	g.lname = "Brodkin" 
	g.address = "45 Graystone Terrace" 
	g.city = "San Francisco"
	g.zip = "94114"
	g.ntrp = "M3.5"
	g.email = "henrybrodkin@sbcglobal.net" 
	g.year = 2019 

	g.help = "" 
	g.other = "" 
	g.ip = "" 

	g.put() 

	selfobj.response.write("Lynn Little 125 Baltimore Ave lynmlittle@hotmail.com W4.0") 
	selfobj.response.write("<br>") 
	g =GGTC(key=ndb.Key(GGTC,"1539581954")) 
	g.fname = "Lynn" 
	g.lname = "Little" 
	g.address = "125 Baltimore Ave" 
	g.city = "Corte Madera"
	g.zip = "94925"
	g.ntrp = "W4.0"
	g.email = "lynmlittle@hotmail.com" 
	g.year = 2019 

	g.help = "" 
	g.other = "" 
	g.ip = "" 
	g.put() 

	selfobj.response.write("Jane Cloniger 75 Sheridan St #102 jane.cloninger@gmail.com W3.5") 
	selfobj.response.write("<br>") 
	g =GGTC(key=ndb.Key(GGTC,"1539925533")) 
	g.fname = "Jane" 
	g.lname = "Cloniger" 
	g.address = "75 Sheridan St #102" 
	g.city = "San Francisco"
	g.zip = "94103"
	g.ntrp = "W3.5"
	g.email = "jane.cloninger@gmail.com" 
	g.year = 2019 

	g.help = "" 
	g.other = "" 
	g.ip = "" 
	g.put() 

	selfobj.response.write("Lily Lew 710 11th Ave lily_lew@yahoo.com W3.5") 
	selfobj.response.write("<br>") 
	g =GGTC(key=ndb.Key(GGTC,"1539893728")) 
	g.fname = "Lily" 
	g.lname = "Lew" 
	g.address = "710 11th Ave" 
	g.city = "San Francisco"
	g.zip = "94118"
	g.ntrp = "W3.5"
	g.email = "lily_lew@yahoo.com" 
	g.year = 2019 

	g.help = "" 
	g.other = "" 
	g.ip = "" 
	g.put() 

	selfobj.response.write("Bryan Fong 2373 Sharon Rd bdbdbd309@yahoo.com M4.0") 
	selfobj.response.write("<br>") 
	g =GGTC(key=ndb.Key(GGTC,"1540981087")) 
	g.fname = "Bryan" 
	g.lname = "Fong" 
	g.address = "2373 Sharon Rd" 
	g.city = "Menlo Park"
	g.zip = "94025"
	g.ntrp = "M4.0"
	g.email = "bdbdbd309@yahoo.com" 
	g.year = 2019 

	g.help = "" 
	g.other = "" 
	g.ip = "" 
	g.put() 

	selfobj.response.write("Patricia Crisea 155 Yerba Buena patzcrisera@gmail.com W3.5") 
	selfobj.response.write("<br>") 
	g =GGTC(key=ndb.Key(GGTC,"1540959093")) 
	g.fname = "Patricia" 
	g.lname = "Crisea" 
	g.address = "155 Yerba Buena" 
	g.city = "San Francisco"
	g.zip = "94127"
	g.ntrp = "W3.5"
	g.email = "patzcrisera@gmail.com" 
	g.year = 2019 

	g.help = "" 
	g.other = "" 
	g.ip = "" 

	g.put() 

	selfobj.response.write("Anne Kavanagh 452 Cavour St annekava@gmail.com W4.0") 
	selfobj.response.write("<br>") 
	g =GGTC(key=ndb.Key(GGTC,"1541040470")) 
	g.fname = "Anne" 
	g.lname = "Kavanagh" 
	g.address = "452 Cavour St" 
	g.city = "Oakland"
	g.zip = "94618"
	g.ntrp = "W4.0"
	g.email = "annekava@gmail.com" 
	g.year = 2019 


	g.help = "" 
	g.other = "" 
	g.ip = "" 
	g.put() 

	selfobj.response.write("Kathy Raffel 21 Ora Way kkraffel@mac.com W3.5") 
	selfobj.response.write("<br>") 
	g =GGTC(key=ndb.Key(GGTC,"1541100566")) 
	g.fname = "Kathy" 
	g.lname = "Raffel" 
	g.address = "21 Ora Way" 
	g.city = "San Francisco"
	g.zip = "94131"
	g.ntrp = "W3.5"
	g.email = "kkraffel@mac.com" 
	g.year = 2019 

	g.help = "" 
	g.other = "" 
	g.ip = "" 

	g.put() 

	selfobj.response.write("Marilyn Esquivel 816 3rd Ave mesquivel@sanbrunocable.com W3.5") 
	selfobj.response.write("<br>") 
	g =GGTC(key=ndb.Key(GGTC,"1541050609")) 
	g.fname = "Marilyn" 
	g.lname = "Esquivel" 
	g.address = "816 3rd Ave" 
	g.city = "San Bruno"
	g.zip = "94006"
	g.ntrp = "W3.5"
	g.email = "mesquivel@sanbrunocable.com" 
	g.year = 2019 

	g.help = "" 
	g.other = "" 
	g.ip = "" 

	g.put() 

	selfobj.response.write("Ruth Fleming 335 2nd Ave reflem@rockisland.com W") 
	selfobj.response.write("<br>") 
	g =GGTC(key=ndb.Key(GGTC,"1541043628")) 
	g.fname = "Ruth" 
	g.lname = "Fleming" 
	g.address = "335 2nd Ave" 
	g.city = "San Francisco"
	g.zip = "94118"
	g.ntrp = "W"
	g.email = "reflem@rockisland.com" 
	g.year = 2019 


	g.help = "" 
	g.other = "" 
	g.ip = "" 
	g.put() 

	selfobj.response.write("Henry Soong  h.soong@gmail.com M4.0") 
	selfobj.response.write("<br>") 
	g =GGTC(key=ndb.Key(GGTC,"1540657125")) 
	g.fname = "Henry" 
	g.lname = "Soong" 
	g.address = "" 
	g.city = "Hayward"
	g.zip = "94618"
	g.ntrp = "M4.0"
	g.email = "h.soong@gmail.com" 
	g.year = 2019 


	g.help = "" 
	g.other = "" 
	g.ip = "" 

	g.put() 


