

#
#
#select * from paypal where year = "2017"  union select * from bycheck where year =  "2017" order by year,lname 
#
#
import webapp2
from datastore import  *


def santaclara2017(selfobj):


#1 

	selfobj.response.write("Karen  Abad  abadkj@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1491519046")) 
	g.year=2017
	g.fname="Karen"
	g.lname="Abad"
	g.email="abadkj@sbcglobal.net" 
	g.address="2786 Eversole Drive" 
	g.city="San Jose" 
	g.phone="(408) 499-8279" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#2 

	selfobj.response.write("Jennifer  Adams  jenyferadams@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1486357847")) 
	g.year=2017
	g.fname="Jennifer"
	g.lname="Adams"
	g.email="jenyferadams@sbcglobal.net" 
	g.address="847 Colleen Drive" 
	g.city="San Jose" 
	g.phone="(408) 313-4405" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#3 

	selfobj.response.write("Sanjay  Agarwal  agarwalsanjay@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1487978787")) 
	g.year=2017
	g.fname="Sanjay"
	g.lname="Agarwal"
	g.email="agarwalsanjay@gmail.com" 
	g.address="4231 Norwalk Dr, Apt EE101" 
	g.city="San Jose" 
	g.phone="(408) 839-6887" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#4 

	selfobj.response.write("Alok  Aggarwal  alok.cdac@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1487705518")) 
	g.year=2017
	g.fname="Alok"
	g.lname="Aggarwal"
	g.email="alok.cdac@gmail.com" 
	g.address="501 Murphy Ranch Road, Apt 429" 
	g.city="Milpitas" 
	g.phone="(510) 925-6995" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#5 

	selfobj.response.write("Sreenivas  Aluru  salur1@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1483323409")) 
	g.year=2017
	g.fname="Sreenivas"
	g.lname="Aluru"
	g.email="salur1@yahoo.com" 
	g.address="10816 Alderbrook ln" 
	g.city="Cupertino" 
	g.phone="(408) 406-1885" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#6 

	selfobj.response.write("Mark  Alves  markalves01@aol.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1491409409")) 
	g.year=2017
	g.fname="Mark"
	g.lname="Alves"
	g.email="markalves01@aol.com" 
	g.address="1491 Bellomy St" 
	g.city="Santa Clara" 
	g.phone="(408) 205-4389" 
	g.ntrp="M3.0" 
	g.mtype="RS" 
	g.put()
#7 

	selfobj.response.write("Nancy  Andersen  nbragaandersen@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1488386464")) 
	g.year=2017
	g.fname="Nancy"
	g.lname="Andersen"
	g.email="nbragaandersen@gmail.com" 
	g.address="3032 Cameron Way" 
	g.city="Santa Clara" 
	g.phone="(408) 799-3678" 
	g.ntrp="F3.5" 
	g.mtype="RF" 
	g.put()
#8 

	selfobj.response.write("Brooke  Andrews  rvbrooke@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1501800229")) 
	g.year=2017
	g.fname="Brooke"
	g.lname="Andrews"
	g.email="rvbrooke@gmail.com" 
	g.address="P O Box 56109" 
	g.city="San Jose" 
	g.phone="(408) 921-5017" 
	g.ntrp="F2.5" 
	g.mtype="NRS" 
	g.put()
#9 

	selfobj.response.write("Hideko  Azama  tennissenior@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1494913887")) 
	g.year=2017
	g.fname="Hideko"
	g.lname="Azama"
	g.email="tennissenior@yahoo.com" 
	g.address="3115 Maurica Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 246-5129" 
	g.ntrp="F3.5" 
	g.mtype="RS" 
	g.put()
#10 

	selfobj.response.write("Matt  Bays  mbayse@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1480890110")) 
	g.year=2017
	g.fname="Matt"
	g.lname="Bays"
	g.email="mbayse@gmail.com" 
	g.address="471 Tanoak Drive" 
	g.city="Santa Clara" 
	g.phone="(408) 355-4095" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#11 

	selfobj.response.write("Naoko  Bean  naokobean@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1494714725")) 
	g.year=2017
	g.fname="Naoko"
	g.lname="Bean"
	g.email="naokobean@yahoo.com" 
	g.address="3440 El Camino Real #316" 
	g.city="Santa Clara" 
	g.phone="(408) 888-2290" 
	g.ntrp="F4.5" 
	g.mtype="RS" 
	g.put()
#12 

	selfobj.response.write("Chris  Becker (Andersen)  nbragaandersen@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1488387611")) 
	g.year=2017
	g.fname="Chris"
	g.lname="Becker (Andersen)"
	g.email="nbragaandersen@gmail.com" 
	g.address="3032 Cameron Way" 
	g.city="Santa Clara" 
	g.phone="(408) 984-5489" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#13 

	selfobj.response.write("Khalid  Beg  mirzakzbeg@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1491538287")) 
	g.year=2017
	g.fname="Khalid"
	g.lname="Beg"
	g.email="mirzakzbeg@gmail.com" 
	g.address="270 Calvert Dr" 
	g.city="Santa Clara" 
	g.phone="(408) 707-8346" 
	g.ntrp="M" 
	g.mtype="RS" 
	g.put()
#14 

	selfobj.response.write("Nikhat  Beg  mirzakzbeg@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1493947318")) 
	g.year=2017
	g.fname="Nikhat"
	g.lname="Beg"
	g.email="mirzakzbeg@gmail.com" 
	g.address="270 Calvert Dr" 
	g.city="Santa Clara" 
	g.phone="(408) 707-8346" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#15 

	selfobj.response.write("Jonathan  Bell  c.p.bell@att.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1482545237")) 
	g.year=2017
	g.fname="Jonathan"
	g.lname="Bell"
	g.email="c.p.bell@att.net" 
	g.address="1244 Maryann Drive" 
	g.city="Santa Clara" 
	g.phone="(408) 464-3177" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#16 

	selfobj.response.write("Randy  Bell  c.p.bell@att.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1482542574")) 
	g.year=2017
	g.fname="Randy"
	g.lname="Bell"
	g.email="c.p.bell@att.net" 
	g.address="1244 Maryann Drive" 
	g.city="Santa Clara" 
	g.phone="(408) 464-3177" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#17 

	selfobj.response.write("Carrie  Bell  c.p.bell@att.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1482523313")) 
	g.year=2017
	g.fname="Carrie"
	g.lname="Bell"
	g.email="c.p.bell@att.net" 
	g.address="1244 Maryann Drive" 
	g.city="Santa Clara" 
	g.phone="(408) 464-3177" 
	g.ntrp="F4.0" 
	g.mtype="RF" 
	g.put()
#18 

	selfobj.response.write("Ben   Borowiec  c.p.bell@att.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1494891408")) 
	g.year=2017
	g.fname="Ben "
	g.lname="Borowiec"
	g.email="c.p.bell@att.net" 
	g.address="166 Muir Ave." 
	g.city="Santa Clara" 
	g.phone="(408) 464-3177" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#19 

	selfobj.response.write("Brax  Borowiec  c.p.bell@att.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1494891564")) 
	g.year=2017
	g.fname="Brax"
	g.lname="Borowiec"
	g.email="c.p.bell@att.net" 
	g.address="166 Muir Ave." 
	g.city="Santa Clara" 
	g.phone="(408) 464-3177" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#20 

	selfobj.response.write("Kelly  Borowiec  c.p.bell@att.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1494891216")) 
	g.year=2017
	g.fname="Kelly"
	g.lname="Borowiec"
	g.email="c.p.bell@att.net" 
	g.address="166 Muir Ave." 
	g.city="Santa Clara" 
	g.phone="(408) 464-3177" 
	g.ntrp="F" 
	g.mtype="RF" 
	g.put()
#21 

	selfobj.response.write("Greg  Borromeo  triplegg1956@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1507670508")) 
	g.year=2017
	g.fname="Greg"
	g.lname="Borromeo"
	g.email="triplegg1956@yahoo.com" 
	g.address="3743 Acapulco Drive" 
	g.city="Campbell" 
	g.phone="() -" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#22 

	selfobj.response.write("Robert  Brunkhorst  bob.brunkhorst@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1483485189")) 
	g.year=2017
	g.fname="Robert"
	g.lname="Brunkhorst"
	g.email="bob.brunkhorst@gmail.com" 
	g.address="849 Humewick Way" 
	g.city="Sunnyvale" 
	g.phone="(408) 667-5902" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#23 

	selfobj.response.write("Ike  Bunanta  ibunanta@mac.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1484698277")) 
	g.year=2017
	g.fname="Ike"
	g.lname="Bunanta"
	g.email="ibunanta@mac.com" 
	g.address="15070 Stratford Ct." 
	g.city="Monte Sereno" 
	g.phone="(408) 406-5830" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#24 

	selfobj.response.write("Hilary  Butler  butler.hilary@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1486061729")) 
	g.year=2017
	g.fname="Hilary"
	g.lname="Butler"
	g.email="butler.hilary@gmail.com" 
	g.address="18310 Daves Ave" 
	g.city="Monte Sereno" 
	g.phone="(408) 621-7234" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#25 

	selfobj.response.write("Gary  Buzzell  Gary.Buzzell@siemens-healthineers.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1491610004")) 
	g.year=2017
	g.fname="Gary"
	g.lname="Buzzell"
	g.email="Gary.Buzzell@siemens-healthineers.com" 
	g.address="847 Pagoda Tree Ct" 
	g.city="Sunnyvale" 
	g.phone="(650) 417-5065" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#26 

	selfobj.response.write("Thomas  Calvello  volgab@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1488746925")) 
	g.year=2017
	g.fname="Thomas"
	g.lname="Calvello"
	g.email="volgab@yahoo.com" 
	g.address="1974 Homestead" 
	g.city="Santa Clara" 
	g.phone="(650) 303-1151" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#27 

	selfobj.response.write("Volga  Calvello  volgab@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1488746763")) 
	g.year=2017
	g.fname="Volga"
	g.lname="Calvello"
	g.email="volgab@yahoo.com" 
	g.address="1974 Homestead" 
	g.city="Santa Clara" 
	g.phone="(650) 303-1151" 
	g.ntrp="F" 
	g.mtype="RF" 
	g.put()
#28 

	selfobj.response.write("Kathy  Camet  kygc333@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1490227696")) 
	g.year=2017
	g.fname="Kathy"
	g.lname="Camet"
	g.email="kygc333@gmail.com" 
	g.address="910 Forest Ridge Drive" 
	g.city="San Jose" 
	g.phone="(408) 368-9456" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#29 

	selfobj.response.write("Theresa B  Campbell  tbcampbell@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1483840841")) 
	g.year=2017
	g.fname="Theresa B"
	g.lname="Campbell"
	g.email="tbcampbell@sbcglobal.net" 
	g.address="1379 Country Club Drive" 
	g.city="Los Altos" 
	g.phone="(650) 996-0646" 
	g.ntrp="F3.0" 
	g.mtype="NRS" 
	g.put()
#30 

	selfobj.response.write("Delia  Cannon  nbragaandersen@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1488387732")) 
	g.year=2017
	g.fname="Delia"
	g.lname="Cannon"
	g.email="nbragaandersen@gmail.com" 
	g.address="3032 Cameron Way" 
	g.city="Santa Clara" 
	g.phone="(408) 985-5489" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#31 

	selfobj.response.write("Natalie  Cannon  nbragaandersen@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1488388091")) 
	g.year=2017
	g.fname="Natalie"
	g.lname="Cannon"
	g.email="nbragaandersen@gmail.com" 
	g.address="3032 Cameron Way" 
	g.city="Santa Clara" 
	g.phone="(408) 799-3678" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#32 

	selfobj.response.write("Francesca  Cappellini  volgab@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1488747011")) 
	g.year=2017
	g.fname="Francesca"
	g.lname="Cappellini"
	g.email="volgab@yahoo.com" 
	g.address="1974 Homestead" 
	g.city="Santa Clara" 
	g.phone="(650) 303-1151" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#33 

	selfobj.response.write("Alessandro  Cappellini  volgab@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1488746956")) 
	g.year=2017
	g.fname="Alessandro"
	g.lname="Cappellini"
	g.email="volgab@yahoo.com" 
	g.address="1974 Homestead" 
	g.city="Santa Clara" 
	g.phone="(650) 303-1151" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#34 

	selfobj.response.write("Cristy  Cappellini  volgab@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1488746984")) 
	g.year=2017
	g.fname="Cristy"
	g.lname="Cappellini"
	g.email="volgab@yahoo.com" 
	g.address="1974 Homestead" 
	g.city="Santa Clara" 
	g.phone="(650) 303-1151" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#35 

	selfobj.response.write("Wendy Wei Hwa  Cheng  wendcheng@hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1490648867")) 
	g.year=2017
	g.fname="Wendy Wei Hwa"
	g.lname="Cheng"
	g.email="wendcheng@hotmail.com" 
	g.address="1000 Kiely blvd #201" 
	g.city="Santa Clara" 
	g.phone="(408) 910-1676" 
	g.ntrp="F4.5" 
	g.mtype="RS" 
	g.put()
#36 

	selfobj.response.write("Patty  Cheng  pochuncheng@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1486750992")) 
	g.year=2017
	g.fname="Patty"
	g.lname="Cheng"
	g.email="pochuncheng@gmail.com" 
	g.address="3175 Emerson St." 
	g.city="Palo Alto" 
	g.phone="(646) 541-5271" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#37 

	selfobj.response.write("Myoung Taeck  Chiang  taeckchiang@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1491518533")) 
	g.year=2017
	g.fname="Myoung Taeck"
	g.lname="Chiang"
	g.email="taeckchiang@gmail.com" 
	g.address="1235 De Altura Commons" 
	g.city="San Jose" 
	g.phone="(408) 306-3657" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#38 

	selfobj.response.write("Paul   Choe  paulichoe@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1494952535")) 
	g.year=2017
	g.fname="Paul "
	g.lname="Choe"
	g.email="paulichoe@sbcglobal.net" 
	g.address="941 Lorne Way" 
	g.city="Sunnyvale" 
	g.phone="(408) 893-7374" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#39 

	selfobj.response.write("Deepak  Chotrani  deepak_c15@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1488928124")) 
	g.year=2017
	g.fname="Deepak"
	g.lname="Chotrani"
	g.email="deepak_c15@yahoo.com" 
	g.address="3722 Europe Ct" 
	g.city="Santa Clara" 
	g.phone="(607) 351-0812" 
	g.ntrp="M4.0" 
	g.mtype="RS" 
	g.put()
#40 

	selfobj.response.write("Ramon  Crichlow  ramon@nanoair.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1500004437")) 
	g.year=2017
	g.fname="Ramon"
	g.lname="Crichlow"
	g.email="ramon@nanoair.com" 
	g.address="2900 hearth place" 
	g.city="santa clara" 
	g.phone="(650) 237-9871" 
	g.ntrp="M3.5" 
	g.mtype="RS" 
	g.put()
#41 

	selfobj.response.write("Liliane  Cromer  lilianec@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1483393036")) 
	g.year=2017
	g.fname="Liliane"
	g.lname="Cromer"
	g.email="lilianec@sbcglobal.net" 
	g.address="14120 Palomino Ways" 
	g.city="Saratoga" 
	g.phone="(408) 823-6448" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#42 

	selfobj.response.write("Jason  Cvitkovich  wendcheng@hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1494111107")) 
	g.year=2017
	g.fname="Jason"
	g.lname="Cvitkovich"
	g.email="wendcheng@hotmail.com" 
	g.address="1000 Kiely blvd #201" 
	g.city="Santa Clara" 
	g.phone="(408) 910-1676" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#43 

	selfobj.response.write("Machiko  Cyr  machikoc@pacbell.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1483897093")) 
	g.year=2017
	g.fname="Machiko"
	g.lname="Cyr"
	g.email="machikoc@pacbell.net" 
	g.address="5518 Castle Manor Dr." 
	g.city="San Jose" 
	g.phone="(408) 315-7606" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#44 

	selfobj.response.write("Thomas  Dang  t.dunham24@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1481521367")) 
	g.year=2017
	g.fname="Thomas"
	g.lname="Dang"
	g.email="t.dunham24@gmail.com" 
	g.address="3666 Franklin ave." 
	g.city="Fremont" 
	g.phone="(510) 673-6300" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#45 

	selfobj.response.write("Brian  Dang  briandang000@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1487136469")) 
	g.year=2017
	g.fname="Brian"
	g.lname="Dang"
	g.email="briandang000@yahoo.com" 
	g.address="1961 Linden Ln" 
	g.city="Milpitas" 
	g.phone="(408) 712-8450" 
	g.ntrp="M3.0" 
	g.mtype="NRS" 
	g.put()
#46 

	selfobj.response.write("jessica  de bosson  jessica4tennis@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1504334008")) 
	g.year=2017
	g.fname="jessica"
	g.lname="de bosson"
	g.email="jessica4tennis@gmail.com" 
	g.address="5273 coco palm drive" 
	g.city="fremont" 
	g.phone="(510) 366-4118" 
	g.ntrp="F3.0" 
	g.mtype="NRS" 
	g.put()
#47 

	selfobj.response.write("Onofre  de Souza  onofre2237@aol.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1489344244")) 
	g.year=2017
	g.fname="Onofre"
	g.lname="de Souza"
	g.email="onofre2237@aol.com" 
	g.address="2983 Millar Ave" 
	g.city="Santa Clara,CA." 
	g.phone="(408) 386-4862" 
	g.ntrp="M" 
	g.mtype="RS" 
	g.put()
#48 

	selfobj.response.write("Michelle  Deguzman  Mpdeguz@Gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1491516240")) 
	g.year=2017
	g.fname="Michelle"
	g.lname="Deguzman"
	g.email="Mpdeguz@Gmail.com" 
	g.address="3607 Kendra way" 
	g.city="San jose" 
	g.phone="(201) 951-5525" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#49 

	selfobj.response.write("Ahad  Dil  Ahadf5050@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1483654822")) 
	g.year=2017
	g.fname="Ahad"
	g.lname="Dil"
	g.email="Ahadf5050@gmail.com" 
	g.address="1700 Ponca Ct" 
	g.city="Fremont" 
	g.phone="(510) 491-5050" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#50 

	selfobj.response.write("Diep  Doan  thacdoan3060@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1491892062")) 
	g.year=2017
	g.fname="Diep"
	g.lname="Doan"
	g.email="thacdoan3060@gmail.com" 
	g.address="3060 Dibble Court" 
	g.city="Santa Clara" 
	g.phone="(408) 996-9717" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#51 

	selfobj.response.write("Quynh  Doan  quintus162@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1491892009")) 
	g.year=2017
	g.fname="Quynh"
	g.lname="Doan"
	g.email="quintus162@gmail.com" 
	g.address="3060 Dibble Court" 
	g.city="Santa Clara" 
	g.phone="(408) 996-9717" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#52 

	selfobj.response.write("Thac  Doan  thacdoan3060@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1491891860")) 
	g.year=2017
	g.fname="Thac"
	g.lname="Doan"
	g.email="thacdoan3060@gmail.com" 
	g.address="3060 Dibble Court" 
	g.city="Santa Clara" 
	g.phone="(408) 996-9717" 
	g.ntrp="M" 
	g.mtype="RF" 
	g.put()
#53 

	selfobj.response.write("Lisa  Doan  thacdoan3060@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1491891946")) 
	g.year=2017
	g.fname="Lisa"
	g.lname="Doan"
	g.email="thacdoan3060@gmail.com" 
	g.address="3060 Dibble Court" 
	g.city="Santa Clara" 
	g.phone="(408) 996-9717" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#54 

	selfobj.response.write("Chandrakant  Dollin  cdollin@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1484612630")) 
	g.year=2017
	g.fname="Chandrakant"
	g.lname="Dollin"
	g.email="cdollin@yahoo.com" 
	g.address="1151 Topaz Ave" 
	g.city="San Jose" 
	g.phone="(408) 425-2020" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#55 

	selfobj.response.write("Susan   Domingo  Suskidoll@Gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1502225841")) 
	g.year=2017
	g.fname="Susan "
	g.lname="Domingo"
	g.email="Suskidoll@Gmail.com" 
	g.address="866 Brookline Drive" 
	g.city="Sunnyvale" 
	g.phone="(408) 348-0380" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#56 

	selfobj.response.write("Consuelo  Domingo  conniedomingo@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1483458464")) 
	g.year=2017
	g.fname="Consuelo"
	g.lname="Domingo"
	g.email="conniedomingo@sbcglobal.net" 
	g.address="25627 Franklin Avenue" 
	g.city="Hayward" 
	g.phone="(408) 646-8654" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#57 

	selfobj.response.write("Sara  Durkin  glassford.sara@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1497025733")) 
	g.year=2017
	g.fname="Sara"
	g.lname="Durkin"
	g.email="glassford.sara@gmail.com" 
	g.address="1283 W McKinley Ave #8" 
	g.city="Sunnyvale" 
	g.phone="(920) 254-6344" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#58 

	selfobj.response.write("Susanne  Edgerton  smedgerton@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1504299650")) 
	g.year=2017
	g.fname="Susanne"
	g.lname="Edgerton"
	g.email="smedgerton@yahoo.com" 
	g.address="737Henrietta Avenue" 
	g.city="Sunnyvale" 
	g.phone="(408) 940-2172" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#59 

	selfobj.response.write("Kaori  Enomoto  kaori@saphirellc.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1487647609")) 
	g.year=2017
	g.fname="Kaori"
	g.lname="Enomoto"
	g.email="kaori@saphirellc.com" 
	g.address="851 W. Remington Dr." 
	g.city="Sunnyvale" 
	g.phone="(408) 623-5702" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#60 

	selfobj.response.write("Marie  Fan  msfan00@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1483840366")) 
	g.year=2017
	g.fname="Marie"
	g.lname="Fan"
	g.email="msfan00@yahoo.com" 
	g.address="1297 Weibel Way" 
	g.city="San Jose" 
	g.phone="(408) 332-6026" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#61 

	selfobj.response.write("Kaddie  Feng-Ashley  k417tennis@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1501277233")) 
	g.year=2017
	g.fname="Kaddie"
	g.lname="Feng-Ashley"
	g.email="k417tennis@gmail.com" 
	g.address="17245 James Ln" 
	g.city="Morgan Hill" 
	g.phone="(408) 776-2734" 
	g.ntrp="F3.0" 
	g.mtype="NRS" 
	g.put()
#62 

	selfobj.response.write("Jackie  Fenton  jdfenton26@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1488417026")) 
	g.year=2017
	g.fname="Jackie"
	g.lname="Fenton"
	g.email="jdfenton26@gmail.com" 
	g.address="536 Hawthorne Ave apt C" 
	g.city="Palo Alto" 
	g.phone="(443) 812-4374" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#63 

	selfobj.response.write("Ed  Fletcher  fletcherian@mac.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1484298352")) 
	g.year=2017
	g.fname="Ed"
	g.lname="Fletcher"
	g.email="fletcherian@mac.com" 
	g.address="869 Hilmar Street" 
	g.city="Santa Clara" 
	g.phone="(650) 492-1925" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#64 

	selfobj.response.write("Amanda   Fletcher   puffthemagicrabbit@me.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1484298920")) 
	g.year=2017
	g.fname="Amanda "
	g.lname="Fletcher "
	g.email="puffthemagicrabbit@me.com" 
	g.address="869 Hilmar Street" 
	g.city="Santa Clara" 
	g.phone="(650) 224-9616" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#65 

	selfobj.response.write("Audrey  Fletcher  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1484298534")) 
	g.year=2017
	g.fname="Audrey"
	g.lname="Fletcher"
	g.email="" 
	g.address="869 Hilmar Street" 
	g.city="Santa Clara" 
	g.phone="(650) 492-1930" 
	g.ntrp="F3.0" 
	g.mtype="RF_" 
	g.put()
#66 

	selfobj.response.write("Laura   Fletcher   fletch4him1@mac.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1484298150")) 
	g.year=2017
	g.fname="Laura "
	g.lname="Fletcher "
	g.email="fletch4him1@mac.com" 
	g.address="869 Hilmar Street" 
	g.city="Santa Clara" 
	g.phone="(650) 492-1930" 
	g.ntrp="F3.5" 
	g.mtype="RF" 
	g.put()
#67 

	selfobj.response.write("Arielle   Fletcher  annonsfootprints@me.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1484298699")) 
	g.year=2017
	g.fname="Arielle "
	g.lname="Fletcher"
	g.email="annonsfootprints@me.com" 
	g.address="869 Hilmar Street" 
	g.city="Santa Clara" 
	g.phone="(650) 224-1107" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#68 

	selfobj.response.write("Janelle   Flores  janelle.c.flores@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1488396772")) 
	g.year=2017
	g.fname="Janelle "
	g.lname="Flores"
	g.email="janelle.c.flores@gmail.com" 
	g.address="1537 altamont ave" 
	g.city="san jose" 
	g.phone="(408) 497-9329" 
	g.ntrp="F3.0" 
	g.mtype="NRF" 
	g.put()
#69 

	selfobj.response.write("Giana  Flores  flores.giana@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1488396951")) 
	g.year=2017
	g.fname="Giana"
	g.lname="Flores"
	g.email="flores.giana@gmail.com" 
	g.address="1537 altamont Ave" 
	g.city="San Jose" 
	g.phone="() -" 
	g.ntrp="F3.5" 
	g.mtype="NRF_" 
	g.put()
#70 

	selfobj.response.write("Amy  Fontarensky  amyfontarensky@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1485197698")) 
	g.year=2017
	g.fname="Amy"
	g.lname="Fontarensky"
	g.email="amyfontarensky@gmail.com" 
	g.address="1489 Fruitdale Ave #12" 
	g.city="San Jose" 
	g.phone="(408) 623-4098" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#71 

	selfobj.response.write("Ginger  Furuta-Sera  Seramg@aol.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1501617359")) 
	g.year=2017
	g.fname="Ginger"
	g.lname="Furuta-Sera"
	g.email="Seramg@aol.com" 
	g.address="5833 Capilano Drive" 
	g.city="San Jose" 
	g.phone="(408) 270-6002" 
	g.ntrp="F" 
	g.mtype="NRS" 
	g.put()
#72 

	selfobj.response.write("Mar  Garcia  margarciaus@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1483382023")) 
	g.year=2017
	g.fname="Mar"
	g.lname="Garcia"
	g.email="margarciaus@gmail.com" 
	g.address="56 Paterson Pl" 
	g.city="Santa Clara" 
	g.phone="(408) 679-0634" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#73 

	selfobj.response.write("Anne  Giannini  Rudyannie@AOL.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1483653004")) 
	g.year=2017
	g.fname="Anne"
	g.lname="Giannini"
	g.email="Rudyannie@AOL.com" 
	g.address="430 Laurel Avenue" 
	g.city="Millbrae" 
	g.phone="(650) 678-8812" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#74 

	selfobj.response.write("Sally  Graves   sallygravesrich@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1489721372")) 
	g.year=2017
	g.fname="Sally"
	g.lname="Graves "
	g.email="sallygravesrich@yahoo.com" 
	g.address="979 Chelan Drive" 
	g.city="Sunnyvale" 
	g.phone="(858) 254-4235" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#75 

	selfobj.response.write("Tarun  Gupta  tarun.iitm@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1488224024")) 
	g.year=2017
	g.fname="Tarun"
	g.lname="Gupta"
	g.email="tarun.iitm@gmail.com" 
	g.address="2118 Beech Cir" 
	g.city="San Jose" 
	g.phone="(858) 527-5792" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#76 

	selfobj.response.write("Senthil  Gurusamy  senthil.gk25@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1487705689")) 
	g.year=2017
	g.fname="Senthil"
	g.lname="Gurusamy"
	g.email="senthil.gk25@yahoo.com" 
	g.address="3650 Buckley St, APT 507" 
	g.city="Santa Clara" 
	g.phone="(716) 239-7768" 
	g.ntrp="M" 
	g.mtype="RS" 
	g.put()
#77 

	selfobj.response.write("Hyeok  Hahn  hhahn00@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1484346736")) 
	g.year=2017
	g.fname="Hyeok"
	g.lname="Hahn"
	g.email="hhahn00@yahoo.com" 
	g.address="2926 Roma Ct." 
	g.city="Santa Clara" 
	g.phone="(408) 507-2848" 
	g.ntrp="M3.5" 
	g.mtype="RS" 
	g.put()
#78 

	selfobj.response.write("Sameer  Halepete  halepete@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1488226460")) 
	g.year=2017
	g.fname="Sameer"
	g.lname="Halepete"
	g.email="halepete@gmail.com" 
	g.address="496 Rialto Pl" 
	g.city="San Jose" 
	g.phone="(408) 274-9492" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#79 

	selfobj.response.write("Lucille  Harendza  lharendza@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1484616350")) 
	g.year=2017
	g.fname="Lucille"
	g.lname="Harendza"
	g.email="lharendza@yahoo.com" 
	g.address="267 Cahill Park Drive" 
	g.city="San Jose" 
	g.phone="(408) 888-2447" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#80 

	selfobj.response.write("Sharon  Haugen  bertnsharon@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1488956388")) 
	g.year=2017
	g.fname="Sharon"
	g.lname="Haugen"
	g.email="bertnsharon@yahoo.com" 
	g.address="1575 Keith Drive" 
	g.city="Campbell" 
	g.phone="(408) 379-9889" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#81 

	selfobj.response.write("Julie  Hawkes  hawkes_julie@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1483412313")) 
	g.year=2017
	g.fname="Julie"
	g.lname="Hawkes"
	g.email="hawkes_julie@yahoo.com" 
	g.address="5984 Dry Oak Court" 
	g.city="San Jose" 
	g.phone="(408) 622-4544" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#82 

	selfobj.response.write("Samantha  Herman  samantha.milner@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1494948870")) 
	g.year=2017
	g.fname="Samantha"
	g.lname="Herman"
	g.email="samantha.milner@gmail.com" 
	g.address="2492 Robertson Rd" 
	g.city="Santa Clara" 
	g.phone="(661) 713-9869" 
	g.ntrp="F4.5" 
	g.mtype="RF" 
	g.put()
#83 

	selfobj.response.write("Walter  Herman  samantha.milner@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1494949072")) 
	g.year=2017
	g.fname="Walter"
	g.lname="Herman"
	g.email="samantha.milner@gmail.com" 
	g.address="2492 Robertson Rd" 
	g.city="Santa Clara" 
	g.phone="(661) 713-9869" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#84 

	selfobj.response.write("Henry  Herman  henry.herman@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1494948982")) 
	g.year=2017
	g.fname="Henry"
	g.lname="Herman"
	g.email="henry.herman@gmail.com" 
	g.address="2492 Robertson Rd" 
	g.city="Santa Clara" 
	g.phone="(661) 713-9869" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#85 

	selfobj.response.write("William  Hidalgo  meiwillh@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1486166612")) 
	g.year=2017
	g.fname="William"
	g.lname="Hidalgo"
	g.email="meiwillh@gmail.com" 
	g.address="1619 S Main St Ste 103" 
	g.city="Milpitas" 
	g.phone="(510) 386-4918" 
	g.ntrp="M" 
	g.mtype="NRS" 
	g.put()
#86 

	selfobj.response.write("Jeanette  Hoggatt  queenb_95051@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1483928537")) 
	g.year=2017
	g.fname="Jeanette"
	g.lname="Hoggatt"
	g.email="queenb_95051@yahoo.com" 
	g.address="3070 Dibble Court" 
	g.city="Santa Clara" 
	g.phone="(408) 243-4381" 
	g.ntrp="F4.0" 
	g.mtype="RF" 
	g.put()
#87 

	selfobj.response.write("Herta  Hoggatt  queenb_95051@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1483928751")) 
	g.year=2017
	g.fname="Herta"
	g.lname="Hoggatt"
	g.email="queenb_95051@yahoo.com" 
	g.address="3070 Dibble Court" 
	g.city="Santa Clara" 
	g.phone="(408) 243-4381" 
	g.ntrp="F2.0" 
	g.mtype="RF_" 
	g.put()
#88 

	selfobj.response.write("Pamela  Hoggatt  pnhoggatt@hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1483928836")) 
	g.year=2017
	g.fname="Pamela"
	g.lname="Hoggatt"
	g.email="pnhoggatt@hotmail.com" 
	g.address="3070 Dibble Court" 
	g.city="Santa Clara" 
	g.phone="(408) 243-4381" 
	g.ntrp="F3.0" 
	g.mtype="RF_" 
	g.put()
#89 

	selfobj.response.write("Norma  Hughes  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1481241960")) 
	g.year=2017
	g.fname="Norma"
	g.lname="Hughes"
	g.email="" 
	g.address="508 Bancroft St" 
	g.city="Santa Clara" 
	g.phone="() -" 
	g.ntrp="F" 
	g.mtype="RF" 
	g.put()
#90 

	selfobj.response.write("Akari  Ikeda  aikeda14@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1490133218")) 
	g.year=2017
	g.fname="Akari"
	g.lname="Ikeda"
	g.email="aikeda14@yahoo.com" 
	g.address="2250 Monroe St #196" 
	g.city="Santa Clara" 
	g.phone="() -" 
	g.ntrp="F4.5" 
	g.mtype="RS" 
	g.put()
#91 

	selfobj.response.write("Matthew  Isaacson  aliceisaacson@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1493854079")) 
	g.year=2017
	g.fname="Matthew"
	g.lname="Isaacson"
	g.email="aliceisaacson@yahoo.com" 
	g.address="513 Hickory Place" 
	g.city="Santa Clara" 
	g.phone="(408) 247-0343" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#92 

	selfobj.response.write("Nicole  Isaacson  aliceisaacson@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1493854244")) 
	g.year=2017
	g.fname="Nicole"
	g.lname="Isaacson"
	g.email="aliceisaacson@yahoo.com" 
	g.address="513 Hickory Place" 
	g.city="Santa Clara" 
	g.phone="(408) 247-0343" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#93 

	selfobj.response.write("Alice  Isaacson  aliceisaacson@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1490230582")) 
	g.year=2017
	g.fname="Alice"
	g.lname="Isaacson"
	g.email="aliceisaacson@yahoo.com" 
	g.address="513 Hickory Place" 
	g.city="Santa Clara" 
	g.phone="(408) 247-0343" 
	g.ntrp="F4.0" 
	g.mtype="RF" 
	g.put()
#94 

	selfobj.response.write("Mark  Isaacson  aliceisaacson@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1493853793")) 
	g.year=2017
	g.fname="Mark"
	g.lname="Isaacson"
	g.email="aliceisaacson@yahoo.com" 
	g.address="513 Hickory Place" 
	g.city="Santa Clara" 
	g.phone="(408) 247-0343" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#95 

	selfobj.response.write("Taryn  Ishida  tarynishida@Gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1485976018")) 
	g.year=2017
	g.fname="Taryn"
	g.lname="Ishida"
	g.email="tarynishida@Gmail.com" 
	g.address="95 Hobson St. 3A" 
	g.city="San Jose" 
	g.phone="(408) 767-0536" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#96 

	selfobj.response.write("Jitesh  Jagadish  jitesh.jagadish@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1489879985")) 
	g.year=2017
	g.fname="Jitesh"
	g.lname="Jagadish"
	g.email="jitesh.jagadish@gmail.com" 
	g.address="135 Rio Robles E unit 417" 
	g.city="San Jose" 
	g.phone="(770) 862-3711" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#97 

	selfobj.response.write("Dhruv  Jain  DHRUV.JAIN@GMAIL.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1489253104")) 
	g.year=2017
	g.fname="Dhruv"
	g.lname="Jain"
	g.email="DHRUV.JAIN@GMAIL.com" 
	g.address="2110 COOLIDGE DR" 
	g.city="SANTA CLARA" 
	g.phone="(650) 353-1964" 
	g.ntrp="M3.0" 
	g.mtype="RF" 
	g.put()
#98 

	selfobj.response.write("Vicky  Jha  vicky.jha24@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1491504354")) 
	g.year=2017
	g.fname="Vicky"
	g.lname="Jha"
	g.email="vicky.jha24@gmail.com" 
	g.address="1560 Vista Club Circle, Apt # 305" 
	g.city="Santa Clara" 
	g.phone="(214) 600-2346" 
	g.ntrp="M3.5" 
	g.mtype="RS" 
	g.put()
#99 

	selfobj.response.write("Jacqueline  Kerkhove  jkerkhove@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1484025099")) 
	g.year=2017
	g.fname="Jacqueline"
	g.lname="Kerkhove"
	g.email="jkerkhove@gmail.com" 
	g.address="755 Santa Paula Ave" 
	g.city="Sunnyvale" 
	g.phone="(408) 499-6233" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#100 

	selfobj.response.write("Saayaka  Kishino  ksh_kishino@hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1484102727")) 
	g.year=2017
	g.fname="Saayaka"
	g.lname="Kishino"
	g.email="ksh_kishino@hotmail.com" 
	g.address="1058 W Remington Dr" 
	g.city="Sunnyvale" 
	g.phone="(408) 431-6187" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#101 

	selfobj.response.write("Rose  Koot-Lianides  RoseKL@comcast.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1503423867")) 
	g.year=2017
	g.fname="Rose"
	g.lname="Koot-Lianides"
	g.email="RoseKL@comcast.net" 
	g.address="220 Wedgewood Ave." 
	g.city="Los Gatos" 
	g.phone="(408) 866-7960" 
	g.ntrp="F3.5" 
	g.mtype="NRF_" 
	g.put()
#102 

	selfobj.response.write("Hana  Koraitem  jeanneoxford@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1481038283")) 
	g.year=2017
	g.fname="Hana"
	g.lname="Koraitem"
	g.email="jeanneoxford@sbcglobal.net" 
	g.address="3251 Loma Alta Drive" 
	g.city="Santa Clara" 
	g.phone="(408) 985-7901" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#103 

	selfobj.response.write("Hosoon  Ku  hosoonku@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1483493178")) 
	g.year=2017
	g.fname="Hosoon"
	g.lname="Ku"
	g.email="hosoonku@yahoo.com" 
	g.address="3959 Veritas way" 
	g.city="San Ramon" 
	g.phone="(925) 997-3927" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#104 

	selfobj.response.write("Jonathan  Kwan  jonnyjack@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1490070543")) 
	g.year=2017
	g.fname="Jonathan"
	g.lname="Kwan"
	g.email="jonnyjack@gmail.com" 
	g.address="1390 Monroe Street, Apt. 8" 
	g.city="Santa Clara" 
	g.phone="(510) 589-0651" 
	g.ntrp="M4.0" 
	g.mtype="RF" 
	g.put()
#105 

	selfobj.response.write("Hang  Lee  lee.hang@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1499390669")) 
	g.year=2017
	g.fname="Hang"
	g.lname="Lee"
	g.email="lee.hang@yahoo.com" 
	g.address="4558 Cheeney" 
	g.city="Santa Clara" 
	g.phone="(408) 506-2089" 
	g.ntrp="M4.0" 
	g.mtype="RF" 
	g.put()
#106 

	selfobj.response.write("Brandon  Lee  lee.hang@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1499391546")) 
	g.year=2017
	g.fname="Brandon"
	g.lname="Lee"
	g.email="lee.hang@yahoo.com" 
	g.address="4558 Cheeney" 
	g.city="Santa Clara" 
	g.phone="() -" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#107 

	selfobj.response.write("Angela  Lee  leeac05@hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1491546492")) 
	g.year=2017
	g.fname="Angela"
	g.lname="Lee"
	g.email="leeac05@hotmail.com" 
	g.address="680 Epic Way, Apt 434" 
	g.city="San Jose" 
	g.phone="(847) 226-3865" 
	g.ntrp="F2.5" 
	g.mtype="NRS" 
	g.put()
#108 

	selfobj.response.write("Nathan  Lee  lee.hang@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1499391584")) 
	g.year=2017
	g.fname="Nathan"
	g.lname="Lee"
	g.email="lee.hang@yahoo.com" 
	g.address="4558 Cheeney" 
	g.city="Santa Clara" 
	g.phone="() -" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#109 

	selfobj.response.write("Mark  Lianides  RoseKL@comcast.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1503097187")) 
	g.year=2017
	g.fname="Mark"
	g.lname="Lianides"
	g.email="RoseKL@comcast.net" 
	g.address="220 Wedgewood Ave." 
	g.city="Los Gatos" 
	g.phone="(408) 866-7960" 
	g.ntrp="M4.0" 
	g.mtype="NRF" 
	g.put()
#110 

	selfobj.response.write("Kevin  Lien  wtp12345678@Yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1485992018")) 
	g.year=2017
	g.fname="Kevin"
	g.lname="Lien"
	g.email="wtp12345678@Yahoo.com" 
	g.address="1444 Glenn Ct" 
	g.city="San Jose" 
	g.phone="(408) 409-6802" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#111 

	selfobj.response.write("Owen  Lin  owen.lin@sjsu.edu")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1508366777")) 
	g.year=2017
	g.fname="Owen"
	g.lname="Lin"
	g.email="owen.lin@sjsu.edu" 
	g.address="1484 Pollard Road #145" 
	g.city="Los Gatos" 
	g.phone="(408) 921-2694" 
	g.ntrp="M3.0" 
	g.mtype="NRS" 
	g.put()
#112 

	selfobj.response.write("Al  Linke   Alinke2000@Gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1485384005")) 
	g.year=2017
	g.fname="Al"
	g.lname="Linke "
	g.email="Alinke2000@Gmail.com" 
	g.address="1285 main street" 
	g.city="Santa Clara" 
	g.phone="(408) 892-1718" 
	g.ntrp="M4.0" 
	g.mtype="RS" 
	g.put()
#113 

	selfobj.response.write("Linda  Liu  weiwan.liu@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1493947768")) 
	g.year=2017
	g.fname="Linda"
	g.lname="Liu"
	g.email="weiwan.liu@gmail.com" 
	g.address="59 Cabot Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 598-0292" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#114 

	selfobj.response.write("Weiwan  Liu  weiwan.liu@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1488040974")) 
	g.year=2017
	g.fname="Weiwan"
	g.lname="Liu"
	g.email="weiwan.liu@gmail.com" 
	g.address="59 Cabot Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 598-0292" 
	g.ntrp="M3.0" 
	g.mtype="RS" 
	g.put()
#115 

	selfobj.response.write("Marshall  Madamba  mmadamba@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1484352881")) 
	g.year=2017
	g.fname="Marshall"
	g.lname="Madamba"
	g.email="mmadamba@gmail.com" 
	g.address="350 E Taylor St Apt 6114" 
	g.city="San Jose" 
	g.phone="(408) 691-5652" 
	g.ntrp="M3.0" 
	g.mtype="NRF" 
	g.put()
#116 

	selfobj.response.write("Ashok  Mangalore  ashmangalore@hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1508629411")) 
	g.year=2017
	g.fname="Ashok"
	g.lname="Mangalore"
	g.email="ashmangalore@hotmail.com" 
	g.address="36900 Papaya Street" 
	g.city="Newark" 
	g.phone="(510) 676-8975" 
	g.ntrp="M3.0" 
	g.mtype="NRS" 
	g.put()
#117 

	selfobj.response.write("Bill  Mannina  bill.williamtennis@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1510470317")) 
	g.year=2017
	g.fname="Bill"
	g.lname="Mannina"
	g.email="bill.williamtennis@yahoo.com" 
	g.address="177 Monroe Street #7" 
	g.city="Santa Clara" 
	g.phone="(408) 910-6003" 
	g.ntrp="M4.0" 
	g.mtype="RS" 
	g.put()
#118 

	selfobj.response.write("Di  Mao  weiwan.liu@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1493947561")) 
	g.year=2017
	g.fname="Di"
	g.lname="Mao"
	g.email="weiwan.liu@gmail.com" 
	g.address="59 Cabot Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 598-0292" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#119 

	selfobj.response.write("Jaime  Mark  Earthboar@Comcast.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1494960906")) 
	g.year=2017
	g.fname="Jaime"
	g.lname="Mark"
	g.email="Earthboar@Comcast.net" 
	g.address="30 Lydia Ct" 
	g.city="Hillsbough" 
	g.phone="(650) 759-2253" 
	g.ntrp="M4.0" 
	g.mtype="NRF" 
	g.put()
#120 

	selfobj.response.write("Renee  Mark  reneemarky@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1494961567")) 
	g.year=2017
	g.fname="Renee"
	g.lname="Mark"
	g.email="reneemarky@gmail.com" 
	g.address="30 Lydia Ct" 
	g.city="Hillsbough" 
	g.phone="(650) 759-2253" 
	g.ntrp="F4.0" 
	g.mtype="NRF_" 
	g.put()
#121 

	selfobj.response.write("Sue  Markuson  smarkuson@comcast.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1486706887")) 
	g.year=2017
	g.fname="Sue"
	g.lname="Markuson"
	g.email="smarkuson@comcast.net" 
	g.address="10280 Stonydale Drive" 
	g.city="Cupertino" 
	g.phone="(408) 313-7605" 
	g.ntrp="F3.0" 
	g.mtype="NRS" 
	g.put()
#122 

	selfobj.response.write("Elizabeth  Martinez  Lizzy321@Sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1493414970")) 
	g.year=2017
	g.fname="Elizabeth"
	g.lname="Martinez"
	g.email="Lizzy321@Sbcglobal.net" 
	g.address="2123 warburton avenue" 
	g.city="Santa clara" 
	g.phone="(408) 393-6130" 
	g.ntrp="F3.5" 
	g.mtype="RS" 
	g.put()
#123 

	selfobj.response.write("Luzmaria  Martinez  katsulas@aol.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1484353123")) 
	g.year=2017
	g.fname="Luzmaria"
	g.lname="Martinez"
	g.email="katsulas@aol.com" 
	g.address="350 E Taylor St Apt 6114" 
	g.city="San Jose" 
	g.phone="(408) 691-5758" 
	g.ntrp="F3.5" 
	g.mtype="NRF_" 
	g.put()
#124 

	selfobj.response.write("Helen  Matsumoto  geetennis@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1482376874")) 
	g.year=2017
	g.fname="Helen"
	g.lname="Matsumoto"
	g.email="geetennis@yahoo.com" 
	g.address="1247 Redoaks Drive" 
	g.city="San Jose" 
	g.phone="(408) 248-7922" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#125 

	selfobj.response.write("Valerie  McCarthy  valeriebays@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1480889910")) 
	g.year=2017
	g.fname="Valerie"
	g.lname="McCarthy"
	g.email="valeriebays@gmail.com" 
	g.address="471 Tanoak Drive" 
	g.city="Santa Clara" 
	g.phone="(408) 355-4095" 
	g.ntrp="F3.0" 
	g.mtype="RS" 
	g.put()
#126 

	selfobj.response.write("Trevor  McGuire  temcguir@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1489047861")) 
	g.year=2017
	g.fname="Trevor"
	g.lname="McGuire"
	g.email="temcguir@gmail.com" 
	g.address="900 Pepper Tree Lane Apt. 212" 
	g.city="Santa Clara" 
	g.phone="(707) 799-0577" 
	g.ntrp="M3.5" 
	g.mtype="RF" 
	g.put()
#127 

	selfobj.response.write("Nathan W.  Mertz  tennis61911@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1504368181")) 
	g.year=2017
	g.fname="Nathan W."
	g.lname="Mertz"
	g.email="tennis61911@yahoo.com" 
	g.address="2071 Bowers Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 469-0521" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#128 

	selfobj.response.write("Aurora  Mertz  tennis61911@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1504368665")) 
	g.year=2017
	g.fname="Aurora"
	g.lname="Mertz"
	g.email="tennis61911@yahoo.com" 
	g.address="2071 Bowers Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 469-0521" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#129 

	selfobj.response.write("Karen  Mertz  tennis61911@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1504368370")) 
	g.year=2017
	g.fname="Karen"
	g.lname="Mertz"
	g.email="tennis61911@yahoo.com" 
	g.address="2071 Bowers Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 469-0521" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#130 

	selfobj.response.write("Breanna  Mertz  tennis61911@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1504368835")) 
	g.year=2017
	g.fname="Breanna"
	g.lname="Mertz"
	g.email="tennis61911@yahoo.com" 
	g.address="2071 Bowers Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 469-0521" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#131 

	selfobj.response.write("Megan  Mertz  tennis61911@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1504368522")) 
	g.year=2017
	g.fname="Megan"
	g.lname="Mertz"
	g.email="tennis61911@yahoo.com" 
	g.address="2071 Bowers Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 469-0521" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#132 

	selfobj.response.write("Nathan  Mertz  tennis61911@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1501655700")) 
	g.year=2017
	g.fname="Nathan"
	g.lname="Mertz"
	g.email="tennis61911@yahoo.com" 
	g.address="2071 Bowers Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 469-0521" 
	g.ntrp="M3.5" 
	g.mtype="RF" 
	g.put()
#133 

	selfobj.response.write("Yuko  Mihara  miharayuko@hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1491002267")) 
	g.year=2017
	g.fname="Yuko"
	g.lname="Mihara"
	g.email="miharayuko@hotmail.com" 
	g.address="2017 Somewhere Street" 
	g.city="Sunnyvale" 
	g.phone="() -" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#134 

	selfobj.response.write("Melissa   Miller  melissamiller5533@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1488945942")) 
	g.year=2017
	g.fname="Melissa "
	g.lname="Miller"
	g.email="melissamiller5533@gmail.com" 
	g.address="350 East Taylor Street, apt 1103" 
	g.city="San Jose" 
	g.phone="(415) 819-5937" 
	g.ntrp="F3.5" 
	g.mtype="NRF" 
	g.put()
#135 

	selfobj.response.write("Sandra  Miller  Snadra39@Yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1483587264")) 
	g.year=2017
	g.fname="Sandra"
	g.lname="Miller"
	g.email="Snadra39@Yahoo.com" 
	g.address="10390 Malvern Ct" 
	g.city="CUpertino" 
	g.phone="(408) 892-6617" 
	g.ntrp="F3.0" 
	g.mtype="NRS" 
	g.put()
#136 

	selfobj.response.write("Roy  Molseed  roy.molseed@vta.org")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1482040622")) 
	g.year=2017
	g.fname="Roy"
	g.lname="Molseed"
	g.email="roy.molseed@vta.org" 
	g.address="238 N Cypress Avenue" 
	g.city="Santa Clara" 
	g.phone="(408) 580-6396" 
	g.ntrp="M4.0" 
	g.mtype="RF_" 
	g.put()
#137 

	selfobj.response.write("Gayle  Moore  tennissenior@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1494913979")) 
	g.year=2017
	g.fname="Gayle"
	g.lname="Moore"
	g.email="tennissenior@yahoo.com" 
	g.address="3115 Maurica Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 246-5129" 
	g.ntrp="F3.5" 
	g.mtype="RS" 
	g.put()
#138 

	selfobj.response.write("Francisca  Mortensen  back40@Creative-services.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1486764192")) 
	g.year=2017
	g.fname="Francisca"
	g.lname="Mortensen"
	g.email="back40@Creative-services.com" 
	g.address="3584  Irlanda Way" 
	g.city="San Jose" 
	g.phone="(408) 410-7836" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#139 

	selfobj.response.write("Cindy  Motamedi  cindy@americanprinting.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1508969014")) 
	g.year=2017
	g.fname="Cindy"
	g.lname="Motamedi"
	g.email="cindy@americanprinting.com" 
	g.address="2697 Rutherford Pl" 
	g.city="Fremont" 
	g.phone="(510) 407-3307" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#140 

	selfobj.response.write("Pradeep  Nair  pradeepn1@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1483659674")) 
	g.year=2017
	g.fname="Pradeep"
	g.lname="Nair"
	g.email="pradeepn1@gmail.com" 
	g.address="1921 Garzoni Place" 
	g.city="Santa Clara" 
	g.phone="(408) 839-1703" 
	g.ntrp="M4.0" 
	g.mtype="RS" 
	g.put()
#141 

	selfobj.response.write("Vishnu  Nandakumar  nvishnuvardhan@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1487879555")) 
	g.year=2017
	g.fname="Vishnu"
	g.lname="Nandakumar"
	g.email="nvishnuvardhan@gmail.com" 
	g.address="420 Riverside Ct, Apt 302" 
	g.city="Santa Clara" 
	g.phone="(814) 308-3611" 
	g.ntrp="M3.5" 
	g.mtype="RS" 
	g.put()
#142 

	selfobj.response.write("Shiv  Natarajan  shiv.natarajan@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1486870546")) 
	g.year=2017
	g.fname="Shiv"
	g.lname="Natarajan"
	g.email="shiv.natarajan@yahoo.com" 
	g.address="4813 Verbena Way" 
	g.city="San Jose" 
	g.phone="(408) 480-1044" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#143 

	selfobj.response.write("Joane  Nelson  joanelso10@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1497533611")) 
	g.year=2017
	g.fname="Joane"
	g.lname="Nelson"
	g.email="joanelso10@yahoo.com" 
	g.address="3719 Fernwood St" 
	g.city="San Mateo" 
	g.phone="(650) 312-8555" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#144 

	selfobj.response.write("Kim  Nemeth  knemeth@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1483814682")) 
	g.year=2017
	g.fname="Kim"
	g.lname="Nemeth"
	g.email="knemeth@sbcglobal.net" 
	g.address="1610 Sweetbriar Dr." 
	g.city="San Jose" 
	g.phone="(408) 396-0608" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#145 

	selfobj.response.write("Sally  Nettleton  sallyjnettleton@hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1481518446")) 
	g.year=2017
	g.fname="Sally"
	g.lname="Nettleton"
	g.email="sallyjnettleton@hotmail.com" 
	g.address="22431 Palm avenue" 
	g.city="cupertino" 
	g.phone="(408) 718-0876" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#146 

	selfobj.response.write("Lloyd  Ngo  lloydngo@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1493852859")) 
	g.year=2017
	g.fname="Lloyd"
	g.lname="Ngo"
	g.email="lloydngo@yahoo.com" 
	g.address="3399 Victoria Ave." 
	g.city="Santa Clara" 
	g.phone="(408) 891-1154" 
	g.ntrp="M" 
	g.mtype="RF" 
	g.put()
#147 

	selfobj.response.write("Lai  Ngo  lloydngo@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1493853199")) 
	g.year=2017
	g.fname="Lai"
	g.lname="Ngo"
	g.email="lloydngo@yahoo.com" 
	g.address="3399 Victoria Ave." 
	g.city="Santa Clara" 
	g.phone="(408) 891-1154" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#148 

	selfobj.response.write("Paul  Nguyen  paulinium@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1487189486")) 
	g.year=2017
	g.fname="Paul"
	g.lname="Nguyen"
	g.email="paulinium@gmail.com" 
	g.address="17246 James Lex Ln" 
	g.city="Morgan Hill" 
	g.phone="(916) 202-6892" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#149 

	selfobj.response.write("Thi  Nguyen  baothiy2k@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1484515480")) 
	g.year=2017
	g.fname="Thi"
	g.lname="Nguyen"
	g.email="baothiy2k@yahoo.com" 
	g.address="1925 White Oaks Road" 
	g.city="Campbell" 
	g.phone="(408) 497-8889" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#150 

	selfobj.response.write("Nancy  Nii  udderniis@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1473293007")) 
	g.year=2017
	g.fname="Nancy"
	g.lname="Nii"
	g.email="udderniis@yahoo.com" 
	g.address="1838 Montemar Way" 
	g.city="San Jose" 
	g.phone="(408) 464-3177" 
	g.ntrp="F4.0" 
	g.mtype="NRF" 
	g.put()
#151 

	selfobj.response.write("Carlos  Nino de Guzman  cng94087@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1484804020")) 
	g.year=2017
	g.fname="Carlos"
	g.lname="Nino de Guzman"
	g.email="cng94087@yahoo.com" 
	g.address="2464 El Camino Real 160" 
	g.city="Santa Clara" 
	g.phone="(510) 300-4863" 
	g.ntrp="M3.5" 
	g.mtype="RS" 
	g.put()
#152 

	selfobj.response.write("Rosa  Nunez  rosa.nunez2@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1494965808")) 
	g.year=2017
	g.fname="Rosa"
	g.lname="Nunez"
	g.email="rosa.nunez2@yahoo.com" 
	g.address="3500 Granada ave, APT 160" 
	g.city="Santa Clara" 
	g.phone="(201) 892-1647" 
	g.ntrp="F3.0" 
	g.mtype="RS" 
	g.put()
#153 

	selfobj.response.write("Joseph  Nuniz  josephnuniz@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1488936192")) 
	g.year=2017
	g.fname="Joseph"
	g.lname="Nuniz"
	g.email="josephnuniz@yahoo.com" 
	g.address="1416, San Martino Court" 
	g.city="San Jose" 
	g.phone="(214) 808-1633" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#154 

	selfobj.response.write("Yuri  Oda  yurijudy123@Yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1483392254")) 
	g.year=2017
	g.fname="Yuri"
	g.lname="Oda"
	g.email="yurijudy123@Yahoo.com" 
	g.address="17265 Grosvenor Ct" 
	g.city="Monte Sereno" 
	g.phone="(408) 307-7815" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#155 

	selfobj.response.write("Thomas  Oda  todaxyz@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1491693125")) 
	g.year=2017
	g.fname="Thomas"
	g.lname="Oda"
	g.email="todaxyz@yahoo.com" 
	g.address="17265 Grosvenor Ct" 
	g.city="Monte Sereno" 
	g.phone="(408) 316-6084" 
	g.ntrp="M3.5" 
	g.mtype="NRF" 
	g.put()
#156 

	selfobj.response.write("Junko  Ohoka  junko.ohoka@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1486880196")) 
	g.year=2017
	g.fname="Junko"
	g.lname="Ohoka"
	g.email="junko.ohoka@gmail.com" 
	g.address="992 Foxworthy Ave." 
	g.city="San Jose" 
	g.phone="(408) 582-4035" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#157 

	selfobj.response.write("Roger  Okamoto  tennis.mutt@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1488841425")) 
	g.year=2017
	g.fname="Roger"
	g.lname="Okamoto"
	g.email="tennis.mutt@gmail.com" 
	g.address="PO Box 604" 
	g.city="Mountain View" 
	g.phone="(408) 800-7646" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#158 

	selfobj.response.write("Ken  Okazaki  Okaken1@AOL.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1486182404")) 
	g.year=2017
	g.fname="Ken"
	g.lname="Okazaki"
	g.email="Okaken1@AOL.com" 
	g.address="814 Daffodil Way" 
	g.city="San Jose" 
	g.phone="(408) 387-0460" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#159 

	selfobj.response.write("Rachel  Okazaki  Japanesegrace@Gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1490071078")) 
	g.year=2017
	g.fname="Rachel"
	g.lname="Okazaki"
	g.email="Japanesegrace@Gmail.com" 
	g.address="1390 Monroe Street, Apt. 8" 
	g.city="Santa Clara" 
	g.phone="(408) 390-2915" 
	g.ntrp="F4.0" 
	g.mtype="RF_" 
	g.put()
#160 

	selfobj.response.write("Chester  Okuno  chesterokuno@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1491408143")) 
	g.year=2017
	g.fname="Chester"
	g.lname="Okuno"
	g.email="chesterokuno@gmail.com" 
	g.address="1497 Miramonte Ave" 
	g.city="Los Altos" 
	g.phone="(408) 489-3142" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#161 

	selfobj.response.write("Michelle  Olivas  Michelle.E.Olivas@Gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1497662745")) 
	g.year=2017
	g.fname="Michelle"
	g.lname="Olivas"
	g.email="Michelle.E.Olivas@Gmail.com" 
	g.address="395 S Buena Vista Ave #2" 
	g.city="San Jose" 
	g.phone="(831) 578-3922" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#162 

	selfobj.response.write("Noriko  Osawa  noriko_osawa@hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1486014040")) 
	g.year=2017
	g.fname="Noriko"
	g.lname="Osawa"
	g.email="noriko_osawa@hotmail.com" 
	g.address="157 Kensington Way" 
	g.city="Los Gatos" 
	g.phone="(408) 401-9977" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#163 

	selfobj.response.write("Ace  Oxford  jeanneoxford@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1480969772")) 
	g.year=2017
	g.fname="Ace"
	g.lname="Oxford"
	g.email="jeanneoxford@sbcglobal.net" 
	g.address="3251 Loma Alta Drive" 
	g.city="Santa Clara" 
	g.phone="(408) 985-7901" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#164 

	selfobj.response.write("Jeanne  Oxford  jeanneoxford@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1480969644")) 
	g.year=2017
	g.fname="Jeanne"
	g.lname="Oxford"
	g.email="jeanneoxford@sbcglobal.net" 
	g.address="3251 Loma Alta Drive" 
	g.city="Santa Clara" 
	g.phone="(408) 985-7901" 
	g.ntrp="F3.0" 
	g.mtype="RF" 
	g.put()
#165 

	selfobj.response.write("Karen   Panian   kpanian@comcast.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1486696452")) 
	g.year=2017
	g.fname="Karen "
	g.lname="Panian "
	g.email="kpanian@comcast.net" 
	g.address="1704 Harrison St." 
	g.city="Santa Clara" 
	g.phone="(408) 313-8883" 
	g.ntrp="F3.5" 
	g.mtype="RS" 
	g.put()
#166 

	selfobj.response.write("Christine  Peters  ck.peters@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1484512936")) 
	g.year=2017
	g.fname="Christine"
	g.lname="Peters"
	g.email="ck.peters@sbcglobal.net" 
	g.address="1390 Saddle Rack St, #349" 
	g.city="San Jose" 
	g.phone="(408) 921-1610" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#167 

	selfobj.response.write("Elisapeta  Peterson  peta.peterson@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1486158151")) 
	g.year=2017
	g.fname="Elisapeta"
	g.lname="Peterson"
	g.email="peta.peterson@sbcglobal.net" 
	g.address="13970 Saratoga Ave" 
	g.city="Saratoga CA" 
	g.phone="( 40) 867-6947" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#168 

	selfobj.response.write("Liz  Pham  phamliz@comcast.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1499752539")) 
	g.year=2017
	g.fname="Liz"
	g.lname="Pham"
	g.email="phamliz@comcast.net" 
	g.address="4122 Linetta Court" 
	g.city="San Jose" 
	g.phone="(408) 694-7206" 
	g.ntrp="F3.0" 
	g.mtype="NRS" 
	g.put()
#169 

	selfobj.response.write("Bettye  Pham-Vo  bettyediem@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1483457566")) 
	g.year=2017
	g.fname="Bettye"
	g.lname="Pham-Vo"
	g.email="bettyediem@gmail.com" 
	g.address="3657 Lisbon Ct." 
	g.city="San Jose" 
	g.phone="(408) 250-5658" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#170 

	selfobj.response.write("Sachiko  Pieczulewski  piecz@earthlink.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1504301464")) 
	g.year=2017
	g.fname="Sachiko"
	g.lname="Pieczulewski"
	g.email="piecz@earthlink.net" 
	g.address="6693 Dartmoor Way" 
	g.city="San Jose" 
	g.phone="(408) 966-4508" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#171 

	selfobj.response.write("Tonya  Podkuiko  tpodkuiko@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1499309852")) 
	g.year=2017
	g.fname="Tonya"
	g.lname="Podkuiko"
	g.email="tpodkuiko@gmail.com" 
	g.address="1320 White Drive" 
	g.city="Santa Clara" 
	g.phone="(814) 441-9576" 
	g.ntrp="F" 
	g.mtype="RF" 
	g.put()
#172 

	selfobj.response.write("Haran  Pradeep Chidambaram  haranpc@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1493689821")) 
	g.year=2017
	g.fname="Haran"
	g.lname="Pradeep Chidambaram"
	g.email="haranpc@gmail.com" 
	g.address="3655 Pruneridge avenue" 
	g.city="Santaclara" 
	g.phone="(512) 810-9787" 
	g.ntrp="M3.0" 
	g.mtype="RS" 
	g.put()
#173 

	selfobj.response.write("Catherine  Puzon  caetz2000@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1491893648")) 
	g.year=2017
	g.fname="Catherine"
	g.lname="Puzon"
	g.email="caetz2000@yahoo.com" 
	g.address="5431 Sanchez Dr" 
	g.city="San Jose" 
	g.phone="(650) 455-1577" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#174 

	selfobj.response.write("Rajasundaram  Rajasekaran  rajasundaramr@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1489986405")) 
	g.year=2017
	g.fname="Rajasundaram"
	g.lname="Rajasekaran"
	g.email="rajasundaramr@gmail.com" 
	g.address="60 descanso drive, Apt 2220" 
	g.city="san jose" 
	g.phone="(585) 738-5897" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#175 

	selfobj.response.write("Balakumar  Rajendran  balakumar85@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1487782716")) 
	g.year=2017
	g.fname="Balakumar"
	g.lname="Rajendran"
	g.email="balakumar85@gmail.com" 
	g.address="3043 Rossmore Way" 
	g.city="San Jose" 
	g.phone="(513) 739-2747" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#176 

	selfobj.response.write("Vyass  Ramakrishnan  rvyass@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1485990128")) 
	g.year=2017
	g.fname="Vyass"
	g.lname="Ramakrishnan"
	g.email="rvyass@gmail.com" 
	g.address="555 E El Camino Real Apt 101" 
	g.city="Sunnyvale" 
	g.phone="(469) 213-9145" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#177 

	selfobj.response.write("Aditya  Rawat  ad.rawat30@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1487471275")) 
	g.year=2017
	g.fname="Aditya"
	g.lname="Rawat"
	g.email="ad.rawat30@gmail.com" 
	g.address="600 Epic Way Unit 463" 
	g.city="San Jose" 
	g.phone="(219) 964-5051" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#178 

	selfobj.response.write("Elisa  Salazar  kddsalazar@comcast.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1494892119")) 
	g.year=2017
	g.fname="Elisa"
	g.lname="Salazar"
	g.email="kddsalazar@comcast.net" 
	g.address="989 Perreira Dr" 
	g.city="Santa Clara" 
	g.phone="(408) 296-2379" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#179 

	selfobj.response.write("Kenneth  Salazar  kddsalazar@comcast.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1494892302")) 
	g.year=2017
	g.fname="Kenneth"
	g.lname="Salazar"
	g.email="kddsalazar@comcast.net" 
	g.address="989 Perreira Dr" 
	g.city="Santa Clara" 
	g.phone="(408) 296-2379" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#180 

	selfobj.response.write("Dolores  Salazar  kddsalazar@comcast.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1485464449")) 
	g.year=2017
	g.fname="Dolores"
	g.lname="Salazar"
	g.email="kddsalazar@comcast.net" 
	g.address="989 Perreira Dr" 
	g.city="Santa Clara" 
	g.phone="(408) 296-2379" 
	g.ntrp="F3.0" 
	g.mtype="RF" 
	g.put()
#181 

	selfobj.response.write("Dempsey  Salazar  kddsalazar@comcast.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1494891939")) 
	g.year=2017
	g.fname="Dempsey"
	g.lname="Salazar"
	g.email="kddsalazar@comcast.net" 
	g.address="989 Perreira Dr" 
	g.city="Santa Clara" 
	g.phone="(408) 296-2379" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#182 

	selfobj.response.write("Lauren  Salazar  kddsalazar@comcast.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1494892464")) 
	g.year=2017
	g.fname="Lauren"
	g.lname="Salazar"
	g.email="kddsalazar@comcast.net" 
	g.address="989 Perreira Dr" 
	g.city="Santa Clara" 
	g.phone="(408) 296-2379" 
	g.ntrp="F" 
	g.mtype="RF_" 
	g.put()
#183 

	selfobj.response.write("Cecilia  Santillanes  cicigirl56@Yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1501395994")) 
	g.year=2017
	g.fname="Cecilia"
	g.lname="Santillanes"
	g.email="cicigirl56@Yahoo.com" 
	g.address="17363 Serene  Dr." 
	g.city="Morgan Hill" 
	g.phone="(408) 334-5776" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#184 

	selfobj.response.write("Mei  See  meisee68@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1481515946")) 
	g.year=2017
	g.fname="Mei"
	g.lname="See"
	g.email="meisee68@yahoo.com" 
	g.address="238 N Cypress Avenue" 
	g.city="Santa Clara" 
	g.phone="(408) 480-1880" 
	g.ntrp="F3.0" 
	g.mtype="RF" 
	g.put()
#185 

	selfobj.response.write("TzeYin  Segalman  yin.segalman@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1496796918")) 
	g.year=2017
	g.fname="TzeYin"
	g.lname="Segalman"
	g.email="yin.segalman@gmail.com" 
	g.address="154 S 23rd St" 
	g.city="San Jose" 
	g.phone="(505) 480-4384" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#186 

	selfobj.response.write("Neeshil  Shah  ketan_f3@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1496002394")) 
	g.year=2017
	g.fname="Neeshil"
	g.lname="Shah"
	g.email="ketan_f3@yahoo.com" 
	g.address="3414 Notre Dame Dr." 
	g.city="Santa Clara" 
	g.phone="(408) 315-2798" 
	g.ntrp="M" 
	g.mtype="RS" 
	g.put()
#187 

	selfobj.response.write("Sharath  Shankar  sharathbshankar@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1503383151")) 
	g.year=2017
	g.fname="Sharath"
	g.lname="Shankar"
	g.email="sharathbshankar@gmail.com" 
	g.address="1073 Loyola Ct." 
	g.city="Santa Clara" 
	g.phone="(408) 836-7864" 
	g.ntrp="M3.0" 
	g.mtype="RS" 
	g.put()
#188 

	selfobj.response.write("Cynthia  Shannon  cyn.tennis@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1483907590")) 
	g.year=2017
	g.fname="Cynthia"
	g.lname="Shannon"
	g.email="cyn.tennis@sbcglobal.net" 
	g.address="97 Waterside Circle" 
	g.city="Redwood City" 
	g.phone="() -" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#189 

	selfobj.response.write("Wade  Smithson  wado@wado.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1490094771")) 
	g.year=2017
	g.fname="Wade"
	g.lname="Smithson"
	g.email="wado@wado.com" 
	g.address="332 Carriage Dr. #2" 
	g.city="Santa Clara" 
	g.phone="(408) 655-6019" 
	g.ntrp="M4.0" 
	g.mtype="RS" 
	g.put()
#190 

	selfobj.response.write("AleJandro   Sosa  sosa12822@hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1505877487")) 
	g.year=2017
	g.fname="AleJandro "
	g.lname="Sosa"
	g.email="sosa12822@hotmail.com" 
	g.address="900 Henderson Ave Sp. 101" 
	g.city="Santa Clara" 
	g.phone="(408) 836-8574" 
	g.ntrp="M4.0" 
	g.mtype="RS" 
	g.put()
#191 

	selfobj.response.write("Cory  Sprague Williams  corsprague@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1487899678")) 
	g.year=2017
	g.fname="Cory"
	g.lname="Sprague Williams"
	g.email="corsprague@gmail.com" 
	g.address="1000 Kiely Blvd Apt 38" 
	g.city="SANTA CLARA" 
	g.phone="(619) 206-2884" 
	g.ntrp="F4.0" 
	g.mtype="RF" 
	g.put()
#192 

	selfobj.response.write("Sheryl   Strebel  sherylstrebel@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1480897005")) 
	g.year=2017
	g.fname="Sheryl "
	g.lname="Strebel"
	g.email="sherylstrebel@gmail.com" 
	g.address="938 Clark Ave #41" 
	g.city="Mountain View" 
	g.phone="(408) 505-8849" 
	g.ntrp="F3.0" 
	g.mtype="NRS" 
	g.put()
#193 

	selfobj.response.write("Susan  Stulz  sstulz@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1483638277")) 
	g.year=2017
	g.fname="Susan"
	g.lname="Stulz"
	g.email="sstulz@gmail.com" 
	g.address="27260 Sherlock Rd" 
	g.city="Los Altos Hills" 
	g.phone="(650) 380-2062" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#194 

	selfobj.response.write("Shawn  Sullivan  sperrow94@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1504286211")) 
	g.year=2017
	g.fname="Shawn"
	g.lname="Sullivan"
	g.email="sperrow94@gmail.com" 
	g.address="3180 Rubino Drive Apt. 201" 
	g.city="San Jose" 
	g.phone="(925) 787-6409" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#195 

	selfobj.response.write("Fumie  Taguchi  fumie916@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1491893585")) 
	g.year=2017
	g.fname="Fumie"
	g.lname="Taguchi"
	g.email="fumie916@gmail.com" 
	g.address="1454 Thunderbird Ave." 
	g.city="Sunnyvale" 
	g.phone="(408) 244-4310" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#196 

	selfobj.response.write("Tomoe  Tajima  tomoetajima@earthlink.net@")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1490739021")) 
	g.year=2017
	g.fname="Tomoe"
	g.lname="Tajima"
	g.email="tomoetajima@earthlink.net@" 
	g.address="1020 Prune Ct." 
	g.city="Sunnyvale" 
	g.phone="(408) 963-3084" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#197 

	selfobj.response.write("Svend  Tang-Petersen  svend_tangpetersen@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1483381928")) 
	g.year=2017
	g.fname="Svend"
	g.lname="Tang-Petersen"
	g.email="svend_tangpetersen@yahoo.com" 
	g.address="56 Paterson Pl" 
	g.city="Santa Clara" 
	g.phone="(408) 768-1093" 
	g.ntrp="M" 
	g.mtype="RF" 
	g.put()
#198 

	selfobj.response.write("Yuko  Tasaka   ayratasaka@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1486489805")) 
	g.year=2017
	g.fname="Yuko"
	g.lname="Tasaka "
	g.email="ayratasaka@gmail.com" 
	g.address="19790 Auburn Dr" 
	g.city="Cupertino" 
	g.phone="(408) 533-5322" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#199 

	selfobj.response.write("Lev  Tauz  levtauz@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1485937350")) 
	g.year=2017
	g.fname="Lev"
	g.lname="Tauz"
	g.email="levtauz@gmail.com" 
	g.address="617 Arcadia Terrace, 201" 
	g.city="Sunnyvale" 
	g.phone="(818) 350-2308" 
	g.ntrp="M3.0" 
	g.mtype="NRS" 
	g.put()
#200 

	selfobj.response.write("Tom  Taylor  ttaylor5209@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1497666352")) 
	g.year=2017
	g.fname="Tom"
	g.lname="Taylor"
	g.email="ttaylor5209@yahoo.com" 
	g.address="3299 LOMA ALTA DR." 
	g.city="Santa Clara" 
	g.phone="(408) 510-4623" 
	g.ntrp="M" 
	g.mtype="RS" 
	g.put()
#201 

	selfobj.response.write("Michelle  Te  chelle_mhae2003@Yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1487283346")) 
	g.year=2017
	g.fname="Michelle"
	g.lname="Te"
	g.email="chelle_mhae2003@Yahoo.com" 
	g.address="416 Boynton Ave apt #102" 
	g.city="San Jose" 
	g.phone="(925) 788-8524" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#202 

	selfobj.response.write("Praveen  Thangavelu  praveenst@icloud.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1507667991")) 
	g.year=2017
	g.fname="Praveen"
	g.lname="Thangavelu"
	g.email="praveenst@icloud.com" 
	g.address="2122 Cabrillo Avenue" 
	g.city="Santa Clara" 
	g.phone="(916) 340-5270" 
	g.ntrp="M" 
	g.mtype="RS" 
	g.put()
#203 

	selfobj.response.write("Gautam   Thockchom  gautam@mytiecon.org")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1493677744")) 
	g.year=2017
	g.fname="Gautam "
	g.lname="Thockchom"
	g.email="gautam@mytiecon.org" 
	g.address="3310 Princeton Way" 
	g.city="Santa Clara" 
	g.phone="(408) 476-7538" 
	g.ntrp="M3.5" 
	g.mtype="RS" 
	g.put()
#204 

	selfobj.response.write("Debbie  Tripiano  dtripiano@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1483406787")) 
	g.year=2017
	g.fname="Debbie"
	g.lname="Tripiano"
	g.email="dtripiano@gmail.com" 
	g.address="1291 Pomeroy Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 772-6104" 
	g.ntrp="F4.0" 
	g.mtype="RS" 
	g.put()
#205 

	selfobj.response.write("Thomas  Truong  thomas_g_truong@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1491540581")) 
	g.year=2017
	g.fname="Thomas"
	g.lname="Truong"
	g.email="thomas_g_truong@yahoo.com" 
	g.address="2167 Weston pl" 
	g.city="Santa Clara" 
	g.phone="(408) 219-2377" 
	g.ntrp="M4.0" 
	g.mtype="RS" 
	g.put()
#206 

	selfobj.response.write("Thomas  Truong  thomas_g_truong@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1491610172")) 
	g.year=2017
	g.fname="Thomas"
	g.lname="Truong"
	g.email="thomas_g_truong@yahoo.com" 
	g.address="2167 Weston PL" 
	g.city="Santa Clara" 
	g.phone="(408) 219-2377" 
	g.ntrp="M4.0" 
	g.mtype="RS" 
	g.put()
#207 

	selfobj.response.write("Klara  Turner  Klaraturnersalon@Yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1502236133")) 
	g.year=2017
	g.fname="Klara"
	g.lname="Turner"
	g.email="Klaraturnersalon@Yahoo.com" 
	g.address="10837 Northridge Square" 
	g.city="Cupertino" 
	g.phone="(650) 323-0735" 
	g.ntrp="F3.0" 
	g.mtype="NRS" 
	g.put()
#208 

	selfobj.response.write("Ryan  Ventura  tubadude222@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1484749075")) 
	g.year=2017
	g.fname="Ryan"
	g.lname="Ventura"
	g.email="tubadude222@gmail.com" 
	g.address="2653 Elliot Street" 
	g.city="Santa Clara" 
	g.phone="(408) 425-3420" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#209 

	selfobj.response.write("Lori  Ventura  loriv@me.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1484748328")) 
	g.year=2017
	g.fname="Lori"
	g.lname="Ventura"
	g.email="loriv@me.com" 
	g.address="2653 Elliot Street" 
	g.city="Santa Clara" 
	g.phone="(408) 425-3420" 
	g.ntrp="F3.5" 
	g.mtype="RF" 
	g.put()
#210 

	selfobj.response.write("Vince  Ventura  aceventura3@mac.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1484748904")) 
	g.year=2017
	g.fname="Vince"
	g.lname="Ventura"
	g.email="aceventura3@mac.com" 
	g.address="2653 Elliot Street" 
	g.city="Santa Clara" 
	g.phone="(408) 209-5354" 
	g.ntrp="M" 
	g.mtype="RF_" 
	g.put()
#211 

	selfobj.response.write("Shashank  Verma  shashank.verma590@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1504286425")) 
	g.year=2017
	g.fname="Shashank"
	g.lname="Verma"
	g.email="shashank.verma590@gmail.com" 
	g.address="655 S Fair Oaks Avenue, Apartment J117" 
	g.city="Sunnyvale" 
	g.phone="(669) 264-7886" 
	g.ntrp="M3.0" 
	g.mtype="NRS" 
	g.put()
#212 

	selfobj.response.write("Madan Kumar  Vijayakumar  madanvkumarster@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1505242444")) 
	g.year=2017
	g.fname="Madan Kumar"
	g.lname="Vijayakumar"
	g.email="madanvkumarster@gmail.com" 
	g.address="5573 Starcrest drive" 
	g.city="San Jose" 
	g.phone="(408) 650-2837" 
	g.ntrp="M3.0" 
	g.mtype="NRS" 
	g.put()
#213 

	selfobj.response.write("Jasmine  Vu  haiquangvu@Yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1506364496")) 
	g.year=2017
	g.fname="Jasmine"
	g.lname="Vu"
	g.email="haiquangvu@Yahoo.com" 
	g.address="148 Perry st." 
	g.city="Milpitas" 
	g.phone="(408) 910-3970" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#214 

	selfobj.response.write("Asa  Williams  asawilliams@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1487899798")) 
	g.year=2017
	g.fname="Asa"
	g.lname="Williams"
	g.email="asawilliams@gmail.com" 
	g.address="1000 Kiely Blvd Apt 38" 
	g.city="SANTA CLARA" 
	g.phone="(619) 206-0937" 
	g.ntrp="M3.0" 
	g.mtype="RF_" 
	g.put()
#215 

	selfobj.response.write("Jason  Wu  jcwu84@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1489898433")) 
	g.year=2017
	g.fname="Jason"
	g.lname="Wu"
	g.email="jcwu84@gmail.com" 
	g.address="279 St Catherine Drive" 
	g.city="Daly City" 
	g.phone="(650) 278-9118" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#216 

	selfobj.response.write("Warren  Yamaguchi  winini@comcast.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1487709973")) 
	g.year=2017
	g.fname="Warren"
	g.lname="Yamaguchi"
	g.email="winini@comcast.net" 
	g.address="1291 Pomeroy Avenue" 
	g.city="Santa Clara" 
	g.phone="(408) 641-0221" 
	g.ntrp="M4.0" 
	g.mtype="RS" 
	g.put()
#217 

	selfobj.response.write("Hyungwoo  Yang  hwoo.yang@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1503027558")) 
	g.year=2017
	g.fname="Hyungwoo"
	g.lname="Yang"
	g.email="hwoo.yang@gmail.com" 
	g.address="1883 AGNEW RD #430" 
	g.city="santa clara" 
	g.phone="(408) 334-6752" 
	g.ntrp="M3.0" 
	g.mtype="RS" 
	g.put()
#218 

	selfobj.response.write("Quingquig  Yu  qingqingfish@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1493678196")) 
	g.year=2017
	g.fname="Quingquig"
	g.lname="Yu"
	g.email="qingqingfish@gmail.com" 
	g.address="3642 Eastwood Circle" 
	g.city="Santa Clara" 
	g.phone="() -" 
	g.ntrp="F" 
	g.mtype="RF" 
	g.put()
