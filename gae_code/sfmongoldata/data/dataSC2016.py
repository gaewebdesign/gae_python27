

#
#
#select * from paypal where year = "2015"  union select * from bycheck where year =  "2015" order by year,lname 
#
#
import webapp2
from datastore import  *


def santaclara2015(selfobj):


#1 

	selfobj.response.write("Mike   Adame  michaelanthony139@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1427154651")) 
	g.year=2015
	g.fname="Mike"
	g.lname=" Adame"
	g.email="michaelanthony139@gmail.com" 
	g.address="2206 San Antonio Pl" 
	g.city="Santa Clara Ca" 
	g.phone="(408) 202-1118" 
	g.ntrp="M3.0" 
	g.mtype="RF" 
	g.put()
#2 

	selfobj.response.write("April  Abreau-Bostic  a.abreau@comcast.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1435367220")) 
	g.year=2015
	g.fname="April"
	g.lname="Abreau-Bostic"
	g.email="a.abreau@comcast.net" 
	g.address="856 Ferngrove Drive" 
	g.city="Cupertino" 
	g.phone="(408) 858-3102" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#3 

	selfobj.response.write("Jennifer  Adams  jenyferadams@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1424143719")) 
	g.year=2015
	g.fname="Jennifer"
	g.lname="Adams"
	g.email="jenyferadams@sbcglobal.net" 
	g.address="5971 Countess Drive" 
	g.city="San Jose" 
	g.phone="(408) 313-4405" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#4 

	selfobj.response.write("Sreenivas  Aluru  salur1@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1429136711")) 
	g.year=2015
	g.fname="Sreenivas"
	g.lname="Aluru"
	g.email="salur1@yahoo.com" 
	g.address="10816 Alderbrook Ln" 
	g.city="Cupertino" 
	g.phone="(408) 406-1885" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#5 

	selfobj.response.write("Nancy  Andersen  canandfam@earthlink.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1426881209")) 
	g.year=2015
	g.fname="Nancy"
	g.lname="Andersen"
	g.email="canandfam@earthlink.net" 
	g.address="3032 Cameron Way" 
	g.city="Santa Clara" 
	g.phone="(408) 985-5489" 
	g.ntrp="F3.5" 
	g.mtype="RF_" 
	g.put()
#6 

	selfobj.response.write("Brant  Armstrong  fiann1955@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1441660694")) 
	g.year=2015
	g.fname="Brant"
	g.lname="Armstrong"
	g.email="fiann1955@yahoo.com" 
	g.address="3102 Fresno Street" 
	g.city="Santa Clara" 
	g.phone="(408) 910-7003" 
	g.ntrp="M3.5" 
	g.mtype="RS" 
	g.put()
#7 

	selfobj.response.write("Janet  Arsenault  j6ma@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1425433337")) 
	g.year=2015
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

	selfobj.response.write("Hideko  Azama  tennissenior@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1435277994")) 
	g.year=2015
	g.fname="Hideko"
	g.lname="Azama"
	g.email="tennissenior@yahoo.com" 
	g.address="3115 Maurica Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 246-5129" 
	g.ntrp="M3.5" 
	g.mtype="RF" 
	g.put()
#9 

	selfobj.response.write("Lujean  Badenhorst  lujean17@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1436902416")) 
	g.year=2015
	g.fname="Lujean"
	g.lname="Badenhorst"
	g.email="lujean17@gmail.com" 
	g.address="4349 Renaissance Drive Apt 318" 
	g.city="San Jose" 
	g.phone="() -" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#10 

	selfobj.response.write("Orhan  Baser  obaser@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1416203602")) 
	g.year=2015
	g.fname="Orhan"
	g.lname="Baser"
	g.email="obaser@gmail.com" 
	g.address="544 Hickory Place" 
	g.city="Santa Clara" 
	g.phone="(408) 887-2514" 
	g.ntrp="M4.0" 
	g.mtype="RF" 
	g.put()
#11 

	selfobj.response.write("Aysen  Baser  obaser@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1437883315")) 
	g.year=2015
	g.fname="Aysen"
	g.lname="Baser"
	g.email="obaser@gmail.com" 
	g.address="544 Hickory Place" 
	g.city="Santa Clara" 
	g.phone="(408) 887-2514" 
	g.ntrp="F2.5" 
	g.mtype="RF_" 
	g.put()
#12 

	selfobj.response.write("Peri  Baser  obaser@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1437883586")) 
	g.year=2015
	g.fname="Peri"
	g.lname="Baser"
	g.email="obaser@gmail.com" 
	g.address="544 Hickory Place" 
	g.city="Santa Clara" 
	g.phone="(408) 887-2514" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#13 

	selfobj.response.write("Naoko   Bean  naokobean@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1424933873")) 
	g.year=2015
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

	selfobj.response.write("Randy  Bell  c.p.bell@att.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1418691588")) 
	g.year=2015
	g.fname="Randy"
	g.lname="Bell"
	g.email="c.p.bell@att.net" 
	g.address="1244 Maryann Drive" 
	g.city="Santa Clara, CA" 
	g.phone="(408) 241-6793" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#15 

	selfobj.response.write("Jonathan  Bell  c.p.bell@att.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1418691795")) 
	g.year=2015
	g.fname="Jonathan"
	g.lname="Bell"
	g.email="c.p.bell@att.net" 
	g.address="1244 Maryann Drive" 
	g.city="Santa Clara, CA" 
	g.phone="(408) 464-3177" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#16 

	selfobj.response.write("Carrie  Bell  c.p.bell@att.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1418691235")) 
	g.year=2015
	g.fname="Carrie"
	g.lname="Bell"
	g.email="c.p.bell@att.net" 
	g.address="1244 Maryann Drive" 
	g.city="Santa Clara, CA" 
	g.phone="(408) 241-6793" 
	g.ntrp="F4.0" 
	g.mtype="RF" 
	g.put()
#17 

	selfobj.response.write("Manikandan  Bhaskaran  manibhaskaran@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1426960832")) 
	g.year=2015
	g.fname="Manikandan"
	g.lname="Bhaskaran"
	g.email="manibhaskaran@gmail.com" 
	g.address="1750 Nantucket Circle Apt 236" 
	g.city="Santa Clara" 
	g.phone="(510) 710-2670" 
	g.ntrp="M3.0" 
	g.mtype="RS" 
	g.put()
#18 

	selfobj.response.write("Mike  Branch  unoamico@msn.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1432260622")) 
	g.year=2015
	g.fname="Mike"
	g.lname="Branch"
	g.email="unoamico@msn.com" 
	g.address="437 Jefferson Street" 
	g.city="Santa Clara" 
	g.phone="(408) 656-6123" 
	g.ntrp="M3.0" 
	g.mtype="RS" 
	g.put()
#19 

	selfobj.response.write("Robert  Brunkhorst  bob.brunkhorst@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1420585074")) 
	g.year=2015
	g.fname="Robert"
	g.lname="Brunkhorst"
	g.email="bob.brunkhorst@gmail.com" 
	g.address="849 Humewick Way" 
	g.city="Sunnyvale" 
	g.phone="(408) 667-5902" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#20 

	selfobj.response.write("Ike   Bunanta  ibunanta@me.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1424229406")) 
	g.year=2015
	g.fname="Ike "
	g.lname="Bunanta"
	g.email="ibunanta@me.com" 
	g.address="1059 Konstanz Terrace" 
	g.city="Sunnyvale" 
	g.phone="() -" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#21 

	selfobj.response.write("Hilary  Butler  butler.hilary@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1419299751")) 
	g.year=2015
	g.fname="Hilary"
	g.lname="Butler"
	g.email="butler.hilary@gmail.com" 
	g.address="18310 Daves Ave" 
	g.city="Monte Sereno" 
	g.phone="(408) 354-4209" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#22 

	selfobj.response.write("Volga   Calvello   volgab@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1420750713")) 
	g.year=2015
	g.fname="Volga "
	g.lname="Calvello "
	g.email="volgab@yahoo.com" 
	g.address="1974 Homestead Road" 
	g.city="Santa Clara" 
	g.phone="(650) 303-1151" 
	g.ntrp="F3.0" 
	g.mtype="RF" 
	g.put()
#23 

	selfobj.response.write("Thomas   Calvello   volgab@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1420751512")) 
	g.year=2015
	g.fname="Thomas "
	g.lname="Calvello "
	g.email="volgab@yahoo.com" 
	g.address="1974 Homestead Road" 
	g.city="Santa Clara" 
	g.phone="(650) 303-1151" 
	g.ntrp="M3.0" 
	g.mtype="RF_" 
	g.put()
#24 

	selfobj.response.write("Natalie  Cannon  natcannon@earthlink.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1426813122")) 
	g.year=2015
	g.fname="Natalie"
	g.lname="Cannon"
	g.email="natcannon@earthlink.net" 
	g.address="3032 Cameron Way" 
	g.city="Santa Clara" 
	g.phone="(408) 985-5489" 
	g.ntrp="F" 
	g.mtype="RF" 
	g.put()
#25 

	selfobj.response.write("Cristy  Cappellini  volgab@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1420751771")) 
	g.year=2015
	g.fname="Cristy"
	g.lname="Cappellini"
	g.email="volgab@yahoo.com" 
	g.address="1974 Homestead Road" 
	g.city="Santa Clara" 
	g.phone="(650) 303-1151" 
	g.ntrp="F3.0" 
	g.mtype="RF_" 
	g.put()
#26 

	selfobj.response.write("Jacob  Carrillo  maccarr54@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1428374853")) 
	g.year=2015
	g.fname="Jacob"
	g.lname="Carrillo"
	g.email="maccarr54@gmail.com" 
	g.address="3321 Benton St." 
	g.city="Santa Clara" 
	g.phone="(408) 236-1507" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#27 

	selfobj.response.write("Mitch  Carrillo  maccarr54@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1428374297")) 
	g.year=2015
	g.fname="Mitch"
	g.lname="Carrillo"
	g.email="maccarr54@gmail.com" 
	g.address="3321 Benton St." 
	g.city="Santa Clara" 
	g.phone="(408) 236-1507" 
	g.ntrp="M3.0" 
	g.mtype="RF" 
	g.put()
#28 

	selfobj.response.write("Linda  Carrillo  maccarr54@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1428374723")) 
	g.year=2015
	g.fname="Linda"
	g.lname="Carrillo"
	g.email="maccarr54@gmail.com" 
	g.address="3321 Benton St." 
	g.city="Santa Clara" 
	g.phone="(408) 236-1507" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#29 

	selfobj.response.write("Jennifer  Cashman  jjcashman1@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1427945377")) 
	g.year=2015
	g.fname="Jennifer"
	g.lname="Cashman"
	g.email="jjcashman1@gmail.com" 
	g.address="14690 Wyrick Ave" 
	g.city="San Jose" 
	g.phone="() -" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#30 

	selfobj.response.write("Andrew  Charfauros  asc567@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1422839668")) 
	g.year=2015
	g.fname="Andrew"
	g.lname="Charfauros"
	g.email="asc567@yahoo.com" 
	g.address="322 California Street" 
	g.city="Campbell" 
	g.phone="(408) 234-6302" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#31 

	selfobj.response.write("Ellen  Chen  turning.leaf@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1430876568")) 
	g.year=2015
	g.fname="Ellen"
	g.lname="Chen"
	g.email="turning.leaf@yahoo.com" 
	g.address="14690 Wyrick Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 425-8889" 
	g.ntrp="F3.0" 
	g.mtype="RS" 
	g.put()
#32 

	selfobj.response.write("Po  Chen  pkc3112@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1445321620")) 
	g.year=2015
	g.fname="Po"
	g.lname="Chen"
	g.email="pkc3112@gmail.com" 
	g.address="" 
	g.city="San Jose" 
	g.phone="() -" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#33 

	selfobj.response.write("Myoung Taeck  Chiang  taeckchiang@aol.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1434519873")) 
	g.year=2015
	g.fname="Myoung Taeck"
	g.lname="Chiang"
	g.email="taeckchiang@aol.com" 
	g.address="1235 De Altura Commons" 
	g.city="San Jose" 
	g.phone="(408) 306-3657" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#34 

	selfobj.response.write("Chalapathi  Chitta  chalaps@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1424478956")) 
	g.year=2015
	g.fname="Chalapathi"
	g.lname="Chitta"
	g.email="chalaps@yahoo.com" 
	g.address="Unknown Address" 
	g.city="San Jose" 
	g.phone="(510) 881-6944" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#35 

	selfobj.response.write("Deepak  Chotrani  deepak_c15@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1425869717")) 
	g.year=2015
	g.fname="Deepak"
	g.lname="Chotrani"
	g.email="deepak_c15@yahoo.com" 
	g.address="3722 Europe Ct" 
	g.city="SANTA CLARA" 
	g.phone="(607) 351-0812" 
	g.ntrp="M3.5" 
	g.mtype="RS" 
	g.put()
#36 

	selfobj.response.write("Ethan  Chou  ihsienchou@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1432926640")) 
	g.year=2015
	g.fname="Ethan"
	g.lname="Chou"
	g.email="ihsienchou@gmail.com" 
	g.address="1153 Crowley Ave." 
	g.city="Santa Clara" 
	g.phone="(858) 401-9617" 
	g.ntrp="M3.5" 
	g.mtype="RS" 
	g.put()
#37 

	selfobj.response.write("Jayant  Chowdhary  jayantc11@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1430200233")) 
	g.year=2015
	g.fname="Jayant"
	g.lname="Chowdhary"
	g.email="jayantc11@gmail.com" 
	g.address="60 Descanso Drive" 
	g.city="San Jose" 
	g.phone="(412) 378-4267" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#38 

	selfobj.response.write("Maria  Crema  gmcrema@aol.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1441160079")) 
	g.year=2015
	g.fname="Maria"
	g.lname="Crema"
	g.email="gmcrema@aol.com" 
	g.address="38 N. Almaden Blvd. #2201" 
	g.city="San Jose" 
	g.phone="(408) 239-9691" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#39 

	selfobj.response.write("Liliane  Cromer  lilianec@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1419741615")) 
	g.year=2015
	g.fname="Liliane"
	g.lname="Cromer"
	g.email="lilianec@sbcglobal.net" 
	g.address="14120 Palomino Way" 
	g.city="Saratoga" 
	g.phone="(408) 823-6448" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#40 

	selfobj.response.write("Lori  Cruz-Spray  Cruzspray@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1423458989")) 
	g.year=2015
	g.fname="Lori"
	g.lname="Cruz-Spray"
	g.email="Cruzspray@gmail.com" 
	g.address="555 Minton Lane" 
	g.city="Mountain View" 
	g.phone="(650) 690-0022" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#41 

	selfobj.response.write("Machiko  Cyr  machikoc@pacbell.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1423720928")) 
	g.year=2015
	g.fname="Machiko"
	g.lname="Cyr"
	g.email="machikoc@pacbell.net" 
	g.address="5518 Castle Manor Dr." 
	g.city="San Jose" 
	g.phone="(408) 315-7606" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#42 

	selfobj.response.write("Brian  Dang  briandang000@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1431716849")) 
	g.year=2015
	g.fname="Brian"
	g.lname="Dang"
	g.email="briandang000@yahoo.com" 
	g.address="1961 Linden Ln" 
	g.city="Milpitas" 
	g.phone="(408) 712-8450" 
	g.ntrp="M" 
	g.mtype="NRS" 
	g.put()
#43 

	selfobj.response.write("Thomas  Dang (Dunham)  t.dunham24@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1424739591")) 
	g.year=2015
	g.fname="Thomas"
	g.lname="Dang (Dunham)"
	g.email="t.dunham24@gmail.com" 
	g.address="3666 Franklin ave." 
	g.city="Fremont" 
	g.phone="(510) 673-6300" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#44 

	selfobj.response.write("Ayanangshu  Das  ayanangshu.das@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1439235419")) 
	g.year=2015
	g.fname="Ayanangshu"
	g.lname="Das"
	g.email="ayanangshu.das@gmail.com" 
	g.address="3548 Agate Dr" 
	g.city="Santa Clara" 
	g.phone="(630) 337-4856" 
	g.ntrp="M5.5" 
	g.mtype="RF" 
	g.put()
#45 

	selfobj.response.write("Ipsita  Das  isengupta25@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1439235790")) 
	g.year=2015
	g.fname="Ipsita"
	g.lname="Das"
	g.email="isengupta25@gmail.com" 
	g.address="3548 Agate Dr" 
	g.city="Santa Clara" 
	g.phone="(630) 337-4856" 
	g.ntrp="F1.5" 
	g.mtype="RF_" 
	g.put()
#46 

	selfobj.response.write("Onofre                    de Souza  onofre2237@aol.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1425005219")) 
	g.year=2015
	g.fname="Onofre                  "
	g.lname="de Souza"
	g.email="onofre2237@aol.com" 
	g.address="2983 Millar avenue" 
	g.city="Santa Clara" 
	g.phone="(408) 386-4862" 
	g.ntrp="M" 
	g.mtype="RS" 
	g.put()
#47 

	selfobj.response.write("Adam  DePuit  adepuit@hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1425920512")) 
	g.year=2015
	g.fname="Adam"
	g.lname="DePuit"
	g.email="adepuit@hotmail.com" 
	g.address="210 Peppermint Tree Terr #4" 
	g.city="Sunnyvale" 
	g.phone="(315) 857-7497" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#48 

	selfobj.response.write("Christina  Deshera  cdesheagle@aol.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1434990320")) 
	g.year=2015
	g.fname="Christina"
	g.lname="Deshera"
	g.email="cdesheagle@aol.com" 
	g.address="2973 Sally Court" 
	g.city="Santa Clara" 
	g.phone="(408) 243-1744" 
	g.ntrp="F2.5" 
	g.mtype="RF_" 
	g.put()
#49 

	selfobj.response.write("Rick  Deshera  cdesheagle@aol.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1431021689")) 
	g.year=2015
	g.fname="Rick"
	g.lname="Deshera"
	g.email="cdesheagle@aol.com" 
	g.address="2973 Sally Court" 
	g.city="Santa Clara" 
	g.phone="(408) 243-1744" 
	g.ntrp="M2.5" 
	g.mtype="RF" 
	g.put()
#50 

	selfobj.response.write("Cathy  Deshera  descheagle@aol.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1431021826")) 
	g.year=2015
	g.fname="Cathy"
	g.lname="Deshera"
	g.email="descheagle@aol.com" 
	g.address="2973 Sally Court" 
	g.city="Santa Clara" 
	g.phone="(408) 243-1744" 
	g.ntrp="F2.5" 
	g.mtype="RF_" 
	g.put()
#51 

	selfobj.response.write("Gurpreet  Dhaman  gurpreet_tennis@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1424822902")) 
	g.year=2015
	g.fname="Gurpreet"
	g.lname="Dhaman"
	g.email="gurpreet_tennis@yahoo.com" 
	g.address="932 Planetree Place" 
	g.city="Sunnyvale" 
	g.phone="(206) 372-8688" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#52 

	selfobj.response.write("Olivia  Dixon  awesomeolivia1@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1434995532")) 
	g.year=2015
	g.fname="Olivia"
	g.lname="Dixon"
	g.email="awesomeolivia1@gmail.com" 
	g.address="P.O. Box 3615" 
	g.city="Santa Clara" 
	g.phone="(408) 680-3125" 
	g.ntrp="F" 
	g.mtype="NRS" 
	g.put()
#53 

	selfobj.response.write("Diep  Doan  thacdoan3060@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1427519580")) 
	g.year=2015
	g.fname="Diep"
	g.lname="Doan"
	g.email="thacdoan3060@gmail.com" 
	g.address="3060 Dibble Ct" 
	g.city="Santa Clara" 
	g.phone="(408) 966-9717" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#54 

	selfobj.response.write("Thac  Doan  thacdoan3060@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1427341318")) 
	g.year=2015
	g.fname="Thac"
	g.lname="Doan"
	g.email="thacdoan3060@gmail.com" 
	g.address="3060 Dibble Ct" 
	g.city="Santa Clara" 
	g.phone="(408) 966-9717" 
	g.ntrp="M" 
	g.mtype="RF" 
	g.put()
#55 

	selfobj.response.write("Lisa  Doan  thacdoan3060@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1427519558")) 
	g.year=2015
	g.fname="Lisa"
	g.lname="Doan"
	g.email="thacdoan3060@gmail.com" 
	g.address="3060 Dibble Ct" 
	g.city="Santa Clara" 
	g.phone="(408) 966-9717" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#56 

	selfobj.response.write("Consuelo  Domingo  conniedomingo@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1418159623")) 
	g.year=2015
	g.fname="Consuelo"
	g.lname="Domingo"
	g.email="conniedomingo@sbcglobal.net" 
	g.address="6645 Dairy Avenue" 
	g.city="Newark, CA" 
	g.phone="(408) 646-8654" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#57 

	selfobj.response.write("Carl  Dunlap  highaffinitycarl@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1422993194")) 
	g.year=2015
	g.fname="Carl"
	g.lname="Dunlap"
	g.email="highaffinitycarl@yahoo.com" 
	g.address="990 B La Mesa Terrace" 
	g.city="Sunnyvale" 
	g.phone="(408) 245-5445" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#58 

	selfobj.response.write("Tho  Duong  tho.duong@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1435277926")) 
	g.year=2015
	g.fname="Tho"
	g.lname="Duong"
	g.email="tho.duong@gmail.com" 
	g.address="3740 Peacock Ct" 
	g.city="Santa Clara" 
	g.phone="(408) 483-8936" 
	g.ntrp="M3.5" 
	g.mtype="RF" 
	g.put()
#59 

	selfobj.response.write("Pat  Durnhofer  patodurnhofer@Gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1424008815")) 
	g.year=2015
	g.fname="Pat"
	g.lname="Durnhofer"
	g.email="patodurnhofer@Gmail.com" 
	g.address="986  I  la mesa terrace" 
	g.city="Sunnyvale" 
	g.phone="(408) 807-2992" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#60 

	selfobj.response.write("Kaori  Enomoto  kaori@saphirellc.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1423809454")) 
	g.year=2015
	g.fname="Kaori"
	g.lname="Enomoto"
	g.email="kaori@saphirellc.com" 
	g.address="851 W. Remington Dr." 
	g.city="Sunnyvale" 
	g.phone="(408) 623-5702" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#61 

	selfobj.response.write("Marie  Fan  msfan00@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1418353390")) 
	g.year=2015
	g.fname="Marie"
	g.lname="Fan"
	g.email="msfan00@yahoo.com" 
	g.address="1297 Weibel Way" 
	g.city="San Jose" 
	g.phone="(408) 332-6026" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#62 

	selfobj.response.write("Jackie  Fenton  jdfenton26@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1423684676")) 
	g.year=2015
	g.fname="Jackie"
	g.lname="Fenton"
	g.email="jdfenton26@gmail.com" 
	g.address="536 Hawthorne Ave Apt C" 
	g.city="Palo Alto" 
	g.phone="(443) 812-4374" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#63 

	selfobj.response.write("Laura  Fletcher  fletch4Him1@mac.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1420961861")) 
	g.year=2015
	g.fname="Laura"
	g.lname="Fletcher"
	g.email="fletch4Him1@mac.com" 
	g.address="431 El Camino Real #1210" 
	g.city="Santa Clara" 
	g.phone="(650) 492-1930" 
	g.ntrp="F3.5" 
	g.mtype="RF" 
	g.put()
#64 

	selfobj.response.write("Janelle  Flores  janelle.c.flores@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1442340742")) 
	g.year=2015
	g.fname="Janelle"
	g.lname="Flores"
	g.email="janelle.c.flores@gmail.com" 
	g.address="1537 Altamont Ave" 
	g.city="San Jose" 
	g.phone="(408) 497-9329" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#65 

	selfobj.response.write("Karen  Fong  kafong@aol.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1418105995")) 
	g.year=2015
	g.fname="Karen"
	g.lname="Fong"
	g.email="kafong@aol.com" 
	g.address="3444 Notre Dame Drive" 
	g.city="Santa Clara" 
	g.phone="(408) 742-3036" 
	g.ntrp="F3.0" 
	g.mtype="RS" 
	g.put()
#66 

	selfobj.response.write("Susan  Foster  lizzyfoster1958@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1429733594")) 
	g.year=2015
	g.fname="Susan"
	g.lname="Foster"
	g.email="lizzyfoster1958@gmail.com" 
	g.address="2648 Elliot Street" 
	g.city="Santa Clara" 
	g.phone="(408) 246-1548" 
	g.ntrp="F2.5" 
	g.mtype="RF" 
	g.put()
#67 

	selfobj.response.write("Lizzy  Foster  lizzyfoster1958@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1429733771")) 
	g.year=2015
	g.fname="Lizzy"
	g.lname="Foster"
	g.email="lizzyfoster1958@gmail.com" 
	g.address="2653 Elliot Street" 
	g.city="Santa Clara" 
	g.phone="(408) 246-1548" 
	g.ntrp="F2.5" 
	g.mtype="RF_" 
	g.put()
#68 

	selfobj.response.write("Nathan  Foster  lizzyfoster1958@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1429733863")) 
	g.year=2015
	g.fname="Nathan"
	g.lname="Foster"
	g.email="lizzyfoster1958@gmail.com" 
	g.address="2648 Elliot Street" 
	g.city="Santa Clara" 
	g.phone="(408) 246-1548" 
	g.ntrp="M3.0" 
	g.mtype="RF_" 
	g.put()
#69 

	selfobj.response.write("John  Fox  foxman@me.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1429231138")) 
	g.year=2015
	g.fname="John"
	g.lname="Fox"
	g.email="foxman@me.com" 
	g.address="1021 Pomeroy Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 455-5501" 
	g.ntrp="M3.5" 
	g.mtype="RS" 
	g.put()
#70 

	selfobj.response.write("Leslie  Francis  lesliefrancis@alum.mit.edu")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1444146202")) 
	g.year=2015
	g.fname="Leslie"
	g.lname="Francis"
	g.email="lesliefrancis@alum.mit.edu" 
	g.address="18910 Bellgrove Circle" 
	g.city="Saratoga" 
	g.phone="(408) 679-8032" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#71 

	selfobj.response.write("Susan  Frank  susanfrank1@hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1440737451")) 
	g.year=2015
	g.fname="Susan"
	g.lname="Frank"
	g.email="susanfrank1@hotmail.com" 
	g.address="132 Promethean Way" 
	g.city="Mountain View" 
	g.phone="(650) 400-0423" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#72 

	selfobj.response.write("Brian  Freidman  nsavending@hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1427996474")) 
	g.year=2015
	g.fname="Brian"
	g.lname="Freidman"
	g.email="nsavending@hotmail.com" 
	g.address="385 River Oaks Parkway Apt#3091" 
	g.city="San Jose" 
	g.phone="(949) 233-1230" 
	g.ntrp="M4.0" 
	g.mtype="NRF" 
	g.put()
#73 

	selfobj.response.write("Chuck  Fujita  chuckfujita@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1425484921")) 
	g.year=2015
	g.fname="Chuck"
	g.lname="Fujita"
	g.email="chuckfujita@gmail.com" 
	g.address="1390 Monroe St #8" 
	g.city="Santa Clara" 
	g.phone="(408) 390-2915" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#74 

	selfobj.response.write("Anne  Giannini  rudyannie@aol.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1419968229")) 
	g.year=2015
	g.fname="Anne"
	g.lname="Giannini"
	g.email="rudyannie@aol.com" 
	g.address="430 Laurel Avenue" 
	g.city="Millbrae" 
	g.phone="(650) 678-8812" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#75 

	selfobj.response.write("Kunal  Godbole  kunalgodbole@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1447544918")) 
	g.year=2015
	g.fname="Kunal"
	g.lname="Godbole"
	g.email="kunalgodbole@gmail.com" 
	g.address="1957 Silva Pl" 
	g.city="Santa Clara" 
	g.phone="(858) 431-9481" 
	g.ntrp="M3.5" 
	g.mtype="RF" 
	g.put()
#76 

	selfobj.response.write("Nirmala  Gopalan  ngopalan02@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1425873312")) 
	g.year=2015
	g.fname="Nirmala"
	g.lname="Gopalan"
	g.email="ngopalan02@yahoo.com" 
	g.address="7567 RAINBOW DR" 
	g.city="CUPERTINO" 
	g.phone="(408) 253-3143" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#77 

	selfobj.response.write("Karthi  Gopalan  karthigopalan@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1428097988")) 
	g.year=2015
	g.fname="Karthi"
	g.lname="Gopalan"
	g.email="karthigopalan@yahoo.com" 
	g.address="1616 HOPE DRIVE, 423" 
	g.city="SANTA CLARA" 
	g.phone="(408) 910-5128" 
	g.ntrp="F4.0" 
	g.mtype="RS" 
	g.put()
#78 

	selfobj.response.write("Hye-Yoon  Hahn  hhahn00@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1429136518")) 
	g.year=2015
	g.fname="Hye-Yoon"
	g.lname="Hahn"
	g.email="hhahn00@yahoo.com" 
	g.address="2926 Roma Ct." 
	g.city="Santa Clara" 
	g.phone="() -" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#79 

	selfobj.response.write("Dah-Young  Hahn  hhahn00@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1429137092")) 
	g.year=2015
	g.fname="Dah-Young"
	g.lname="Hahn"
	g.email="hhahn00@yahoo.com" 
	g.address="2926 Roma Ct." 
	g.city="Santa Clara" 
	g.phone="() -" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#80 

	selfobj.response.write("Hyeok  Hahn  hhahn00@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1425933996")) 
	g.year=2015
	g.fname="Hyeok"
	g.lname="Hahn"
	g.email="hhahn00@yahoo.com" 
	g.address="2926 Roma Ct." 
	g.city="Santa Clara" 
	g.phone="(408) 507-2848" 
	g.ntrp="M3.5" 
	g.mtype="RF" 
	g.put()
#81 

	selfobj.response.write("Julie  Hahn  hhahn00@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1429136959")) 
	g.year=2015
	g.fname="Julie"
	g.lname="Hahn"
	g.email="hhahn00@yahoo.com" 
	g.address="2926 Roma Ct." 
	g.city="Santa Clara" 
	g.phone="() -" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#82 

	selfobj.response.write("Lisa  Halpern  HalpernLK@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1424712086")) 
	g.year=2015
	g.fname="Lisa"
	g.lname="Halpern"
	g.email="HalpernLK@gmail.com" 
	g.address="304 Elm Street" 
	g.city="San Mateo" 
	g.phone="(650) 773-2300" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#83 

	selfobj.response.write("Aram  Hamidi  Aram1Hamidi@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1427398256")) 
	g.year=2015
	g.fname="Aram"
	g.lname="Hamidi"
	g.email="Aram1Hamidi@gmail.com" 
	g.address="1955 De La Pena Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 442-8860" 
	g.ntrp="F3.0" 
	g.mtype="RS" 
	g.put()
#84 

	selfobj.response.write("Lucy  Harendza  lharendza@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1420428636")) 
	g.year=2015
	g.fname="Lucy"
	g.lname="Harendza"
	g.email="lharendza@yahoo.com" 
	g.address="267 Cahill Park Drive" 
	g.city="San Jose" 
	g.phone="(408) 888-2447" 
	g.ntrp="F3.0" 
	g.mtype="NRS" 
	g.put()
#85 

	selfobj.response.write("Sharon  Haugen  bertnsharon@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1423972955")) 
	g.year=2015
	g.fname="Sharon"
	g.lname="Haugen"
	g.email="bertnsharon@yahoo.com" 
	g.address="1575 Keith Drive" 
	g.city="Campbell" 
	g.phone="(408) 379-9889" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#86 

	selfobj.response.write("Mike  Hawkes  hawkes_julie@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1424309724")) 
	g.year=2015
	g.fname="Mike"
	g.lname="Hawkes"
	g.email="hawkes_julie@yahoo.com" 
	g.address="1061 Waterbird Way" 
	g.city="Santa Clara" 
	g.phone="(408) 296-6629" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#87 

	selfobj.response.write("Julie  Hawkes  hawkes_julie@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1419363615")) 
	g.year=2015
	g.fname="Julie"
	g.lname="Hawkes"
	g.email="hawkes_julie@yahoo.com" 
	g.address="1061 Waterbird Way" 
	g.city="Santa Clara" 
	g.phone="(408) 296-6629" 
	g.ntrp="F4.0" 
	g.mtype="RF" 
	g.put()
#88 

	selfobj.response.write("Henry  Herman  henry.herman@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1424374640")) 
	g.year=2015
	g.fname="Henry"
	g.lname="Herman"
	g.email="henry.herman@gmail.com" 
	g.address="984 Kiely Blvd Unit L" 
	g.city="Santa Clara" 
	g.phone="(714) 697-2298" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#89 

	selfobj.response.write("Samantha  Herman (Milner)  samantha.milner@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1424374337")) 
	g.year=2015
	g.fname="Samantha"
	g.lname="Herman (Milner)"
	g.email="samantha.milner@gmail.com" 
	g.address="984 Kiely Blvd Unit L" 
	g.city="Santa Clara" 
	g.phone="(661) 713-9869" 
	g.ntrp="F4.0" 
	g.mtype="RF" 
	g.put()
#90 

	selfobj.response.write("Norah  Hibbits  norellha@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1433127642")) 
	g.year=2015
	g.fname="Norah"
	g.lname="Hibbits"
	g.email="norellha@yahoo.com" 
	g.address="1091 Essex Ave" 
	g.city="Sunnyvale" 
	g.phone="(301) 580-8329" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#91 

	selfobj.response.write("Delphine  Hill  delhill09@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1424846791")) 
	g.year=2015
	g.fname="Delphine"
	g.lname="Hill"
	g.email="delhill09@gmail.com" 
	g.address="2165 Addison Ave" 
	g.city="Palo Alto" 
	g.phone="(408) 472-5823" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#92 

	selfobj.response.write("Jeanette  Hoggatt  queenb_95051@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1419307538")) 
	g.year=2015
	g.fname="Jeanette"
	g.lname="Hoggatt"
	g.email="queenb_95051@yahoo.com" 
	g.address="3070 Dibble Court" 
	g.city="Santa Clara" 
	g.phone="(408) 781-0420" 
	g.ntrp="F4.0" 
	g.mtype="RF" 
	g.put()
#93 

	selfobj.response.write("Herta  Hoggatt  queenb_95051@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1419307780")) 
	g.year=2015
	g.fname="Herta"
	g.lname="Hoggatt"
	g.email="queenb_95051@yahoo.com" 
	g.address="3070 Dibble Court" 
	g.city="Santa Clara" 
	g.phone="(408) 781-0420" 
	g.ntrp="F2.0" 
	g.mtype="RF_" 
	g.put()
#94 

	selfobj.response.write("Pamela  Hoggatt  queenb_95051@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1419307899")) 
	g.year=2015
	g.fname="Pamela"
	g.lname="Hoggatt"
	g.email="queenb_95051@yahoo.com" 
	g.address="3070 Dibble Court" 
	g.city="Santa Clara" 
	g.phone="(408) 781-0420" 
	g.ntrp="F3.0" 
	g.mtype="RF_" 
	g.put()
#95 

	selfobj.response.write("Norma  Hughes  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1416202590")) 
	g.year=2015
	g.fname="Norma"
	g.lname="Hughes"
	g.email="" 
	g.address="598 Bancroft St" 
	g.city="Santa Clara" 
	g.phone="(408) 296-1271" 
	g.ntrp="F2.5" 
	g.mtype="RS" 
	g.put()
#96 

	selfobj.response.write("Akari  Ikeda   aikeda14@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1424203103")) 
	g.year=2015
	g.fname="Akari"
	g.lname="Ikeda "
	g.email="aikeda14@yahoo.com" 
	g.address="1396 Lafayette St" 
	g.city="Santa Clara" 
	g.phone="(408) 916-7875" 
	g.ntrp="F4.5" 
	g.mtype="RS" 
	g.put()
#97 

	selfobj.response.write("Nicole  Isaacson  aliceisaacson@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1434947039")) 
	g.year=2015
	g.fname="Nicole"
	g.lname="Isaacson"
	g.email="aliceisaacson@yahoo.com" 
	g.address="513 Hickory Place" 
	g.city="Santa Clara" 
	g.phone="(408) 247-0" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#98 

	selfobj.response.write("Mark  Isaacson  aliceisaacson@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1434946746")) 
	g.year=2015
	g.fname="Mark"
	g.lname="Isaacson"
	g.email="aliceisaacson@yahoo.com" 
	g.address="513 Hickory Place" 
	g.city="Santa Clara" 
	g.phone="(408) 247-0343" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#99 

	selfobj.response.write("Alice  Isaacson  aliceisaacson@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1434417973")) 
	g.year=2015
	g.fname="Alice"
	g.lname="Isaacson"
	g.email="aliceisaacson@yahoo.com" 
	g.address="513 Hickory Place" 
	g.city="Santa Clara" 
	g.phone="(408) 247-0343" 
	g.ntrp="F4.0" 
	g.mtype="RF" 
	g.put()
#100 

	selfobj.response.write("Matthew  Isaacson  aliceisaacson@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1434946921")) 
	g.year=2015
	g.fname="Matthew"
	g.lname="Isaacson"
	g.email="aliceisaacson@yahoo.com" 
	g.address="513 Hickory Place" 
	g.city="Santa Clara" 
	g.phone="(408) 247-0343" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#101 

	selfobj.response.write("Taryn  Ishida  tarynishida@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1424147315")) 
	g.year=2015
	g.fname="Taryn"
	g.lname="Ishida"
	g.email="tarynishida@gmail.com" 
	g.address="95 Hobson St. 3A" 
	g.city="San Jose" 
	g.phone="(408) 568-9595" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#102 

	selfobj.response.write("Cindy  Jeung  cljeung@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1442009337")) 
	g.year=2015
	g.fname="Cindy"
	g.lname="Jeung"
	g.email="cljeung@yahoo.com" 
	g.address="315 Beresford Ave" 
	g.city="Redwood City" 
	g.phone="(650) 365-7532" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#103 

	selfobj.response.write("Leslie  Johnson  coachleslie2012@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1426391892")) 
	g.year=2015
	g.fname="Leslie"
	g.lname="Johnson"
	g.email="coachleslie2012@gmail.com" 
	g.address="1691 Cunningham St" 
	g.city="Santa Clara" 
	g.phone="(408) 499-5387" 
	g.ntrp="F3.0" 
	g.mtype="RS" 
	g.put()
#104 

	selfobj.response.write("Alexandra  Kalayta  makalayta@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1424040136")) 
	g.year=2015
	g.fname="Alexandra"
	g.lname="Kalayta"
	g.email="makalayta@gmail.com" 
	g.address="250 Curtner Ave, Apt 26" 
	g.city="Palo Alto" 
	g.phone="(530) 632-7651" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#105 

	selfobj.response.write("Kim  Kallbrier  kimkallbrier@hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1423787790")) 
	g.year=2015
	g.fname="Kim"
	g.lname="Kallbrier"
	g.email="kimkallbrier@hotmail.com" 
	g.address="12250 Viewoak Dr" 
	g.city="Saratoga" 
	g.phone="(408) 806-2400" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#106 

	selfobj.response.write("Sachin  Kancharla  vjkancharla@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1428452355")) 
	g.year=2015
	g.fname="Sachin"
	g.lname="Kancharla"
	g.email="vjkancharla@yahoo.com" 
	g.address="990 Live Oak Dr" 
	g.city="Santa Clara" 
	g.phone="(415) 269-6939" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#107 

	selfobj.response.write("Vijay  Kancharla  vjkancharla@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1428451235")) 
	g.year=2015
	g.fname="Vijay"
	g.lname="Kancharla"
	g.email="vjkancharla@yahoo.com" 
	g.address="990 Live Oak Dr" 
	g.city="Santa Clara" 
	g.phone="(415) 269-6939" 
	g.ntrp="M3.5" 
	g.mtype="RF" 
	g.put()
#108 

	selfobj.response.write("Geetha  Kancharla  vjkancharla@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1428452537")) 
	g.year=2015
	g.fname="Geetha"
	g.lname="Kancharla"
	g.email="vjkancharla@yahoo.com" 
	g.address="990 Live Oak Dr" 
	g.city="Santa Clara" 
	g.phone="(415) 269-6939" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#109 

	selfobj.response.write("Nitin  Kancharla  vjkancharla@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1428452165")) 
	g.year=2015
	g.fname="Nitin"
	g.lname="Kancharla"
	g.email="vjkancharla@yahoo.com" 
	g.address="990 Live Oak Dr" 
	g.city="Santa Clara" 
	g.phone="(415) 269-6939" 
	g.ntrp="M3.5" 
	g.mtype="RF_" 
	g.put()
#110 

	selfobj.response.write("Thonsey  Keopanya  thonsey@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1427853399")) 
	g.year=2015
	g.fname="Thonsey"
	g.lname="Keopanya"
	g.email="thonsey@gmail.com" 
	g.address="29 Orinda Way #1964" 
	g.city="Orinda" 
	g.phone="(925) 999-0556" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#111 

	selfobj.response.write("James  Kern  jhkern@hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1426812888")) 
	g.year=2015
	g.fname="James"
	g.lname="Kern"
	g.email="jhkern@hotmail.com" 
	g.address="1330 Warner" 
	g.city="Sunnyvale" 
	g.phone="(407) 739-6808" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#112 

	selfobj.response.write("Sayaka  Kishino  ksh_kishino@hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1424138602")) 
	g.year=2015
	g.fname="Sayaka"
	g.lname="Kishino"
	g.email="ksh_kishino@hotmail.com" 
	g.address="1173 Susan Way" 
	g.city="Sunnyvale" 
	g.phone="(408) 773-0659" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#113 

	selfobj.response.write("Hosoon  Ku  hosoonku@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1421807281")) 
	g.year=2015
	g.fname="Hosoon"
	g.lname="Ku"
	g.email="hosoonku@yahoo.com" 
	g.address="3959 Veritas Way" 
	g.city="San Ramon" 
	g.phone="(925) 997-3927" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#114 

	selfobj.response.write("Jonathan  Kwan  jonnyjack@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1434438388")) 
	g.year=2015
	g.fname="Jonathan"
	g.lname="Kwan"
	g.email="jonnyjack@gmail.com" 
	g.address="5081 Sloan Way" 
	g.city="Union City" 
	g.phone="(408) 313-7144" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#115 

	selfobj.response.write("Yulie  Law  YULIELAW@GMAIL.COM")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1418789780")) 
	g.year=2015
	g.fname="Yulie"
	g.lname="Law"
	g.email="YULIELAW@GMAIL.COM" 
	g.address="417 Seneca St" 
	g.city="Palo Alto" 
	g.phone="(650) 704-1314" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#116 

	selfobj.response.write("Brook  Lee  bm.lee@verizon.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1434518950")) 
	g.year=2015
	g.fname="Brook"
	g.lname="Lee"
	g.email="bm.lee@verizon.net" 
	g.address="1172 Morse Ave" 
	g.city="Sunnyvale" 
	g.phone="(856) 261-3277" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#117 

	selfobj.response.write("Lisa  Lee  lee.hang@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1438119881")) 
	g.year=2015
	g.fname="Lisa"
	g.lname="Lee"
	g.email="lee.hang@yahoo.com" 
	g.address="4558 Cheeney St" 
	g.city="Santa Clara" 
	g.phone="(408) 506-2089" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#118 

	selfobj.response.write("Nathan  Lee  lee.hang@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1438119860")) 
	g.year=2015
	g.fname="Nathan"
	g.lname="Lee"
	g.email="lee.hang@yahoo.com" 
	g.address="4558 Cheeney St" 
	g.city="Santa Clara" 
	g.phone="(408) 506-2089" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#119 

	selfobj.response.write("Angela  Lee  leeac05@hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1443462802")) 
	g.year=2015
	g.fname="Angela"
	g.lname="Lee"
	g.email="leeac05@hotmail.com" 
	g.address="121 E. Tasman Drive," 
	g.city="San Jose" 
	g.phone="(847) 226-3865" 
	g.ntrp="F2.5" 
	g.mtype="NRS" 
	g.put()
#120 

	selfobj.response.write("Hang  Lee  lee.hang@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1438119690")) 
	g.year=2015
	g.fname="Hang"
	g.lname="Lee"
	g.email="lee.hang@yahoo.com" 
	g.address="4558 Cheeney St" 
	g.city="Santa Clara" 
	g.phone="(408) 506-2089" 
	g.ntrp="M4.0" 
	g.mtype="RF" 
	g.put()
#121 

	selfobj.response.write("Brandon  Lee  lee.hang@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1438119968")) 
	g.year=2015
	g.fname="Brandon"
	g.lname="Lee"
	g.email="lee.hang@yahoo.com" 
	g.address="4558 Cheeney St" 
	g.city="Santa Clara" 
	g.phone="(408) 506-2089" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#122 

	selfobj.response.write("Joy  Lenz  jlenz77@hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1438832722")) 
	g.year=2015
	g.fname="Joy"
	g.lname="Lenz"
	g.email="jlenz77@hotmail.com" 
	g.address="5938 Country Club Parkway" 
	g.city="San Jose" 
	g.phone="(408) 705-5121" 
	g.ntrp="F4.5" 
	g.mtype="NRF" 
	g.put()
#123 

	selfobj.response.write("Scott  Lenz  scott.lenz@Sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1432737836")) 
	g.year=2015
	g.fname="Scott"
	g.lname="Lenz"
	g.email="scott.lenz@Sbcglobal.net" 
	g.address="5938 Country Club Pkwy" 
	g.city="San Jose" 
	g.phone="(408) 531-1699" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#124 

	selfobj.response.write("Larry  Lessler  tttlessler@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1438811117")) 
	g.year=2015
	g.fname="Larry"
	g.lname="Lessler"
	g.email="tttlessler@gmail.com" 
	g.address="21372 Milford Dr" 
	g.city="Cupertino" 
	g.phone="(408) 307-6837" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#125 

	selfobj.response.write("Zuohua  Liang  zl_603@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1424377277")) 
	g.year=2015
	g.fname="Zuohua"
	g.lname="Liang"
	g.email="zl_603@yahoo.com" 
	g.address="10104 Imperial Ave" 
	g.city="Cupertino" 
	g.phone="(408) 253-2511" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#126 

	selfobj.response.write("Martin  Lim  martin998899@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1424376872")) 
	g.year=2015
	g.fname="Martin"
	g.lname="Lim"
	g.email="martin998899@gmail.com" 
	g.address="2368 Susan Dr" 
	g.city="Santa Clara" 
	g.phone="(408) 246-4137" 
	g.ntrp="M3.0" 
	g.mtype="RF" 
	g.put()
#127 

	selfobj.response.write("Janet  Lim  martin998899@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1424376965")) 
	g.year=2015
	g.fname="Janet"
	g.lname="Lim"
	g.email="martin998899@gmail.com" 
	g.address="2368 Susan Dr" 
	g.city="Santa Clara" 
	g.phone="(408) 246-4137" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#128 

	selfobj.response.write("Erin  Linke  alinke@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1429136202")) 
	g.year=2015
	g.fname="Erin"
	g.lname="Linke"
	g.email="alinke@yahoo.com" 
	g.address="1285 Main Street" 
	g.city="Santa Clara" 
	g.phone="() -" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#129 

	selfobj.response.write("Leila  Linke  alinke@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1429136294")) 
	g.year=2015
	g.fname="Leila"
	g.lname="Linke"
	g.email="alinke@yahoo.com" 
	g.address="1285 Main Street" 
	g.city="Santa Clara" 
	g.phone="() -" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#130 

	selfobj.response.write("Al  Linke  alinke2000@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1428540827")) 
	g.year=2015
	g.fname="Al"
	g.lname="Linke"
	g.email="alinke2000@gmail.com" 
	g.address="1285 Main Street" 
	g.city="Santa Clara" 
	g.phone="(408) 246-6828" 
	g.ntrp="M4.0" 
	g.mtype="RF" 
	g.put()
#131 

	selfobj.response.write("Mina  Linke  alinke@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1429136381")) 
	g.year=2015
	g.fname="Mina"
	g.lname="Linke"
	g.email="alinke@yahoo.com" 
	g.address="1285 Main Street" 
	g.city="Santa Clara" 
	g.phone="() -" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#132 

	selfobj.response.write("Weiwan  Liu  liudavis@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1421017088")) 
	g.year=2015
	g.fname="Weiwan"
	g.lname="Liu"
	g.email="liudavis@yahoo.com" 
	g.address="59 Cabot Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 598-0292" 
	g.ntrp="M3.0" 
	g.mtype="RF" 
	g.put()
#133 

	selfobj.response.write("Linda  Liu  liudavis@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1421017613")) 
	g.year=2015
	g.fname="Linda"
	g.lname="Liu"
	g.email="liudavis@yahoo.com" 
	g.address="59 Cabot Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 598-0292" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#134 

	selfobj.response.write("Kevin  Liu  liudavis@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1421017468")) 
	g.year=2015
	g.fname="Kevin"
	g.lname="Liu"
	g.email="liudavis@yahoo.com" 
	g.address="59 Cabot Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 598-0292" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#135 

	selfobj.response.write("Daniel  Lu  daniel.kee.lu@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1425398189")) 
	g.year=2015
	g.fname="Daniel"
	g.lname="Lu"
	g.email="daniel.kee.lu@gmail.com" 
	g.address="4319 Renaissance Dr Apt 318" 
	g.city="San Jose" 
	g.phone="(209) 242-4599" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#136 

	selfobj.response.write("mark  luo  marcluo777@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1445752334")) 
	g.year=2015
	g.fname="mark"
	g.lname="luo"
	g.email="marcluo777@gmail.com" 
	g.address="p.o.box 362288" 
	g.city="MILPITAS" 
	g.phone="(408) 657-9983" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#137 

	selfobj.response.write("Marshall  Madamba  mmadamba@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1426611795")) 
	g.year=2015
	g.fname="Marshall"
	g.lname="Madamba"
	g.email="mmadamba@gmail.com" 
	g.address="350 E Taylor St #6114" 
	g.city="San Jose" 
	g.phone="(408) 691-5652" 
	g.ntrp="M3.0" 
	g.mtype="NRF" 
	g.put()
#138 

	selfobj.response.write("Helena   Mak  menlogrowers1@aol.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1424914390")) 
	g.year=2015
	g.fname="Helena "
	g.lname="Mak"
	g.email="menlogrowers1@aol.com" 
	g.address="11605 New Ave." 
	g.city="Gilroy" 
	g.phone="(408) 427-1828" 
	g.ntrp="F3.0" 
	g.mtype="NRF_" 
	g.put()
#139 

	selfobj.response.write("James  Manning  jmanning54@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1435278195")) 
	g.year=2015
	g.fname="James"
	g.lname="Manning"
	g.email="jmanning54@gmail.com" 
	g.address="1255 Bracebridge Ct" 
	g.city="Campbell" 
	g.phone="(408) 805-8346" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#140 

	selfobj.response.write("Di  Mao  liudavis@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1421017542")) 
	g.year=2015
	g.fname="Di"
	g.lname="Mao"
	g.email="liudavis@yahoo.com" 
	g.address="59 Cabot Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 598-0292" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#141 

	selfobj.response.write("Stephen  Mao  stephen.a.mao@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1420171601")) 
	g.year=2015
	g.fname="Stephen"
	g.lname="Mao"
	g.email="stephen.a.mao@gmail.com" 
	g.address="826 Christopher Court" 
	g.city="Santa Clara" 
	g.phone="(832) 526-9142" 
	g.ntrp="M4.0" 
	g.mtype="RS" 
	g.put()
#142 

	selfobj.response.write("Luzmaria  Martinez  katsulas@aol.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1426611968")) 
	g.year=2015
	g.fname="Luzmaria"
	g.lname="Martinez"
	g.email="katsulas@aol.com" 
	g.address="350 E Taylor St #6114" 
	g.city="San Jose" 
	g.phone="(408) 691-5758" 
	g.ntrp="F3.5" 
	g.mtype="NRF_" 
	g.put()
#143 

	selfobj.response.write("Courtney  Martinez  loriv@me.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1419401373")) 
	g.year=2015
	g.fname="Courtney"
	g.lname="Martinez"
	g.email="loriv@me.com" 
	g.address="2653 Elliot Street" 
	g.city="Santa Clara" 
	g.phone="(408) 425-3420" 
	g.ntrp="F2.5" 
	g.mtype="RF_" 
	g.put()
#144 

	selfobj.response.write("Helen  Matsumoto  geetennis@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1422403224")) 
	g.year=2015
	g.fname="Helen"
	g.lname="Matsumoto"
	g.email="geetennis@yahoo.com" 
	g.address="1247 Redoaks Drive" 
	g.city="San Jose" 
	g.phone="(408) 248-7922" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#145 

	selfobj.response.write("Valerie  McCarthy  valeriebays@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1425519355")) 
	g.year=2015
	g.fname="Valerie"
	g.lname="McCarthy"
	g.email="valeriebays@gmail.com" 
	g.address="471 Tanoak Drive" 
	g.city="Santa Clara" 
	g.phone="(408) 355-4095" 
	g.ntrp="F3.0" 
	g.mtype="RS" 
	g.put()
#146 

	selfobj.response.write("Sally  McElravey  samcelravey@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1434947519")) 
	g.year=2015
	g.fname="Sally"
	g.lname="McElravey"
	g.email="samcelravey@gmail.com" 
	g.address="12486 Brookglen Drive" 
	g.city="Saratoga" 
	g.phone="(408) 255-3248" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#147 

	selfobj.response.write("Trevor  McGuire  temcguir@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1424558884")) 
	g.year=2015
	g.fname="Trevor"
	g.lname="McGuire"
	g.email="temcguir@gmail.com" 
	g.address="900 Pepper Tree Lane Apt. 212" 
	g.city="Santa Clara" 
	g.phone="(707) 799-0577" 
	g.ntrp="M3.5" 
	g.mtype="RF" 
	g.put()
#148 

	selfobj.response.write("Nathan Michael  Mertz  tennis61911@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1430272636")) 
	g.year=2015
	g.fname="Nathan Michael"
	g.lname="Mertz"
	g.email="tennis61911@yahoo.com" 
	g.address="2071 Bowers Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 469-0521" 
	g.ntrp="M4.0" 
	g.mtype="RS" 
	g.put()
#149 

	selfobj.response.write("Suzanne  Miller-Moody  clifton.moody@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1441660205")) 
	g.year=2015
	g.fname="Suzanne"
	g.lname="Miller-Moody"
	g.email="clifton.moody@gmail.com" 
	g.address="2528 Rose Way" 
	g.city="Santa Clara" 
	g.phone="(650) 380-3302" 
	g.ntrp="F" 
	g.mtype="RF" 
	g.put()
#150 

	selfobj.response.write("Nikhil  Mishra  nikhilgmishra@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1424641008")) 
	g.year=2015
	g.fname="Nikhil"
	g.lname="Mishra"
	g.email="nikhilgmishra@yahoo.com" 
	g.address="4390 Headen Way" 
	g.city="Santa Clara" 
	g.phone="(408) 540-8961" 
	g.ntrp="M3.0" 
	g.mtype="RF" 
	g.put()
#151 

	selfobj.response.write("Gil  Molina  molinateam@comcast.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1427341572")) 
	g.year=2015
	g.fname="Gil"
	g.lname="Molina"
	g.email="molinateam@comcast.net" 
	g.address="645 Starbush Dr" 
	g.city="Sunnyvale" 
	g.phone="() -" 
	g.ntrp="M" 
	g.mtype="NRS" 
	g.put()
#152 

	selfobj.response.write("Roy   Molseed  roy.molseed@vta.org")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1425398285")) 
	g.year=2015
	g.fname="Roy "
	g.lname="Molseed"
	g.email="roy.molseed@vta.org" 
	g.address="2550 Blue Rock Court" 
	g.city="San Jose" 
	g.phone="(408) 580-6396" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#153 

	selfobj.response.write("Matt  Montana  montanatopspin@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1424934188")) 
	g.year=2015
	g.fname="Matt"
	g.lname="Montana"
	g.email="montanatopspin@yahoo.com" 
	g.address="3440 El Camino Real #316" 
	g.city="Santa Clara" 
	g.phone="() -" 
	g.ntrp="M4.5" 
	g.mtype="RF_" 
	g.put()
#154 

	selfobj.response.write("Robert  Moody  clifton.moody@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1441660000")) 
	g.year=2015
	g.fname="Robert"
	g.lname="Moody"
	g.email="clifton.moody@gmail.com" 
	g.address="2528 Rose Way" 
	g.city="Santa Clara" 
	g.phone="(650) 380-3302" 
	g.ntrp="M" 
	g.mtype="RF" 
	g.put()
#155 

	selfobj.response.write("Waverley  Moody  clifton.moody@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1441660526")) 
	g.year=2015
	g.fname="Waverley"
	g.lname="Moody"
	g.email="clifton.moody@gmail.com" 
	g.address="2528 Rose Way" 
	g.city="Santa Clara" 
	g.phone="(650) 380-3302" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#156 

	selfobj.response.write("Jackson  Moody  clifton.moody@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1441660328")) 
	g.year=2015
	g.fname="Jackson"
	g.lname="Moody"
	g.email="clifton.moody@gmail.com" 
	g.address="2528 Rose Way" 
	g.city="Santa Clara" 
	g.phone="(650) 380-3302" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#157 

	selfobj.response.write("Gayle  Moore  tennissenior@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1435278376")) 
	g.year=2015
	g.fname="Gayle"
	g.lname="Moore"
	g.email="tennissenior@yahoo.com" 
	g.address="3115 Maurica Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 246-5129" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#158 

	selfobj.response.write("Roy  Morishige  morishige8@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1426816070")) 
	g.year=2015
	g.fname="Roy"
	g.lname="Morishige"
	g.email="morishige8@gmail.com" 
	g.address="1133 Bay Laurel Lane" 
	g.city="San Jose" 
	g.phone="(408) 684-1049" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#159 

	selfobj.response.write("Francisca  Mortensen   Back40@Creative-services.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1444864199")) 
	g.year=2015
	g.fname="Francisca"
	g.lname="Mortensen "
	g.email="Back40@Creative-services.com" 
	g.address="3584 IrlandaWay" 
	g.city="San Jose" 
	g.phone="(408) 410-7836" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#160 

	selfobj.response.write("Karl  Mosgofian  karlm@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1418172432")) 
	g.year=2015
	g.fname="Karl"
	g.lname="Mosgofian"
	g.email="karlm@yahoo.com" 
	g.address="1691 Cunningham St." 
	g.city="Santa Clara" 
	g.phone="(650) 520-1374" 
	g.ntrp="M3.0" 
	g.mtype="RS" 
	g.put()
#161 

	selfobj.response.write("Steve  Murata  stevemmurata@aol.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1438439862")) 
	g.year=2015
	g.fname="Steve"
	g.lname="Murata"
	g.email="stevemmurata@aol.com" 
	g.address="144 South Third Street Unit 242" 
	g.city="San Jose" 
	g.phone="(650) 740-4693" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#162 

	selfobj.response.write("Pradeep  Nair  pradeepn1@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1424751663")) 
	g.year=2015
	g.fname="Pradeep"
	g.lname="Nair"
	g.email="pradeepn1@gmail.com" 
	g.address="1921 Garzoni Place" 
	g.city="Santa Clara" 
	g.phone="(408) 839-1703" 
	g.ntrp="M4.0" 
	g.mtype="RS" 
	g.put()
#163 

	selfobj.response.write("Jon  Nakamoto  mayornakamoto@att.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1482989193")) 
	g.year=2015
	g.fname="Jon"
	g.lname="Nakamoto"
	g.email="mayornakamoto@att.net" 
	g.address="1349 Sierra Ave" 
	g.city="San Jose" 
	g.phone="() -" 
	g.ntrp="M3.5" 
	g.mtype="NRF" 
	g.put()
#164 

	selfobj.response.write("Su  Nakamoto  commander.nakamoto@att.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1482990004")) 
	g.year=2015
	g.fname="Su"
	g.lname="Nakamoto"
	g.email="commander.nakamoto@att.net" 
	g.address="1349 Sierra Ave" 
	g.city="San Jose" 
	g.phone="() -" 
	g.ntrp="M3.5" 
	g.mtype="NRF_" 
	g.put()
#165 

	selfobj.response.write("Shiv  Natarajan  shiv.natarajan@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1425456002")) 
	g.year=2015
	g.fname="Shiv"
	g.lname="Natarajan"
	g.email="shiv.natarajan@yahoo.com" 
	g.address="4813 Verbena Way" 
	g.city="San Jose" 
	g.phone="(408) 480-1044" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#166 

	selfobj.response.write("Kimberley  Nemeth  knemeth@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1419297638")) 
	g.year=2015
	g.fname="Kimberley"
	g.lname="Nemeth"
	g.email="knemeth@sbcglobal.net" 
	g.address="1610 sweetbriar dr" 
	g.city="san jose" 
	g.phone="(408) 266-9580" 
	g.ntrp="F3.5" 
	g.mtype="NRF" 
	g.put()
#167 

	selfobj.response.write("Sally  Nettleton  sallyjnettleton@hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1441915027")) 
	g.year=2015
	g.fname="Sally"
	g.lname="Nettleton"
	g.email="sallyjnettleton@hotmail.com" 
	g.address="22431 Palm Ave" 
	g.city="Cupetino" 
	g.phone="(408) 446-1426" 
	g.ntrp="F3.0" 
	g.mtype="NRS" 
	g.put()
#168 

	selfobj.response.write("Keith  Ng  kng@ix.netcom.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1420522613")) 
	g.year=2015
	g.fname="Keith"
	g.lname="Ng"
	g.email="kng@ix.netcom.com" 
	g.address="5660 Coniston Way" 
	g.city="San Jose, CA" 
	g.phone="(408) 204-5074" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#169 

	selfobj.response.write("Lloyd  Ngo  lloydngo@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1427341454")) 
	g.year=2015
	g.fname="Lloyd"
	g.lname="Ngo"
	g.email="lloydngo@yahoo.com" 
	g.address="3399 Victoria Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 891-1154" 
	g.ntrp="M" 
	g.mtype="RS" 
	g.put()
#170 

	selfobj.response.write("Dan Thao  Nguyen  aadent9@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1424216296")) 
	g.year=2015
	g.fname="Dan Thao"
	g.lname="Nguyen"
	g.email="aadent9@yahoo.com" 
	g.address="1500 Emory Street" 
	g.city="San Jose" 
	g.phone="(408) 315-0208" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#171 

	selfobj.response.write("Trang  Nguyen  trangie2000@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1418434493")) 
	g.year=2015
	g.fname="Trang"
	g.lname="Nguyen"
	g.email="trangie2000@yahoo.com" 
	g.address="322 CALIFORNIA ST" 
	g.city="CAMPBELL" 
	g.phone="(408) 761-3758" 
	g.ntrp="F3.0" 
	g.mtype="NRS" 
	g.put()
#172 

	selfobj.response.write("Thi  Nguyen  baothiy2k@Yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1424186113")) 
	g.year=2015
	g.fname="Thi"
	g.lname="Nguyen"
	g.email="baothiy2k@Yahoo.com" 
	g.address="2625 Hayward Dr" 
	g.city="Santa Clara" 
	g.phone="(408) 497-8889" 
	g.ntrp="F4.5" 
	g.mtype="RS" 
	g.put()
#173 

	selfobj.response.write("Nancy  Nii  udderniis@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1423811373")) 
	g.year=2015
	g.fname="Nancy"
	g.lname="Nii"
	g.email="udderniis@yahoo.com" 
	g.address="1838 Montemar Way" 
	g.city="San Jose" 
	g.phone="(408) 559-0747" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#174 

	selfobj.response.write("Carlos  Nino-de-Guzman  cng94087@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1429243639")) 
	g.year=2015
	g.fname="Carlos"
	g.lname="Nino-de-Guzman"
	g.email="cng94087@yahoo.com" 
	g.address="1085 Tasman Dr. - SPC 431" 
	g.city="Sunnyvale" 
	g.phone="(510) 300-4863" 
	g.ntrp="M" 
	g.mtype="NRS" 
	g.put()
#175 

	selfobj.response.write("Junko  Ohoka  junko.ohoka@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1423976638")) 
	g.year=2015
	g.fname="Junko"
	g.lname="Ohoka"
	g.email="junko.ohoka@gmail.com" 
	g.address="1007 Bryant Way" 
	g.city="Sunnyvale" 
	g.phone="(408) 245-2667" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#176 

	selfobj.response.write("Roger  Okamoto  tennis.mutt@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1424029787")) 
	g.year=2015
	g.fname="Roger"
	g.lname="Okamoto"
	g.email="tennis.mutt@gmail.com" 
	g.address="1349 Mariposa Ave" 
	g.city="San Jose" 
	g.phone="(408) 800-7646" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#177 

	selfobj.response.write("Ken  Okazaki  okaken1@aol.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1424387602")) 
	g.year=2015
	g.fname="Ken"
	g.lname="Okazaki"
	g.email="okaken1@aol.com" 
	g.address="814 Daffodil Way" 
	g.city="San Jose" 
	g.phone="(408) 387-0460" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#178 

	selfobj.response.write("Rachel  Okazaki  japanesegrace@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1425484833")) 
	g.year=2015
	g.fname="Rachel"
	g.lname="Okazaki"
	g.email="japanesegrace@gmail.com" 
	g.address="1390 Monroe St #8" 
	g.city="Santa Clara" 
	g.phone="(408) 390-2915" 
	g.ntrp="F4.0" 
	g.mtype="RF" 
	g.put()
#179 

	selfobj.response.write("Natsuko  Okumura  tomonatsu720@yahoo.co.jp")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1423361210")) 
	g.year=2015
	g.fname="Natsuko"
	g.lname="Okumura"
	g.email="tomonatsu720@yahoo.co.jp" 
	g.address="4271 Norwalk Dr Apt.X305" 
	g.city="Sanjose" 
	g.phone="(408) 221-3712" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#180 

	selfobj.response.write("Chester  Okuno  Chesterokuno@Gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1433483426")) 
	g.year=2015
	g.fname="Chester"
	g.lname="Okuno"
	g.email="Chesterokuno@Gmail.com" 
	g.address="1497 Miramonte Ave" 
	g.city="Los Altos" 
	g.phone="(408) 489-3142" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#181 

	selfobj.response.write("Della  Ong  dello2013@hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1434989310")) 
	g.year=2015
	g.fname="Della"
	g.lname="Ong"
	g.email="dello2013@hotmail.com" 
	g.address="5939 Friar way" 
	g.city="san jose" 
	g.phone="() -" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#182 

	selfobj.response.write("Jeanne  Oxford  JEANNEOXFORD@SBCGLOBAL.NET")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1419357337")) 
	g.year=2015
	g.fname="Jeanne"
	g.lname="Oxford"
	g.email="JEANNEOXFORD@SBCGLOBAL.NET" 
	g.address="3251 LOMA ALTA DRIVE" 
	g.city="SANTA CLARA" 
	g.phone="(408) 985-7901" 
	g.ntrp="F3.0" 
	g.mtype="RS" 
	g.put()
#183 

	selfobj.response.write("Pilar  Pablo  pilarlpablo@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1424012238")) 
	g.year=2015
	g.fname="Pilar"
	g.lname="Pablo"
	g.email="pilarlpablo@gmail.com" 
	g.address="15970 west road" 
	g.city="Los gatos" 
	g.phone="(408) 316-5073" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#184 

	selfobj.response.write("Sugam  Pandey  sugam.pandey@Gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1437144681")) 
	g.year=2015
	g.fname="Sugam"
	g.lname="Pandey"
	g.email="sugam.pandey@Gmail.com" 
	g.address="5255 stevens creek blvd, STE 218" 
	g.city="SANTA CLARA" 
	g.phone="(413) 687-4870" 
	g.ntrp="M3.0" 
	g.mtype="RS" 
	g.put()
#185 

	selfobj.response.write("Karen  Panian  Kpanian@Comcast.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1427089807")) 
	g.year=2015
	g.fname="Karen"
	g.lname="Panian"
	g.email="Kpanian@Comcast.net" 
	g.address="1704 Harrison st." 
	g.city="Santa Clara" 
	g.phone="(408) 313-8883" 
	g.ntrp="F3.5" 
	g.mtype="RS" 
	g.put()
#186 

	selfobj.response.write("Christine  Peters  ck.peters@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1423703240")) 
	g.year=2015
	g.fname="Christine"
	g.lname="Peters"
	g.email="ck.peters@sbcglobal.net" 
	g.address="1390 Saddle Rack St #349" 
	g.city="San Jose" 
	g.phone="(408) 279-4616" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#187 

	selfobj.response.write("Elisapeta  Peterson  peta.peterson@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1424054165")) 
	g.year=2015
	g.fname="Elisapeta"
	g.lname="Peterson"
	g.email="peta.peterson@sbcglobal.net" 
	g.address="13970 Saratoga Ave" 
	g.city="Saratogs" 
	g.phone="(408) 867-6947" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#188 

	selfobj.response.write("Bettye  Pham-Vo  bettyediem@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1423707833")) 
	g.year=2015
	g.fname="Bettye"
	g.lname="Pham-Vo"
	g.email="bettyediem@gmail.com" 
	g.address="3657 lisbon Ct." 
	g.city="San Jose" 
	g.phone="(408) 250-5658" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#189 

	selfobj.response.write("James  Pierce  jamesedwardpierce@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1425377018")) 
	g.year=2015
	g.fname="James"
	g.lname="Pierce"
	g.email="jamesedwardpierce@gmail.com" 
	g.address="3494 Quarry Park Dr" 
	g.city="San Jose" 
	g.phone="(408) 489-3880" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#190 

	selfobj.response.write("Balakumar  Rajendran  balakumar85@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1427220291")) 
	g.year=2015
	g.fname="Balakumar"
	g.lname="Rajendran"
	g.email="balakumar85@gmail.com" 
	g.address="3043 Rossmore Way" 
	g.city="San Jose" 
	g.phone="(513) 739-2747" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#191 

	selfobj.response.write("Vyass  Ramakrishnan  rvyass@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1424829563")) 
	g.year=2015
	g.fname="Vyass"
	g.lname="Ramakrishnan"
	g.email="rvyass@gmail.com" 
	g.address="2451 Mission College Blvd" 
	g.city="Santa Clara" 
	g.phone="(469) 213-9145" 
	g.ntrp="M3.5" 
	g.mtype="RS" 
	g.put()
#192 

	selfobj.response.write("Sanjay  Raval  sanjay_raval@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1422993350")) 
	g.year=2015
	g.fname="Sanjay"
	g.lname="Raval"
	g.email="sanjay_raval@yahoo.com" 
	g.address="Santa Clara" 
	g.city="Santa Clara" 
	g.phone="(408) 245-5445" 
	g.ntrp="M3.5" 
	g.mtype="RS" 
	g.put()
#193 

	selfobj.response.write("Aditya  Rawat  ad.rawat30@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1427732231")) 
	g.year=2015
	g.fname="Aditya"
	g.lname="Rawat"
	g.email="ad.rawat30@gmail.com" 
	g.address="600 Epic Way Unit 463" 
	g.city="San Jose" 
	g.phone="(219) 964-5051" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#194 

	selfobj.response.write("Larry  Rinek  lrinek@aol.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1430839237")) 
	g.year=2015
	g.fname="Larry"
	g.lname="Rinek"
	g.email="lrinek@aol.com" 
	g.address="80 Gilbert Avenue" 
	g.city="Santa Clara" 
	g.phone="(408) 248-3088" 
	g.ntrp="M3.5" 
	g.mtype="RS" 
	g.put()
#195 

	selfobj.response.write("Jennifer  Roberts  jennroberts2006@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1434948462")) 
	g.year=2015
	g.fname="Jennifer"
	g.lname="Roberts"
	g.email="jennroberts2006@gmail.com" 
	g.address="23863 Mountain Charlie Rd" 
	g.city="Los Gatos" 
	g.phone="(408) 353-3559" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#196 

	selfobj.response.write("Betty  Rooker  tenisbetty@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1432307897")) 
	g.year=2015
	g.fname="Betty"
	g.lname="Rooker"
	g.email="tenisbetty@gmail.com" 
	g.address="376 E. Washington Avenue #2" 
	g.city="Sunnyvale" 
	g.phone="(650) 776-1771" 
	g.ntrp="F" 
	g.mtype="NRS" 
	g.put()
#197 

	selfobj.response.write("Beatrice  Ruhland  beatricelouiser@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1419889383")) 
	g.year=2015
	g.fname="Beatrice"
	g.lname="Ruhland"
	g.email="beatricelouiser@gmail.com" 
	g.address="12562 corbetta lane" 
	g.city="los altos hills" 
	g.phone="(650) 917-1406" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#198 

	selfobj.response.write("Dolores  Salazar  kddsalazar@comcast.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1425701431")) 
	g.year=2015
	g.fname="Dolores"
	g.lname="Salazar"
	g.email="kddsalazar@comcast.net" 
	g.address="3376 Solano Ct." 
	g.city="Santa Clara" 
	g.phone="(408) 296-2379" 
	g.ntrp="F" 
	g.mtype="RS" 
	g.put()
#199 

	selfobj.response.write("Tracy  Schwartz  tracy.schwartz@comcast.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1426218241")) 
	g.year=2015
	g.fname="Tracy"
	g.lname="Schwartz"
	g.email="tracy.schwartz@comcast.net" 
	g.address="1264 Marilyn Drive" 
	g.city="Mountain View" 
	g.phone="(650) 961-7764" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#200 

	selfobj.response.write("Mei  See  meisee68@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1426816183")) 
	g.year=2015
	g.fname="Mei"
	g.lname="See"
	g.email="meisee68@yahoo.com" 
	g.address="1913 Magdalena Circle #109" 
	g.city="Santa Clara" 
	g.phone="(408) 480-1880" 
	g.ntrp="F3.0" 
	g.mtype="RS" 
	g.put()
#201 

	selfobj.response.write("Tony  Serksnis  tonyserks@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1437774555")) 
	g.year=2015
	g.fname="Tony"
	g.lname="Serksnis"
	g.email="tonyserks@gmail.com" 
	g.address="1305 LONGFELLOW WAY" 
	g.city="SAN JOSE" 
	g.phone="(408) 221-2659" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#202 

	selfobj.response.write("Cynthia  Shannon  cyn.tennis@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1421457109")) 
	g.year=2015
	g.fname="Cynthia"
	g.lname="Shannon"
	g.email="cyn.tennis@sbcglobal.net" 
	g.address="97 Waterside Circle" 
	g.city="Redwood City" 
	g.phone="(650) 598-9822" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#203 

	selfobj.response.write("Carol   Shields  carolsf37@aol.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1432433105")) 
	g.year=2015
	g.fname="Carol "
	g.lname="Shields"
	g.email="carolsf37@aol.com" 
	g.address="104 Plazoleta" 
	g.city="Los Gatos" 
	g.phone="(408) 656-0615" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#204 

	selfobj.response.write("Meike  Sillevis Smitt  meike.huizinga@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1418966934")) 
	g.year=2015
	g.fname="Meike"
	g.lname="Sillevis Smitt"
	g.email="meike.huizinga@gmail.com" 
	g.address="2360 Fairgrove Ct" 
	g.city="San Jose" 
	g.phone="(408) 373-4301" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#205 

	selfobj.response.write("Shirley  Silveria  shirlsil@hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1433479970")) 
	g.year=2015
	g.fname="Shirley"
	g.lname="Silveria"
	g.email="shirlsil@hotmail.com" 
	g.address="109 Altura Vista" 
	g.city="Los Gatos" 
	g.phone="(408) 354-0941" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#206 

	selfobj.response.write("Susan  Stulz  sstulz@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1424121658")) 
	g.year=2015
	g.fname="Susan"
	g.lname="Stulz"
	g.email="sstulz@gmail.com" 
	g.address="" 
	g.city="Los Altos" 
	g.phone="(  )    - " 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#207 

	selfobj.response.write("Tomoe  Tajima  tomoetajima@earthlink.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1424229120")) 
	g.year=2015
	g.fname="Tomoe"
	g.lname="Tajima"
	g.email="tomoetajima@earthlink.net" 
	g.address="1007 Bryant Way #A" 
	g.city="Sunnyvale" 
	g.phone="() -" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#208 

	selfobj.response.write("Yuko  Tasaka  ayratasaka@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1441249109")) 
	g.year=2015
	g.fname="Yuko"
	g.lname="Tasaka"
	g.email="ayratasaka@gmail.com" 
	g.address="19790 Auburn Dr." 
	g.city="Cupertino" 
	g.phone="(408) 533-5322" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#209 

	selfobj.response.write("Lourdes  Thevanayagam  namunak@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1425425691")) 
	g.year=2015
	g.fname="Lourdes"
	g.lname="Thevanayagam"
	g.email="namunak@yahoo.com" 
	g.address="1035A, Alta Mira Drive" 
	g.city="Santa Clara" 
	g.phone="(415) 748-1585" 
	g.ntrp="F" 
	g.mtype="RS" 
	g.put()
#210 

	selfobj.response.write("John  Toy  j.g.toy@lmco.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1434607244")) 
	g.year=2015
	g.fname="John"
	g.lname="Toy"
	g.email="j.g.toy@lmco.com" 
	g.address="4077 manzanita drive" 
	g.city="san jose" 
	g.phone="(408) 247-8179" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#211 

	selfobj.response.write("Thanhmy   Tran  thanhthien54@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1421362414")) 
	g.year=2015
	g.fname="Thanhmy "
	g.lname="Tran"
	g.email="thanhthien54@gmail.com" 
	g.address="750 Saratoga Ave; Apt # Y 104" 
	g.city="San Jose, Ca" 
	g.phone="(408) 227-8811" 
	g.ntrp="F3.0" 
	g.mtype="NRS" 
	g.put()
#212 

	selfobj.response.write("Truc  Tran  truc.ttrn@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1434518648")) 
	g.year=2015
	g.fname="Truc"
	g.lname="Tran"
	g.email="truc.ttrn@yahoo.com" 
	g.address="1732 Oswald Place" 
	g.city="Santa Clara" 
	g.phone="(408) 674-7419" 
	g.ntrp="M3.5" 
	g.mtype="RF" 
	g.put()
#213 

	selfobj.response.write("Minh  Tran  truc.ttrn@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1434518938")) 
	g.year=2015
	g.fname="Minh"
	g.lname="Tran"
	g.email="truc.ttrn@yahoo.com" 
	g.address="1732 Oswald Place" 
	g.city="Santa Clara" 
	g.phone="(408) 674-7419" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#214 

	selfobj.response.write("Debbie  Tripiano  dtripiano@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1423861727")) 
	g.year=2015
	g.fname="Debbie"
	g.lname="Tripiano"
	g.email="dtripiano@gmail.com" 
	g.address="1362 Merrivale West Square" 
	g.city="San Jose" 
	g.phone="(408) 772-6104" 
	g.ntrp="F4.0" 
	g.mtype="NRF" 
	g.put()
#215 

	selfobj.response.write("Thomas  Truong  thomas_g_truong@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1426813007")) 
	g.year=2015
	g.fname="Thomas"
	g.lname="Truong"
	g.email="thomas_g_truong@yahoo.com" 
	g.address="2167 Weston Pl" 
	g.city="Santa Clara" 
	g.phone="(408) 219-2377" 
	g.ntrp="M4.0" 
	g.mtype="RS" 
	g.put()
#216 

	selfobj.response.write("John  Tsutsui  john.tsutsui@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1421129377")) 
	g.year=2015
	g.fname="John"
	g.lname="Tsutsui"
	g.email="john.tsutsui@gmail.com" 
	g.address="32 Wistaria Way" 
	g.city="Santa Clara" 
	g.phone="(408) 206-0496" 
	g.ntrp="M4.0" 
	g.mtype="RF" 
	g.put()
#217 

	selfobj.response.write("Suzanne  Tuchler  suztuchler@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1420333003")) 
	g.year=2015
	g.fname="Suzanne"
	g.lname="Tuchler"
	g.email="suztuchler@gmail.com" 
	g.address="2161 Tankit Drive" 
	g.city="Campbell" 
	g.phone="(408) 307-6900" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#218 

	selfobj.response.write("Lori  Ventura  Loriv@Me.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1419312829")) 
	g.year=2015
	g.fname="Lori"
	g.lname="Ventura"
	g.email="Loriv@Me.com" 
	g.address="2653 Elliot Street" 
	g.city="Santa Clara" 
	g.phone="(408) 425-3420" 
	g.ntrp="F4.0" 
	g.mtype="RF" 
	g.put()
#219 

	selfobj.response.write("Vince  Ventura  loriv@me.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1419401307")) 
	g.year=2015
	g.fname="Vince"
	g.lname="Ventura"
	g.email="loriv@me.com" 
	g.address="2653 Elliot Street" 
	g.city="Santa Clara" 
	g.phone="(408) 425-3420" 
	g.ntrp="M2.5" 
	g.mtype="RF_" 
	g.put()
#220 

	selfobj.response.write("Ryan  Ventura  loriv@me.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1419401330")) 
	g.year=2015
	g.fname="Ryan"
	g.lname="Ventura"
	g.email="loriv@me.com" 
	g.address="2653 Elliot Street" 
	g.city="Santa Clara" 
	g.phone="(408) 425-3420" 
	g.ntrp="M2.5" 
	g.mtype="RF_" 
	g.put()
#221 

	selfobj.response.write("Michael   Vogel  menlogrowers1@aol.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1424913587")) 
	g.year=2015
	g.fname="Michael "
	g.lname="Vogel"
	g.email="menlogrowers1@aol.com" 
	g.address="11605 New Ave." 
	g.city="Gilroy" 
	g.phone="(408) 427-1828" 
	g.ntrp="M3.5" 
	g.mtype="NRF" 
	g.put()
#222 

	selfobj.response.write("Katsue  Watts  katsuew@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1425240266")) 
	g.year=2015
	g.fname="Katsue"
	g.lname="Watts"
	g.email="katsuew@yahoo.com" 
	g.address="3480 Granada Ave. APT #204" 
	g.city="Santa Clara" 
	g.phone="(650) 201-2896" 
	g.ntrp="F3.0" 
	g.mtype="RS" 
	g.put()
#223 

	selfobj.response.write("Nason  Wessel  brianwessel2013@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1427683524")) 
	g.year=2015
	g.fname="Nason"
	g.lname="Wessel"
	g.email="brianwessel2013@gmail.com" 
	g.address="555 S. Park Victoria Dr. #303" 
	g.city="Milpitas" 
	g.phone="(928) 245-1340" 
	g.ntrp="M" 
	g.mtype="NRF_" 
	g.put()
#224 

	selfobj.response.write("Brian  Wessel  brianwessel_2000@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1427672175")) 
	g.year=2015
	g.fname="Brian"
	g.lname="Wessel"
	g.email="brianwessel_2000@yahoo.com" 
	g.address="555 S. Park Victoria Dr. #303" 
	g.city="Milpitas" 
	g.phone="(928) 245-1340" 
	g.ntrp="M4.0" 
	g.mtype="NRF" 
	g.put()
#225 

	selfobj.response.write("Salaneta  Wessel  salaneta@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1427682929")) 
	g.year=2015
	g.fname="Salaneta"
	g.lname="Wessel"
	g.email="salaneta@yahoo.com" 
	g.address="555 S. Park Victoria Dr. #303" 
	g.city="Milpitas" 
	g.phone="(928) 379-3576" 
	g.ntrp="F3.0" 
	g.mtype="NRF_" 
	g.put()
#226 

	selfobj.response.write("Jason   Wu  jcwu84@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1427168076")) 
	g.year=2015
	g.fname="Jason "
	g.lname="Wu"
	g.email="jcwu84@gmail.com" 
	g.address="633 Callippe Ct" 
	g.city="Brisbane" 
	g.phone="(650) 278-9118" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#227 

	selfobj.response.write("Warren  Yamaguchi  winini@comcast.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1423861953")) 
	g.year=2015
	g.fname="Warren"
	g.lname="Yamaguchi"
	g.email="winini@comcast.net" 
	g.address="1362 Merrivale West Square" 
	g.city="San Jose" 
	g.phone="(408) 772-6104" 
	g.ntrp="M4.0" 
	g.mtype="NRF_" 
	g.put()
#228 

	selfobj.response.write("Yasumitsu  Yamamoto  yasu@yasuyamamoto.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1434606915")) 
	g.year=2015
	g.fname="Yasumitsu"
	g.lname="Yamamoto"
	g.email="yasu@yasuyamamoto.com" 
	g.address="2246 Francis Avenue" 
	g.city="Santa Clara" 
	g.phone="(408) 205-6801" 
	g.ntrp="M4.0" 
	g.mtype="RS" 
	g.put()
#229 

	selfobj.response.write("Irene  Ydens  irene@ydens.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1432304578")) 
	g.year=2015
	g.fname="Irene"
	g.lname="Ydens"
	g.email="irene@ydens.com" 
	g.address="263 West Latimer Avenue" 
	g.city="Campbell" 
	g.phone="(408) 761-5612" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
