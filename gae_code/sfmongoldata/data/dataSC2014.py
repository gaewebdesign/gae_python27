

#
#
#select * from paypal where year = "2014"  union select * from bycheck where year =  "2014" order by year,lname 
#
#
import webapp2
from datastore import  *


def santaclara2014(selfobj):


#1 

	selfobj.response.write("Mike  Adame  mike_adame@comcast.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1405136086")) 
	g.year=2014
	g.fname="Mike"
	g.lname="Adame"
	g.email="mike_adame@comcast.net" 
	g.address="2206 San Antonia Pl" 
	g.city="Santa Clara" 
	g.phone="(408) 202-1118" 
	g.ntrp="M3.5" 
	g.mtype="RS" 
	g.put()
#2 

	selfobj.response.write("Jennifer  Adams  Jenyferadams@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1394310868")) 
	g.year=2014
	g.fname="Jennifer"
	g.lname="Adams"
	g.email="Jenyferadams@sbcglobal.net" 
	g.address="5971 Countess Drive" 
	g.city="San Jose" 
	g.phone="(408) 313-4405" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#3 

	selfobj.response.write("Sreenivas  Aluru  salur1@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1394569951")) 
	g.year=2014
	g.fname="Sreenivas"
	g.lname="Aluru"
	g.email="salur1@yahoo.com" 
	g.address="10816 alderbrook lane" 
	g.city="Cupertino" 
	g.phone="(408) 406-1885" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#4 

	selfobj.response.write("Nancy  Andersen  canandfam@earthlink.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1400108131")) 
	g.year=2014
	g.fname="Nancy"
	g.lname="Andersen"
	g.email="canandfam@earthlink.net" 
	g.address="3032 Cameron Way" 
	g.city="Santa Clara" 
	g.phone="(408) 799-3678" 
	g.ntrp="F3.0" 
	g.mtype="RS" 
	g.put()
#5 

	selfobj.response.write("Don  Anderson  donranderson@hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1395466193")) 
	g.year=2014
	g.fname="Don"
	g.lname="Anderson"
	g.email="donranderson@hotmail.com" 
	g.address="4890 Clarendon Dr." 
	g.city="San Jose" 
	g.phone="(408) 725-1337" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#6 

	selfobj.response.write("Ashok  Anumandla  aashoke@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1405136473")) 
	g.year=2014
	g.fname="Ashok"
	g.lname="Anumandla"
	g.email="aashoke@yahoo.com" 
	g.address="" 
	g.city="Campbell" 
	g.phone="() -" 
	g.ntrp="M4.5" 
	g.mtype="NRS" 
	g.put()
#7 

	selfobj.response.write("Janet  Arsenault  j6ma@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1405136712")) 
	g.year=2014
	g.fname="Janet"
	g.lname="Arsenault"
	g.email="j6ma@sbcglobal.net" 
	g.address="1312 Meadowlark Ave" 
	g.city="San Jose" 
	g.phone="(408) 656-4722" 
	g.ntrp="F3.0" 
	g.mtype="NRS" 
	g.put()
#8 

	selfobj.response.write("Huzefa   Aurangabadi  huzefa23@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1398869769")) 
	g.year=2014
	g.fname="Huzefa "
	g.lname="Aurangabadi"
	g.email="huzefa23@gmail.com" 
	g.address="2451 Mission College Blvd" 
	g.city="Santa Clara" 
	g.phone="(408) 893-6557" 
	g.ntrp="M3.5" 
	g.mtype="RF_" 
	g.put()
#9 

	selfobj.response.write("Hideko  Azama  tennissenior@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1405136231")) 
	g.year=2014
	g.fname="Hideko"
	g.lname="Azama"
	g.email="tennissenior@yahoo.com" 
	g.address="3115 Mauricia Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 246-5129" 
	g.ntrp="F" 
	g.mtype="RS" 
	g.put()
#10 

	selfobj.response.write("Michal  Bajdich  bajdich@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1395720164")) 
	g.year=2014
	g.fname="Michal"
	g.lname="Bajdich"
	g.email="bajdich@gmail.com" 
	g.address="3542 OAK KNOLL DR" 
	g.city="Emerald Hills" 
	g.phone="(919) 649-9318" 
	g.ntrp="M4.5" 
	g.mtype="NRS" 
	g.put()
#11 

	selfobj.response.write("Benny  Barbero  bennybarbero@netzero.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1395856058")) 
	g.year=2014
	g.fname="Benny"
	g.lname="Barbero"
	g.email="bennybarbero@netzero.com" 
	g.address="3209 Orthello Way" 
	g.city="Santa Clara" 
	g.phone="(408) 507-0957" 
	g.ntrp="M4.0" 
	g.mtype="RS" 
	g.put()
#12 

	selfobj.response.write("Orhan  Baser  obaser@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1414560674")) 
	g.year=2014
	g.fname="Orhan"
	g.lname="Baser"
	g.email="obaser@gmail.com" 
	g.address="544 Hickory Place" 
	g.city="Santa Clara" 
	g.phone="(408) 887-2514" 
	g.ntrp="M4.0" 
	g.mtype="RF" 
	g.put()
#13 

	selfobj.response.write("Naoko   Bean  naokobean@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1398387897")) 
	g.year=2014
	g.fname="Naoko "
	g.lname="Bean"
	g.email="naokobean@yahoo.com" 
	g.address="3440 El Camino Real #316" 
	g.city="Santa Clara" 
	g.phone="(408) 888-2290" 
	g.ntrp="F4.5" 
	g.mtype="RF" 
	g.put()
#14 

	selfobj.response.write("Jonathan  Bell  c.p.bell@att.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1390674770")) 
	g.year=2014
	g.fname="Jonathan"
	g.lname="Bell"
	g.email="c.p.bell@att.net" 
	g.address="1244 Maryann Drive" 
	g.city="Santa Clara" 
	g.phone="(408) 241-6793" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#15 

	selfobj.response.write("Randy  Bell  c.p.bell@att.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1390674574")) 
	g.year=2014
	g.fname="Randy"
	g.lname="Bell"
	g.email="c.p.bell@att.net" 
	g.address="1244 Maryann Drive" 
	g.city="Santa Clara" 
	g.phone="(408) 241-6793" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#16 

	selfobj.response.write("Carrie  Bell  c.p.bell@att.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1390591384")) 
	g.year=2014
	g.fname="Carrie"
	g.lname="Bell"
	g.email="c.p.bell@att.net" 
	g.address="1244 Maryann Drive" 
	g.city="Santa Clara" 
	g.phone="(408) 464-3177" 
	g.ntrp="F4.5" 
	g.mtype="RF" 
	g.put()
#17 

	selfobj.response.write("Fumiko  Beniyama  fmkbeni@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1395685077")) 
	g.year=2014
	g.fname="Fumiko"
	g.lname="Beniyama"
	g.email="fmkbeni@gmail.com" 
	g.address="550 Moreland Way APT1206" 
	g.city="Santa Clara" 
	g.phone="(408) 318-1603" 
	g.ntrp="F4.5" 
	g.mtype="RF" 
	g.put()
#18 

	selfobj.response.write("Nobuo  Beniyama  nb3298@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1405136942")) 
	g.year=2014
	g.fname="Nobuo"
	g.lname="Beniyama"
	g.email="nb3298@gmail.com" 
	g.address="550 Moreland Way APT1206" 
	g.city="Santq Clara" 
	g.phone="(408) 960-5470" 
	g.ntrp="M3.0" 
	g.mtype="RF_" 
	g.put()
#19 

	selfobj.response.write("Theresa  Berg  tberg@apple.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1395961112")) 
	g.year=2014
	g.fname="Theresa"
	g.lname="Berg"
	g.email="tberg@apple.com" 
	g.address="2672 Skylark Drive" 
	g.city="San Jose" 
	g.phone="(408) 497-0736" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#20 

	selfobj.response.write("Shar  Bishop  shardean@comcast.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1393792813")) 
	g.year=2014
	g.fname="Shar"
	g.lname="Bishop"
	g.email="shardean@comcast.net" 
	g.address="1220 Tasman Dr # 461" 
	g.city="Sunnyvale" 
	g.phone="(408) 431-4605" 
	g.ntrp="F3.0" 
	g.mtype="NRS" 
	g.put()
#21 

	selfobj.response.write("Gregorio  Borromeo  triplegg2001@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1393185304")) 
	g.year=2014
	g.fname="Gregorio"
	g.lname="Borromeo"
	g.email="triplegg2001@yahoo.com" 
	g.address="" 
	g.city="Campbell" 
	g.phone="() -" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#22 

	selfobj.response.write("Daniel  Braud  dbraud@mac.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1404703778")) 
	g.year=2014
	g.fname="Daniel"
	g.lname="Braud"
	g.email="dbraud@mac.com" 
	g.address="180 Kiely Blvd., Apt D" 
	g.city="Santa Clara" 
	g.phone="(504) 421-0908" 
	g.ntrp="M" 
	g.mtype="RS" 
	g.put()
#23 

	selfobj.response.write("Robert  Brunkhorst  bbrunkhorst@sandisk.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1398194705")) 
	g.year=2014
	g.fname="Robert"
	g.lname="Brunkhorst"
	g.email="bbrunkhorst@sandisk.com" 
	g.address="849 Humewick Way" 
	g.city="Sunnyvale" 
	g.phone="(408) 739-6480" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#24 

	selfobj.response.write("Ike  Bunanta  ibunanta@me.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1394651381")) 
	g.year=2014
	g.fname="Ike"
	g.lname="Bunanta"
	g.email="ibunanta@me.com" 
	g.address="1059 Konstanz Terrace" 
	g.city="Sunnyvale" 
	g.phone="(408) 406-5830" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#25 

	selfobj.response.write("Thomas  Calvello  volgab@Yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1393828611")) 
	g.year=2014
	g.fname="Thomas"
	g.lname="Calvello"
	g.email="volgab@Yahoo.com" 
	g.address="1974 Homestead Road" 
	g.city="Santa Clara" 
	g.phone="(650) 303-1151" 
	g.ntrp="M3.0" 
	g.mtype="RF_" 
	g.put()
#26 

	selfobj.response.write("Volga  Calvello  volgab@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1393826286")) 
	g.year=2014
	g.fname="Volga"
	g.lname="Calvello"
	g.email="volgab@yahoo.com" 
	g.address="1974 Homestead Road" 
	g.city="Santa Clara" 
	g.phone="(650) 303-1151" 
	g.ntrp="F3.0" 
	g.mtype="RF" 
	g.put()
#27 

	selfobj.response.write("Mitch  Carillo  mitch_carrillo@agilent.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1395786293")) 
	g.year=2014
	g.fname="Mitch"
	g.lname="Carillo"
	g.email="mitch_carrillo@agilent.com" 
	g.address="3321 Benton St" 
	g.city="Santa Clara" 
	g.phone="(408) 514-7340" 
	g.ntrp="M" 
	g.mtype="RF" 
	g.put()
#28 

	selfobj.response.write("Jacob  Carrillo  mitch_carrillo@agilent.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1395888861")) 
	g.year=2014
	g.fname="Jacob"
	g.lname="Carrillo"
	g.email="mitch_carrillo@agilent.com" 
	g.address="3321 Benton St" 
	g.city="Santa Clara" 
	g.phone="() -" 
	g.ntrp="M2.5" 
	g.mtype="RF_" 
	g.put()
#29 

	selfobj.response.write("Alysha  Carrillo  mitch_carrillo@agilent.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1395888829")) 
	g.year=2014
	g.fname="Alysha"
	g.lname="Carrillo"
	g.email="mitch_carrillo@agilent.com" 
	g.address="3321 Benton St" 
	g.city="Santa Clara" 
	g.phone="() -" 
	g.ntrp="F2.0" 
	g.mtype="RF_" 
	g.put()
#30 

	selfobj.response.write("Erlinda  Carrillo  mitch_carrillo@agilent.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1395870586")) 
	g.year=2014
	g.fname="Erlinda"
	g.lname="Carrillo"
	g.email="mitch_carrillo@agilent.com" 
	g.address="3321 Benton St" 
	g.city="Santa Clara" 
	g.phone="(408) 514-7340" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#31 

	selfobj.response.write("Patricia  Carrillo  mitch_carrillo@agilent.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1395888802")) 
	g.year=2014
	g.fname="Patricia"
	g.lname="Carrillo"
	g.email="mitch_carrillo@agilent.com" 
	g.address="3321 Benton St" 
	g.city="Santa Clara" 
	g.phone="() -" 
	g.ntrp="F2.0" 
	g.mtype="RF_" 
	g.put()
#32 

	selfobj.response.write("Myoung  Chiang  Taeckchiang@Gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1395876235")) 
	g.year=2014
	g.fname="Myoung"
	g.lname="Chiang"
	g.email="Taeckchiang@Gmail.com" 
	g.address="1235 de altura comns" 
	g.city="San Jose" 
	g.phone="(408) 306-3657" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#33 

	selfobj.response.write("Elaine  Chiu  elaineschiu@aol.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1412926143")) 
	g.year=2014
	g.fname="Elaine"
	g.lname="Chiu"
	g.email="elaineschiu@aol.com" 
	g.address="5678 Algonquin Way" 
	g.city="San Jose" 
	g.phone="(408) 921-6330" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#34 

	selfobj.response.write("Eric   Choksi  eric.choksi@hp.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1395714781")) 
	g.year=2014
	g.fname="Eric "
	g.lname="Choksi"
	g.email="eric.choksi@hp.com" 
	g.address="367 Shelby Drive" 
	g.city="Mountain View" 
	g.phone="(408) 835-9622" 
	g.ntrp="M4.5" 
	g.mtype="NRS" 
	g.put()
#35 

	selfobj.response.write("May  Chou  may@maychouinsurance.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1398297398")) 
	g.year=2014
	g.fname="May"
	g.lname="Chou"
	g.email="may@maychouinsurance.com" 
	g.address="2905 Stender Way, #18E" 
	g.city="Santa Clara" 
	g.phone="(408) 689-2987" 
	g.ntrp="F3.0" 
	g.mtype="NRS" 
	g.put()
#36 

	selfobj.response.write("Paul  Chou  paulchou@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1399864211")) 
	g.year=2014
	g.fname="Paul"
	g.lname="Chou"
	g.email="paulchou@gmail.com" 
	g.address="4274 Rivermark Parkway" 
	g.city="Santa Clara" 
	g.phone="(408) 829-7627" 
	g.ntrp="M" 
	g.mtype="RF" 
	g.put()
#37 

	selfobj.response.write("Lori  Cruz-Spray   cruzspray@Gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1394609484")) 
	g.year=2014
	g.fname="Lori"
	g.lname="Cruz-Spray "
	g.email="cruzspray@Gmail.com" 
	g.address="555 Minton Ln" 
	g.city="Mountain View" 
	g.phone="(650) 690-0022" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#38 

	selfobj.response.write("Onofre  de Souza   onofre2237@aol.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1393203840")) 
	g.year=2014
	g.fname="Onofre"
	g.lname="de Souza "
	g.email="onofre2237@aol.com" 
	g.address="2983 Millar Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 241-0102" 
	g.ntrp="M3.0" 
	g.mtype="RF" 
	g.put()
#39 

	selfobj.response.write("Mark  de Souza  onofre2237@aol.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1393280655")) 
	g.year=2014
	g.fname="Mark"
	g.lname="de Souza"
	g.email="onofre2237@aol.com" 
	g.address="2983 Millar Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 241-0102" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#40 

	selfobj.response.write("Marky  de Souza  onofre2237@aol.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1393280679")) 
	g.year=2014
	g.fname="Marky"
	g.lname="de Souza"
	g.email="onofre2237@aol.com" 
	g.address="2983 Millar Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 241-0102" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#41 

	selfobj.response.write("Thanh  Do  une.vagabonde@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1395892844")) 
	g.year=2014
	g.fname="Thanh"
	g.lname="Do"
	g.email="une.vagabonde@gmail.com" 
	g.address="2458 Moraine Drive" 
	g.city="Santa Clara" 
	g.phone="(415) 513-6099" 
	g.ntrp="F3.5" 
	g.mtype="RS" 
	g.put()
#42 

	selfobj.response.write("Thac  Doan  thacdoan3060@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1405148250")) 
	g.year=2014
	g.fname="Thac"
	g.lname="Doan"
	g.email="thacdoan3060@gmail.com" 
	g.address="3060 Dibble Ct" 
	g.city="Santa Clara" 
	g.phone="(408) 966-9717" 
	g.ntrp="M" 
	g.mtype="RF" 
	g.put()
#43 

	selfobj.response.write("Lisa  Doan  thacdoan3060@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1405148250")) 
	g.year=2014
	g.fname="Lisa"
	g.lname="Doan"
	g.email="thacdoan3060@gmail.com" 
	g.address="3060 Dibble Ct" 
	g.city="Santa Clara" 
	g.phone="(408) 966-9717" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#44 

	selfobj.response.write("Diep  Doan  thacdoan3060@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1405148250")) 
	g.year=2014
	g.fname="Diep"
	g.lname="Doan"
	g.email="thacdoan3060@gmail.com" 
	g.address="3060 Dibble Ct" 
	g.city="Santa Clara" 
	g.phone="(408) 966-9717" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#45 

	selfobj.response.write("Thomas  Dunham  t.dunham24@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1395706971")) 
	g.year=2014
	g.fname="Thomas"
	g.lname="Dunham"
	g.email="t.dunham24@gmail.com" 
	g.address="3666 Franklin ave." 
	g.city="Fremont" 
	g.phone="(510) 673-6300" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#46 

	selfobj.response.write("Carl  Dunlap  highaffinitycarl@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1405138063")) 
	g.year=2014
	g.fname="Carl"
	g.lname="Dunlap"
	g.email="highaffinitycarl@yahoo.com" 
	g.address="990 B La Mesa Terrace" 
	g.city="Sunnyvale" 
	g.phone="(408) 245-5405" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#47 

	selfobj.response.write("Michael  Durrigan  mdurrigan@att.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1405138237")) 
	g.year=2014
	g.fname="Michael"
	g.lname="Durrigan"
	g.email="mdurrigan@att.net" 
	g.address="250 San Fe Terrace #224" 
	g.city="Sunnyvale" 
	g.phone="(408) 203-0861" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#48 

	selfobj.response.write("Kaori  Enomoto  kaori@saphirellc.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1392098348")) 
	g.year=2014
	g.fname="Kaori"
	g.lname="Enomoto"
	g.email="kaori@saphirellc.com" 
	g.address="10250 Vicksburg Ct." 
	g.city="Cupertino" 
	g.phone="(408) 623-5702" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#49 

	selfobj.response.write("Maurice  Ewert   snowbound1962@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1392696780")) 
	g.year=2014
	g.fname="Maurice"
	g.lname="Ewert"
	g.email=" snowbound1962@yahoo.com" 
	g.address="" 
	g.city="San Jose" 
	g.phone="(  )   -" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#50 

	selfobj.response.write("Jerry  Fan  jerry.fan@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1396418841")) 
	g.year=2014
	g.fname="Jerry"
	g.lname="Fan"
	g.email="jerry.fan@gmail.com" 
	g.address="12300 Larchmont" 
	g.city="Saratoga" 
	g.phone="(408) 505-8781" 
	g.ntrp="M4.0" 
	g.mtype="RS" 
	g.put()
#51 

	selfobj.response.write("Laura  Fletcher  fletch4him1@mac.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1412966683")) 
	g.year=2014
	g.fname="Laura"
	g.lname="Fletcher"
	g.email="fletch4him1@mac.com" 
	g.address="431 El Camino Real #1210" 
	g.city="Santa Clara" 
	g.phone="(650) 492-1930" 
	g.ntrp="F3.5" 
	g.mtype="RF" 
	g.put()
#52 

	selfobj.response.write("Jill   Foster  jilldeanefoster@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1396298134")) 
	g.year=2014
	g.fname="Jill "
	g.lname="Foster"
	g.email="jilldeanefoster@gmail.com" 
	g.address="122 Westhill Drive" 
	g.city="Los Gatos" 
	g.phone="(408) 540-8215" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#53 

	selfobj.response.write("Susan  Frank  susanfrank1@hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1410202108")) 
	g.year=2014
	g.fname="Susan"
	g.lname="Frank"
	g.email="susanfrank1@hotmail.com" 
	g.address="132 Promethean Way" 
	g.city="Mountain View" 
	g.phone="(650) 400-0423" 
	g.ntrp="F" 
	g.mtype="NRS" 
	g.put()
#54 

	selfobj.response.write("Gina  Funaro  gina.funaro@stanfordalumni.org")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1393185404")) 
	g.year=2014
	g.fname="Gina"
	g.lname="Funaro"
	g.email="gina.funaro@stanfordalumni.org" 
	g.address="" 
	g.city="Cupertino" 
	g.phone="() -" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#55 

	selfobj.response.write("Vikas  Gokhale  vikasgok@hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1407178626")) 
	g.year=2014
	g.fname="Vikas"
	g.lname="Gokhale"
	g.email="vikasgok@hotmail.com" 
	g.address="2797 Estella Dr." 
	g.city="Santa Clara" 
	g.phone="(408) 823-1965" 
	g.ntrp="M3.5" 
	g.mtype="RF" 
	g.put()
#56 

	selfobj.response.write("Allan  Greenberg  allgreen@ucla.edu")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1405138388")) 
	g.year=2014
	g.fname="Allan"
	g.lname="Greenberg"
	g.email="allgreen@ucla.edu" 
	g.address="550 Moreland Way Apt 2403" 
	g.city="Santa Clara" 
	g.phone="(320) 576-1310" 
	g.ntrp="M3.5" 
	g.mtype="RF" 
	g.put()
#57 

	selfobj.response.write("Hyeok  Hahn  hhahn00@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1396306224")) 
	g.year=2014
	g.fname="Hyeok"
	g.lname="Hahn"
	g.email="hhahn00@yahoo.com" 
	g.address="2926 Roma Ct." 
	g.city="Santa Clara" 
	g.phone="(408) 507-2848" 
	g.ntrp="M3.5" 
	g.mtype="RF" 
	g.put()
#58 

	selfobj.response.write("Lucille  Harendza  lharendza@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1395332821")) 
	g.year=2014
	g.fname="Lucille"
	g.lname="Harendza"
	g.email="lharendza@yahoo.com" 
	g.address="267 Cahill Park Drive" 
	g.city="San Jose" 
	g.phone="(408) 888-2447" 
	g.ntrp="F3.0" 
	g.mtype="NRS" 
	g.put()
#59 

	selfobj.response.write("Sharon  Haugen  haugen500@earthlink.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1410240689")) 
	g.year=2014
	g.fname="Sharon"
	g.lname="Haugen"
	g.email="haugen500@earthlink.net" 
	g.address="1575 Keith Drive" 
	g.city="Campbell" 
	g.phone="(408) 379-9889" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#60 

	selfobj.response.write("Julie  Hawkes  hawkes_julie@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1392696531")) 
	g.year=2014
	g.fname="Julie"
	g.lname="Hawkes"
	g.email="hawkes_julie@yahoo.com" 
	g.address="" 
	g.city="Santa Clara" 
	g.phone="(  )   -" 
	g.ntrp="F4.0" 
	g.mtype="RF" 
	g.put()
#61 

	selfobj.response.write("Henry  Herman  henry.herman@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1406754077")) 
	g.year=2014
	g.fname="Henry"
	g.lname="Herman"
	g.email="henry.herman@gmail.com" 
	g.address="984 Kiely Blvd Unit L" 
	g.city="Santa Clara" 
	g.phone="(714) 697-2298" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#62 

	selfobj.response.write("Susan  Hoey  susanhoey5@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1395412809")) 
	g.year=2014
	g.fname="Susan"
	g.lname="Hoey"
	g.email="susanhoey5@gmail.com" 
	g.address="13831 Campo Vista Lane" 
	g.city="Los Altos Hills" 
	g.phone="(650) 996-5325" 
	g.ntrp="F" 
	g.mtype="NRS" 
	g.put()
#63 

	selfobj.response.write("Pamela  Hoggatt  queenb_95051@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1391656513")) 
	g.year=2014
	g.fname="Pamela"
	g.lname="Hoggatt"
	g.email="queenb_95051@yahoo.com" 
	g.address="3070 Dibble Court" 
	g.city="Santa Clara" 
	g.phone="(408) 243-4381" 
	g.ntrp="F3.0" 
	g.mtype="RF_" 
	g.put()
#64 

	selfobj.response.write("Herta  Hoggatt  queenb_95051@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1391656590")) 
	g.year=2014
	g.fname="Herta"
	g.lname="Hoggatt"
	g.email="queenb_95051@yahoo.com" 
	g.address="3070 Dibble Court" 
	g.city="Santa Clara" 
	g.phone="(408) 243-4381" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#65 

	selfobj.response.write("Jeanette  Hoggatt  queenb_95051@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1391656436")) 
	g.year=2014
	g.fname="Jeanette"
	g.lname="Hoggatt"
	g.email="queenb_95051@yahoo.com" 
	g.address="3070 Dibble Court" 
	g.city="Santa Clara" 
	g.phone="(408) 243-4381" 
	g.ntrp="F3.5" 
	g.mtype="RF" 
	g.put()
#66 

	selfobj.response.write("Rosemary  Hopkins  rosemarh@hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1405138807")) 
	g.year=2014
	g.fname="Rosemary"
	g.lname="Hopkins"
	g.email="rosemarh@hotmail.com" 
	g.address="920 Laurel Glen Drive" 
	g.city="Palo Alto" 
	g.phone="(650) 948-0827" 
	g.ntrp="F" 
	g.mtype="NRS" 
	g.put()
#67 

	selfobj.response.write("Mihoko  Hosoi  mihoko.hosoi@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1392797429")) 
	g.year=2014
	g.fname="Mihoko"
	g.lname="Hosoi"
	g.email="mihoko.hosoi@gmail.com" 
	g.address="600 Rainbow Dr. Apt. 108" 
	g.city="Mountain View" 
	g.phone="(650) 526-8623" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#68 

	selfobj.response.write("Norma  Hughes  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2014
	g.fname="Norma"
	g.lname="Hughes"
	g.email="" 
	g.address="598 Bancroft St." 
	g.city="Santa Clara" 
	g.phone="(408) 296-1271" 
	g.ntrp="F2.5" 
	g.mtype="RS" 
	g.put()
#69 

	selfobj.response.write("Gabriel  Ibarra  gubbypix@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1392697060")) 
	g.year=2014
	g.fname="Gabriel"
	g.lname="Ibarra"
	g.email="gubbypix@yahoo.com" 
	g.address="" 
	g.city="Santa Clara" 
	g.phone="() -" 
	g.ntrp="M4.5" 
	g.mtype="RF" 
	g.put()
#70 

	selfobj.response.write("Akari  Ikeda  aikeda14@Yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1393143475")) 
	g.year=2014
	g.fname="Akari"
	g.lname="Ikeda"
	g.email="aikeda14@Yahoo.com" 
	g.address="1396 Lafayette St" 
	g.city="Santa Clara" 
	g.phone="(408) 916-7875" 
	g.ntrp="F4.5" 
	g.mtype="RS" 
	g.put()
#71 

	selfobj.response.write("Robert  Inocencio  hover_1518@hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1396087984")) 
	g.year=2014
	g.fname="Robert"
	g.lname="Inocencio"
	g.email="hover_1518@hotmail.com" 
	g.address="690 Whitewater Court," 
	g.city="San Jose" 
	g.phone="(408) 876-7682" 
	g.ntrp="M4.5" 
	g.mtype="NRS" 
	g.put()
#72 

	selfobj.response.write("Nicole  Isaacson  aliceisaacson@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1392617594")) 
	g.year=2014
	g.fname="Nicole"
	g.lname="Isaacson"
	g.email="aliceisaacson@yahoo.com" 
	g.address="513 Hickory Place" 
	g.city="Santa Clara" 
	g.phone="(408) 247-0343" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#73 

	selfobj.response.write("Mark  Isaacson  aliceisaacson@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1392617545")) 
	g.year=2014
	g.fname="Mark"
	g.lname="Isaacson"
	g.email="aliceisaacson@yahoo.com" 
	g.address="513 Hickory Place" 
	g.city="Santa Clara" 
	g.phone="(408) 247-0343" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#74 

	selfobj.response.write("Matthew  Isaacson  aliceisaacson@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1392617570")) 
	g.year=2014
	g.fname="Matthew"
	g.lname="Isaacson"
	g.email="aliceisaacson@yahoo.com" 
	g.address="513 Hickory Place" 
	g.city="Santa Clara" 
	g.phone="(408) 247-0343" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#75 

	selfobj.response.write("Alice  Isaacson  aliceisaacson@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1392616936")) 
	g.year=2014
	g.fname="Alice"
	g.lname="Isaacson"
	g.email="aliceisaacson@yahoo.com" 
	g.address="513 Hickory Place" 
	g.city="Santa Clara" 
	g.phone="(408) 247-0343" 
	g.ntrp="F3.5" 
	g.mtype="RF" 
	g.put()
#76 

	selfobj.response.write("Taryn  Ishida  tarynishida@Gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1393198990")) 
	g.year=2014
	g.fname="Taryn"
	g.lname="Ishida"
	g.email="tarynishida@Gmail.com" 
	g.address="95 Hobson St 3A" 
	g.city="San Jose" 
	g.phone="(808) 294-7065" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#77 

	selfobj.response.write("Megan  Jellinek  megan.anne@mac.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1410396714")) 
	g.year=2014
	g.fname="Megan"
	g.lname="Jellinek"
	g.email="megan.anne@mac.com" 
	g.address="321 Bachman Avenue" 
	g.city="Los Gatos" 
	g.phone="(408) 410-3208" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#78 

	selfobj.response.write("Vicky  Jha  vicks_jha@yahoo.co.in")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1396161138")) 
	g.year=2014
	g.fname="Vicky"
	g.lname="Jha"
	g.email="vicks_jha@yahoo.co.in" 
	g.address="4349 Renaissance Dr" 
	g.city="San Jose" 
	g.phone="(214) 600-2346" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#79 

	selfobj.response.write("Tom  Jiang  lzhang83713@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1405148250")) 
	g.year=2014
	g.fname="Tom"
	g.lname="Jiang"
	g.email="lzhang83713@yahoo.com" 
	g.address="460 Norwood Circle" 
	g.city="Santa Clara" 
	g.phone="(208) 939-2835" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#80 

	selfobj.response.write("Adam  Jiang  lzhang83713@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1405148293")) 
	g.year=2014
	g.fname="Adam"
	g.lname="Jiang"
	g.email="lzhang83713@yahoo.com" 
	g.address="460 Norwood Circle" 
	g.city="Santa Clara" 
	g.phone="(208) 939-2835" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#81 

	selfobj.response.write("Robert  Jiang  lzhang83713@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1405148315")) 
	g.year=2014
	g.fname="Robert"
	g.lname="Jiang"
	g.email="lzhang83713@yahoo.com" 
	g.address="460 Norwood Circle" 
	g.city="Santa Clara" 
	g.phone="(208) 939-2835" 
	g.ntrp="M4.0" 
	g.mtype="RF_" 
	g.put()
#82 

	selfobj.response.write("Mihoko  Jimbo  andyjim@rj9.so.net.ne.jp")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1400601447")) 
	g.year=2014
	g.fname="Mihoko"
	g.lname="Jimbo"
	g.email="andyjim@rj9.so.net.ne.jp" 
	g.address="954 Kiely Blvd #8" 
	g.city="Santa Clara" 
	g.phone="(408) 393-5333" 
	g.ntrp="F4.5" 
	g.mtype="RF" 
	g.put()
#83 

	selfobj.response.write("Takanori  Jimbo  andyjim@rj9.so.net.ne.jp")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1400601701")) 
	g.year=2014
	g.fname="Takanori"
	g.lname="Jimbo"
	g.email="andyjim@rj9.so.net.ne.jp" 
	g.address="954 Kiely Blvd #8" 
	g.city="Santa Clara" 
	g.phone="(408) 393-5333" 
	g.ntrp="M4.0" 
	g.mtype="RF_" 
	g.put()
#84 

	selfobj.response.write("Eiko  Johnson  eikoj@earthlink.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1405148208")) 
	g.year=2014
	g.fname="Eiko"
	g.lname="Johnson"
	g.email="eikoj@earthlink.net" 
	g.address="18112 Daves Ave" 
	g.city="Monte Sereno" 
	g.phone="(408) 354-1261" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#85 

	selfobj.response.write("Ambert  Jue  ambertj@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1396326612")) 
	g.year=2014
	g.fname="Ambert"
	g.lname="Jue"
	g.email="ambertj@gmail.com" 
	g.address="584 S Eden Ave" 
	g.city="Sunnyvale" 
	g.phone="(408) 431-9874" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#86 

	selfobj.response.write("Ellen  Juna  allgreen@ucla.edu")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1405138430")) 
	g.year=2014
	g.fname="Ellen"
	g.lname="Juna"
	g.email="allgreen@ucla.edu" 
	g.address="550 Moreland Way Apt 2403" 
	g.city="Santa Clara" 
	g.phone="(320) 576-1310" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#87 

	selfobj.response.write("Balaji  Kakkadasam  krbalaji@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1401333777")) 
	g.year=2014
	g.fname="Balaji"
	g.lname="Kakkadasam"
	g.email="krbalaji@gmail.com" 
	g.address="1933 Hillebrant Place" 
	g.city="Santa Clara" 
	g.phone="(469) 955-7827" 
	g.ntrp="M" 
	g.mtype="RF" 
	g.put()
#88 

	selfobj.response.write("Jacqueline  Kerkhove  JKerkhove@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1392659469")) 
	g.year=2014
	g.fname="Jacqueline"
	g.lname="Kerkhove"
	g.email="JKerkhove@gmail.com" 
	g.address="755 Santa Paula Ave" 
	g.city="Sunnyvale" 
	g.phone="(408) 499-6233" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#89 

	selfobj.response.write("James  Kern  jhkern@hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1405140618")) 
	g.year=2014
	g.fname="James"
	g.lname="Kern"
	g.email="jhkern@hotmail.com" 
	g.address="1330 Warner" 
	g.city="Sunnyvale" 
	g.phone="(650) 465-9009" 
	g.ntrp="M4" 
	g.mtype="NRS" 
	g.put()
#90 

	selfobj.response.write("Hemalata  Khiani  sanjayvaswani@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1402340931")) 
	g.year=2014
	g.fname="Hemalata"
	g.lname="Khiani"
	g.email="sanjayvaswani@yahoo.com" 
	g.address="2181 Esperanca Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 666-2302" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#91 

	selfobj.response.write("Sang Gyum  Kim  sanggyum.kim@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1395717658")) 
	g.year=2014
	g.fname="Sang Gyum"
	g.lname="Kim"
	g.email="sanggyum.kim@gmail.com" 
	g.address="3750 Miraverde Ct APT139" 
	g.city="Santa Clara" 
	g.phone="(510) 926-2837" 
	g.ntrp="M4.5" 
	g.mtype="RS" 
	g.put()
#92 

	selfobj.response.write("Soo  Kim  skimmy000@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1392795415")) 
	g.year=2014
	g.fname="Soo"
	g.lname="Kim"
	g.email="skimmy000@yahoo.com" 
	g.address="2968 Moorpark Avenue #11" 
	g.city="San Jose" 
	g.phone="(650) 996-3613" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#93 

	selfobj.response.write("Sayaka  Kishino  ksh_kishino@hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1396567262")) 
	g.year=2014
	g.fname="Sayaka"
	g.lname="Kishino"
	g.email="ksh_kishino@hotmail.com" 
	g.address="1173 Susan Way" 
	g.city="Sunnyvale" 
	g.phone="(408) 773-0659" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#94 

	selfobj.response.write("Sayaka  Kobayashi  sayaka.kobayashi0325@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1395977638")) 
	g.year=2014
	g.fname="Sayaka"
	g.lname="Kobayashi"
	g.email="sayaka.kobayashi0325@gmail.com" 
	g.address="25 Rio Robles East #428" 
	g.city="San Jose" 
	g.phone="(408) 489-3357" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#95 

	selfobj.response.write("Fran  Kristofferson  franmavia@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1405141037")) 
	g.year=2014
	g.fname="Fran"
	g.lname="Kristofferson"
	g.email="franmavia@yahoo.com" 
	g.address="4 Rosevelt Circle" 
	g.city="Palo Alto" 
	g.phone="() -" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#96 

	selfobj.response.write("Hosoon  Ku  hosoonku@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1395554694")) 
	g.year=2014
	g.fname="Hosoon"
	g.lname="Ku"
	g.email="hosoonku@yahoo.com" 
	g.address="3959 Veritas Way" 
	g.city="San Ramon" 
	g.phone="(925) 997-3927" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#97 

	selfobj.response.write("Tony  Lacy-Thompson  LT1GB@aol.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1396220660")) 
	g.year=2014
	g.fname="Tony"
	g.lname="Lacy-Thompson"
	g.email="LT1GB@aol.com" 
	g.address="548 Crawford Dr" 
	g.city="Sunnyvale" 
	g.phone="(408) 398-6284" 
	g.ntrp="M4.5" 
	g.mtype="NRS" 
	g.put()
#98 

	selfobj.response.write("Hang  Lee  lee.hang@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1405141275")) 
	g.year=2014
	g.fname="Hang"
	g.lname="Lee"
	g.email="lee.hang@yahoo.com" 
	g.address="4558 Cheeney St" 
	g.city="Santa Clara" 
	g.phone="(408) 506-2089" 
	g.ntrp="M" 
	g.mtype="RF" 
	g.put()
#99 

	selfobj.response.write("Nathan  Lee  lee.hang@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1405141405")) 
	g.year=2014
	g.fname="Nathan"
	g.lname="Lee"
	g.email="lee.hang@yahoo.com" 
	g.address="4558 Cheeney St" 
	g.city="Santa Clara" 
	g.phone="(408) 506-2089" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#100 

	selfobj.response.write("Jaclyn  Lee  jn.lee295@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1412319628")) 
	g.year=2014
	g.fname="Jaclyn"
	g.lname="Lee"
	g.email="jn.lee295@gmail.com" 
	g.address="1172 Morse Avenue" 
	g.city="Sunnyvale" 
	g.phone="(408) 470-9863" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#101 

	selfobj.response.write("John  Lee  lbongsun@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1396153778")) 
	g.year=2014
	g.fname="John"
	g.lname="Lee"
	g.email="lbongsun@gmail.com" 
	g.address="10175 Parkwood Dr. #8" 
	g.city="Cupertino" 
	g.phone="(408) 996-7262" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#102 

	selfobj.response.write("Lisa  Lee  lee.hang@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1405141430")) 
	g.year=2014
	g.fname="Lisa"
	g.lname="Lee"
	g.email="lee.hang@yahoo.com" 
	g.address="4558 Cheeney St" 
	g.city="Santa Clara" 
	g.phone="(408) 506-2089" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#103 

	selfobj.response.write("Brandon  Lee  lee.hang@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1405141383")) 
	g.year=2014
	g.fname="Brandon"
	g.lname="Lee"
	g.email="lee.hang@yahoo.com" 
	g.address="4558 Cheeney St" 
	g.city="Santa Clara" 
	g.phone="(408) 506-2089" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#104 

	selfobj.response.write("Joy  Lenz  joy.lenz@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1410595409")) 
	g.year=2014
	g.fname="Joy"
	g.lname="Lenz"
	g.email="joy.lenz@sbcglobal.net" 
	g.address="5938 Country Club Parkway" 
	g.city="San Jose" 
	g.phone="(408) 705-5121" 
	g.ntrp="F4.5" 
	g.mtype="NRF" 
	g.put()
#105 

	selfobj.response.write("Ben  Lewis  benlewissf@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1405141550")) 
	g.year=2014
	g.fname="Ben"
	g.lname="Lewis"
	g.email="benlewissf@gmail.com" 
	g.address="2256 Dianne Dr" 
	g.city="Santa Clara" 
	g.phone="(415) 902-4787" 
	g.ntrp="M4.0" 
	g.mtype="RS" 
	g.put()
#106 

	selfobj.response.write("Andrew  Li  ahklpharmd@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1395519704")) 
	g.year=2014
	g.fname="Andrew"
	g.lname="Li"
	g.email="ahklpharmd@gmail.com" 
	g.address="2580 Homestead Rd Apt 6203" 
	g.city="Santa Clara, CA" 
	g.phone="(408) 596-3618" 
	g.ntrp="M3.5" 
	g.mtype="RF" 
	g.put()
#107 

	selfobj.response.write("Erin  Linke  alinke@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1405142149")) 
	g.year=2014
	g.fname="Erin"
	g.lname="Linke"
	g.email="alinke@yahoo.com" 
	g.address="1285 Main St" 
	g.city="Santa Clara" 
	g.phone="(408) 892-1718" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#108 

	selfobj.response.write("Cleo  Linke  alinke@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1405142218")) 
	g.year=2014
	g.fname="Cleo"
	g.lname="Linke"
	g.email="alinke@yahoo.com" 
	g.address="1285 Main St" 
	g.city="Santa Clara" 
	g.phone="(408) 892-1718" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#109 

	selfobj.response.write("Al  Linke  alinke@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1405141837")) 
	g.year=2014
	g.fname="Al"
	g.lname="Linke"
	g.email="alinke@yahoo.com" 
	g.address="1285 Main St" 
	g.city="Santa Clara" 
	g.phone="(408) 892-1718" 
	g.ntrp="M4.0" 
	g.mtype="RF" 
	g.put()
#110 

	selfobj.response.write("Mina  Linke  alinke@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1405142171")) 
	g.year=2014
	g.fname="Mina"
	g.lname="Linke"
	g.email="alinke@yahoo.com" 
	g.address="1285 Main St" 
	g.city="Santa Clara" 
	g.phone="(408) 892-1718" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#111 

	selfobj.response.write("Leila  Linke  alinke@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1405142195")) 
	g.year=2014
	g.fname="Leila"
	g.lname="Linke"
	g.email="alinke@yahoo.com" 
	g.address="1285 Main St" 
	g.city="Santa Clara" 
	g.phone="(408) 892-1718" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#112 

	selfobj.response.write("Marshall  Madamba  mmadamba@redshift.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1392940267")) 
	g.year=2014
	g.fname="Marshall"
	g.lname="Madamba"
	g.email="mmadamba@redshift.com" 
	g.address="350 E TAYLOR ST, APT 6114" 
	g.city="SAN JOSE" 
	g.phone="(408) 691-5652" 
	g.ntrp="M3.5" 
	g.mtype="NRF" 
	g.put()
#113 

	selfobj.response.write("Chris  Madsen  chrismadsen2112@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1397257755")) 
	g.year=2014
	g.fname="Chris"
	g.lname="Madsen"
	g.email="chrismadsen2112@gmail.com" 
	g.address="1560 Camden Village Circle" 
	g.city="San Jose" 
	g.phone="(408) 489-3993" 
	g.ntrp="M4.5" 
	g.mtype="NRS" 
	g.put()
#114 

	selfobj.response.write("Ronald  Mah  ronaldmah@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1396629389")) 
	g.year=2014
	g.fname="Ronald"
	g.lname="Mah"
	g.email="ronaldmah@sbcglobal.net" 
	g.address="2495 Tasso St." 
	g.city="Palo Alto" 
	g.phone="(650) 303-7114" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#115 

	selfobj.response.write("Sujatha  Mandava  sjt_m@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1412966785")) 
	g.year=2014
	g.fname="Sujatha"
	g.lname="Mandava"
	g.email="sjt_m@yahoo.com" 
	g.address="862 Bremerton Drive" 
	g.city="Sunnyvale" 
	g.phone="(408) 832-2315" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#116 

	selfobj.response.write("Michael  Mansour  michael@themansours.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1398296999")) 
	g.year=2014
	g.fname="Michael"
	g.lname="Mansour"
	g.email="michael@themansours.com" 
	g.address="4416 Grimsby Dr" 
	g.city="San Jose" 
	g.phone="(408) 332-2226" 
	g.ntrp="M" 
	g.mtype="NRS" 
	g.put()
#117 

	selfobj.response.write("Luzmaria  Martinez  katsulas@aol.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1392940581")) 
	g.year=2014
	g.fname="Luzmaria"
	g.lname="Martinez"
	g.email="katsulas@aol.com" 
	g.address="350 E TAYLOR ST, APT 6114" 
	g.city="SAN JOSE" 
	g.phone="(408) 691-5758" 
	g.ntrp="F3.5" 
	g.mtype="NRF_" 
	g.put()
#118 

	selfobj.response.write("Helen  Matsumoto  geetennis@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1392003380")) 
	g.year=2014
	g.fname="Helen"
	g.lname="Matsumoto"
	g.email="geetennis@yahoo.com" 
	g.address="1247 Redoaks Drive" 
	g.city="San Jose" 
	g.phone="(408) 248-7922" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#119 

	selfobj.response.write("Anna  Matthiasson  a_matthiasson@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1410501434")) 
	g.year=2014
	g.fname="Anna"
	g.lname="Matthiasson"
	g.email="a_matthiasson@yahoo.com" 
	g.address="16298 Oleander Avenue" 
	g.city="Los Gatos" 
	g.phone="(408) 203-9657" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#120 

	selfobj.response.write("Valerie  McCarthy  valeriebays@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1405144415")) 
	g.year=2014
	g.fname="Valerie"
	g.lname="McCarthy"
	g.email="valeriebays@gmail.com" 
	g.address="471 Tanoak Drive" 
	g.city="Santa Clara" 
	g.phone="(408) 248-7843" 
	g.ntrp="F" 
	g.mtype="RS" 
	g.put()
#121 

	selfobj.response.write("Colleen  McCullough  collmc1999@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1405145575")) 
	g.year=2014
	g.fname="Colleen"
	g.lname="McCullough"
	g.email="collmc1999@yahoo.com" 
	g.address="713 Astor Ct" 
	g.city="Mountain View" 
	g.phone="(650) 996-0432" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#122 

	selfobj.response.write("Trevor  McGuire  temcguir@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1393997137")) 
	g.year=2014
	g.fname="Trevor"
	g.lname="McGuire"
	g.email="temcguir@gmail.com" 
	g.address="900 Pepper Tree Lane #212" 
	g.city="Santa Clara" 
	g.phone="(707) 799-0577" 
	g.ntrp="M3.0" 
	g.mtype="RF" 
	g.put()
#123 

	selfobj.response.write("Christi  McNay  cmmcnay@comcast.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1405144510")) 
	g.year=2014
	g.fname="Christi"
	g.lname="McNay"
	g.email="cmmcnay@comcast.net" 
	g.address="14131 Azalea Way" 
	g.city="Los Gatos" 
	g.phone="(408) 454-1548" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#124 

	selfobj.response.write("Ingeborg  Melcher  ingeborgmelcher@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1405148208")) 
	g.year=2014
	g.fname="Ingeborg"
	g.lname="Melcher"
	g.email="ingeborgmelcher@yahoo.com" 
	g.address="808 Partridge Ave" 
	g.city="Menlo Park" 
	g.phone="(602) 432-2304" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#125 

	selfobj.response.write("Nathan Michael  Mertz  tennis61911@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1405225977")) 
	g.year=2014
	g.fname="Nathan Michael"
	g.lname="Mertz"
	g.email="tennis61911@yahoo.com" 
	g.address="2071 Bowers Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 469-0521" 
	g.ntrp="M4.0" 
	g.mtype="RS" 
	g.put()
#126 

	selfobj.response.write("Judy  Mihanovic  judymihan@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1395377806")) 
	g.year=2014
	g.fname="Judy"
	g.lname="Mihanovic"
	g.email="judymihan@sbcglobal.net" 
	g.address="25000 OKeefe Lane" 
	g.city="Los Altos Hills" 
	g.phone="(650) 949-3608" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#127 

	selfobj.response.write("Yuko  Mihara  miharayuko@hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1395095975")) 
	g.year=2014
	g.fname="Yuko"
	g.lname="Mihara"
	g.email="miharayuko@hotmail.com" 
	g.address="20208 Northwest Sq" 
	g.city="Cupertino" 
	g.phone="(408) 393-5333" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#128 

	selfobj.response.write("Vivian  Miller  millervivian7@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1412966974")) 
	g.year=2014
	g.fname="Vivian"
	g.lname="Miller"
	g.email="millervivian7@gmail.com" 
	g.address="1290 Mandarin Dr" 
	g.city="Sunnyvale" 
	g.phone="(805) 215-8021" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#129 

	selfobj.response.write("Samantha  Milner  samantha.milner@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1406753903")) 
	g.year=2014
	g.fname="Samantha"
	g.lname="Milner"
	g.email="samantha.milner@gmail.com" 
	g.address="984 Kiely Blvd Unit L" 
	g.city="Santa Clara" 
	g.phone="(661) 713-9869" 
	g.ntrp="F3.5" 
	g.mtype="RF" 
	g.put()
#130 

	selfobj.response.write("Veronique  Miro  vhmiro@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1405144589")) 
	g.year=2014
	g.fname="Veronique"
	g.lname="Miro"
	g.email="vhmiro@yahoo.com" 
	g.address="1795 Marich Way" 
	g.city="Mountain View" 
	g.phone="(650) 787-6601" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#131 

	selfobj.response.write("Akiyo  Mizutani  kxb00454@nifty.ne.jp")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1397108646")) 
	g.year=2014
	g.fname="Akiyo"
	g.lname="Mizutani"
	g.email="kxb00454@nifty.ne.jp" 
	g.address="119 Arcadia Avenue" 
	g.city="Santa Clara" 
	g.phone="(408) 921-6578" 
	g.ntrp="F3.5" 
	g.mtype="RF" 
	g.put()
#132 

	selfobj.response.write("Tohru  Mizutani  kxb00454@nifty.ne.jp")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1397108901")) 
	g.year=2014
	g.fname="Tohru"
	g.lname="Mizutani"
	g.email="kxb00454@nifty.ne.jp" 
	g.address="119 Arcadia Avenue" 
	g.city="Santa Clara" 
	g.phone="(408) 921-6578" 
	g.ntrp="M4.0" 
	g.mtype="RF_" 
	g.put()
#133 

	selfobj.response.write("Roy  Molseed  roy.molseed@vta.org")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1392696958")) 
	g.year=2014
	g.fname="Roy"
	g.lname="Molseed"
	g.email="roy.molseed@vta.org" 
	g.address="2550 Blue Rock Ct" 
	g.city="San Jose" 
	g.phone="(408) 580-6396" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#134 

	selfobj.response.write("Matt  Montana  montanatopspin@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1398387989")) 
	g.year=2014
	g.fname="Matt"
	g.lname="Montana"
	g.email="montanatopspin@yahoo.com" 
	g.address="3440 El Camino Real #316" 
	g.city="Santa Clara" 
	g.phone="(408) 768-3515" 
	g.ntrp="M4.5" 
	g.mtype="RF_" 
	g.put()
#135 

	selfobj.response.write("Claudia  Moody  claudiammoody@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1394392514")) 
	g.year=2014
	g.fname="Claudia"
	g.lname="Moody"
	g.email="claudiammoody@gmail.com" 
	g.address="900 Pepper Tree Lane #212" 
	g.city="Santa Clara" 
	g.phone="(408) 616-9680" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#136 

	selfobj.response.write("Francisca  Mortensen  Back40@Creative-services.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1408549971")) 
	g.year=2014
	g.fname="Francisca"
	g.lname="Mortensen"
	g.email="Back40@Creative-services.com" 
	g.address="1704 Harrison st" 
	g.city="Santa Clara" 
	g.phone="(408) 410-7836" 
	g.ntrp="F3.0" 
	g.mtype="RS" 
	g.put()
#137 

	selfobj.response.write("Pradeep  Nair  pradeepn1@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1396306272")) 
	g.year=2014
	g.fname="Pradeep"
	g.lname="Nair"
	g.email="pradeepn1@gmail.com" 
	g.address="1921 Garzoni Place" 
	g.city="Santa Clara" 
	g.phone="(408) 839-1703" 
	g.ntrp="M4.0" 
	g.mtype="RS" 
	g.put()
#138 

	selfobj.response.write("Shiv  Natarajan  shiv.natarajan@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1393961102")) 
	g.year=2014
	g.fname="Shiv"
	g.lname="Natarajan"
	g.email="shiv.natarajan@yahoo.com" 
	g.address="4813 Verbena Way" 
	g.city="San Jose" 
	g.phone="(408) 480-1044" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#139 

	selfobj.response.write("Keith  Ng  kng@ix.netcom.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1392696725")) 
	g.year=2014
	g.fname="Keith"
	g.lname="Ng"
	g.email="kng@ix.netcom.com" 
	g.address="" 
	g.city="San Jose" 
	g.phone="(  )   -" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#140 

	selfobj.response.write("Lloyd  Ngo  lloydngo@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1405145186")) 
	g.year=2014
	g.fname="Lloyd"
	g.lname="Ngo"
	g.email="lloydngo@yahoo.com" 
	g.address="3399 Victoria Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 891-1154" 
	g.ntrp="M3.5" 
	g.mtype="RS" 
	g.put()
#141 

	selfobj.response.write("Nguyen  Nguyen  ngunguye@Icloud.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1410910571")) 
	g.year=2014
	g.fname="Nguyen"
	g.lname="Nguyen"
	g.email="ngunguye@Icloud.com" 
	g.address="5403 Canyon  Hills Lane" 
	g.city="San Jose" 
	g.phone="(408) 813-3555" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#142 

	selfobj.response.write("Thi  Nguyen  baothiy2k@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1396567045")) 
	g.year=2014
	g.fname="Thi"
	g.lname="Nguyen"
	g.email="baothiy2k@yahoo.com" 
	g.address="1925 White Oaks Rd" 
	g.city="Campbell" 
	g.phone="(408) 897-9677" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#143 

	selfobj.response.write("Chuong  Nguyen  alache@rocketmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1395431433")) 
	g.year=2014
	g.fname="Chuong"
	g.lname="Nguyen"
	g.email="alache@rocketmail.com" 
	g.address="2421 Mission college Blvd" 
	g.city="santa clara" 
	g.phone="(408) 992-1858" 
	g.ntrp="M3.5" 
	g.mtype="RS" 
	g.put()
#144 

	selfobj.response.write("Junko  Ohoka  junko.ohoka@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1393313946")) 
	g.year=2014
	g.fname="Junko"
	g.lname="Ohoka"
	g.email="junko.ohoka@gmail.com" 
	g.address="1007 Bryant Way" 
	g.city="Sunnyvale" 
	g.phone="(408) 582-4035" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#145 

	selfobj.response.write("Roger  Okamoto  tennis.mutt@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1394863787")) 
	g.year=2014
	g.fname="Roger"
	g.lname="Okamoto"
	g.email="tennis.mutt@gmail.com" 
	g.address="1349 Mariposa Ave" 
	g.city="San Jose" 
	g.phone="(510) 878-4404" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#146 

	selfobj.response.write("Rachel  Okazaki  Japanesegrace@Gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1393730875")) 
	g.year=2014
	g.fname="Rachel"
	g.lname="Okazaki"
	g.email="Japanesegrace@Gmail.com" 
	g.address="814 Daffodil Way" 
	g.city="San Jose" 
	g.phone="(408) 984-7697" 
	g.ntrp="F4.0" 
	g.mtype="NRF_" 
	g.put()
#147 

	selfobj.response.write("Matt  Okazaki  ally.taylor87@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1405145786")) 
	g.year=2014
	g.fname="Matt"
	g.lname="Okazaki"
	g.email="ally.taylor87@gmail.com" 
	g.address="2851 Homestead Rd #308" 
	g.city="Santa Clara" 
	g.phone="(763) 607-7449" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#148 

	selfobj.response.write("Ally  Okazaki  ally.taylor87@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1405145719")) 
	g.year=2014
	g.fname="Ally"
	g.lname="Okazaki"
	g.email="ally.taylor87@gmail.com" 
	g.address="2851 Homestead Rd #308" 
	g.city="Santa Clara" 
	g.phone="(763) 607-7449" 
	g.ntrp="F4.5" 
	g.mtype="RF" 
	g.put()
#149 

	selfobj.response.write("Ken  Okazaki  Okaken1@Aol.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1393730558")) 
	g.year=2014
	g.fname="Ken"
	g.lname="Okazaki"
	g.email="Okaken1@Aol.com" 
	g.address="814 Daffodil Way" 
	g.city="San Jose" 
	g.phone="(408) 984-7697" 
	g.ntrp="M4.0" 
	g.mtype="NRF" 
	g.put()
#150 

	selfobj.response.write("Chester  Okuno  Chesterokuno@Gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1398572778")) 
	g.year=2014
	g.fname="Chester"
	g.lname="Okuno"
	g.email="Chesterokuno@Gmail.com" 
	g.address="3410 Laguna" 
	g.city="Santa Clara" 
	g.phone="(408) 489-3142" 
	g.ntrp="M4.0" 
	g.mtype="RF" 
	g.put()
#151 

	selfobj.response.write("Noriko  Osawa  noriko_osawa@hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1405146008")) 
	g.year=2014
	g.fname="Noriko"
	g.lname="Osawa"
	g.email="noriko_osawa@hotmail.com" 
	g.address="157 Kensington Way" 
	g.city="Los Gatos" 
	g.phone="(408) 401-9977" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#152 

	selfobj.response.write("Karen  Panian  Kpanian@Comcast.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1408549976")) 
	g.year=2014
	g.fname="Karen"
	g.lname="Panian"
	g.email="Kpanian@Comcast.net" 
	g.address="1704  Harrison st." 
	g.city="Santa Clara" 
	g.phone="(408) 313-8883" 
	g.ntrp="F3.5" 
	g.mtype="RS" 
	g.put()
#153 

	selfobj.response.write("Vickie  Panova  vickie200555@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1405146156")) 
	g.year=2014
	g.fname="Vickie"
	g.lname="Panova"
	g.email="vickie200555@yahoo.com" 
	g.address="979 La Mesa Terrace Apt D" 
	g.city="Sunnyale" 
	g.phone="(408) 455-3922" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#154 

	selfobj.response.write("Sridevi  Parise  srideviparise@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1393185653")) 
	g.year=2014
	g.fname="Sridevi"
	g.lname="Parise"
	g.email="srideviparise@gmail.com" 
	g.address="" 
	g.city="Sunnyvale" 
	g.phone="() -" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#155 

	selfobj.response.write("John  Pattinson  john_pattinson@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1405146319")) 
	g.year=2014
	g.fname="John"
	g.lname="Pattinson"
	g.email="john_pattinson@yahoo.com" 
	g.address="1574 Finch Way" 
	g.city="Sunnyale" 
	g.phone="(408) 733-9070" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#156 

	selfobj.response.write("Lisa  Pawloski  LPJOY1109@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1395449825")) 
	g.year=2014
	g.fname="Lisa"
	g.lname="Pawloski"
	g.email="LPJOY1109@gmail.com" 
	g.address="1803 Van Buren" 
	g.city="Mountain View" 
	g.phone="(650) 793-5260" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#157 

	selfobj.response.write("Christine  Peters  ck.peters@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1394146051")) 
	g.year=2014
	g.fname="Christine"
	g.lname="Peters"
	g.email="ck.peters@sbcglobal.net" 
	g.address="1390 Saddle Rack St. #349" 
	g.city="San  Jose" 
	g.phone="(408) 921-1610" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#158 

	selfobj.response.write("Elisapeta  Peterson  peta.peterson@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1396567815")) 
	g.year=2014
	g.fname="Elisapeta"
	g.lname="Peterson"
	g.email="peta.peterson@sbcglobal.net" 
	g.address="13970 Saratoga Ave" 
	g.city="Saratoga" 
	g.phone="(408) 867-6947" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#159 

	selfobj.response.write("Yumiko  Pflaum  ypflaum@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1405146420")) 
	g.year=2014
	g.fname="Yumiko"
	g.lname="Pflaum"
	g.email="ypflaum@gmail.com" 
	g.address="1272 Alderbrook Lane" 
	g.city="San Jose" 
	g.phone="(408) 490-4527" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#160 

	selfobj.response.write("Bettye  Pham-Vo  bettyediem@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1392046013")) 
	g.year=2014
	g.fname="Bettye"
	g.lname="Pham-Vo"
	g.email="bettyediem@gmail.com" 
	g.address="3657 lisbon Ct." 
	g.city="San Jose" 
	g.phone="(408) 250-5658" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#161 

	selfobj.response.write("Balakumar  Rajendran  balakumar85@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1403635297")) 
	g.year=2014
	g.fname="Balakumar"
	g.lname="Rajendran"
	g.email="balakumar85@gmail.com" 
	g.address="1610 Nantucket Cir Apt 210" 
	g.city="Santa Clara" 
	g.phone="(513) 739-2747" 
	g.ntrp="M3.0" 
	g.mtype="RF" 
	g.put()
#162 

	selfobj.response.write("Jagannath  Rallapalli  rallapalli_jagan@hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1395858131")) 
	g.year=2014
	g.fname="Jagannath"
	g.lname="Rallapalli"
	g.email="rallapalli_jagan@hotmail.com" 
	g.address="807 Batista Dr" 
	g.city="San Jose" 
	g.phone="(408) 978-7576" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#163 

	selfobj.response.write("Vyass  Ramakrishnan  rvyass@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1397924847")) 
	g.year=2014
	g.fname="Vyass"
	g.lname="Ramakrishnan"
	g.email="rvyass@gmail.com" 
	g.address="2451 Mission College Blvd" 
	g.city="Santa Clara, CA" 
	g.phone="(469) 213-9145" 
	g.ntrp="M3.5" 
	g.mtype="RF" 
	g.put()
#164 

	selfobj.response.write("Aditya  Rawat  ad.rawat30@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1405148208")) 
	g.year=2014
	g.fname="Aditya"
	g.lname="Rawat"
	g.email="ad.rawat30@gmail.com" 
	g.address="4301 Renaissance Dr #306" 
	g.city="San Jose" 
	g.phone="(219) 964-5051" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#165 

	selfobj.response.write("Stacey  Reitmeir  reitmeir@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1399267655")) 
	g.year=2014
	g.fname="Stacey"
	g.lname="Reitmeir"
	g.email="reitmeir@sbcglobal.net" 
	g.address="xxxxx" 
	g.city="Los Altos" 
	g.phone="(650) xxx-xxxx" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#166 

	selfobj.response.write("Larry  Rinek  lrinek@aol.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1405146729")) 
	g.year=2014
	g.fname="Larry"
	g.lname="Rinek"
	g.email="lrinek@aol.com" 
	g.address="80 Gilbert" 
	g.city="Santa Clara" 
	g.phone="(408) 248-3088" 
	g.ntrp="M" 
	g.mtype="RS" 
	g.put()
#167 

	selfobj.response.write("Jan-Marie  Robinson  jan.marie.r@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1395846666")) 
	g.year=2014
	g.fname="Jan-Marie"
	g.lname="Robinson"
	g.email="jan.marie.r@gmail.com" 
	g.address="353 Lakeview Way" 
	g.city="Emerald Hills" 
	g.phone="(650) 520-4452" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#168 

	selfobj.response.write("Dolores  Salazar  kddsalazar@comcast.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1397405424")) 
	g.year=2014
	g.fname="Dolores"
	g.lname="Salazar"
	g.email="kddsalazar@comcast.net" 
	g.address="3376 Solano Ct." 
	g.city="Santa Clara" 
	g.phone="(408) 296-2379" 
	g.ntrp="F2.5" 
	g.mtype="RS" 
	g.put()
#169 

	selfobj.response.write("Ella  Samuels  ellasamuels@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1392830685")) 
	g.year=2014
	g.fname="Ella"
	g.lname="Samuels"
	g.email="ellasamuels@gmail.com" 
	g.address="1409 petal way" 
	g.city="San Jose" 
	g.phone="(408) 623-8789" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#170 

	selfobj.response.write("Shrithik  Sareddy  shrithik1@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1400801216")) 
	g.year=2014
	g.fname="Shrithik"
	g.lname="Sareddy"
	g.email="shrithik1@gmail.com" 
	g.address="2818 COZUMEL CIR" 
	g.city="SANTA CLARA" 
	g.phone="(727) 507-1969" 
	g.ntrp="M3.5" 
	g.mtype="RF_" 
	g.put()
#171 

	selfobj.response.write("Sudhakar  Sareddy  ssr824@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1400800700")) 
	g.year=2014
	g.fname="Sudhakar"
	g.lname="Sareddy"
	g.email="ssr824@gmail.com" 
	g.address="2818 COZUMEL CIR" 
	g.city="SANTA CLARA" 
	g.phone="(408) 755-9347" 
	g.ntrp="M3.5" 
	g.mtype="RF" 
	g.put()
#172 

	selfobj.response.write("Lewis  Satrijo  lsatrijo@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1405147286")) 
	g.year=2014
	g.fname="Lewis"
	g.lname="Satrijo"
	g.email="lsatrijo@yahoo.com" 
	g.address="2007 Heather Glen Dr" 
	g.city="San Jose" 
	g.phone="(408) 507-8064" 
	g.ntrp="M3.0" 
	g.mtype="NRS" 
	g.put()
#173 

	selfobj.response.write("Chris  Schubert  wcschubert@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1404081766")) 
	g.year=2014
	g.fname="Chris"
	g.lname="Schubert"
	g.email="wcschubert@yahoo.com" 
	g.address="3390  El Camino Real, # 108" 
	g.city="Santa Clara" 
	g.phone="(408) 230-5591" 
	g.ntrp="M4.0" 
	g.mtype="RS" 
	g.put()
#174 

	selfobj.response.write("Mei  See  meisee68@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1411701826")) 
	g.year=2014
	g.fname="Mei"
	g.lname="See"
	g.email="meisee68@yahoo.com" 
	g.address="1913 Magdalena Circle #109" 
	g.city="Santa Clara" 
	g.phone="(408) 480-1880" 
	g.ntrp="F3.0" 
	g.mtype="RS" 
	g.put()
#175 

	selfobj.response.write("Atsushi  Shirai  atst@hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1392696658")) 
	g.year=2014
	g.fname="Atsushi"
	g.lname="Shirai"
	g.email="atst@hotmail.com" 
	g.address="" 
	g.city="San Jose" 
	g.phone="(  )   -" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#176 

	selfobj.response.write("Ryan  Sin  jenny.rex@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1412970682")) 
	g.year=2014
	g.fname="Ryan"
	g.lname="Sin"
	g.email="jenny.rex@yahoo.com" 
	g.address="3220 Scott Blvd" 
	g.city="Santa Clara" 
	g.phone="(650) 793-2207" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#177 

	selfobj.response.write("Chauncey  Smith  chauncester@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1396288091")) 
	g.year=2014
	g.fname="Chauncey"
	g.lname="Smith"
	g.email="chauncester@gmail.com" 
	g.address="317 Toscana Way" 
	g.city="Hayward" 
	g.phone="(650) 924-2371" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#178 

	selfobj.response.write("Wanda  Soon  wsoon8@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1396449960")) 
	g.year=2014
	g.fname="Wanda"
	g.lname="Soon"
	g.email="wsoon8@yahoo.com" 
	g.address="130 Barneson Avenue, #8" 
	g.city="San Mateo" 
	g.phone="(415) 298-7098" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#179 

	selfobj.response.write("Susan  Stulz  sstulz@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1392696208")) 
	g.year=2014
	g.fname="Susan"
	g.lname="Stulz"
	g.email="sstulz@gmail.com" 
	g.address="" 
	g.city="Los Altos Hills" 
	g.phone="(  )   -" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#180 

	selfobj.response.write("David   Susnitzky  susnitzky@comcast.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1396844677")) 
	g.year=2014
	g.fname="David "
	g.lname="Susnitzky"
	g.email="susnitzky@comcast.net" 
	g.address="789 Cornell Drive" 
	g.city="Santa Clara" 
	g.phone="(408) 203-3412" 
	g.ntrp="M4.0" 
	g.mtype="RS" 
	g.put()
#181 

	selfobj.response.write("Tsuneko  Suzuki  nekochancat@aol.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1393185470")) 
	g.year=2014
	g.fname="Tsuneko"
	g.lname="Suzuki"
	g.email="nekochancat@aol.com" 
	g.address="" 
	g.city="Milpitas" 
	g.phone="() -" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#182 

	selfobj.response.write("Elizabeth (Betty)  Symonds  bsym2000@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1405147409")) 
	g.year=2014
	g.fname="Elizabeth (Betty)"
	g.lname="Symonds"
	g.email="bsym2000@yahoo.com" 
	g.address="1556 Rosecrest Terrace" 
	g.city="San Jose" 
	g.phone="(408) 287-7807" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#183 

	selfobj.response.write("Tomoe  Tajima  tomoetajima@earthlink.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1395436823")) 
	g.year=2014
	g.fname="Tomoe"
	g.lname="Tajima"
	g.email="tomoetajima@earthlink.net" 
	g.address="1007 Bryant Way #A" 
	g.city="Sunnyvale" 
	g.phone="(408) 963-3084" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#184 

	selfobj.response.write("Janet  Tallett  jttallett@comcast.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1393269234")) 
	g.year=2014
	g.fname="Janet"
	g.lname="Tallett"
	g.email="jttallett@comcast.net" 
	g.address="6 Daffodil Lane" 
	g.city="San Carlos" 
	g.phone="(650) 208-2655" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#185 

	selfobj.response.write("Minchene  Tang  jeanne_myriam@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1395537759")) 
	g.year=2014
	g.fname="Minchene"
	g.lname="Tang"
	g.email="jeanne_myriam@yahoo.com" 
	g.address="246 OKeefe Way" 
	g.city="Mountain View" 
	g.phone="(650) 814-9227" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#186 

	selfobj.response.write("Lourdes  Thevanayagam  namunk@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1411701753")) 
	g.year=2014
	g.fname="Lourdes"
	g.lname="Thevanayagam"
	g.email="namunk@yahoo.com" 
	g.address="1035A Alta Mira Dr" 
	g.city="Santa Clara" 
	g.phone="() -" 
	g.ntrp="F3.0" 
	g.mtype="RS" 
	g.put()
#187 

	selfobj.response.write("Thomas  Truong  thomas.g.truong@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1405147585")) 
	g.year=2014
	g.fname="Thomas"
	g.lname="Truong"
	g.email="thomas.g.truong@yahoo.com" 
	g.address="2167 Weston Pl" 
	g.city="Santa Clara" 
	g.phone="(408) 219-2377" 
	g.ntrp="M4.0" 
	g.mtype="RF" 
	g.put()
#188 

	selfobj.response.write("Ryan  Truong  thomas.g.truong@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1405147659")) 
	g.year=2014
	g.fname="Ryan"
	g.lname="Truong"
	g.email="thomas.g.truong@yahoo.com" 
	g.address="2167 Weston Pl" 
	g.city="Santa Clara" 
	g.phone="(408) 219-2377" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#189 

	selfobj.response.write("Nina  Tsuneda  ntsuneda@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1393186124")) 
	g.year=2014
	g.fname="Nina"
	g.lname="Tsuneda"
	g.email="ntsuneda@gmail.com" 
	g.address="" 
	g.city="Mountain View" 
	g.phone="() -" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#190 

	selfobj.response.write("Julie  Tsutsui  john.tsutsui@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1405147851")) 
	g.year=2014
	g.fname="Julie"
	g.lname="Tsutsui"
	g.email="john.tsutsui@gmail.com" 
	g.address="32 Wistaria Way" 
	g.city="Santa Clara" 
	g.phone="(408) 206-0496" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#191 

	selfobj.response.write("John  Tsutsui  john.tsutsui@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1405147803")) 
	g.year=2014
	g.fname="John"
	g.lname="Tsutsui"
	g.email="john.tsutsui@gmail.com" 
	g.address="32 Wistaria Way" 
	g.city="Santa Clara" 
	g.phone="(408) 206-0496" 
	g.ntrp="M4.0" 
	g.mtype="RF" 
	g.put()
#192 

	selfobj.response.write("Cary  Tucker  carywtucker@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1399064974")) 
	g.year=2014
	g.fname="Cary"
	g.lname="Tucker"
	g.email="carywtucker@gmail.com" 
	g.address="980 Kiely Blvd., Unit 323" 
	g.city="Santa Clara" 
	g.phone="(408) 239-7329" 
	g.ntrp="M2.5" 
	g.mtype="RS" 
	g.put()
#193 

	selfobj.response.write("Tracy  VanDenBerg  vandenberg.tl@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1410310190")) 
	g.year=2014
	g.fname="Tracy"
	g.lname="VanDenBerg"
	g.email="vandenberg.tl@gmail.com" 
	g.address="714 Astor Court" 
	g.city="Mountain View" 
	g.phone="(408) 242-0925" 
	g.ntrp="F3.0" 
	g.mtype="NRS" 
	g.put()
#194 

	selfobj.response.write("Preesha  Vaswani  sanjayvaswani@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1402341020")) 
	g.year=2014
	g.fname="Preesha"
	g.lname="Vaswani"
	g.email="sanjayvaswani@yahoo.com" 
	g.address="2181 Esperanca Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 666-2302" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#195 

	selfobj.response.write("Sanjay  Vaswani  sanjayvaswani@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1402340764")) 
	g.year=2014
	g.fname="Sanjay"
	g.lname="Vaswani"
	g.email="sanjayvaswani@yahoo.com" 
	g.address="2181 Esperanca Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 666-2302" 
	g.ntrp="M" 
	g.mtype="RF" 
	g.put()
#196 

	selfobj.response.write("Ryan  Ventura  loriv@me.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1392674105")) 
	g.year=2014
	g.fname="Ryan"
	g.lname="Ventura"
	g.email="loriv@me.com" 
	g.address="2653 Elliot St" 
	g.city="Santa Clara" 
	g.phone="(408) 425-3420" 
	g.ntrp="M2.5" 
	g.mtype="RF_" 
	g.put()
#197 

	selfobj.response.write("Vince  Ventura  loriv@me.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1392674076")) 
	g.year=2014
	g.fname="Vince"
	g.lname="Ventura"
	g.email="loriv@me.com" 
	g.address="2653 Elliot St" 
	g.city="Santa Clara" 
	g.phone="(408) 425-3420" 
	g.ntrp="M2.5" 
	g.mtype="RF_" 
	g.put()
#198 

	selfobj.response.write("Lori  Ventura  loriv@me.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1392673512")) 
	g.year=2014
	g.fname="Lori"
	g.lname="Ventura"
	g.email="loriv@me.com" 
	g.address="2653 Elliot St" 
	g.city="Santa Clara" 
	g.phone="(408) 425-3420" 
	g.ntrp="F3.5" 
	g.mtype="RF" 
	g.put()
#199 

	selfobj.response.write("Katie  Vien  thomas.g.truong@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1405147688")) 
	g.year=2014
	g.fname="Katie"
	g.lname="Vien"
	g.email="thomas.g.truong@yahoo.com" 
	g.address="2167 Weston Pl" 
	g.city="Santa Clara" 
	g.phone="(408) 219-2377" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#200 

	selfobj.response.write("Justin  Ware  justin_ware@hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1395760218")) 
	g.year=2014
	g.fname="Justin"
	g.lname="Ware"
	g.email="justin_ware@hotmail.com" 
	g.address="2345 Raggio Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 396-8599" 
	g.ntrp="M4.5" 
	g.mtype="RS" 
	g.put()
#201 

	selfobj.response.write("Jason  Wu  jcwu84@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1396305233")) 
	g.year=2014
	g.fname="Jason"
	g.lname="Wu"
	g.email="jcwu84@gmail.com" 
	g.address="633 Callippe Ct" 
	g.city="Brisbane" 
	g.phone="(650) 278-9118" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#202 

	selfobj.response.write("Susan  Wuthrich  susan.wuthrich@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1396410200")) 
	g.year=2014
	g.fname="Susan"
	g.lname="Wuthrich"
	g.email="susan.wuthrich@gmail.com" 
	g.address="7531 Newcastle Dr." 
	g.city="Cupertino" 
	g.phone="(408) 429-5004" 
	g.ntrp="FW3.5" 
	g.mtype="NRS" 
	g.put()
#203 

	selfobj.response.write("Warren  Yamaguchi  winini@comcast.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1395764483")) 
	g.year=2014
	g.fname="Warren"
	g.lname="Yamaguchi"
	g.email="winini@comcast.net" 
	g.address="1362 Merrivale West Square" 
	g.city="San Jose" 
	g.phone="(408) 641-0221" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#204 

	selfobj.response.write("Kiran Kumar   Yarlagadda  yarkirankumar@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1411947446")) 
	g.year=2014
	g.fname="Kiran Kumar "
	g.lname="Yarlagadda"
	g.email="yarkirankumar@gmail.com" 
	g.address="3500 Granada Ave Apt 429" 
	g.city="Santa Clara" 
	g.phone="(408) 797-5947" 
	g.ntrp="M" 
	g.mtype="RS" 
	g.put()
#205 

	selfobj.response.write("Jenny  Yip  jenny.rex@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1412970510")) 
	g.year=2014
	g.fname="Jenny"
	g.lname="Yip"
	g.email="jenny.rex@yahoo.com" 
	g.address="3220 Scott Blvd" 
	g.city="Santa Clara" 
	g.phone="(650) 793-2207" 
	g.ntrp="F3.0" 
	g.mtype="RF" 
	g.put()
#206 

	selfobj.response.write("Lynda  Zhang  lzhang83713@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1405148208")) 
	g.year=2014
	g.fname="Lynda"
	g.lname="Zhang"
	g.email="lzhang83713@yahoo.com" 
	g.address="460 Norwood Circle" 
	g.city="Santa Clara" 
	g.phone="(208) 939-2835" 
	g.ntrp="F4.0" 
	g.mtype="RF" 
	g.put()
