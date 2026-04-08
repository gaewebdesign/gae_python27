

#
#
#select * from paypal where year = "2018"  union select * from bycheck where year =  "2018" order by year,lname 
#
#
import webapp2
from datastore import  *


def santaclara2018(selfobj):


#1 

	selfobj.response.write("Karen  Abad  abadkj@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1513898705")) 
	g.year=2018
	g.fname="Karen"
	g.lname="Abad"
	g.email="abadkj@sbcglobal.net" 
	g.address="2786 EVERSOLE DR" 
	g.city="SAN JOSE" 
	g.phone="(408) 499-8279" 
	g.zip="95133" 
	g.ntrp="F" 
	g.mtype="NRS" 
	g.put()
#2 

	selfobj.response.write("Jennifer   Adams  jenyferadams@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1521663717")) 
	g.year=2018
	g.fname="Jennifer "
	g.lname="Adams"
	g.email="jenyferadams@sbcglobal.net" 
	g.address="847 Colleen Drive" 
	g.city="San Jose" 
	g.phone="(408) 313-4405" 
	g.zip="95123" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#3 

	selfobj.response.write("Sanjay  Agarwal  agarwalsanjay@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1515524949")) 
	g.year=2018
	g.fname="Sanjay"
	g.lname="Agarwal"
	g.email="agarwalsanjay@gmail.com" 
	g.address="4231 NORWALK DR, APT EE101" 
	g.city="SAN JOSE" 
	g.phone="(408) 839-6887" 
	g.zip="95129" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#4 

	selfobj.response.write("Alok  Aggarwal  alok.cdac@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1521856692")) 
	g.year=2018
	g.fname="Alok"
	g.lname="Aggarwal"
	g.email="alok.cdac@gmail.com" 
	g.address="501 Murphy Ranch Road, Apt 429" 
	g.city="Milpitas" 
	g.phone="(510) 925-6995" 
	g.zip="95035" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#5 

	selfobj.response.write("Sreenivas  aluru  salur1@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1519674572")) 
	g.year=2018
	g.fname="Sreenivas"
	g.lname="aluru"
	g.email="salur1@yahoo.com" 
	g.address="10816 Alderbrook ln" 
	g.city="Cupertino" 
	g.phone="(408) 406-1885" 
	g.zip="95014" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#6 

	selfobj.response.write("Michael  Alvarez  mickeya62@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1515619932")) 
	g.year=2018
	g.fname="Michael"
	g.lname="Alvarez"
	g.email="mickeya62@yahoo.com" 
	g.address="1060 South 3rd St, #183" 
	g.city="San Jose" 
	g.phone="(408) 315-6385" 
	g.zip="95112" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#7 

	selfobj.response.write("Mark  Alves  markalves01@aol.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1521673230")) 
	g.year=2018
	g.fname="Mark"
	g.lname="Alves"
	g.email="markalves01@aol.com" 
	g.address="1491 Bellomy St" 
	g.city="Santa Clara" 
	g.phone="(408) 205-4389" 
	g.zip="95050" 
	g.ntrp="M3.5" 
	g.mtype="RS" 
	g.put()
#8 

	selfobj.response.write("Nancy  Andersen  Nbragaandersen@Gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1514991893")) 
	g.year=2018
	g.fname="Nancy"
	g.lname="Andersen"
	g.email="Nbragaandersen@Gmail.com" 
	g.address="3032 Cameron Way" 
	g.city="Santa Clara" 
	g.phone="(408) 799-3678" 
	g.zip="95051" 
	g.ntrp="F3.5" 
	g.mtype="RF" 
	g.put()
#9 

	selfobj.response.write("Andres  Aparicio  a.aparicio@att.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1515463715")) 
	g.year=2018
	g.fname="Andres"
	g.lname="Aparicio"
	g.email="a.aparicio@att.net" 
	g.address="5711 Venado Ct" 
	g.city="San Jose" 
	g.phone="(408) 775-4921" 
	g.zip="95123" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#10 

	selfobj.response.write("Brant  Armstrong  brant55@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1514317011")) 
	g.year=2018
	g.fname="Brant"
	g.lname="Armstrong"
	g.email="brant55@sbcglobal.net" 
	g.address="3102 Fresno St" 
	g.city="Santa Clara" 
	g.phone="(408) 910-7003" 
	g.zip="95051" 
	g.ntrp="M4.0" 
	g.mtype="RS" 
	g.put()
#11 

	selfobj.response.write("Janet  Armstrong  brant55@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1519937455")) 
	g.year=2018
	g.fname="Janet"
	g.lname="Armstrong"
	g.email="brant55@sbcglobal.net" 
	g.address="3102 Fresno St" 
	g.city="Santa Clara" 
	g.phone="(408) 910-7003" 
	g.zip="95051" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#12 

	selfobj.response.write("Hideko  Azama  tennissenior@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1520297534")) 
	g.year=2018
	g.fname="Hideko"
	g.lname="Azama"
	g.email="tennissenior@yahoo.com" 
	g.address="3115 Maurica Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 246-5129" 
	g.zip="95051" 
	g.ntrp="F3.5" 
	g.mtype="RF" 
	g.put()
#13 

	selfobj.response.write("Lisa  Backus  lisa.backus3@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1532394412")) 
	g.year=2018
	g.fname="Lisa"
	g.lname="Backus"
	g.email="lisa.backus3@gmail.com" 
	g.address="10565 San Leandro Avenue" 
	g.city="Cupertino" 
	g.phone="(415) 577-7183" 
	g.zip="95014" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#14 

	selfobj.response.write("Matt  Bays  valeriebays@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1513044417")) 
	g.year=2018
	g.fname="Matt"
	g.lname="Bays"
	g.email="valeriebays@gmail.com" 
	g.address="471 Tanoak Drive" 
	g.city="Santa Clara" 
	g.phone="(408) 355-4095" 
	g.zip="95051" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#15 

	selfobj.response.write("Naoko K  Bean  naokobean@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1534117953")) 
	g.year=2018
	g.fname="Naoko K"
	g.lname="Bean"
	g.email="naokobean@yahoo.com" 
	g.address="3440. El Camino. Real  Warburton Village #316" 
	g.city="Santa Clara" 
	g.phone="(408) 888-2290" 
	g.zip="95051" 
	g.ntrp="F" 
	g.mtype="RS" 
	g.put()
#16 

	selfobj.response.write("Linda  Becker  beckerfive@comcast.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1531535720")) 
	g.year=2018
	g.fname="Linda"
	g.lname="Becker"
	g.email="beckerfive@comcast.net" 
	g.address="1890 Woodland Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 244-4864" 
	g.zip="95050" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#17 

	selfobj.response.write("Chris   Becker   Chbcircle@Comcast.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1514992009")) 
	g.year=2018
	g.fname="Chris "
	g.lname="Becker "
	g.email="Chbcircle@Comcast.net" 
	g.address="3032 Cameron Way" 
	g.city="Santa Clara" 
	g.phone="(408) 985-5489" 
	g.zip="95051" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#18 

	selfobj.response.write("Bruce  Becker  beckerfive@comcast.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1531535518")) 
	g.year=2018
	g.fname="Bruce"
	g.lname="Becker"
	g.email="beckerfive@comcast.net" 
	g.address="1890 Woodland Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 244-4864" 
	g.zip="95050" 
	g.ntrp="M4.0" 
	g.mtype="RF" 
	g.put()
#19 

	selfobj.response.write("Jonathan  Bell  c.p.bell@att.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1512436116")) 
	g.year=2018
	g.fname="Jonathan"
	g.lname="Bell"
	g.email="c.p.bell@att.net" 
	g.address="1244 Maryann Drive" 
	g.city="Santa Clara" 
	g.phone="(408) 464-3177" 
	g.zip="95050" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#20 

	selfobj.response.write("Carrie  Bell  c.p.bell@att.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1512435840")) 
	g.year=2018
	g.fname="Carrie"
	g.lname="Bell"
	g.email="c.p.bell@att.net" 
	g.address="1244 Maryann Drive" 
	g.city="Santa Clara" 
	g.phone="(408) 464-3177" 
	g.zip="95050" 
	g.ntrp="F4.0" 
	g.mtype="RF" 
	g.put()
#21 

	selfobj.response.write("Randy  Bell  c.p.bell@att.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1512436011")) 
	g.year=2018
	g.fname="Randy"
	g.lname="Bell"
	g.email="c.p.bell@att.net" 
	g.address="1244 Maryann Drive" 
	g.city="Santa Clara" 
	g.phone="(408) 464-3177" 
	g.zip="95050" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#22 

	selfobj.response.write("Deanne  Benetz  c.p.bell@att.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1525728281")) 
	g.year=2018
	g.fname="Deanne"
	g.lname="Benetz"
	g.email="c.p.bell@att.net" 
	g.address="660 Moreno Lane" 
	g.city="Santa Clara" 
	g.phone="(408) 464-3177" 
	g.zip="95050" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#23 

	selfobj.response.write("Shane  Benetz  c.p.bell@att.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1525728559")) 
	g.year=2018
	g.fname="Shane"
	g.lname="Benetz"
	g.email="c.p.bell@att.net" 
	g.address="660 Moreno Lane" 
	g.city="Santa Clara" 
	g.phone="(408) 464-3177" 
	g.zip="95050" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#24 

	selfobj.response.write("Alexi  Benetz  c.p.bell@att.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1525728372")) 
	g.year=2018
	g.fname="Alexi"
	g.lname="Benetz"
	g.email="c.p.bell@att.net" 
	g.address="660 Moreno Lane" 
	g.city="Santa Clara" 
	g.phone="(408) 464-3177" 
	g.zip="95050" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#25 

	selfobj.response.write("Dan  Benetz  c.p.bell@att.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1525728147")) 
	g.year=2018
	g.fname="Dan"
	g.lname="Benetz"
	g.email="c.p.bell@att.net" 
	g.address="660 Moreno Lane" 
	g.city="Santa Clara" 
	g.phone="(408) 464-3177" 
	g.zip="95050" 
	g.ntrp="M" 
	g.mtype="RF" 
	g.put()
#26 

	selfobj.response.write("Collin  Benetz  c.p.bell@att.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1525728472")) 
	g.year=2018
	g.fname="Collin"
	g.lname="Benetz"
	g.email="c.p.bell@att.net" 
	g.address="660 Moreno Lane" 
	g.city="Santa Clara" 
	g.phone="(408) 464-3177" 
	g.zip="95050" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#27 

	selfobj.response.write("Jason  Bergado  jbergado@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1540746242")) 
	g.year=2018
	g.fname="Jason"
	g.lname="Bergado"
	g.email="jbergado@gmail.com" 
	g.address="1244 Blackfield Dr" 
	g.city="Santa Clara" 
	g.phone="(408) 835-6550" 
	g.zip="95051" 
	g.ntrp="M3.5" 
	g.mtype="RS" 
	g.put()
#28 

	selfobj.response.write("Steven  Boljonis  sboljonis@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1515028969")) 
	g.year=2018
	g.fname="Steven"
	g.lname="Boljonis"
	g.email="sboljonis@gmail.com" 
	g.address="13081 West Sunset Dr" 
	g.city="Los Altos" 
	g.phone="(212) 929-1555" 
	g.zip="94022" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#29 

	selfobj.response.write("Bruce  Bolvary  iiibgiii@aol.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1527801503")) 
	g.year=2018
	g.fname="Bruce"
	g.lname="Bolvary"
	g.email="iiibgiii@aol.com" 
	g.address="2093 Town & Country Lane, #1" 
	g.city="Santa Clara" 
	g.phone="(408) 375-9040" 
	g.zip="95050" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#30 

	selfobj.response.write("Noemi  Bolvary  noemib2737@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1527801220")) 
	g.year=2018
	g.fname="Noemi"
	g.lname="Bolvary"
	g.email="noemib2737@gmail.com" 
	g.address="2093 Town & Country Lane, #1" 
	g.city="Santa Clara" 
	g.phone="(408) 997-3344" 
	g.zip="95050" 
	g.ntrp="F2.5" 
	g.mtype="RF" 
	g.put()
#31 

	selfobj.response.write("KC  Branscomb Kelley  Branscomb@Att.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1521586321")) 
	g.year=2018
	g.fname="KC"
	g.lname="Branscomb Kelley"
	g.email="Branscomb@Att.net" 
	g.address="27 Alverno Ct" 
	g.city="Redwood City" 
	g.phone="(650) 549-8334" 
	g.zip="94061" 
	g.ntrp="F3.0" 
	g.mtype="NRS" 
	g.put()
#32 

	selfobj.response.write("Makayla  Brinquis  brinquis@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1522697117")) 
	g.year=2018
	g.fname="Makayla"
	g.lname="Brinquis"
	g.email="brinquis@gmail.com" 
	g.address="3700 CASA VERDE ST. APT. 3116" 
	g.city="SAN JOSE" 
	g.phone="(505) 604-0709" 
	g.zip="95134" 
	g.ntrp="F" 
	g.mtype="NRF_" 
	g.put()
#33 

	selfobj.response.write("Josephus  Brinquis  brinquis@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1522696589")) 
	g.year=2018
	g.fname="Josephus"
	g.lname="Brinquis"
	g.email="brinquis@gmail.com" 
	g.address="3700 CASA VERDE ST. APT. 3116" 
	g.city="SAN JOSE" 
	g.phone="(505) 604-0709" 
	g.zip="95134" 
	g.ntrp="M" 
	g.mtype="NRF" 
	g.put()
#34 

	selfobj.response.write("Natalie  Brinquis  jwbrinquis@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1522697196")) 
	g.year=2018
	g.fname="Natalie"
	g.lname="Brinquis"
	g.email="jwbrinquis@gmail.com" 
	g.address="3700 CASA VERDE ST. APT. 3116" 
	g.city="SAN JOSE" 
	g.phone="() -" 
	g.zip="95134" 
	g.ntrp="F" 
	g.mtype="NRF_" 
	g.put()
#35 

	selfobj.response.write("Jessica   Brinquis  jwbrinquis@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1522697004")) 
	g.year=2018
	g.fname="Jessica "
	g.lname="Brinquis"
	g.email="jwbrinquis@gmail.com" 
	g.address="3700 CASA VERDE ST. APT. 3116" 
	g.city="SAN JOSE" 
	g.phone="(505) 702-4452" 
	g.zip="95134" 
	g.ntrp="F" 
	g.mtype="NRF_" 
	g.put()
#36 

	selfobj.response.write("Celeste  Brinquis  brinquis@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1522697270")) 
	g.year=2018
	g.fname="Celeste"
	g.lname="Brinquis"
	g.email="brinquis@gmail.com" 
	g.address="3700 CASA VERDE ST. APT. 3116" 
	g.city="SAN JOSE" 
	g.phone="(505) 604-0709" 
	g.zip="95134" 
	g.ntrp="F" 
	g.mtype="NRF_" 
	g.put()
#37 

	selfobj.response.write("Robert  Brunkhorst  bob.brunkhorst@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1514943004")) 
	g.year=2018
	g.fname="Robert"
	g.lname="Brunkhorst"
	g.email="bob.brunkhorst@gmail.com" 
	g.address="849 Humewick Way" 
	g.city="Sunnyvale" 
	g.phone="(408) 667-5902" 
	g.zip="94087" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#38 

	selfobj.response.write("Ike  Bunanta  Ibunanta@Mac.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1521177326")) 
	g.year=2018
	g.fname="Ike"
	g.lname="Bunanta"
	g.email="Ibunanta@Mac.com" 
	g.address="15070 Stratford Ct." 
	g.city="Monte Sereno" 
	g.phone="(408) 406-5830" 
	g.zip="95030" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#39 

	selfobj.response.write("Gary  Buzzell  glbuzzell@aol.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1522125145")) 
	g.year=2018
	g.fname="Gary"
	g.lname="Buzzell"
	g.email="glbuzzell@aol.com" 
	g.address="847 Pagoda Tree Ct" 
	g.city="Sunnyvale" 
	g.phone="(650) 417-1325" 
	g.zip="94086" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#40 

	selfobj.response.write("Volga  Calvello  volgab@Yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1515303640")) 
	g.year=2018
	g.fname="Volga"
	g.lname="Calvello"
	g.email="volgab@Yahoo.com" 
	g.address="1974 Homestead Road" 
	g.city="Santa Clara" 
	g.phone="(650) 303-1151" 
	g.zip="95050" 
	g.ntrp="F3.5" 
	g.mtype="RF" 
	g.put()
#41 

	selfobj.response.write("Thomas  Calvello  volgab@Yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1515304015")) 
	g.year=2018
	g.fname="Thomas"
	g.lname="Calvello"
	g.email="volgab@Yahoo.com" 
	g.address="1974 Homestead Road" 
	g.city="Santa Clara" 
	g.phone="(650) 303-1151" 
	g.zip="95050" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#42 

	selfobj.response.write("Kathy  Camet  kygc333@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1515037535")) 
	g.year=2018
	g.fname="Kathy"
	g.lname="Camet"
	g.email="kygc333@gmail.com" 
	g.address="910 Forest Ridge Drive" 
	g.city="San Jose" 
	g.phone="(408) 368-9456" 
	g.zip="95129" 
	g.ntrp="F" 
	g.mtype="NRS" 
	g.put()
#43 

	selfobj.response.write("Theresa B  Campbell  tbcampbell@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1514851203")) 
	g.year=2018
	g.fname="Theresa B"
	g.lname="Campbell"
	g.email="tbcampbell@sbcglobal.net" 
	g.address="1379 Country Club Drive" 
	g.city="LOS ALTOS" 
	g.phone="(650) 996-0646" 
	g.zip="94024" 
	g.ntrp="F3.0" 
	g.mtype="NRS" 
	g.put()
#44 

	selfobj.response.write("Delia  Cannon   Decannon@Gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1514992089")) 
	g.year=2018
	g.fname="Delia"
	g.lname="Cannon "
	g.email="Decannon@Gmail.com" 
	g.address="3032 Cameron Way" 
	g.city="Santa Clara" 
	g.phone="() -" 
	g.zip="95051" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#45 

	selfobj.response.write("Natalie   Cannon   Natcannon@Gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1514992157")) 
	g.year=2018
	g.fname="Natalie "
	g.lname="Cannon "
	g.email="Natcannon@Gmail.com" 
	g.address="3032 Cameron Way" 
	g.city="Santa Clara" 
	g.phone="() -" 
	g.zip="95051" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#46 

	selfobj.response.write("Kristine  Carber-White  kcarber@aol.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1515026298")) 
	g.year=2018
	g.fname="Kristine"
	g.lname="Carber-White"
	g.email="kcarber@aol.com" 
	g.address="111 Stonewood Drive" 
	g.city="Scotts Valley" 
	g.phone="(650) 575-4286" 
	g.zip="95066" 
	g.ntrp="F3.0" 
	g.mtype="NRF" 
	g.put()
#47 

	selfobj.response.write("Dan  Chen  drdanchen@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1512976339")) 
	g.year=2018
	g.fname="Dan"
	g.lname="Chen"
	g.email="drdanchen@gmail.com" 
	g.address="1135 Laureles Dr" 
	g.city="Los Altos" 
	g.phone="(415) 672-9558" 
	g.zip="94022" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#48 

	selfobj.response.write("Ellen  Chen  turning.leaf@Yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1533802710")) 
	g.year=2018
	g.fname="Ellen"
	g.lname="Chen"
	g.email="turning.leaf@Yahoo.com" 
	g.address="1400 Bowe Ave Apt 204" 
	g.city="Santa Clara" 
	g.phone="(408) 425-8889" 
	g.zip="95051" 
	g.ntrp="F3.5" 
	g.mtype="RF" 
	g.put()
#49 

	selfobj.response.write("Myoung  Chiang  Taeckchiang@Gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1513904751")) 
	g.year=2018
	g.fname="Myoung"
	g.lname="Chiang"
	g.email="Taeckchiang@Gmail.com" 
	g.address="1235 de altura commons" 
	g.city="San jose" 
	g.phone="(408) 306-3657" 
	g.zip="95126" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#50 

	selfobj.response.write("Jeff  Cole  jeff7write@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1534470673")) 
	g.year=2018
	g.fname="Jeff"
	g.lname="Cole"
	g.email="jeff7write@gmail.com" 
	g.address="19361 Greenwood Circle" 
	g.city="Cupertino" 
	g.phone="(408) 568-4556" 
	g.zip="95014" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#51 

	selfobj.response.write("Ramon  Crichlow  ramon@nanoair.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1517967006")) 
	g.year=2018
	g.fname="Ramon"
	g.lname="Crichlow"
	g.email="ramon@nanoair.com" 
	g.address="2900 hearth place S316" 
	g.city="santa clara" 
	g.phone="(650) 237-9871" 
	g.zip="95051" 
	g.ntrp="M4" 
	g.mtype="RS" 
	g.put()
#52 

	selfobj.response.write("Liliane  Cromer  Lilianec@Sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1520637689")) 
	g.year=2018
	g.fname="Liliane"
	g.lname="Cromer"
	g.email="Lilianec@Sbcglobal.net" 
	g.address="14120 Palomino Way" 
	g.city="Saratoga" 
	g.phone="(408) 823-6448" 
	g.zip="95070" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#53 

	selfobj.response.write("Machiko  Cyr  machikoc@pacbell.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1513030284")) 
	g.year=2018
	g.fname="Machiko"
	g.lname="Cyr"
	g.email="machikoc@pacbell.net" 
	g.address="5518 Castle Manor Dr." 
	g.city="San Jose" 
	g.phone="(408) 315-7606" 
	g.zip="95129" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#54 

	selfobj.response.write("Brian  Dang  briandang000@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1512540926")) 
	g.year=2018
	g.fname="Brian"
	g.lname="Dang"
	g.email="briandang000@yahoo.com" 
	g.address="1961 Linden Ln" 
	g.city="Milpitas" 
	g.phone="(408) 712-8450" 
	g.zip="95035" 
	g.ntrp="M3.0" 
	g.mtype="NRS" 
	g.put()
#55 

	selfobj.response.write("Theresa  Dao-Makiyama   Thdaodds@Yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1521497837")) 
	g.year=2018
	g.fname="Theresa"
	g.lname="Dao-Makiyama "
	g.email="Thdaodds@Yahoo.com" 
	g.address="1561 dry creek road" 
	g.city="San Jose" 
	g.phone="(408) 476-7287" 
	g.zip="95125" 
	g.ntrp="F2.5" 
	g.mtype="NRS" 
	g.put()
#56 

	selfobj.response.write("Jessica  De Bosson  jessica4tennis@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1509807188")) 
	g.year=2018
	g.fname="Jessica"
	g.lname="De Bosson"
	g.email="jessica4tennis@gmail.com" 
	g.address="5273 Coco Palm Drive" 
	g.city="Fremont" 
	g.phone="(510) 366-4118" 
	g.zip="94538" 
	g.ntrp="F3.0" 
	g.mtype="NRS" 
	g.put()
#57 

	selfobj.response.write("Onofre  de Souza  onofre2237@aol.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1517263203")) 
	g.year=2018
	g.fname="Onofre"
	g.lname="de Souza"
	g.email="onofre2237@aol.com" 
	g.address="2983 Millar Ave" 
	g.city="Santa Clara,CA." 
	g.phone="(408) 386-4862" 
	g.zip="95051" 
	g.ntrp="M" 
	g.mtype="RS" 
	g.put()
#58 

	selfobj.response.write("Glen  DePalma  glen.depalma@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1532445325")) 
	g.year=2018
	g.fname="Glen"
	g.lname="DePalma"
	g.email="glen.depalma@gmail.com" 
	g.address="1 South Market St 2007" 
	g.city="San Jose" 
	g.phone="(513) 309-5526" 
	g.zip="95113" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#59 

	selfobj.response.write("Ahad  Dil  ahadf5050@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1517968064")) 
	g.year=2018
	g.fname="Ahad"
	g.lname="Dil"
	g.email="ahadf5050@gmail.com" 
	g.address="1700 Ponca Court" 
	g.city="Fremont" 
	g.phone="() -" 
	g.zip="94539" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#60 

	selfobj.response.write("Thac  Doan  thacdoan3060@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1524538202")) 
	g.year=2018
	g.fname="Thac"
	g.lname="Doan"
	g.email="thacdoan3060@gmail.com" 
	g.address="3060 Dibble Court" 
	g.city="Santa Clara" 
	g.phone="() -" 
	g.zip="95051" 
	g.ntrp="M" 
	g.mtype="RS" 
	g.put()
#61 

	selfobj.response.write("Lisa  Doan  thacdoan3060@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1525386234")) 
	g.year=2018
	g.fname="Lisa"
	g.lname="Doan"
	g.email="thacdoan3060@gmail.com" 
	g.address="3060 Dibble Court" 
	g.city="Santa Clara" 
	g.phone="(408) 996-9717" 
	g.zip="95051" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#62 

	selfobj.response.write("Diep  Doan  thacdoan3060@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1525386095")) 
	g.year=2018
	g.fname="Diep"
	g.lname="Doan"
	g.email="thacdoan3060@gmail.com" 
	g.address="3060 Dibble Court" 
	g.city="Santa Clara" 
	g.phone="(408) 996-9717" 
	g.zip="95051" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#63 

	selfobj.response.write("Consuelo  Domingo  conniedomingo@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1518707824")) 
	g.year=2018
	g.fname="Consuelo"
	g.lname="Domingo"
	g.email="conniedomingo@sbcglobal.net" 
	g.address="25627 Franklin Avenue" 
	g.city="Hayward" 
	g.phone="(408) 646-8654" 
	g.zip="94544" 
	g.ntrp="F3.5" 
	g.mtype="" 
	g.put()
#64 

	selfobj.response.write("susanne  edgerton  smedgerton@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1517094111")) 
	g.year=2018
	g.fname="susanne"
	g.lname="edgerton"
	g.email="smedgerton@yahoo.com" 
	g.address="737 henrietta ave" 
	g.city="sunnyvale" 
	g.phone="(408) 739-4561" 
	g.zip="94086" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#65 

	selfobj.response.write("Ron  Eng  175.ron@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1513995891")) 
	g.year=2018
	g.fname="Ron"
	g.lname="Eng"
	g.email="175.ron@gmail.com" 
	g.address="175 Loma Alta Avenue" 
	g.city="Los Gatos" 
	g.phone="(408) 395-0649" 
	g.zip="95030" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#66 

	selfobj.response.write("Marie  Fan  msfan00@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1519002637")) 
	g.year=2018
	g.fname="Marie"
	g.lname="Fan"
	g.email="msfan00@yahoo.com" 
	g.address="1297 Weibel Way" 
	g.city="San Jose" 
	g.phone="(408) 332-6026" 
	g.zip="95125" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#67 

	selfobj.response.write("Kaddie  Feng-Ashley  k417tennis@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1514064028")) 
	g.year=2018
	g.fname="Kaddie"
	g.lname="Feng-Ashley"
	g.email="k417tennis@gmail.com" 
	g.address="PO Box 518" 
	g.city="Morgan Hill" 
	g.phone="(408) 776-2734" 
	g.zip="95038" 
	g.ntrp="F3.0" 
	g.mtype="NRS" 
	g.put()
#68 

	selfobj.response.write("Jackie  Fenton  jdfenton26@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1519240435")) 
	g.year=2018
	g.fname="Jackie"
	g.lname="Fenton"
	g.email="jdfenton26@gmail.com" 
	g.address="970 Corte Madera Ave apt 904" 
	g.city="Sunnyvale" 
	g.phone="(443) 812-4374" 
	g.zip="94085" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#69 

	selfobj.response.write("Ed  Fletcher  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1517156197")) 
	g.year=2018
	g.fname="Ed"
	g.lname="Fletcher"
	g.email="" 
	g.address="869 Hilmar Street" 
	g.city="Santa Clara" 
	g.phone="(650) 492-1925" 
	g.zip="95050" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#70 

	selfobj.response.write("Audrey  Fletcher  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1517156369")) 
	g.year=2018
	g.fname="Audrey"
	g.lname="Fletcher"
	g.email="" 
	g.address="869 Hilmar Street" 
	g.city="Santa Clara" 
	g.phone="(650) 224-9616" 
	g.zip="95050" 
	g.ntrp="F3.0" 
	g.mtype="RF_" 
	g.put()
#71 

	selfobj.response.write("Laura  Fletcher  fletch4him1@mac.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1517156028")) 
	g.year=2018
	g.fname="Laura"
	g.lname="Fletcher"
	g.email="fletch4him1@mac.com" 
	g.address="869 Hilmar Street" 
	g.city="Santa Clara" 
	g.phone="(650) 492-1930" 
	g.zip="95050" 
	g.ntrp="F" 
	g.mtype="RF" 
	g.put()
#72 

	selfobj.response.write("Janelle  Flores  janelle.c.flores@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1521662851")) 
	g.year=2018
	g.fname="Janelle"
	g.lname="Flores"
	g.email="janelle.c.flores@gmail.com" 
	g.address="1537 altamont ave" 
	g.city="san jose" 
	g.phone="(408) 497-9329" 
	g.zip="95125" 
	g.ntrp="F3.5" 
	g.mtype="NRF" 
	g.put()
#73 

	selfobj.response.write("Giana  Flores  flores.giana@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1521663135")) 
	g.year=2018
	g.fname="Giana"
	g.lname="Flores"
	g.email="flores.giana@gmail.com" 
	g.address="1537 altamont ave" 
	g.city="san jose" 
	g.phone="(408) 465-6185" 
	g.zip="95125" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#74 

	selfobj.response.write("Leslie  Francis  lesliefrancis@alum.mit.edu")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1491423064")) 
	g.year=2018
	g.fname="Leslie"
	g.lname="Francis"
	g.email="lesliefrancis@alum.mit.edu" 
	g.address="18910 Bellgrove Circle" 
	g.city="Saratoga" 
	g.phone="(408) 679-8032" 
	g.zip="95070" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#75 

	selfobj.response.write("Ginger  Furuta-Sera  seramg@aol.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1522204276")) 
	g.year=2018
	g.fname="Ginger"
	g.lname="Furuta-Sera"
	g.email="seramg@aol.com" 
	g.address="5833 Capilano Drive" 
	g.city="San Jose" 
	g.phone="(408) 270-6002" 
	g.zip="95138" 
	g.ntrp="F" 
	g.mtype="NRS" 
	g.put()
#76 

	selfobj.response.write("thiruvarun  ganesan  itzmevarun@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1521731568")) 
	g.year=2018
	g.fname="thiruvarun"
	g.lname="ganesan"
	g.email="itzmevarun@gmail.com" 
	g.address="166 monroe st apt 6" 
	g.city="Santa Clara" 
	g.phone="(405) 414-9984" 
	g.zip="95050" 
	g.ntrp="M3.5" 
	g.mtype="RS" 
	g.put()
#77 

	selfobj.response.write("Mar  Garcia Tang-Petersen  margarciaus@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1510688012")) 
	g.year=2018
	g.fname="Mar"
	g.lname="Garcia Tang-Petersen"
	g.email="margarciaus@gmail.com" 
	g.address="56 Paterson Place" 
	g.city="Santa Clara" 
	g.phone="(408) 679-0634" 
	g.zip="95050" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#78 

	selfobj.response.write("Anne  Giannini  Rudyannie@Aol.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1521180074")) 
	g.year=2018
	g.fname="Anne"
	g.lname="Giannini"
	g.email="Rudyannie@Aol.com" 
	g.address="430 Laurel Avenue" 
	g.city="Millbrae" 
	g.phone="(650) 678-8812" 
	g.zip="94030" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#79 

	selfobj.response.write("Sayoko  Gibbs  sayokogibbs@comcast.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1534179336")) 
	g.year=2018
	g.fname="Sayoko"
	g.lname="Gibbs"
	g.email="sayokogibbs@comcast.net" 
	g.address="799 W Homestead Rd" 
	g.city="Sunnyvale" 
	g.phone="(360) 513-9946" 
	g.zip="94087" 
	g.ntrp="F" 
	g.mtype="NRS" 
	g.put()
#80 

	selfobj.response.write("Jeffrey  Gilbert  isa_cristi@hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1520187051")) 
	g.year=2018
	g.fname="Jeffrey"
	g.lname="Gilbert"
	g.email="isa_cristi@hotmail.com" 
	g.address="235 Mount Hamilton Ave" 
	g.city="Los Altos" 
	g.phone="(415) 298-2473" 
	g.zip="94022" 
	g.ntrp="M" 
	g.mtype="NRF_" 
	g.put()
#81 

	selfobj.response.write("Vincent  Gilbert  isa_cristi@hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1520187160")) 
	g.year=2018
	g.fname="Vincent"
	g.lname="Gilbert"
	g.email="isa_cristi@hotmail.com" 
	g.address="235 Mount Hamilton Ave" 
	g.city="Los Altos" 
	g.phone="(415) 298-2473" 
	g.zip="94022" 
	g.ntrp="M" 
	g.mtype="NRF_" 
	g.put()
#82 

	selfobj.response.write("Isabel  Gilbert  isabel_gilbert@fmailbox.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1520186721")) 
	g.year=2018
	g.fname="Isabel"
	g.lname="Gilbert"
	g.email="isabel_gilbert@fmailbox.com" 
	g.address="235 Mount Hamilton Ave" 
	g.city="Los Altos" 
	g.phone="(415) 298-2473" 
	g.zip="94022" 
	g.ntrp="F2.5S" 
	g.mtype="NRF" 
	g.put()
#83 

	selfobj.response.write("Valerie  Gilbert  isa_cristi@hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1520187256")) 
	g.year=2018
	g.fname="Valerie"
	g.lname="Gilbert"
	g.email="isa_cristi@hotmail.com" 
	g.address="235 Mount Hamilton Ave" 
	g.city="Los Altos" 
	g.phone="(415) 298-2473" 
	g.zip="94022" 
	g.ntrp="F" 
	g.mtype="NRF_" 
	g.put()
#84 

	selfobj.response.write("Elizabeth  Gomez  elizabeth@hexabus.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1521647791")) 
	g.year=2018
	g.fname="Elizabeth"
	g.lname="Gomez"
	g.email="elizabeth@hexabus.com" 
	g.address="551 Quartz St." 
	g.city="Redwood City" 
	g.phone="(650) 361-8696" 
	g.zip="94062" 
	g.ntrp="F3.0" 
	g.mtype="NRS" 
	g.put()
#85 

	selfobj.response.write("Elizabeth  Grover  Elizgrover@Me.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1528307176")) 
	g.year=2018
	g.fname="Elizabeth"
	g.lname="Grover"
	g.email="Elizgrover@Me.com" 
	g.address="332 Carriage Deive Apt 3" 
	g.city="Santa Clara" 
	g.phone="(650) 303-4446" 
	g.zip="95050" 
	g.ntrp="F3.0" 
	g.mtype="RS" 
	g.put()
#86 

	selfobj.response.write("Senthil  Gurusamy  senthil.gk25@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1521658650")) 
	g.year=2018
	g.fname="Senthil"
	g.lname="Gurusamy"
	g.email="senthil.gk25@yahoo.com" 
	g.address="3650 BUCKLEY ST," 
	g.city="SANTA CLARA" 
	g.phone="(716) 239-7768" 
	g.zip="95051" 
	g.ntrp="M3.5" 
	g.mtype="RS" 
	g.put()
#87 

	selfobj.response.write("Farlin  Halsey  farlinhalsey@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1525711341")) 
	g.year=2018
	g.fname="Farlin"
	g.lname="Halsey"
	g.email="farlinhalsey@gmail.com" 
	g.address="4506 Carlyle Ct.  Apt 773" 
	g.city="Santa Clara" 
	g.phone="(214) 517-3576" 
	g.zip="95054" 
	g.ntrp="M3.5" 
	g.mtype="RF_" 
	g.put()
#88 

	selfobj.response.write("Alex   Han  alexhan@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1517964332")) 
	g.year=2018
	g.fname="Alex "
	g.lname="Han"
	g.email="alexhan@yahoo.com" 
	g.address="22800 Mercedes Rd." 
	g.city="Cupertino" 
	g.phone="(408) 234-0462" 
	g.zip="95014" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#89 

	selfobj.response.write("Lucille  Harendza  lharendza@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1513186387")) 
	g.year=2018
	g.fname="Lucille"
	g.lname="Harendza"
	g.email="lharendza@yahoo.com" 
	g.address="267 Cahill Park Drive" 
	g.city="San Jose" 
	g.phone="(408) 888-2447" 
	g.zip="95126" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#90 

	selfobj.response.write("Sharon  Haugen  bertnsharon@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1515102487")) 
	g.year=2018
	g.fname="Sharon"
	g.lname="Haugen"
	g.email="bertnsharon@yahoo.com" 
	g.address="1575 Keith Drive" 
	g.city="Campbell" 
	g.phone="(408) 379-9889" 
	g.zip="95008" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#91 

	selfobj.response.write("Julie  Hawkes  hawkes_julie@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1513456525")) 
	g.year=2018
	g.fname="Julie"
	g.lname="Hawkes"
	g.email="hawkes_julie@yahoo.com" 
	g.address="5984 Dry Oak Court" 
	g.city="San Jose" 
	g.phone="(408) 622-4544" 
	g.zip="95120" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#92 

	selfobj.response.write("Patrick  Herbert  patrickherbs@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1522517149")) 
	g.year=2018
	g.fname="Patrick"
	g.lname="Herbert"
	g.email="patrickherbs@gmail.com" 
	g.address="909 Visconti Pl" 
	g.city="Santa Clara" 
	g.phone="(408) 621-2648" 
	g.zip="95050" 
	g.ntrp="M3.0" 
	g.mtype="RS" 
	g.put()
#93 

	selfobj.response.write("Pamela  Hoggatt  pnhoggatt@hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1515214452")) 
	g.year=2018
	g.fname="Pamela"
	g.lname="Hoggatt"
	g.email="pnhoggatt@hotmail.com" 
	g.address="3070 Dibble Court" 
	g.city="Santa Clara" 
	g.phone="(408) 243-4381" 
	g.zip="95051" 
	g.ntrp="F3.0" 
	g.mtype="RF_" 
	g.put()
#94 

	selfobj.response.write("Jeanette  Hoggatt  queenb_95051@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1515213929")) 
	g.year=2018
	g.fname="Jeanette"
	g.lname="Hoggatt"
	g.email="queenb_95051@yahoo.com" 
	g.address="3070 Dibble Court" 
	g.city="Santa Clara" 
	g.phone="(408) 243-4381" 
	g.zip="95051" 
	g.ntrp="F4.0" 
	g.mtype="RF" 
	g.put()
#95 

	selfobj.response.write("Herta  Hoggatt  queenb_95051@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1515214299")) 
	g.year=2018
	g.fname="Herta"
	g.lname="Hoggatt"
	g.email="queenb_95051@yahoo.com" 
	g.address="3070 Dibble Court" 
	g.city="Santa Clara" 
	g.phone="(408) 243-4381" 
	g.zip="95051" 
	g.ntrp="F2.0" 
	g.mtype="RF_" 
	g.put()
#96 

	selfobj.response.write("Norma  Hughes  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1520297757")) 
	g.year=2018
	g.fname="Norma"
	g.lname="Hughes"
	g.email="" 
	g.address="508 Bancroft St" 
	g.city="Santa Clara" 
	g.phone="() -" 
	g.zip="95051" 
	g.ntrp="F3.5" 
	g.mtype="RF" 
	g.put()
#97 

	selfobj.response.write("Akari  Ikeda  aikeda14@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1521441186")) 
	g.year=2018
	g.fname="Akari"
	g.lname="Ikeda"
	g.email="aikeda14@yahoo.com" 
	g.address="3450  El Camino Real STE 1" 
	g.city="Santa Clara" 
	g.phone="(408) 916-7875" 
	g.zip="95051" 
	g.ntrp="F4.5" 
	g.mtype="RS" 
	g.put()
#98 

	selfobj.response.write("Alice  Isaacson  aliceisaacson@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1512595615")) 
	g.year=2018
	g.fname="Alice"
	g.lname="Isaacson"
	g.email="aliceisaacson@yahoo.com" 
	g.address="513 Hickory Place" 
	g.city="Santa Clara" 
	g.phone="(408) 247-0343" 
	g.zip="95051" 
	g.ntrp="F4.0" 
	g.mtype="RF" 
	g.put()
#99 

	selfobj.response.write("Matthew  Isaacson  aliceisaacson@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1519937626")) 
	g.year=2018
	g.fname="Matthew"
	g.lname="Isaacson"
	g.email="aliceisaacson@yahoo.com" 
	g.address="513 Hickory Place" 
	g.city="Santa Clara" 
	g.phone="(408) 247-0343" 
	g.zip="95051" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#100 

	selfobj.response.write("Mark  Isaacson  mji1422@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1512614446")) 
	g.year=2018
	g.fname="Mark"
	g.lname="Isaacson"
	g.email="mji1422@yahoo.com" 
	g.address="513 Hickory Place" 
	g.city="Santa Clara" 
	g.phone="(408) 247-0343" 
	g.zip="95051" 
	g.ntrp="M3.5" 
	g.mtype="RF_" 
	g.put()
#101 

	selfobj.response.write("Nicole  Isaacson  aliceisaacson@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1519937724")) 
	g.year=2018
	g.fname="Nicole"
	g.lname="Isaacson"
	g.email="aliceisaacson@yahoo.com" 
	g.address="513 Hickory Place" 
	g.city="Santa Clara" 
	g.phone="(408) 247-0343" 
	g.zip="95051" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#102 

	selfobj.response.write("Taryn  Ishida  tarynishida@Gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1522461410")) 
	g.year=2018
	g.fname="Taryn"
	g.lname="Ishida"
	g.email="tarynishida@Gmail.com" 
	g.address="496 N 19th St." 
	g.city="San Jose" 
	g.phone="(408) 767-0536" 
	g.zip="95112" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#103 

	selfobj.response.write("LeeAnn  Jarrell  4jarrells@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1515007874")) 
	g.year=2018
	g.fname="LeeAnn"
	g.lname="Jarrell"
	g.email="4jarrells@gmail.com" 
	g.address="1140 Portland Ave" 
	g.city="Los Altos" 
	g.phone="(650) 967-4967" 
	g.zip="94024" 
	g.ntrp="F3.0" 
	g.mtype="NRS" 
	g.put()
#104 

	selfobj.response.write("Cindy  Jeung  cljeung@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1520998907")) 
	g.year=2018
	g.fname="Cindy"
	g.lname="Jeung"
	g.email="cljeung@yahoo.com" 
	g.address="315 Beresford Ave" 
	g.city="Redwood City" 
	g.phone="(650) 365-7532" 
	g.zip="94061" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#105 

	selfobj.response.write("Vicky  Jha  vicky.jha24@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1522124324")) 
	g.year=2018
	g.fname="Vicky"
	g.lname="Jha"
	g.email="vicky.jha24@gmail.com" 
	g.address="1560 Vista Club Circle, Apt 305" 
	g.city="Santa Clara" 
	g.phone="(214) 600-2346" 
	g.zip="95054" 
	g.ntrp="M3.5C" 
	g.mtype="RS" 
	g.put()
#106 

	selfobj.response.write("Adam  Jiang  lzhang83713@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1519936907")) 
	g.year=2018
	g.fname="Adam"
	g.lname="Jiang"
	g.email="lzhang83713@yahoo.com" 
	g.address="460 Norwood Circle" 
	g.city="Santa Clara" 
	g.phone="(208) 283-2835" 
	g.zip="95051" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#107 

	selfobj.response.write("Robert  Jiang  lzhang83713@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1519936992")) 
	g.year=2018
	g.fname="Robert"
	g.lname="Jiang"
	g.email="lzhang83713@yahoo.com" 
	g.address="460 Norwood Circle" 
	g.city="Santa Clara" 
	g.phone="(208) 283-2835" 
	g.zip="95051" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#108 

	selfobj.response.write("Tom   Jiang  lzhang83713@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1519936804")) 
	g.year=2018
	g.fname="Tom "
	g.lname="Jiang"
	g.email="lzhang83713@yahoo.com" 
	g.address="460 Norwood Circle" 
	g.city="Santa Clara" 
	g.phone="(208) 283-2835" 
	g.zip="95051" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#109 

	selfobj.response.write("Soon-Gil  Jung  jungsoongil@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1539819064")) 
	g.year=2018
	g.fname="Soon-Gil"
	g.lname="Jung"
	g.email="jungsoongil@gmail.com" 
	g.address="328 Dawson Drive" 
	g.city="Santa Clara" 
	g.phone="(408) 472-1545" 
	g.zip="95051" 
	g.ntrp="M4.0" 
	g.mtype="RS" 
	g.put()
#110 

	selfobj.response.write("Gina  Kelley  puzzlegurl5@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1515654376")) 
	g.year=2018
	g.fname="Gina"
	g.lname="Kelley"
	g.email="puzzlegurl5@gmail.com" 
	g.address="314 Raymundo Dr" 
	g.city="Woodside" 
	g.phone="(650) 722-0814" 
	g.zip="94062" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#111 

	selfobj.response.write("Jacqueline  Kerkhove  jkerkhove@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1521257141")) 
	g.year=2018
	g.fname="Jacqueline"
	g.lname="Kerkhove"
	g.email="jkerkhove@gmail.com" 
	g.address="755 Santa Paula Ave" 
	g.city="Sunnyvale" 
	g.phone="(408) 499-6233" 
	g.zip="94085" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#112 

	selfobj.response.write("Sophia   Kim  sophiashkim@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1532394205")) 
	g.year=2018
	g.fname="Sophia "
	g.lname="Kim"
	g.email="sophiashkim@yahoo.com" 
	g.address="931 W Latimer Ave" 
	g.city="Campbell" 
	g.phone="(408) 230-3024" 
	g.zip="95008" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#113 

	selfobj.response.write("Jade  Kimura  kimura.jade@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1523051447")) 
	g.year=2018
	g.fname="Jade"
	g.lname="Kimura"
	g.email="kimura.jade@gmail.com" 
	g.address="3364 fowler ave" 
	g.city="santa clara" 
	g.phone="(669) 234-2761" 
	g.zip="95051" 
	g.ntrp="M3.5" 
	g.mtype="RS" 
	g.put()
#114 

	selfobj.response.write("Venkat  Kodavati  vkodavati@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1533834785")) 
	g.year=2018
	g.fname="Venkat"
	g.lname="Kodavati"
	g.email="vkodavati@gmail.com" 
	g.address="4286 Marston Lane" 
	g.city="Santa Clara" 
	g.phone="(408) 718-1347" 
	g.zip="95054" 
	g.ntrp="M" 
	g.mtype="RS" 
	g.put()
#115 

	selfobj.response.write("David  Kohls  kohlsins@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1521674015")) 
	g.year=2018
	g.fname="David"
	g.lname="Kohls"
	g.email="kohlsins@gmail.com" 
	g.address="1045 Live Oak Dr." 
	g.city="Santa Clara, CA" 
	g.phone="(408) 472-2387" 
	g.zip="95051" 
	g.ntrp="M2,5" 
	g.mtype="RF" 
	g.put()
#116 

	selfobj.response.write("Darya  Kolesnikova  kolesnikova.d.v@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1520046799")) 
	g.year=2018
	g.fname="Darya"
	g.lname="Kolesnikova"
	g.email="kolesnikova.d.v@gmail.com" 
	g.address="2884 Rustic Drive" 
	g.city="San Jose" 
	g.phone="(704) 904-0768" 
	g.zip="95124" 
	g.ntrp="F3.0" 
	g.mtype="NRS" 
	g.put()
#117 

	selfobj.response.write("Rose  Koot-Lianides  rosekl@comcast.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1514943484")) 
	g.year=2018
	g.fname="Rose"
	g.lname="Koot-Lianides"
	g.email="rosekl@comcast.net" 
	g.address="220 Wedgewood Ave." 
	g.city="Los Gatos" 
	g.phone="(408) 866-7960" 
	g.zip="95032" 
	g.ntrp="F3.0" 
	g.mtype="NRF" 
	g.put()
#118 

	selfobj.response.write("Malik  Koraitem  jeanneoxford@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1527255470")) 
	g.year=2018
	g.fname="Malik"
	g.lname="Koraitem"
	g.email="jeanneoxford@sbcglobal.net" 
	g.address="3251 Loma Alta Drive" 
	g.city="Santa Clara" 
	g.phone="(408) 985-7901" 
	g.zip="95051" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#119 

	selfobj.response.write("Hana  Koraitem  jeanneoxford@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1513564766")) 
	g.year=2018
	g.fname="Hana"
	g.lname="Koraitem"
	g.email="jeanneoxford@sbcglobal.net" 
	g.address="3251 Loma Alta Drive" 
	g.city="Santa Clara" 
	g.phone="(408) 985-7901" 
	g.zip="95051" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#120 

	selfobj.response.write("Hosoon  Ku  hosoonku@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1515525505")) 
	g.year=2018
	g.fname="Hosoon"
	g.lname="Ku"
	g.email="hosoonku@yahoo.com" 
	g.address="3959 Veritas Way, -" 
	g.city="San Ramon" 
	g.phone="(925) 997-3927" 
	g.zip="94582" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#121 

	selfobj.response.write("Albert  Kuo  albertkuo@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1522107849")) 
	g.year=2018
	g.fname="Albert"
	g.lname="Kuo"
	g.email="albertkuo@yahoo.com" 
	g.address="16300 Azalea Way" 
	g.city="Los Gatos" 
	g.phone="(408) 341-6338" 
	g.zip="95032" 
	g.ntrp="M" 
	g.mtype="NRS" 
	g.put()
#122 

	selfobj.response.write("Jonathan  Kwan  jonnyjack@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1520316531")) 
	g.year=2018
	g.fname="Jonathan"
	g.lname="Kwan"
	g.email="jonnyjack@gmail.com" 
	g.address="1390 Monroe Street apt 8" 
	g.city="Santa Clara" 
	g.phone="(510) 589-0651" 
	g.zip="95050" 
	g.ntrp="M4.0" 
	g.mtype="RF_" 
	g.put()
#123 

	selfobj.response.write("Leticia  Lafosse  letidaboss@aol.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1539585324")) 
	g.year=2018
	g.fname="Leticia"
	g.lname="Lafosse"
	g.email="letidaboss@aol.com" 
	g.address="1034 Cascade Drive" 
	g.city="Sunnyvale" 
	g.phone="(408) 640-2548" 
	g.zip="94087" 
	g.ntrp="F3.0" 
	g.mtype="NRS" 
	g.put()
#124 

	selfobj.response.write("Kimberly  Lancaster  K.LANCASTER12@YAHOO.COM")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1526148204")) 
	g.year=2018
	g.fname="Kimberly"
	g.lname="Lancaster"
	g.email="K.LANCASTER12@YAHOO.COM" 
	g.address="444 Saratoga Ave 05-K" 
	g.city="Santa Clara" 
	g.phone="(678) 725-0727" 
	g.zip="95050" 
	g.ntrp="F4.0" 
	g.mtype="RS" 
	g.put()
#125 

	selfobj.response.write("Pearl  Larue  pearlypoo@me.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1525711144")) 
	g.year=2018
	g.fname="Pearl"
	g.lname="Larue"
	g.email="pearlypoo@me.com" 
	g.address="4506 Carlyle Ct.  Apt 773" 
	g.city="Santa Clara" 
	g.phone="(602) 702-2668" 
	g.zip="95054" 
	g.ntrp="F4.0" 
	g.mtype="RF" 
	g.put()
#126 

	selfobj.response.write("Carley  Lavelle  clavelle24@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1531439600")) 
	g.year=2018
	g.fname="Carley"
	g.lname="Lavelle"
	g.email="clavelle24@yahoo.com" 
	g.address="1491 Bellomy St" 
	g.city="Santa Clara" 
	g.phone="(408) 205-4389" 
	g.zip="95050" 
	g.ntrp="F2.5" 
	g.mtype="RF_" 
	g.put()
#127 

	selfobj.response.write("David  Le  David9le@Gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1532195567")) 
	g.year=2018
	g.fname="David"
	g.lname="Le"
	g.email="David9le@Gmail.com" 
	g.address="1975 Main st" 
	g.city="Santa clara" 
	g.phone="(408) 482-5702" 
	g.zip="95050" 
	g.ntrp="M4..0" 
	g.mtype="RS" 
	g.put()
#128 

	selfobj.response.write("Brook  Lee  bm.lee@verizon.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1515388436")) 
	g.year=2018
	g.fname="Brook"
	g.lname="Lee"
	g.email="bm.lee@verizon.net" 
	g.address="1172 Morse Ave" 
	g.city="Sunnyvale" 
	g.phone="(408) 220-4206" 
	g.zip="94089" 
	g.ntrp="M4.0" 
	g.mtype="NRF" 
	g.put()
#129 

	selfobj.response.write("Brandon  Lee  lee.hang@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1525729884")) 
	g.year=2018
	g.fname="Brandon"
	g.lname="Lee"
	g.email="lee.hang@yahoo.com" 
	g.address="4558 Cheeney street" 
	g.city="Santa Clara" 
	g.phone="(408) 506-2089" 
	g.zip="95043" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#130 

	selfobj.response.write("Jaclyn  Lee  jn.lee295@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1521179416")) 
	g.year=2018
	g.fname="Jaclyn"
	g.lname="Lee"
	g.email="jn.lee295@gmail.com" 
	g.address="1172 Morse Ave" 
	g.city="Sunnyvale" 
	g.phone="(408) 470-9863" 
	g.zip="95054" 
	g.ntrp="F4.5" 
	g.mtype="RJ" 
	g.put()
#131 

	selfobj.response.write("Soungmi  Lee  mysticsm69@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1517992041")) 
	g.year=2018
	g.fname="Soungmi"
	g.lname="Lee"
	g.email="mysticsm69@gmail.com" 
	g.address="450 Harvard Ave. 4B" 
	g.city="Santa Clara" 
	g.phone="(408) 893-1586" 
	g.zip="95051" 
	g.ntrp="F3.5" 
	g.mtype="RF_" 
	g.put()
#132 

	selfobj.response.write("Angela  Lee  leeac05@hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1519419702")) 
	g.year=2018
	g.fname="Angela"
	g.lname="Lee"
	g.email="leeac05@hotmail.com" 
	g.address="635 Catamaran St., Apt #4" 
	g.city="Foster City" 
	g.phone="(847) 226-3865" 
	g.zip="94404" 
	g.ntrp="F2.5" 
	g.mtype="NRS" 
	g.put()
#133 

	selfobj.response.write("hang  lee  lee.hang@Yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1525618398")) 
	g.year=2018
	g.fname="hang"
	g.lname="lee"
	g.email="lee.hang@Yahoo.com" 
	g.address="4558 Cheeney street" 
	g.city="Santa Clara" 
	g.phone="(408) 506-2089" 
	g.zip="95054" 
	g.ntrp="M4" 
	g.mtype="RF" 
	g.put()
#134 

	selfobj.response.write("Unjin  Lee  happierjin@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1531699631")) 
	g.year=2018
	g.fname="Unjin"
	g.lname="Lee"
	g.email="happierjin@gmail.com" 
	g.address="900 pepper tree lane APT 605" 
	g.city="Santa Clara" 
	g.phone="(408) 410-9235" 
	g.zip="95051" 
	g.ntrp="F3.5" 
	g.mtype="RS" 
	g.put()
#135 

	selfobj.response.write("Unjin  Lee  happierjin@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1513900421")) 
	g.year=2018
	g.fname="Unjin"
	g.lname="Lee"
	g.email="happierjin@gmail.com" 
	g.address="1279 Water Lily Way" 
	g.city="San Jose" 
	g.phone="(408) 410-9235" 
	g.zip="95129" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#136 

	selfobj.response.write("Nathan  Lee  lee.hang@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1527023481")) 
	g.year=2018
	g.fname="Nathan"
	g.lname="Lee"
	g.email="lee.hang@gmail.com" 
	g.address="4558 Cheeney street" 
	g.city="Santa Clara" 
	g.phone="() -" 
	g.zip="95053" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#137 

	selfobj.response.write("Tony  Lee  a.lee1111@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1512803907")) 
	g.year=2018
	g.fname="Tony"
	g.lname="Lee"
	g.email="a.lee1111@gmail.com" 
	g.address="2271 Grant Road" 
	g.city="LOS ALTOS" 
	g.phone="(650) 279-6388" 
	g.zip="94024" 
	g.ntrp="M3.0" 
	g.mtype="NRS" 
	g.put()
#138 

	selfobj.response.write("Ken  Leong  kenleong0@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1514817829")) 
	g.year=2018
	g.fname="Ken"
	g.lname="Leong"
	g.email="kenleong0@gmail.com" 
	g.address="8017 Pinot Noir Ct" 
	g.city="San Jose" 
	g.phone="(540) 686-1124" 
	g.zip="95135" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#139 

	selfobj.response.write("Mark  Lianides  mark@mcl-cpa.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1514943801")) 
	g.year=2018
	g.fname="Mark"
	g.lname="Lianides"
	g.email="mark@mcl-cpa.com" 
	g.address="220 Wedgewood Ave." 
	g.city="Los Gatos" 
	g.phone="(408) 866-7960" 
	g.zip="95032" 
	g.ntrp="M4.0" 
	g.mtype="NRF_" 
	g.put()
#140 

	selfobj.response.write("Vladimir  Libershteyn  vladimir.libershteyn@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1515204130")) 
	g.year=2018
	g.fname="Vladimir"
	g.lname="Libershteyn"
	g.email="vladimir.libershteyn@gmail.com" 
	g.address="5813 Vargas Ct." 
	g.city="SAN JOSE" 
	g.phone="(408) 892-5937" 
	g.zip="95120" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#141 

	selfobj.response.write("Jane  Liddle  janieliddle@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1521473295")) 
	g.year=2018
	g.fname="Jane"
	g.lname="Liddle"
	g.email="janieliddle@gmail.com" 
	g.address="13525 Indian Trail Road" 
	g.city="Los Gatos" 
	g.phone="(408) 828-5232" 
	g.zip="95033" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#142 

	selfobj.response.write("Owen  Lin  owen.lin@sjsu.edu")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1535909193")) 
	g.year=2018
	g.fname="Owen"
	g.lname="Lin"
	g.email="owen.lin@sjsu.edu" 
	g.address="1484 POLLARD RD # 145" 
	g.city="LOS GATOS" 
	g.phone="(408) 921-2694" 
	g.zip="95032" 
	g.ntrp="M3.0" 
	g.mtype="NRS" 
	g.put()
#143 

	selfobj.response.write("Al  Linke  alinke2000@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1518380808")) 
	g.year=2018
	g.fname="Al"
	g.lname="Linke"
	g.email="alinke2000@gmail.com" 
	g.address="1285 Main Street" 
	g.city="Santa Clara" 
	g.phone="(408) 892-1718" 
	g.zip="95050" 
	g.ntrp="M4" 
	g.mtype="RS" 
	g.put()
#144 

	selfobj.response.write("Weiwan  Liu  liudavis@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1518502127")) 
	g.year=2018
	g.fname="Weiwan"
	g.lname="Liu"
	g.email="liudavis@yahoo.com" 
	g.address="59 Cabot Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 598-0292" 
	g.zip="95051" 
	g.ntrp="M" 
	g.mtype="RS" 
	g.put()
#145 

	selfobj.response.write("Linda  Liu  weiwan.liu@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1525729595")) 
	g.year=2018
	g.fname="Linda"
	g.lname="Liu"
	g.email="weiwan.liu@gmail.com" 
	g.address="59 Cabot Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 598-0292" 
	g.zip="95051" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#146 

	selfobj.response.write("Aina   Lu  aina_lu@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1520583597")) 
	g.year=2018
	g.fname="Aina "
	g.lname="Lu"
	g.email="aina_lu@yahoo.com" 
	g.address="233 Coy Dr" 
	g.city="San Jose" 
	g.phone="(408) 515-0469" 
	g.zip="95123" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#147 

	selfobj.response.write("Joni  Mahoney  jonimahoney@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1520316202")) 
	g.year=2018
	g.fname="Joni"
	g.lname="Mahoney"
	g.email="jonimahoney@gmail.com" 
	g.address="576 Kiholo Terrace" 
	g.city="Sunnyvale" 
	g.phone="(408) 393-4070" 
	g.zip="94089" 
	g.ntrp="F3.0" 
	g.mtype="NRS" 
	g.put()
#148 

	selfobj.response.write("Ashok  Mangalore  ashmangalore@hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1508629427")) 
	g.year=2018
	g.fname="Ashok"
	g.lname="Mangalore"
	g.email="ashmangalore@hotmail.com" 
	g.address="36900 Papaya Street" 
	g.city="Newark" 
	g.phone="(510) 676-8975" 
	g.zip="94560" 
	g.ntrp="M3.0" 
	g.mtype="NRS" 
	g.put()
#149 

	selfobj.response.write("Bill  Mannina  bill.williamtennis@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1510623037")) 
	g.year=2018
	g.fname="Bill"
	g.lname="Mannina"
	g.email="bill.williamtennis@yahoo.com" 
	g.address="177 Monroe Street #7" 
	g.city="Santa Clara" 
	g.phone="() -" 
	g.zip="95050" 
	g.ntrp="M4.0" 
	g.mtype="RF_" 
	g.put()
#150 

	selfobj.response.write("Ashley  Mannina  curbsidechoir@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1528675425")) 
	g.year=2018
	g.fname="Ashley"
	g.lname="Mannina"
	g.email="curbsidechoir@gmail.com" 
	g.address="177 monroe street #7" 
	g.city="santa clara" 
	g.phone="(408) 910-6003" 
	g.zip="95050" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#151 

	selfobj.response.write("kathleenn  mannina  kathleen.mannina@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1534470310")) 
	g.year=2018
	g.fname="kathleenn"
	g.lname="mannina"
	g.email="kathleen.mannina@yahoo.com" 
	g.address="177 monroe street #7" 
	g.city="Santa Clara" 
	g.phone="(408) 910-6003" 
	g.zip="95050" 
	g.ntrp="F2.5" 
	g.mtype="RF_" 
	g.put()
#152 

	selfobj.response.write("Amy  Mao  amymao9898@Yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1521662870")) 
	g.year=2018
	g.fname="Amy"
	g.lname="Mao"
	g.email="amymao9898@Yahoo.com" 
	g.address="22393 McClellan rd" 
	g.city="Cupertino" 
	g.phone="(408) 483-9452" 
	g.zip="95014" 
	g.ntrp="F" 
	g.mtype="NRS" 
	g.put()
#153 

	selfobj.response.write("Di  Mao  weiwan.liu@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1525729697")) 
	g.year=2018
	g.fname="Di"
	g.lname="Mao"
	g.email="weiwan.liu@gmail.com" 
	g.address="59 Cabot Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 598-0292" 
	g.zip="95051" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#154 

	selfobj.response.write("Sue  Markuson  smarkuson@comcast.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1515025420")) 
	g.year=2018
	g.fname="Sue"
	g.lname="Markuson"
	g.email="smarkuson@comcast.net" 
	g.address="10280 Stonydale Drive" 
	g.city="Cupertino" 
	g.phone="(408) 749-8355" 
	g.zip="95014" 
	g.ntrp="F3.0" 
	g.mtype="NRS" 
	g.put()
#155 

	selfobj.response.write("Rajiban  Marshal steevan  tamilboys003@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1535731310")) 
	g.year=2018
	g.fname="Rajiban"
	g.lname="Marshal steevan"
	g.email="tamilboys003@gmail.com" 
	g.address="1350 Warburton ave apt 6" 
	g.city="Santa Clara" 
	g.phone="(408) 903-7426" 
	g.zip="95050" 
	g.ntrp="M" 
	g.mtype="RS" 
	g.put()
#156 

	selfobj.response.write("Elizabeth  Martinez  Liz.martinez@Lmco.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1517270656")) 
	g.year=2018
	g.fname="Elizabeth"
	g.lname="Martinez"
	g.email="Liz.martinez@Lmco.com" 
	g.address="2123 Warburton Avenue" 
	g.city="Santa clara" 
	g.phone="(408) 393-61" 
	g.zip="95050" 
	g.ntrp="F3.5" 
	g.mtype="RS" 
	g.put()
#157 

	selfobj.response.write("Barbara  Massa  massa819@hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1521656602")) 
	g.year=2018
	g.fname="Barbara"
	g.lname="Massa"
	g.email="massa819@hotmail.com" 
	g.address="108 Paseo Laura" 
	g.city="Los Gatos" 
	g.phone="(408) 981-4202" 
	g.zip="95032" 
	g.ntrp="F3.0" 
	g.mtype="NRS" 
	g.put()
#158 

	selfobj.response.write("Helen  Matsumoto  geetennis@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1513037340")) 
	g.year=2018
	g.fname="Helen"
	g.lname="Matsumoto"
	g.email="geetennis@yahoo.com" 
	g.address="1247 Redoaks Drive" 
	g.city="San Jose" 
	g.phone="(408) 248-7922" 
	g.zip="95128" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#159 

	selfobj.response.write("Pam  Mayerfeld  pam.mayerfeld@stanfordalumni.org")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1535689898")) 
	g.year=2018
	g.fname="Pam"
	g.lname="Mayerfeld"
	g.email="pam.mayerfeld@stanfordalumni.org" 
	g.address="890 East Meadow Drive" 
	g.city="Palo Alto" 
	g.phone="(408) 887-2475" 
	g.zip="94303" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#160 

	selfobj.response.write("Valerie  McCarthy  valeriebays@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1513044174")) 
	g.year=2018
	g.fname="Valerie"
	g.lname="McCarthy"
	g.email="valeriebays@gmail.com" 
	g.address="471 Tanoak Drive" 
	g.city="Santa Clara" 
	g.phone="(408) 355-4095" 
	g.zip="95051" 
	g.ntrp="F3.0" 
	g.mtype="RF" 
	g.put()
#161 

	selfobj.response.write("Elaine  McGinnis  elainemcginnis@hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1535690442")) 
	g.year=2018
	g.fname="Elaine"
	g.lname="McGinnis"
	g.email="elainemcginnis@hotmail.com" 
	g.address="14250 Douglass Lane" 
	g.city="Saratoga" 
	g.phone="(408) 888-9845" 
	g.zip="95070" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#162 

	selfobj.response.write("Trevor  McGuire  temcguir@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1520618303")) 
	g.year=2018
	g.fname="Trevor"
	g.lname="McGuire"
	g.email="temcguir@gmail.com" 
	g.address="3419 Flora Vista Avenue" 
	g.city="Santa Clara" 
	g.phone="(707) 799-0577" 
	g.zip="95051" 
	g.ntrp="M3.5" 
	g.mtype="RF" 
	g.put()
#163 

	selfobj.response.write("Claudia  McGuire  temcguir@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1520618382")) 
	g.year=2018
	g.fname="Claudia"
	g.lname="McGuire"
	g.email="temcguir@gmail.com" 
	g.address="3419 Flora Vista Avenue" 
	g.city="Santa Clara" 
	g.phone="(707) 799-0577" 
	g.zip="95051" 
	g.ntrp="F2.5" 
	g.mtype="RF_" 
	g.put()
#164 

	selfobj.response.write("Patrick  Mealey  patrickmealey@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1535603867")) 
	g.year=2018
	g.fname="Patrick"
	g.lname="Mealey"
	g.email="patrickmealey@yahoo.com" 
	g.address="1004 Windermere Ave" 
	g.city="Menlo Park" 
	g.phone="(509) 879-1187" 
	g.zip="94025" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#165 

	selfobj.response.write("Nathan Michael  Mertz  mertznathanmichael@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1520053869")) 
	g.year=2018
	g.fname="Nathan Michael"
	g.lname="Mertz"
	g.email="mertznathanmichael@gmail.com" 
	g.address="2071 Bowers Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 469-0521" 
	g.zip="95051" 
	g.ntrp="M3.5" 
	g.mtype="RF" 
	g.put()
#166 

	selfobj.response.write("Zachary  Mertz  mertznathanmichael@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1520054111")) 
	g.year=2018
	g.fname="Zachary"
	g.lname="Mertz"
	g.email="mertznathanmichael@gmail.com" 
	g.address="2071 Bowers Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 469-0521" 
	g.zip="95051" 
	g.ntrp="M2.0" 
	g.mtype="RF_" 
	g.put()
#167 

	selfobj.response.write("Caroline   Mertz  mertznathanmichael@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1520054293")) 
	g.year=2018
	g.fname="Caroline "
	g.lname="Mertz"
	g.email="mertznathanmichael@gmail.com" 
	g.address="2071 Bowers Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 469-0521" 
	g.zip="95051" 
	g.ntrp="F2.0" 
	g.mtype="RF_" 
	g.put()
#168 

	selfobj.response.write("Nathan W  Mertz  mertznathanmichael@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1520053964")) 
	g.year=2018
	g.fname="Nathan W"
	g.lname="Mertz"
	g.email="mertznathanmichael@gmail.com" 
	g.address="2071 Bowers Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 469-0521" 
	g.zip="95051" 
	g.ntrp="M2.5" 
	g.mtype="RF_" 
	g.put()
#169 

	selfobj.response.write("Megan  Mertz  mertznathanmichael@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1520054149")) 
	g.year=2018
	g.fname="Megan"
	g.lname="Mertz"
	g.email="mertznathanmichael@gmail.com" 
	g.address="2071 Bowers Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 469-0521" 
	g.zip="95051" 
	g.ntrp="F2.0" 
	g.mtype="RF_" 
	g.put()
#170 

	selfobj.response.write("Aurora  Mertz  mertznathanmichael@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1520054362")) 
	g.year=2018
	g.fname="Aurora"
	g.lname="Mertz"
	g.email="mertznathanmichael@gmail.com" 
	g.address="2071 Bowers Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 469-0521" 
	g.zip="95051" 
	g.ntrp="F2.0" 
	g.mtype="RF_" 
	g.put()
#171 

	selfobj.response.write("Karen  Mertz  mertznathanmichael@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1520054014")) 
	g.year=2018
	g.fname="Karen"
	g.lname="Mertz"
	g.email="mertznathanmichael@gmail.com" 
	g.address="2071 Bowers Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 469-0521" 
	g.zip="95051" 
	g.ntrp="F2.0" 
	g.mtype="RF_" 
	g.put()
#172 

	selfobj.response.write("Trevor  Mertz  mertznathanmichael@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1520054227")) 
	g.year=2018
	g.fname="Trevor"
	g.lname="Mertz"
	g.email="mertznathanmichael@gmail.com" 
	g.address="2071 Bowers Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 469-0521" 
	g.zip="95051" 
	g.ntrp="M2.0" 
	g.mtype="RF_" 
	g.put()
#173 

	selfobj.response.write("Breanna  Mertz  mertznathanmichael@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1520054485")) 
	g.year=2018
	g.fname="Breanna"
	g.lname="Mertz"
	g.email="mertznathanmichael@gmail.com" 
	g.address="2071 Bowers Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 469-0521" 
	g.zip="95051" 
	g.ntrp="F2.0" 
	g.mtype="RF_" 
	g.put()
#174 

	selfobj.response.write("Sandra   Miller  Snadra39@Yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1514526662")) 
	g.year=2018
	g.fname="Sandra "
	g.lname="Miller"
	g.email="Snadra39@Yahoo.com" 
	g.address="10390 Malvern Ct" 
	g.city="Cupertino" 
	g.phone="(408) 892-6617" 
	g.zip="95014" 
	g.ntrp="F" 
	g.mtype="NRS" 
	g.put()
#175 

	selfobj.response.write("Shari  Miura  Smiura@Comcast.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1522205751")) 
	g.year=2018
	g.fname="Shari"
	g.lname="Miura"
	g.email="Smiura@Comcast.net" 
	g.address="1691 lederer circle" 
	g.city="San jose" 
	g.phone="(408) 966-0117" 
	g.zip="95131" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#176 

	selfobj.response.write("Roy  Molseed  meisee68@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1515211534")) 
	g.year=2018
	g.fname="Roy"
	g.lname="Molseed"
	g.email="meisee68@yahoo.com" 
	g.address="238 N Cypress Avenue" 
	g.city="Santa Clara" 
	g.phone="(408) 580-6396" 
	g.zip="95050" 
	g.ntrp="M4.0" 
	g.mtype="RF_" 
	g.put()
#177 

	selfobj.response.write("Jennifer  Mooney  jennifer45678@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1527293504")) 
	g.year=2018
	g.fname="Jennifer"
	g.lname="Mooney"
	g.email="jennifer45678@gmail.com" 
	g.address="1652 Cabrillo Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 234-6040" 
	g.zip="95050" 
	g.ntrp="F3.0" 
	g.mtype="RF" 
	g.put()
#178 

	selfobj.response.write("Gayle  Moore  tennissenior@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1520297609")) 
	g.year=2018
	g.fname="Gayle"
	g.lname="Moore"
	g.email="tennissenior@yahoo.com" 
	g.address="3115 Maurica Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 246-5129" 
	g.zip="95051" 
	g.ntrp="F3.5" 
	g.mtype="RF" 
	g.put()
#179 

	selfobj.response.write("Francisca   Mortensen   Back40@Creative-services.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1517615744")) 
	g.year=2018
	g.fname="Francisca "
	g.lname="Mortensen "
	g.email="Back40@Creative-services.com" 
	g.address="3584 Irlanda Way" 
	g.city="San Jose" 
	g.phone="(408) 410-7836" 
	g.zip="95124" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#180 

	selfobj.response.write("Lynne  Mosier  lynne@mosier.name")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1515047682")) 
	g.year=2018
	g.fname="Lynne"
	g.lname="Mosier"
	g.email="lynne@mosier.name" 
	g.address="3980 El Cerrito Rd" 
	g.city="PALO ALTO" 
	g.phone="(650) 400-7769" 
	g.zip="94306" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#181 

	selfobj.response.write("Miyuki  Motegi Tibbetts  minneymouse71@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1535689718")) 
	g.year=2018
	g.fname="Miyuki"
	g.lname="Motegi Tibbetts"
	g.email="minneymouse71@gmail.com" 
	g.address="3452 Bonita Ave" 
	g.city="Santa Clara" 
	g.phone="(248) 790-0736" 
	g.zip="95051" 
	g.ntrp="F4.0" 
	g.mtype="RF" 
	g.put()
#182 

	selfobj.response.write("Pradeep  Nair  pradeepn1@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1515504420")) 
	g.year=2018
	g.fname="Pradeep"
	g.lname="Nair"
	g.email="pradeepn1@gmail.com" 
	g.address="1921 Garzoni Place" 
	g.city="Santa Clara" 
	g.phone="(408) 839-1703" 
	g.zip="95054" 
	g.ntrp="M4.0" 
	g.mtype="RS" 
	g.put()
#183 

	selfobj.response.write("Biju  Nair  prinzbiju@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1538500215")) 
	g.year=2018
	g.fname="Biju"
	g.lname="Nair"
	g.email="prinzbiju@gmail.com" 
	g.address="3385 Forest ave" 
	g.city="santa clara" 
	g.phone="(408) 627-9677" 
	g.zip="95050" 
	g.ntrp="M3.5" 
	g.mtype="RS" 
	g.put()
#184 

	selfobj.response.write("Vishnu  Nandakumar  nvishnuvardhan@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1521781677")) 
	g.year=2018
	g.fname="Vishnu"
	g.lname="Nandakumar"
	g.email="nvishnuvardhan@gmail.com" 
	g.address="3307 Benton Street" 
	g.city="Santa Clara" 
	g.phone="(814) 308-3611" 
	g.zip="95051" 
	g.ntrp="M3.5" 
	g.mtype="RS" 
	g.put()
#185 

	selfobj.response.write("Shiv  Natarajan  shiv.natarajan@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1521151359")) 
	g.year=2018
	g.fname="Shiv"
	g.lname="Natarajan"
	g.email="shiv.natarajan@yahoo.com" 
	g.address="4813 VERBENA WAY" 
	g.city="SAN JOSE" 
	g.phone="(408) 480-1044" 
	g.zip="95129" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#186 

	selfobj.response.write("Kim  Nemeth  knemeth@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1515447720")) 
	g.year=2018
	g.fname="Kim"
	g.lname="Nemeth"
	g.email="knemeth@sbcglobal.net" 
	g.address="1610 Sweetbriar Drive" 
	g.city="San Jose" 
	g.phone="(408) 396-0608" 
	g.zip="91525" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#187 

	selfobj.response.write("Lai  Ngo  lloydngo@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1525386367")) 
	g.year=2018
	g.fname="Lai"
	g.lname="Ngo"
	g.email="lloydngo@yahoo.com" 
	g.address="3399 Victoria Ave." 
	g.city="Santa Clara" 
	g.phone="(408) 891-1154" 
	g.zip="95132" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#188 

	selfobj.response.write("Lloyd  Ngo  lloydngo@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1524537974")) 
	g.year=2018
	g.fname="Lloyd"
	g.lname="Ngo"
	g.email="lloydngo@yahoo.com" 
	g.address="3399 Victoria Ave." 
	g.city="Santa Clara" 
	g.phone="(408) 891-1154" 
	g.zip="95117" 
	g.ntrp="M" 
	g.mtype="RS" 
	g.put()
#189 

	selfobj.response.write("Paul  Nguyen  paulinium@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1520375804")) 
	g.year=2018
	g.fname="Paul"
	g.lname="Nguyen"
	g.email="paulinium@gmail.com" 
	g.address="17246 James Lex Lane" 
	g.city="Morgan Hill" 
	g.phone="(916) 202-6892" 
	g.zip="95037" 
	g.ntrp="M4.0" 
	g.mtype="NRF" 
	g.put()
#190 

	selfobj.response.write("Thi  Nguyen  Baothiy2k@Yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1519831058")) 
	g.year=2018
	g.fname="Thi"
	g.lname="Nguyen"
	g.email="Baothiy2k@Yahoo.com" 
	g.address="1925 white oaks road" 
	g.city="Campbell" 
	g.phone="(408) 497-8889" 
	g.zip="95008" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#191 

	selfobj.response.write("John  Nguyen  john@jasondragon.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1520376032")) 
	g.year=2018
	g.fname="John"
	g.lname="Nguyen"
	g.email="john@jasondragon.net" 
	g.address="17246 James Lex Lane" 
	g.city="Morgan Hill" 
	g.phone="(408) 427-2013" 
	g.zip="95037" 
	g.ntrp="M4.0" 
	g.mtype="NRF_" 
	g.put()
#192 

	selfobj.response.write("alan  nguyen  xamlech@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1514871386")) 
	g.year=2018
	g.fname="alan"
	g.lname="nguyen"
	g.email="xamlech@gmail.com" 
	g.address="4147 park blvd" 
	g.city="palo alto" 
	g.phone="(650) 793-1425" 
	g.zip="94306" 
	g.ntrp="M3.0" 
	g.mtype="NRS" 
	g.put()
#193 

	selfobj.response.write("Tina  Nguyen  tinanguyen_63@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1521736121")) 
	g.year=2018
	g.fname="Tina"
	g.lname="Nguyen"
	g.email="tinanguyen_63@yahoo.com" 
	g.address="1500 Peterson Ave., Apt. 38" 
	g.city="San Jose" 
	g.phone="(408) 813-9485" 
	g.zip="95129" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#194 

	selfobj.response.write("Nancy  Nii  da4niis@Yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1515628178")) 
	g.year=2018
	g.fname="Nancy"
	g.lname="Nii"
	g.email="da4niis@Yahoo.com" 
	g.address="1838 Montemar Way" 
	g.city="San Jose" 
	g.phone="(408) 559-0747" 
	g.zip="95125" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#195 

	selfobj.response.write("Carlos  Nino de Guzman  cng94087@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1539323821")) 
	g.year=2018
	g.fname="Carlos"
	g.lname="Nino de Guzman"
	g.email="cng94087@yahoo.com" 
	g.address="1085 Tasman Dr. SPC 431" 
	g.city="Sunnyvale" 
	g.phone="(510) 300-4863" 
	g.zip="94089" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#196 

	selfobj.response.write("Joseph  Nuniz  josephnuniz@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1521911146")) 
	g.year=2018
	g.fname="Joseph"
	g.lname="Nuniz"
	g.email="josephnuniz@yahoo.com" 
	g.address="1416 San Martino Court" 
	g.city="San Jose" 
	g.phone="(214) 808-1633" 
	g.zip="95126" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#197 

	selfobj.response.write("Yuri  Oda  Yurijudy123@Yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1512578174")) 
	g.year=2018
	g.fname="Yuri"
	g.lname="Oda"
	g.email="Yurijudy123@Yahoo.com" 
	g.address="17265 Grosvenor Court" 
	g.city="Monte Sereno" 
	g.phone="(408) 307-7815" 
	g.zip="95030" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#198 

	selfobj.response.write("Junko  Ohoka  junko.ohoka@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1521696101")) 
	g.year=2018
	g.fname="Junko"
	g.lname="Ohoka"
	g.email="junko.ohoka@gmail.com" 
	g.address="992 Foxworthy Ave., D" 
	g.city="San Jose" 
	g.phone="(408) 582-4035" 
	g.zip="95125" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#199 

	selfobj.response.write("Roger  Okamoto  tennis.mutt@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1520145680")) 
	g.year=2018
	g.fname="Roger"
	g.lname="Okamoto"
	g.email="tennis.mutt@gmail.com" 
	g.address="PO Box 605" 
	g.city="Mountain View" 
	g.phone="(408) 800-7646" 
	g.zip="94040" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#200 

	selfobj.response.write("Ken  Okazaki  okaken1@aol.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1514608874")) 
	g.year=2018
	g.fname="Ken"
	g.lname="Okazaki"
	g.email="okaken1@aol.com" 
	g.address="814 Daffodil Way" 
	g.city="San Jose" 
	g.phone="(408) 387-0460" 
	g.zip="95117" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#201 

	selfobj.response.write("Rachel  Okazaki  japanesegrace@Gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1520226241")) 
	g.year=2018
	g.fname="Rachel"
	g.lname="Okazaki"
	g.email="japanesegrace@Gmail.com" 
	g.address="1390 Monroe Street apt 8" 
	g.city="Santa Clara" 
	g.phone="() -" 
	g.zip="95050" 
	g.ntrp="F4.0" 
	g.mtype="RF" 
	g.put()
#202 

	selfobj.response.write("Chester  Okuno  chesterokuno@Gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1513138585")) 
	g.year=2018
	g.fname="Chester"
	g.lname="Okuno"
	g.email="chesterokuno@Gmail.com" 
	g.address="1497 Miramonte Avenue" 
	g.city="Los Altos" 
	g.phone="(408) 489-3142" 
	g.zip="94024" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#203 

	selfobj.response.write("Corey  Oravetz  corey@oravetz.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1540869038")) 
	g.year=2018
	g.fname="Corey"
	g.lname="Oravetz"
	g.email="corey@oravetz.com" 
	g.address="812 Fountain Park Ln" 
	g.city="Mountain View" 
	g.phone="() -" 
	g.zip="94043" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#204 

	selfobj.response.write("Noriko  Osawa  noriko_osawa@hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1521104837")) 
	g.year=2018
	g.fname="Noriko"
	g.lname="Osawa"
	g.email="noriko_osawa@hotmail.com" 
	g.address="157 Kensington Way" 
	g.city="Los Gatos" 
	g.phone="(408) 401-9977" 
	g.zip="95032" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#205 

	selfobj.response.write("Jeanne  Oxford  jeanneoxford@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1513564528")) 
	g.year=2018
	g.fname="Jeanne"
	g.lname="Oxford"
	g.email="jeanneoxford@sbcglobal.net" 
	g.address="3251 Loma Alta Drive" 
	g.city="Santa Clara" 
	g.phone="(408) 985-7901" 
	g.zip="95051" 
	g.ntrp="F3.0" 
	g.mtype="RF" 
	g.put()
#206 

	selfobj.response.write("Ace  Oxford  jeanneoxford@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1513564656")) 
	g.year=2018
	g.fname="Ace"
	g.lname="Oxford"
	g.email="jeanneoxford@sbcglobal.net" 
	g.address="3251 Loma Alta Drive" 
	g.city="Santa Clara" 
	g.phone="(408) 985-7901" 
	g.zip="95051" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#207 

	selfobj.response.write("Karen  Panian  Kpanian@Comcast.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1535474625")) 
	g.year=2018
	g.fname="Karen"
	g.lname="Panian"
	g.email="Kpanian@Comcast.net" 
	g.address="1704 Harrison St." 
	g.city="Santa Clara" 
	g.phone="(408) 314-8883" 
	g.zip="95050" 
	g.ntrp="F3.5" 
	g.mtype="RS" 
	g.put()
#208 

	selfobj.response.write("Insoo  Park  insoop@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1520564864")) 
	g.year=2018
	g.fname="Insoo"
	g.lname="Park"
	g.email="insoop@gmail.com" 
	g.address="1112 Pomeroy Ave" 
	g.city="Santa Clara" 
	g.phone="(510) 304-5531" 
	g.zip="95051" 
	g.ntrp="M3.5" 
	g.mtype="RS" 
	g.put()
#209 

	selfobj.response.write("Christine  Peters  ck.peters@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1515175214")) 
	g.year=2018
	g.fname="Christine"
	g.lname="Peters"
	g.email="ck.peters@sbcglobal.net" 
	g.address="4749 Castana Drive" 
	g.city="Cameron Park" 
	g.phone="(408) 921-1610" 
	g.zip="95682" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#210 

	selfobj.response.write("Elisapeta  Peterson  peta.peterson@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1515446772")) 
	g.year=2018
	g.fname="Elisapeta"
	g.lname="Peterson"
	g.email="peta.peterson@sbcglobal.net" 
	g.address="13970 Saratoga Avenue" 
	g.city="Saratoga" 
	g.phone="(408) 867-6947" 
	g.zip="95057" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#211 

	selfobj.response.write("Bettye   Pham-Vo  bettyediem@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1514927341")) 
	g.year=2018
	g.fname="Bettye "
	g.lname="Pham-Vo"
	g.email="bettyediem@gmail.com" 
	g.address="3657 Lisbon Ct." 
	g.city="San Jose" 
	g.phone="(408) 250-5658" 
	g.zip="95132" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#212 

	selfobj.response.write("Haran  Pradeep Chidambaram  haranpc1010@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1521825001")) 
	g.year=2018
	g.fname="Haran"
	g.lname="Pradeep Chidambaram"
	g.email="haranpc1010@gmail.com" 
	g.address="112 Florence Street, Apt 4" 
	g.city="Sunnyvale" 
	g.phone="(512) 810-9787" 
	g.zip="94086" 
	g.ntrp="M3.0" 
	g.mtype="NRS" 
	g.put()
#213 

	selfobj.response.write("Jodi  Pruett  jodipruett@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1515001009")) 
	g.year=2018
	g.fname="Jodi"
	g.lname="Pruett"
	g.email="jodipruett@sbcglobal.net" 
	g.address="4877 Blue Ridge Dr" 
	g.city="San Jose" 
	g.phone="(408) 806-4798" 
	g.zip="95129" 
	g.ntrp="F3.0" 
	g.mtype="NRF" 
	g.put()
#214 

	selfobj.response.write("Tom  Pudpai  tompudpai@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1522857468")) 
	g.year=2018
	g.fname="Tom"
	g.lname="Pudpai"
	g.email="tompudpai@gmail.com" 
	g.address="420 Dempsey Rd, Unit 220" 
	g.city="Milpitas" 
	g.phone="(626) 203-9409" 
	g.zip="95035" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#215 

	selfobj.response.write("Kaushik  Raghuraman  kkris24@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1535574919")) 
	g.year=2018
	g.fname="Kaushik"
	g.lname="Raghuraman"
	g.email="kkris24@gmail.com" 
	g.address="4730 Del Loma Ct" 
	g.city="Campbell" 
	g.phone="(480) 205-6777" 
	g.zip="95008" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#216 

	selfobj.response.write("Balakumar  Rajendran  balakumar85@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1521768272")) 
	g.year=2018
	g.fname="Balakumar"
	g.lname="Rajendran"
	g.email="balakumar85@gmail.com" 
	g.address="3043 Rossmore Way" 
	g.city="San Jose" 
	g.phone="(513) 739-2747" 
	g.zip="95148" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#217 

	selfobj.response.write("Vyass  Ramakrishnan  rvyass@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1521004991")) 
	g.year=2018
	g.fname="Vyass"
	g.lname="Ramakrishnan"
	g.email="rvyass@gmail.com" 
	g.address="2890 Monroe St" 
	g.city="Santa Clara" 
	g.phone="(469) 213-9145" 
	g.zip="95051" 
	g.ntrp="M4.0" 
	g.mtype="RS" 
	g.put()
#218 

	selfobj.response.write("Patricia  Ramirez  lprramirez@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1520058902")) 
	g.year=2018
	g.fname="Patricia"
	g.lname="Ramirez"
	g.email="lprramirez@gmail.com" 
	g.address="2865 Homestead Rd Apt 36" 
	g.city="Santa Clara" 
	g.phone="(408) 802-4789" 
	g.zip="95051" 
	g.ntrp="F" 
	g.mtype="RS" 
	g.put()
#219 

	selfobj.response.write("Akash  Ravindranath  akashravindranath@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1535586370")) 
	g.year=2018
	g.fname="Akash"
	g.lname="Ravindranath"
	g.email="akashravindranath@gmail.com" 
	g.address="1700 Halford Ave, Apt 311" 
	g.city="Santa Clara" 
	g.phone="(412) 799-4298" 
	g.zip="95051" 
	g.ntrp="M4" 
	g.mtype="RS" 
	g.put()
#220 

	selfobj.response.write("Aditya  Rawat  ad.rawat30@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1521653462")) 
	g.year=2018
	g.fname="Aditya"
	g.lname="Rawat"
	g.email="ad.rawat30@gmail.com" 
	g.address="1718 Don Ave" 
	g.city="San Jose" 
	g.phone="(219) 964-5051" 
	g.zip="95124" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#221 

	selfobj.response.write("Larry  Rinek  lrinek@aol.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1518818133")) 
	g.year=2018
	g.fname="Larry"
	g.lname="Rinek"
	g.email="lrinek@aol.com" 
	g.address="80 Gilbert Avenue" 
	g.city="Santa Clara" 
	g.phone="(408) 857-5204" 
	g.zip="95051" 
	g.ntrp="M3.0" 
	g.mtype="RS" 
	g.put()
#222 

	selfobj.response.write("Lauren  Salazar  kddsalazar@comcast.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1519963631")) 
	g.year=2018
	g.fname="Lauren"
	g.lname="Salazar"
	g.email="kddsalazar@comcast.net" 
	g.address="989 Perreira Dr" 
	g.city="Santa Clara" 
	g.phone="(408) 296-2379" 
	g.zip="95051" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#223 

	selfobj.response.write("Elisa   Salazar  kddsalazar@comcast.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1519963471")) 
	g.year=2018
	g.fname="Elisa "
	g.lname="Salazar"
	g.email="kddsalazar@comcast.net" 
	g.address="989 Perreira Dr" 
	g.city="Santa Clara" 
	g.phone="(408) 296-2379" 
	g.zip="95051" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#224 

	selfobj.response.write("Dolores  Salazar  kddsalazar@comcast.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1515012829")) 
	g.year=2018
	g.fname="Dolores"
	g.lname="Salazar"
	g.email="kddsalazar@comcast.net" 
	g.address="989 Perreira Dr" 
	g.city="Santa Clara" 
	g.phone="(408) 296-2379" 
	g.zip="95051" 
	g.ntrp="F3.0" 
	g.mtype="RF" 
	g.put()
#225 

	selfobj.response.write("Dempsey  Salazar  kddsalazar@comcast.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1519963548")) 
	g.year=2018
	g.fname="Dempsey"
	g.lname="Salazar"
	g.email="kddsalazar@comcast.net" 
	g.address="989 Perreira Dr" 
	g.city="Santa Clara" 
	g.phone="(408) 296-2379" 
	g.zip="95051" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#226 

	selfobj.response.write("Ken  Salazar  kddsalazar@comcast.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1519963329")) 
	g.year=2018
	g.fname="Ken"
	g.lname="Salazar"
	g.email="kddsalazar@comcast.net" 
	g.address="989 Perreira Dr" 
	g.city="Santa Clara" 
	g.phone="(408) 296-2379" 
	g.zip="95051" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#227 

	selfobj.response.write("Haruko  Sano  haruko0222@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1534119729")) 
	g.year=2018
	g.fname="Haruko"
	g.lname="Sano"
	g.email="haruko0222@gmail.com" 
	g.address="1167 Greenwood Ave" 
	g.city="Palo Alto" 
	g.phone="(650) 861-9878" 
	g.zip="94301" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#228 

	selfobj.response.write("Cecilia  Santillanes  cicigirl56@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1534121292")) 
	g.year=2018
	g.fname="Cecilia"
	g.lname="Santillanes"
	g.email="cicigirl56@yahoo.com" 
	g.address="2845 Buena Knoll Ct." 
	g.city="San Jose" 
	g.phone="(408) 344-5776" 
	g.zip="95121" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#229 

	selfobj.response.write("Michelle  Sarmenta  msarmenta@hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1520198167")) 
	g.year=2018
	g.fname="Michelle"
	g.lname="Sarmenta"
	g.email="msarmenta@hotmail.com" 
	g.address="1682 Naglee Avenue" 
	g.city="San Jose" 
	g.phone="(650) 223-1465" 
	g.zip="95126" 
	g.ntrp="F3.0" 
	g.mtype="NRS" 
	g.put()
#230 

	selfobj.response.write("Pegah  Seddighian  pegah.seddighian@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1523034277")) 
	g.year=2018
	g.fname="Pegah"
	g.lname="Seddighian"
	g.email="pegah.seddighian@gmail.com" 
	g.address="3600 Juliette Ln" 
	g.city="Santa Clara" 
	g.phone="(626) 840-7430" 
	g.zip="95054" 
	g.ntrp="F3.0" 
	g.mtype="RS" 
	g.put()
#231 

	selfobj.response.write("Mei  See  meisee68@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1515211109")) 
	g.year=2018
	g.fname="Mei"
	g.lname="See"
	g.email="meisee68@yahoo.com" 
	g.address="238 N Cypress Avenue" 
	g.city="Santa Clara" 
	g.phone="(408) 480-1880" 
	g.zip="95050" 
	g.ntrp="F3.0" 
	g.mtype="RF" 
	g.put()
#232 

	selfobj.response.write("Yin (TzeYin)  Segalman  yin.segalman@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1532400868")) 
	g.year=2018
	g.fname="Yin (TzeYin)"
	g.lname="Segalman"
	g.email="yin.segalman@gmail.com" 
	g.address="154 S  23rd  St" 
	g.city="San Jose" 
	g.phone="(505) 480-4384" 
	g.zip="95116" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#233 

	selfobj.response.write("Wade  Smithson  wado@wado.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1522769851")) 
	g.year=2018
	g.fname="Wade"
	g.lname="Smithson"
	g.email="wado@wado.com" 
	g.address="332 Carriage Dr. #2" 
	g.city="SANTA CLARA" 
	g.phone="(408) 655-6019" 
	g.zip="95050" 
	g.ntrp="M4.0" 
	g.mtype="RS" 
	g.put()
#234 

	selfobj.response.write("HT  Song  hyungtaes74@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1517991706")) 
	g.year=2018
	g.fname="HT"
	g.lname="Song"
	g.email="hyungtaes74@gmail.com" 
	g.address="450 Harvard Ave. 4B" 
	g.city="Santa Clara" 
	g.phone="(669) 246-0037" 
	g.zip="95051" 
	g.ntrp="M4.0" 
	g.mtype="RF" 
	g.put()
#235 

	selfobj.response.write("Hui-Mei  Spencer  huimeis@me.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1521650147")) 
	g.year=2018
	g.fname="Hui-Mei"
	g.lname="Spencer"
	g.email="huimeis@me.com" 
	g.address="237 W Hemlock Ave" 
	g.city="Sunnyvale" 
	g.phone="(408) 368-7649" 
	g.zip="94085" 
	g.ntrp="F2.5" 
	g.mtype="NRS" 
	g.put()
#236 

	selfobj.response.write("Cory  Sprague Williams  corsprague@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1519189765")) 
	g.year=2018
	g.fname="Cory"
	g.lname="Sprague Williams"
	g.email="corsprague@gmail.com" 
	g.address="1000 Kiely Blvd Apt 38" 
	g.city="SANTA CLARA" 
	g.phone="(619) 206-2884" 
	g.zip="95051" 
	g.ntrp="F4.0" 
	g.mtype="RF" 
	g.put()
#237 

	selfobj.response.write("Adela  Springer  aspringer3@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1520216099")) 
	g.year=2018
	g.fname="Adela"
	g.lname="Springer"
	g.email="aspringer3@sbcglobal.net" 
	g.address="6145 OAK FOREST WAY" 
	g.city="SAN JOSE" 
	g.phone="(408) 997-6525" 
	g.zip="95120" 
	g.ntrp="F2.5" 
	g.mtype="NRS" 
	g.put()
#238 

	selfobj.response.write("Ryan  Stefani  rtstefani@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1527381031")) 
	g.year=2018
	g.fname="Ryan"
	g.lname="Stefani"
	g.email="rtstefani@gmail.com" 
	g.address="50 Saratoga Ave apt #229" 
	g.city="Santa Clara" 
	g.phone="(805) 570-3774" 
	g.zip="95051" 
	g.ntrp="M3.5" 
	g.mtype="RS" 
	g.put()
#239 

	selfobj.response.write("Susan  Stulz  sstulz@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1515459889")) 
	g.year=2018
	g.fname="Susan"
	g.lname="Stulz"
	g.email="sstulz@gmail.com" 
	g.address="27260 SHERLOCK ROAD" 
	g.city="Los Altos Hills" 
	g.phone="(650) 380-2062" 
	g.zip="94022" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#240 

	selfobj.response.write("Fumie  Taguchi  fumie916@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1532407896")) 
	g.year=2018
	g.fname="Fumie"
	g.lname="Taguchi"
	g.email="fumie916@gmail.com" 
	g.address="1454 Thunderbird Avenue" 
	g.city="Sunnyvale" 
	g.phone="(408) 781-7608" 
	g.zip="94087" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#241 

	selfobj.response.write("Daniel  Tai  dantai@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1536611064")) 
	g.year=2018
	g.fname="Daniel"
	g.lname="Tai"
	g.email="dantai@gmail.com" 
	g.address="3460 NOTRE DAME DR" 
	g.city="SANTA CLARA" 
	g.phone="(408) 256-3260" 
	g.zip="95051" 
	g.ntrp="M3.5" 
	g.mtype="RS" 
	g.put()
#242 

	selfobj.response.write("Tomoe  Tajima  tajimatomoe@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1519339280")) 
	g.year=2018
	g.fname="Tomoe"
	g.lname="Tajima"
	g.email="tajimatomoe@gmail.com" 
	g.address="1020 Prune Ct." 
	g.city="Sunnyvale" 
	g.phone="(408) 963-3084" 
	g.zip="94087" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#243 

	selfobj.response.write("Svend  Tang-Petersen  svend_tangpetersen@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1510687896")) 
	g.year=2018
	g.fname="Svend"
	g.lname="Tang-Petersen"
	g.email="svend_tangpetersen@yahoo.com" 
	g.address="56 Paterson Place" 
	g.city="Santa Clara" 
	g.phone="(408) 768-1093" 
	g.zip="95050" 
	g.ntrp="M" 
	g.mtype="RF" 
	g.put()
#244 

	selfobj.response.write("Kirsten   Tasker  kirsten.tasker@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1520891273")) 
	g.year=2018
	g.fname="Kirsten "
	g.lname="Tasker"
	g.email="kirsten.tasker@gmail.com" 
	g.address="1731A Marshall Court" 
	g.city="Los Altos" 
	g.phone="(408) 680-4094" 
	g.zip="94024" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#245 

	selfobj.response.write("Michelle  Te  chelle_mhae2003@Yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1520051213")) 
	g.year=2018
	g.fname="Michelle"
	g.lname="Te"
	g.email="chelle_mhae2003@Yahoo.com" 
	g.address="416 Boynton ave" 
	g.city="San Jose" 
	g.phone="(925) 788-8524" 
	g.zip="95117" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#246 

	selfobj.response.write("Praveen  Thangavelu  praveenst@icloud.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1507668041")) 
	g.year=2018
	g.fname="Praveen"
	g.lname="Thangavelu"
	g.email="praveenst@icloud.com" 
	g.address="2122 Cabrillo Avenue" 
	g.city="Santa Clara" 
	g.phone="(916) 340-5270" 
	g.zip="95051" 
	g.ntrp="M" 
	g.mtype="RS" 
	g.put()
#247 

	selfobj.response.write("Gautam  Thockchom  gautam@mytiecon.org")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1535670648")) 
	g.year=2018
	g.fname="Gautam"
	g.lname="Thockchom"
	g.email="gautam@mytiecon.org" 
	g.address="3310 Princeton Way" 
	g.city="Santa Clara" 
	g.phone="(408) 476-7538" 
	g.zip="95051" 
	g.ntrp="M3.5" 
	g.mtype="RS" 
	g.put()
#248 

	selfobj.response.write("Craig  Tibbetts  craigtibbetts@netscape.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1535690253")) 
	g.year=2018
	g.fname="Craig"
	g.lname="Tibbetts"
	g.email="craigtibbetts@netscape.net" 
	g.address="3452 Bonita Ave" 
	g.city="Santa Clara" 
	g.phone="(248) 514-4380" 
	g.zip="95051" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#249 

	selfobj.response.write("Danijela  Tomic  T_danijela@Hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1538437847")) 
	g.year=2018
	g.fname="Danijela"
	g.lname="Tomic"
	g.email="T_danijela@Hotmail.com" 
	g.address="2720 Columbus Place" 
	g.city="Santa Clara" 
	g.phone="(408) 802-6886" 
	g.zip="95051" 
	g.ntrp="F3.5" 
	g.mtype="RS" 
	g.put()
#250 

	selfobj.response.write("Jelena  Tomic  T_danijela@Hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1530391118")) 
	g.year=2018
	g.fname="Jelena"
	g.lname="Tomic"
	g.email="T_danijela@Hotmail.com" 
	g.address="2720 Columbus Place" 
	g.city="Santa Clara" 
	g.phone="(408) 802-6886" 
	g.zip="95051" 
	g.ntrp="F3.0" 
	g.mtype="RF_" 
	g.put()
#251 

	selfobj.response.write("Danijela   Tomic   T_danijela@Hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1525240133")) 
	g.year=2018
	g.fname="Danijela "
	g.lname="Tomic "
	g.email="T_danijela@Hotmail.com" 
	g.address="2720 Columbus Place" 
	g.city="Santa Clara" 
	g.phone="(408) 802-6886" 
	g.zip="95051" 
	g.ntrp="F3.5" 
	g.mtype="RS" 
	g.put()
#252 

	selfobj.response.write("Debbie  Tripiano  dtripiano@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1513037287")) 
	g.year=2018
	g.fname="Debbie"
	g.lname="Tripiano"
	g.email="dtripiano@gmail.com" 
	g.address="1291 Pomeroy Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 772-6104" 
	g.zip="95051" 
	g.ntrp="F4.0" 
	g.mtype="RF_" 
	g.put()
#253 

	selfobj.response.write("Elaine  Troyan  elainetroyan@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1525810947")) 
	g.year=2018
	g.fname="Elaine"
	g.lname="Troyan"
	g.email="elainetroyan@yahoo.com" 
	g.address="2333 Homestead Road" 
	g.city="Santa clara" 
	g.phone="(408) 712-7104" 
	g.zip="95050" 
	g.ntrp="F2.5" 
	g.mtype="RS" 
	g.put()
#254 

	selfobj.response.write("Roland  Troyan  elainetroyan@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1527532373")) 
	g.year=2018
	g.fname="Roland"
	g.lname="Troyan"
	g.email="elainetroyan@yahoo.com" 
	g.address="2333 Homestead Road" 
	g.city="Santa Clara" 
	g.phone="(408) 712-7104" 
	g.zip="95050" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#255 

	selfobj.response.write("John  Troyan  elainetroyan@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1527532186")) 
	g.year=2018
	g.fname="John"
	g.lname="Troyan"
	g.email="elainetroyan@yahoo.com" 
	g.address="2333 Homestead Road" 
	g.city="Santa Clara" 
	g.phone="(408) 712-7104" 
	g.zip="95050" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#256 

	selfobj.response.write("Shannon  Troyan  elainetroyan@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1527532548")) 
	g.year=2018
	g.fname="Shannon"
	g.lname="Troyan"
	g.email="elainetroyan@yahoo.com" 
	g.address="2333 Homestead Road" 
	g.city="Santa Clara" 
	g.phone="(408) 712-7104" 
	g.zip="95050" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#257 

	selfobj.response.write("Marcia  Truswell  marciatruswell@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1539919766")) 
	g.year=2018
	g.fname="Marcia"
	g.lname="Truswell"
	g.email="marciatruswell@gmail.com" 
	g.address="398 S. 17th Street" 
	g.city="San Jose" 
	g.phone="(408) 219-1935" 
	g.zip="95112" 
	g.ntrp="F" 
	g.mtype="NRF" 
	g.put()
#258 

	selfobj.response.write("Pai (Tim)  Tsai  pc181@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1514855775")) 
	g.year=2018
	g.fname="Pai (Tim)"
	g.lname="Tsai"
	g.email="pc181@yahoo.com" 
	g.address="5855 Royal Ann Dr." 
	g.city="San Jose" 
	g.phone="(408) 832-6811" 
	g.zip="95129" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#259 

	selfobj.response.write("Klara  Turner  klaraturnersalon@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1516007538")) 
	g.year=2018
	g.fname="Klara"
	g.lname="Turner"
	g.email="klaraturnersalon@yahoo.com" 
	g.address="10837 Northridge Square" 
	g.city="Cupertino" 
	g.phone="(650) 323-0735" 
	g.zip="95014" 
	g.ntrp="F3.0" 
	g.mtype="NRS" 
	g.put()
#260 

	selfobj.response.write("William  Van Cleave  eagleeyesaremine@aol.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1536181455")) 
	g.year=2018
	g.fname="William"
	g.lname="Van Cleave"
	g.email="eagleeyesaremine@aol.com" 
	g.address="2950 East Dunne Ave" 
	g.city="Morgan Hill" 
	g.phone="(408) 209-6142" 
	g.zip="95037" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#261 

	selfobj.response.write("Vince  Ventura  loriv@me.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1515092157")) 
	g.year=2018
	g.fname="Vince"
	g.lname="Ventura"
	g.email="loriv@me.com" 
	g.address="2653 Elliot St" 
	g.city="Santa Clara" 
	g.phone="(408) 246-5784" 
	g.zip="95051" 
	g.ntrp="M2.5" 
	g.mtype="RF_" 
	g.put()
#262 

	selfobj.response.write("Ryan  Ventura  loriv@me.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1515092231")) 
	g.year=2018
	g.fname="Ryan"
	g.lname="Ventura"
	g.email="loriv@me.com" 
	g.address="2653 Elliot St" 
	g.city="Santa Clara" 
	g.phone="(408) 246-5784" 
	g.zip="95051" 
	g.ntrp="M2.5" 
	g.mtype="RF_" 
	g.put()
#263 

	selfobj.response.write("Lori  Ventura  Loriv@me.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1515092045")) 
	g.year=2018
	g.fname="Lori"
	g.lname="Ventura"
	g.email="Loriv@me.com" 
	g.address="2653 Elliot St" 
	g.city="Santa Clara" 
	g.phone="(408) 425-3420" 
	g.zip="95051" 
	g.ntrp="F3.5" 
	g.mtype="RF" 
	g.put()
#264 

	selfobj.response.write("Shashank  Verma  shashank.verma590@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1521841461")) 
	g.year=2018
	g.fname="Shashank"
	g.lname="Verma"
	g.email="shashank.verma590@gmail.com" 
	g.address="655 South Fair Oaks Avenue, Apartment J117" 
	g.city="Sunnyvale" 
	g.phone="(669) 264-7886" 
	g.zip="94086" 
	g.ntrp="M" 
	g.mtype="NRS" 
	g.put()
#265 

	selfobj.response.write("Madan Kumar  Vijayakumar  madanvkumar@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1521910488")) 
	g.year=2018
	g.fname="Madan Kumar"
	g.lname="Vijayakumar"
	g.email="madanvkumar@gmail.com" 
	g.address="600, rainbow drive, Apartment#123" 
	g.city="Mountain view" 
	g.phone="(408) 650-2837" 
	g.zip="94041" 
	g.ntrp="M3.0" 
	g.mtype="NRS" 
	g.put()
#266 

	selfobj.response.write("Vasanth  Viswanathan  vasanth.viswanath@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1538085020")) 
	g.year=2018
	g.fname="Vasanth"
	g.lname="Viswanathan"
	g.email="vasanth.viswanath@gmail.com" 
	g.address="770 Saratoga Ave, Apt T110" 
	g.city="San Jose" 
	g.phone="(510) 565-5452" 
	g.zip="95129" 
	g.ntrp="M3.0" 
	g.mtype="NRS" 
	g.put()
#267 

	selfobj.response.write("Ilana  Volfin  ilanavo@Yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1525448244")) 
	g.year=2018
	g.fname="Ilana"
	g.lname="Volfin"
	g.email="ilanavo@Yahoo.com" 
	g.address="2870 Kaiser Dr, Apt 272" 
	g.city="Santa Clara" 
	g.phone="(408) 309-6472" 
	g.zip="95051" 
	g.ntrp="F4.0" 
	g.mtype="RS" 
	g.put()
#268 

	selfobj.response.write("Jasmine  Vu  haiquangvu@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1522268472")) 
	g.year=2018
	g.fname="Jasmine"
	g.lname="Vu"
	g.email="haiquangvu@yahoo.com" 
	g.address="148 Perry St." 
	g.city="Milpitas" 
	g.phone="(408) 910-3970" 
	g.zip="95035" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#269 

	selfobj.response.write("Lyan  Vu  LyPham411@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1517290764")) 
	g.year=2018
	g.fname="Lyan"
	g.lname="Vu"
	g.email="LyPham411@yahoo.com" 
	g.address="142 E Mission Street" 
	g.city="San Jose" 
	g.phone="(408) 874-5380" 
	g.zip="95112" 
	g.ntrp="F" 
	g.mtype="NRS" 
	g.put()
#270 

	selfobj.response.write("Lu  Walker  wumbergee@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1532394521")) 
	g.year=2018
	g.fname="Lu"
	g.lname="Walker"
	g.email="wumbergee@gmail.com" 
	g.address="11491 Cresta Lane" 
	g.city="Dublin" 
	g.phone="(925) 922-1798" 
	g.zip="94568" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#271 

	selfobj.response.write("Ben  Wang  qzhwang@Gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1533802845")) 
	g.year=2018
	g.fname="Ben"
	g.lname="Wang"
	g.email="qzhwang@Gmail.com" 
	g.address="1400 Bowe Ave Apt 204" 
	g.city="Santa Clara" 
	g.phone="(408) 250-1647" 
	g.zip="95051" 
	g.ntrp="M4.0" 
	g.mtype="RF_" 
	g.put()
#272 

	selfobj.response.write("David  Wei  bp_wei@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1513613173")) 
	g.year=2018
	g.fname="David"
	g.lname="Wei"
	g.email="bp_wei@yahoo.com" 
	g.address="10281 Torre Ave ,Unit 819" 
	g.city="Cupertino" 
	g.phone="(952) 693-6199" 
	g.zip="95014" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#273 

	selfobj.response.write("David  White  kcarber@aol.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1536894023")) 
	g.year=2018
	g.fname="David"
	g.lname="White"
	g.email="kcarber@aol.com" 
	g.address="111 Stonewood Drive" 
	g.city="Scotts Valley" 
	g.phone="(650) 575-4286" 
	g.zip="95066" 
	g.ntrp="M4.0" 
	g.mtype="NRF_" 
	g.put()
#274 

	selfobj.response.write("Ross  Williams  rossewilliams@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1520961662")) 
	g.year=2018
	g.fname="Ross"
	g.lname="Williams"
	g.email="rossewilliams@gmail.com" 
	g.address="1491 Bellomy St" 
	g.city="Santa Clara" 
	g.phone="(408) 650-4516" 
	g.zip="95050" 
	g.ntrp="M3.0" 
	g.mtype="RS" 
	g.put()
#275 

	selfobj.response.write("Asa  Williams  asawilliams@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1519189872")) 
	g.year=2018
	g.fname="Asa"
	g.lname="Williams"
	g.email="asawilliams@gmail.com" 
	g.address="1000 Kiely Blvd Apt 38" 
	g.city="SANTA CLARA" 
	g.phone="(619) 206-0937" 
	g.zip="95051" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#276 

	selfobj.response.write("Aaliyah  Wright  jwbrinquis@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1522697358")) 
	g.year=2018
	g.fname="Aaliyah"
	g.lname="Wright"
	g.email="jwbrinquis@gmail.com" 
	g.address="3700 CASA VERDE ST. APT. 3116" 
	g.city="San Jose" 
	g.phone="(505) 702-4452" 
	g.zip="95134" 
	g.ntrp="F" 
	g.mtype="NRF_" 
	g.put()
#277 

	selfobj.response.write("Jason  Wu  jcwu84@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1522648105")) 
	g.year=2018
	g.fname="Jason"
	g.lname="Wu"
	g.email="jcwu84@gmail.com" 
	g.address="1104 Chula Vista Ave. Apt F" 
	g.city="Burlingame" 
	g.phone="(650) 278-9118" 
	g.zip="94010" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#278 

	selfobj.response.write("Warren  Yamaguchi  winini@comcast.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1513037061")) 
	g.year=2018
	g.fname="Warren"
	g.lname="Yamaguchi"
	g.email="winini@comcast.net" 
	g.address="1291 Pomeroy Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 772-6104" 
	g.zip="95051" 
	g.ntrp="M4.0" 
	g.mtype="RF" 
	g.put()
#279 

	selfobj.response.write("Brian  Yorke  carythm007@aol.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1533836218")) 
	g.year=2018
	g.fname="Brian"
	g.lname="Yorke"
	g.email="carythm007@aol.com" 
	g.address="1371 Niagara Dr" 
	g.city="San Jose" 
	g.phone="(408) 656-3921" 
	g.zip="95130" 
	g.ntrp="M3.0" 
	g.mtype="NRS" 
	g.put()
#280 

	selfobj.response.write("Monica  Yoshioka  monica_yoshioka@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1513475610")) 
	g.year=2018
	g.fname="Monica"
	g.lname="Yoshioka"
	g.email="monica_yoshioka@yahoo.com" 
	g.address="1574 Finch Way" 
	g.city="Sunnyvale" 
	g.phone="(408) 368-0860" 
	g.zip="94087" 
	g.ntrp="F3.0" 
	g.mtype="NRS" 
	g.put()
#281 

	selfobj.response.write("Imran  Yusuf  ikyusuf@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1515700958")) 
	g.year=2018
	g.fname="Imran"
	g.lname="Yusuf"
	g.email="ikyusuf@yahoo.com" 
	g.address="1333 Selo Drive" 
	g.city="Sunnyvale" 
	g.phone="(408) 230-7726" 
	g.zip="94087" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#282 

	selfobj.response.write("Lynda  Zhang  lzhang83713@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1515480558")) 
	g.year=2018
	g.fname="Lynda"
	g.lname="Zhang"
	g.email="lzhang83713@yahoo.com" 
	g.address="460 Norwood Circle" 
	g.city="Santa Clara" 
	g.phone="(208) 283-2835" 
	g.zip="95051" 
	g.ntrp="F4.0" 
	g.mtype="RS" 
	g.put()
#283 

	selfobj.response.write("elle  zseng  ellezseng@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1536972207")) 
	g.year=2018
	g.fname="elle"
	g.lname="zseng"
	g.email="ellezseng@gmail.com" 
	g.address="603 valeri ruth ct" 
	g.city="santa clara" 
	g.phone="(530) 574-6139" 
	g.zip="95050" 
	g.ntrp="F3.0" 
	g.mtype="RS" 
	g.put()
