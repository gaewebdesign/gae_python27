

#
#
#select * from paypal where year = "2019"  union select * from bycheck where year =  "2019" order by year,lname 
#
#
import webapp2
from datastore import  *


def santaclara2019(selfobj):


#1 

	selfobj.response.write("Bruce  Becker  beckerfive@comcast.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1542322494")) 
	g.year=2019
	g.fname="Bruce"
	g.lname="Becker"
	g.address="1890 Woodland Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 244-4864" 
	g.ntrp="M4.0" 
	g.mtype="RF_" 
	g.put()
#2 

	selfobj.response.write("Linda  Becker  beckerfive@comcast.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1542322300")) 
	g.year=2019
	g.fname="Linda"
	g.lname="Becker"
	g.address="1890 Woodland Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 244-4864" 
	g.ntrp="F" 
	g.mtype="RF" 
	g.put()
#3 

	selfobj.response.write("Carrie  Bell  c.p.bell@att.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1542054342")) 
	g.year=2019
	g.fname="Carrie"
	g.lname="Bell"
	g.address="1244 Maryann Drive" 
	g.city="Santa Clara" 
	g.phone="(408) 464-3177" 
	g.ntrp="F4.0" 
	g.mtype="RF" 
	g.put()
#4 

	selfobj.response.write("Randy  Bell  c.p.bell@att.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1542054575")) 
	g.year=2019
	g.fname="Randy"
	g.lname="Bell"
	g.address="1244 Maryann Drive" 
	g.city="Santa Clara" 
	g.phone="(408) 507-0956" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#5 

	selfobj.response.write("Jonathan  Bell  c.p.bell@att.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1542054671")) 
	g.year=2019
	g.fname="Jonathan"
	g.lname="Bell"
	g.address="1244 Maryann Drive" 
	g.city="Santa Clara" 
	g.phone="(408) 464-3177" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#6 

	selfobj.response.write("Mar  Garcia  margarciaus@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1542135022")) 
	g.year=2019
	g.fname="Mar"
	g.lname="Garcia"
	g.address="56 Paterson Place" 
	g.city="Santa Clara" 
	g.phone="(408) 679-0634" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#7 

	selfobj.response.write("Elizabeth  Grover  elizgrover@me.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1542317833")) 
	g.year=2019
	g.fname="Elizabeth"
	g.lname="Grover"
	g.address="332 Carriage Drive, Apt. 3" 
	g.city="Santa Clara" 
	g.phone="(650) 303-4446" 
	g.ntrp="F3.0" 
	g.mtype="RF" 
	g.put()
#8 

	selfobj.response.write("Zelda  Grover  elizgrover@me.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1542317980")) 
	g.year=2019
	g.fname="Zelda"
	g.lname="Grover"
	g.address="332 Carriage Drive, Apt. 3" 
	g.city="Santa Clara" 
	g.phone="(650) 303-4446" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#9 

	selfobj.response.write("Alice  Isaacson  aliceisaacson@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1542094003")) 
	g.year=2019
	g.fname="Alice"
	g.lname="Isaacson"
	g.address="513 Hickory Place" 
	g.city="Santa Clara" 
	g.phone="(408) 247-0343" 
	g.ntrp="F" 
	g.mtype="RF" 
	g.put()
#10 

	selfobj.response.write("Mark  Isaacson  mji1422@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1542094711")) 
	g.year=2019
	g.fname="Mark"
	g.lname="Isaacson"
	g.address="513 Hickory Place" 
	g.city="Santa Clara" 
	g.phone="(408) 247-0343" 
	g.ntrp="M3.5" 
	g.mtype="RF_" 
	g.put()
#11 

	selfobj.response.write("david  Kohls  kohlsins@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1542234792")) 
	g.year=2019
	g.fname="david"
	g.lname="Kohls"
	g.address="1045 Live Oak Dr" 
	g.city="Santa Clara" 
	g.phone="(408) 940-7790" 
	g.ntrp="M" 
	g.mtype="RF" 
	g.put()
#12 

	selfobj.response.write("James  Kohls  jameskohls@live.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1542234944")) 
	g.year=2019
	g.fname="James"
	g.lname="Kohls"
	g.address="1045 Live Oak Dr" 
	g.city="Santa Clara" 
	g.phone="(408) 247-3177" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#13 

	selfobj.response.write("Hana  Koraitem  jeanneoxford@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1542245170")) 
	g.year=2019
	g.fname="Hana"
	g.lname="Koraitem"
	g.address="3251 Loma Alta Drive" 
	g.city="Santa Clara" 
	g.phone="(408) 985-7901" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#14 

	selfobj.response.write("Malik  Koraitem  jeanneoxford@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1542245464")) 
	g.year=2019
	g.fname="Malik"
	g.lname="Koraitem"
	g.address="3251 Loma Alta Drive" 
	g.city="Santa Clara" 
	g.phone="(408) 985-7901" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#15 

	selfobj.response.write("Ace  Oxford  jeanneoxford@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1542245078")) 
	g.year=2019
	g.fname="Ace"
	g.lname="Oxford"
	g.address="3251 Loma Alta Drive" 
	g.city="Santa Clara" 
	g.phone="() 985-7901" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#16 

	selfobj.response.write("Jeanne  Oxford  jeanneoxford@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1542244899")) 
	g.year=2019
	g.fname="Jeanne"
	g.lname="Oxford"
	g.address="3251 Loma Alta Drive" 
	g.city="Santa Clara" 
	g.phone="(408) 985-7901" 
	g.ntrp="F3.0" 
	g.mtype="RF" 
	g.put()
#17 

	selfobj.response.write("Svend  Tang-Petersen  svend_tangpetersen@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1542134896")) 
	g.year=2019
	g.fname="Svend"
	g.lname="Tang-Petersen"
	g.address="56 Paterson Place" 
	g.city="Santa Clara" 
	g.phone="(408) 768-1093" 
	g.ntrp="M" 
	g.mtype="RF" 
	g.put()
#18 

	selfobj.response.write("Debbie  Tripiano  dtripiano@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1542121767")) 
	g.year=2019
	g.fname="Debbie"
	g.lname="Tripiano"
	g.address="1291 Pomeroy Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 772-6104" 
	g.ntrp="F4.0" 
	g.mtype="RF" 
	g.put()
#19 

	selfobj.response.write("Vince  Ventura  aceventura3@mac.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1542323574")) 
	g.year=2019
	g.fname="Vince"
	g.lname="Ventura"
	g.address="2653 Elliot Street" 
	g.city="Santa Clara" 
	g.phone="(408) 425-3420" 
	g.ntrp="M2.5" 
	g.mtype="RF_" 
	g.put()
#20 

	selfobj.response.write("Ryan  Ventura  loriv@me.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1542324277")) 
	g.year=2019
	g.fname="Ryan"
	g.lname="Ventura"
	g.address="2653 Elliot Street" 
	g.city="Santa Clara" 
	g.phone="(408) 425-3420" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#21 

	selfobj.response.write("Lori  Ventura  loriv@me.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1542323446")) 
	g.year=2019
	g.fname="Lori"
	g.lname="Ventura"
	g.address="2653 Elliot Street" 
	g.city="Santa Clara" 
	g.phone="(408) 425-3420" 
	g.ntrp="F3.5" 
	g.mtype="RF" 
	g.put()
#22 

	selfobj.response.write("Warren  Yamaguchi  winini@comcast.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1542206560")) 
	g.year=2019
	g.fname="Warren"
	g.lname="Yamaguchi"
	g.address="1291 Pomeroy Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 772-6104" 
	g.ntrp="M4.0" 
	g.mtype="RF_" 
	g.put()
