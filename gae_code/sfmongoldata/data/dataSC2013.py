

#
#
#select * from paypal where year = "2013"  union select * from bycheck where year =  "2013" order by year,lname 
#
#
import webapp2
from datastore import  *


def santaclara2013(selfobj):


#1 

	selfobj.response.write("Karen  Abad  abadkj@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
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

	selfobj.response.write("Jennifer  Adams  jenyferadams@fnf.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Jennifer"
	g.lname="Adams"
	g.email="jenyferadams@fnf.com" 
	g.address="5971 Countess Drive" 
	g.city="San Jose" 
	g.phone="(408) 313-4405" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#3 

	selfobj.response.write("Sreenivas  Aluru  salur1@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Sreenivas"
	g.lname="Aluru"
	g.email="salur1@yahoo.com" 
	g.address="10816 Alderbrook Lane" 
	g.city="Cupertino" 
	g.phone="(408) 406-1885" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#4 

	selfobj.response.write("Ahluwalia  Amandeep  DLW8828@Sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Ahluwalia"
	g.lname="Amandeep"
	g.email="DLW8828@Sbcglobal.net" 
	g.address="18817 Bellgrove Circle" 
	g.city="Saratoga" 
	g.phone="(650) 799-3178" 
	g.ntrp="MJr." 
	g.mtype="NRS" 
	g.put()
#5 

	selfobj.response.write("Nancy  Andersen  NBragaAndersen@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Nancy"
	g.lname="Andersen"
	g.email="NBragaAndersen@gmail.com" 
	g.address="3032 Cameron Way" 
	g.city="Santa Clara" 
	g.phone="(408) 799-3678" 
	g.ntrp="F3.0" 
	g.mtype="RS" 
	g.put()
#6 

	selfobj.response.write("Kip  Anderson  kipanderson2003@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Kip"
	g.lname="Anderson"
	g.email="kipanderson2003@yahoo.com" 
	g.address="2744 Wallace St" 
	g.city="Santa Clara" 
	g.phone="(408) 243-8302" 
	g.ntrp="M4.0" 
	g.mtype="RS" 
	g.put()
#7 

	selfobj.response.write("Janet  Arsenault  j6ma@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Janet"
	g.lname="Arsenault"
	g.email="j6ma@sbcglobal.net" 
	g.address="1312 Meadowlark Ave" 
	g.city="San Jose" 
	g.phone="(408) 244-7508" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#8 

	selfobj.response.write("Hideko  Azama  tennissenior@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Hideko"
	g.lname="Azama"
	g.email="tennissenior@yahoo.com" 
	g.address="3115 Mauricia Ave." 
	g.city="Santa Clara" 
	g.phone="(408) 246-5129" 
	g.ntrp="F4.0" 
	g.mtype="RS" 
	g.put()
#9 

	selfobj.response.write("Patrick  Bacungan  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Patrick"
	g.lname="Bacungan"
	g.email="" 
	g.address="3375 Homestead Rd #70" 
	g.city="Santa Clara" 
	g.phone="(408) 247-3567" 
	g.ntrp="M3.0" 
	g.mtype="RF" 
	g.put()
#10 

	selfobj.response.write("Carolina  Bacungan  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Carolina"
	g.lname="Bacungan"
	g.email="" 
	g.address="3375 Homestead Rd #70" 
	g.city="Santa Clara" 
	g.phone="(408) 247-3567" 
	g.ntrp="F2.5" 
	g.mtype="RF" 
	g.put()
#11 

	selfobj.response.write("Conrado  Bacungan  carolbacungan@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Conrado"
	g.lname="Bacungan"
	g.email="carolbacungan@yahoo.com" 
	g.address="3375 Homestead Rd #70" 
	g.city="Santa Clara" 
	g.phone="(408) 881-2775" 
	g.ntrp="M3.5" 
	g.mtype="RF" 
	g.put()
#12 

	selfobj.response.write("Katherine  Barbour  katchat1992@comcast.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Katherine"
	g.lname="Barbour"
	g.email="katchat1992@comcast.net" 
	g.address="2431 South Park Lane" 
	g.city="Santa Clara" 
	g.phone="(408) 349-0511" 
	g.ntrp="F3.5" 
	g.mtype="RS" 
	g.put()
#13 

	selfobj.response.write("Naoko  Bean  naokobean@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Naoko"
	g.lname="Bean"
	g.email="naokobean@yahoo.com" 
	g.address="3440 El Camino Real #316" 
	g.city="Santa Clara" 
	g.phone="(408) 888-2290" 
	g.ntrp="F4.0" 
	g.mtype="RS" 
	g.put()
#14 

	selfobj.response.write("Carrie  Bell  c.p.bell@att.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Carrie"
	g.lname="Bell"
	g.email="c.p.bell@att.net" 
	g.address="1244 Maryann Dr" 
	g.city="Santa Clara" 
	g.phone="(408) 241-6793" 
	g.ntrp="F4.0" 
	g.mtype="RF" 
	g.put()
#15 

	selfobj.response.write("Melissa  Bell  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Melissa"
	g.lname="Bell"
	g.email="" 
	g.address="362 Manly Court" 
	g.city="Santa Clara" 
	g.phone="(408) 248-3643" 
	g.ntrp="F2.5" 
	g.mtype="RF" 
	g.put()
#16 

	selfobj.response.write("Richard  Bell  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Richard"
	g.lname="Bell"
	g.email="" 
	g.address="362 Manly Ct" 
	g.city="Santa Clara" 
	g.phone="(408) 248-3643" 
	g.ntrp="M3.0" 
	g.mtype="RF" 
	g.put()
#17 

	selfobj.response.write("Randy  Bell  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Randy"
	g.lname="Bell"
	g.email="" 
	g.address="1244 Maryann Dr" 
	g.city="Santa Clara" 
	g.phone="(408) 241-6793" 
	g.ntrp="M2.5" 
	g.mtype="RF" 
	g.put()
#18 

	selfobj.response.write("Cathy  Bell  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Cathy"
	g.lname="Bell"
	g.email="" 
	g.address="362 Manly Ct" 
	g.city="Santa Clara" 
	g.phone="(408) 248-3643" 
	g.ntrp="F2.0" 
	g.mtype="RF" 
	g.put()
#19 

	selfobj.response.write("Tony  Bell  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Tony"
	g.lname="Bell"
	g.email="" 
	g.address="362 Manly Court" 
	g.city="Santa Clara" 
	g.phone="(408) 248-3643" 
	g.ntrp="M3.5" 
	g.mtype="RF" 
	g.put()
#20 

	selfobj.response.write("Peter  Bell  petebell61502@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Peter"
	g.lname="Bell"
	g.email="petebell61502@yahoo.com" 
	g.address="362 Manly Ct" 
	g.city="Santa Clara" 
	g.phone="(408) 248-3643" 
	g.ntrp="M4.0" 
	g.mtype="RF" 
	g.put()
#21 

	selfobj.response.write("Jonathan  Bell  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Jonathan"
	g.lname="Bell"
	g.email="" 
	g.address="1244 Maryann Dr" 
	g.city="Santa Clara" 
	g.phone="(408) 241-6793" 
	g.ntrp="M2.5" 
	g.mtype="RF" 
	g.put()
#22 

	selfobj.response.write("Mary  Bell  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Mary"
	g.lname="Bell"
	g.email="" 
	g.address="362 Manly Court" 
	g.city="Santa Clara" 
	g.phone="(408) 248-3643" 
	g.ntrp="F2.0" 
	g.mtype="RF" 
	g.put()
#23 

	selfobj.response.write("Joan  Bell  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Joan"
	g.lname="Bell"
	g.email="" 
	g.address="362 Manly Court" 
	g.city="Santa Clara" 
	g.phone="(408) 248-3643" 
	g.ntrp="F2.5" 
	g.mtype="RF" 
	g.put()
#24 

	selfobj.response.write("Benoit  Belley  benoit.p.belley@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Benoit"
	g.lname="Belley"
	g.email="benoit.p.belley@gmail.com" 
	g.address="999 W. Evelyn Terrace Apt 8" 
	g.city="Sunnyvale" 
	g.phone="(925) 413-5760" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#25 

	selfobj.response.write("Deanne  Benetz  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Deanne"
	g.lname="Benetz"
	g.email="" 
	g.address="660 Mareno Ln." 
	g.city="Santa Clara" 
	g.phone="() " 
	g.ntrp="F" 
	g.mtype="RS" 
	g.put()
#26 

	selfobj.response.write("Alexi  Benetz  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Alexi"
	g.lname="Benetz"
	g.email="" 
	g.address="660 Mareno Ln." 
	g.city="Santa Clara" 
	g.phone="() " 
	g.ntrp="F" 
	g.mtype="RS" 
	g.put()
#27 

	selfobj.response.write("Dan  Benetz  danbenetz@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Dan"
	g.lname="Benetz"
	g.email="danbenetz@sbcglobal.net" 
	g.address="660 Mareno Ln." 
	g.city="Santa Clara" 
	g.phone="(408) 296-5320" 
	g.ntrp="M" 
	g.mtype="RS" 
	g.put()
#28 

	selfobj.response.write("Collin  Benetz  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Collin"
	g.lname="Benetz"
	g.email="" 
	g.address="660 Mareno Ln." 
	g.city="Santa Clara" 
	g.phone="() " 
	g.ntrp="M" 
	g.mtype="RS" 
	g.put()
#29 

	selfobj.response.write("Shane  Benetz  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Shane"
	g.lname="Benetz"
	g.email="" 
	g.address="660 Mareno Ln." 
	g.city="Santa Clara" 
	g.phone="() " 
	g.ntrp="M" 
	g.mtype="RS" 
	g.put()
#30 

	selfobj.response.write("Nobuo  Beniyama  nb3298@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Nobuo"
	g.lname="Beniyama"
	g.email="nb3298@gmail.com" 
	g.address="550 Moreland Way Apt 1206" 
	g.city="Santa Clara" 
	g.phone="(408) 960-5470" 
	g.ntrp="M" 
	g.mtype="RS" 
	g.put()
#31 

	selfobj.response.write("Fumiko  Beniyama  fmkbeni@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Fumiko"
	g.lname="Beniyama"
	g.email="fmkbeni@gmail.com" 
	g.address="550 Moreland Way Apt 1206" 
	g.city="Santa Clara" 
	g.phone="(408) 960-5470" 
	g.ntrp="F" 
	g.mtype="RS" 
	g.put()
#32 

	selfobj.response.write("Abishek  Bhonsle  abhi.ncsu@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Abishek"
	g.lname="Bhonsle"
	g.email="abhi.ncsu@gmail.com" 
	g.address="900 Pepper Tree Ln. #121" 
	g.city="Santa Clara" 
	g.phone="(919) 449-8369" 
	g.ntrp="M3.5" 
	g.mtype="RS" 
	g.put()
#33 

	selfobj.response.write("Shar  Bishop  shardean@comcast.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Shar"
	g.lname="Bishop"
	g.email="shardean@comcast.net" 
	g.address="1220 Tasman Drive 461" 
	g.city="Sunnyvale" 
	g.phone="(408) 745-1799" 
	g.ntrp="F3.0" 
	g.mtype="NRS" 
	g.put()
#34 

	selfobj.response.write("Susan  Bittner  kidklinic@aol.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Susan"
	g.lname="Bittner"
	g.email="kidklinic@aol.com" 
	g.address="14067 Apricot Hill" 
	g.city="Saratoga" 
	g.phone="(408) 867-7048" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#35 

	selfobj.response.write("Greg  Borromeo  triplegg2001@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Greg"
	g.lname="Borromeo"
	g.email="triplegg2001@yahoo.com" 
	g.address="3743 Acapulco Dr" 
	g.city="Campbell" 
	g.phone="(408) 309-2317" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#36 

	selfobj.response.write("Robert  Brunkhorst  bbrunkhorst@sandisk.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Robert"
	g.lname="Brunkhorst"
	g.email="bbrunkhorst@sandisk.com" 
	g.address="849 Humewick Way" 
	g.city="Sunnyvale" 
	g.phone="(408) 739-6480" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#37 

	selfobj.response.write("Ike  Bunanta  ibunanta@me.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Ike"
	g.lname="Bunanta"
	g.email="ibunanta@me.com" 
	g.address="1059 Konstane Terr" 
	g.city="Sunnyvale" 
	g.phone="(408) 406-5830" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#38 

	selfobj.response.write("Thomas  Cavello  Y@")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Thomas"
	g.lname="Cavello"
	g.email="Y@" 
	g.address="1974 Homestead Rd" 
	g.city="Santa Clara" 
	g.phone="() M" 
	g.ntrp="3" 
	g.mtype="RS" 
	g.put()
#39 

	selfobj.response.write("Volga  Cavello  volgab@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Volga"
	g.lname="Cavello"
	g.email="volgab@yahoo.com" 
	g.address="1974 Homestead Rd" 
	g.city="Santa Clara" 
	g.phone="(650) 303-1151" 
	g.ntrp="F3.0" 
	g.mtype="RS" 
	g.put()
#40 

	selfobj.response.write("Osbert  Chan  chansrus2@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Osbert"
	g.lname="Chan"
	g.email="chansrus2@yahoo.com" 
	g.address="3300 Scott Blvd" 
	g.city="Santa Clara" 
	g.phone="(408) 563-4239" 
	g.ntrp="M4.5" 
	g.mtype="RS" 
	g.put()
#41 

	selfobj.response.write("Taeck  Chiang  Taeckchiang@aol.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Taeck"
	g.lname="Chiang"
	g.email="Taeckchiang@aol.com" 
	g.address="1235 De Agora Comns." 
	g.city="San Jose" 
	g.phone="(408) 306-3657" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#42 

	selfobj.response.write("Harvey  Chin  chinharvey@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Harvey"
	g.lname="Chin"
	g.email="chinharvey@sbcglobal.net" 
	g.address="3366 Solano Ct" 
	g.city="Santa Clara" 
	g.phone="(408) 984-2338" 
	g.ntrp="M3.5" 
	g.mtype="RS" 
	g.put()
#43 

	selfobj.response.write("Liliane  Cromer  lilianec@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Liliane"
	g.lname="Cromer"
	g.email="lilianec@sbcglobal.net" 
	g.address="14120 Palomino Way" 
	g.city="Saratoga" 
	g.phone="(408) 823-6448" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#44 

	selfobj.response.write("Lori  Cruz-Spray  cruzspray@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Lori"
	g.lname="Cruz-Spray"
	g.email="cruzspray@gmail.com" 
	g.address="555 Minton Lane" 
	g.city="Mountain View" 
	g.phone="(650) 690-0022" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#45 

	selfobj.response.write("Machiko  Cyr  machikoc@pacbell.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Machiko"
	g.lname="Cyr"
	g.email="machikoc@pacbell.net" 
	g.address="5518 Castle Manor Dr" 
	g.city="San Jose" 
	g.phone="(408) 257-7971" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#46 

	selfobj.response.write("Jackie  Davidson  jacqlyn.davidson@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Jackie"
	g.lname="Davidson"
	g.email="jacqlyn.davidson@gmail.com" 
	g.address="536 Hawthorne Ave. Apt C" 
	g.city="Palo Alto" 
	g.phone="(443) 812-4374" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#47 

	selfobj.response.write("Jaya  Dawson  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Jaya"
	g.lname="Dawson"
	g.email="" 
	g.address="2329 Thompson Place" 
	g.city="Santa Clara" 
	g.phone="() " 
	g.ntrp="F" 
	g.mtype="RS" 
	g.put()
#48 

	selfobj.response.write("Marcus  Dawson  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Marcus"
	g.lname="Dawson"
	g.email="" 
	g.address="2329 Thompson Place" 
	g.city="Santa Clara" 
	g.phone="() " 
	g.ntrp="M" 
	g.mtype="RS" 
	g.put()
#49 

	selfobj.response.write("Golda  Dawson  goldz0407@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Golda"
	g.lname="Dawson"
	g.email="goldz0407@yahoo.com" 
	g.address="2329 Thompson Place" 
	g.city="Santa Clara" 
	g.phone="(408) 582-2971" 
	g.ntrp="F2.5" 
	g.mtype="RS" 
	g.put()
#50 

	selfobj.response.write("Jessica  DeBooson  jessica4tennis@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Jessica"
	g.lname="DeBooson"
	g.email="jessica4tennis@gmail.com" 
	g.address="Palm Drive" 
	g.city="Fremont" 
	g.phone="(510) 366-4118" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#51 

	selfobj.response.write("Mark  DeSouza  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Mark"
	g.lname="DeSouza"
	g.email="" 
	g.address="2983 Millar Ave." 
	g.city="SantaClara" 
	g.phone="(4008) 241-0102" 
	g.ntrp="M" 
	g.mtype="RF" 
	g.put()
#52 

	selfobj.response.write("Onofre  DeSouza  onofre2237@aol.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Onofre"
	g.lname="DeSouza"
	g.email="onofre2237@aol.com" 
	g.address="2983 Millar Ave." 
	g.city="Santa Clara" 
	g.phone="(408) 241-0102" 
	g.ntrp="M3.0" 
	g.mtype="RF" 
	g.put()
#53 

	selfobj.response.write("Marky  DeSouza  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Marky"
	g.lname="DeSouza"
	g.email="" 
	g.address="2983 Millar Ave." 
	g.city="Santa Clara" 
	g.phone="(408) 241-0102" 
	g.ntrp="M2.5" 
	g.mtype="RF" 
	g.put()
#54 

	selfobj.response.write("Gurpreet  Dhaman  gurpreet_tennis@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Gurpreet"
	g.lname="Dhaman"
	g.email="gurpreet_tennis@yahoo.com" 
	g.address="932 Planetree Place" 
	g.city="Sunnyvale" 
	g.phone="(206) 372-8688" 
	g.ntrp="M3.0" 
	g.mtype="NRS" 
	g.put()
#55 

	selfobj.response.write("Consuelo  Domingo  conniedomingo@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Consuelo"
	g.lname="Domingo"
	g.email="conniedomingo@sbcglobal.net" 
	g.address="6645 Dairy Ave" 
	g.city="Newark" 
	g.phone="(408) 646-8654" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#56 

	selfobj.response.write("Thomas  Dunham  s.dunham@aixtron.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Thomas"
	g.lname="Dunham"
	g.email="s.dunham@aixtron.com" 
	g.address="3654 Franklin Ave" 
	g.city="Fremont" 
	g.phone="(510) 683-9212" 
	g.ntrp="M3.0" 
	g.mtype="NRS" 
	g.put()
#57 

	selfobj.response.write("Carl  Dunlap  highaffinitycarl@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Carl"
	g.lname="Dunlap"
	g.email="highaffinitycarl@yahoo.com" 
	g.address="990B La Mesa Terrace" 
	g.city="Sunnyvale" 
	g.phone="(408) 245-5405" 
	g.ntrp="M3.0" 
	g.mtype="NRS" 
	g.put()
#58 

	selfobj.response.write("Maria  Duong  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Maria"
	g.lname="Duong"
	g.email="" 
	g.address="3730 Peacock Court #2" 
	g.city="Santa Clara" 
	g.phone="(408) 483-8936" 
	g.ntrp="F2.5" 
	g.mtype="RF" 
	g.put()
#59 

	selfobj.response.write("Lauren  Duong  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Lauren"
	g.lname="Duong"
	g.email="" 
	g.address="3730 Peacock Court #2" 
	g.city="Santa Clara" 
	g.phone="(408) 483-8936" 
	g.ntrp="F2.5" 
	g.mtype="RF" 
	g.put()
#60 

	selfobj.response.write("Ryan  Duong  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Ryan"
	g.lname="Duong"
	g.email="" 
	g.address="3730 Peacock Court #2" 
	g.city="Santa Clara" 
	g.phone="(408) 483-8936" 
	g.ntrp="M2.5" 
	g.mtype="RF" 
	g.put()
#61 

	selfobj.response.write("Tho  Duong  tho.duog@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Tho"
	g.lname="Duong"
	g.email="tho.duog@gmail.com" 
	g.address="3730 Peacock Court #2" 
	g.city="Santa Clara" 
	g.phone="(408) 483-8936" 
	g.ntrp="M3.5" 
	g.mtype="RF" 
	g.put()
#62 

	selfobj.response.write("Emma  Duque  emma_duque@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Emma"
	g.lname="Duque"
	g.email="emma_duque@yahoo.com" 
	g.address="121 Macdowell Ter." 
	g.city="Sunnyvale" 
	g.phone="(408) 736-1177" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#63 

	selfobj.response.write("Randall  Elder  red_r_randal@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Randall"
	g.lname="Elder"
	g.email="red_r_randal@yahoo.com" 
	g.address="466 Appian Way" 
	g.city="Union City" 
	g.phone="(510) 493-8110" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#64 

	selfobj.response.write("Kaori  Enomoto  kaori@saphirellc.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Kaori"
	g.lname="Enomoto"
	g.email="kaori@saphirellc.com" 
	g.address="10250 Vicksburg Court" 
	g.city="Cupertino" 
	g.phone="(408) 623-5702" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#65 

	selfobj.response.write("Kaddie  Feng-Ashley  k2008tennis@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Kaddie"
	g.lname="Feng-Ashley"
	g.email="k2008tennis@yahoo.com" 
	g.address="PO Box 518" 
	g.city="Morgan Hill" 
	g.phone="(408) 778-4469" 
	g.ntrp="F3.0" 
	g.mtype="NRS" 
	g.put()
#66 

	selfobj.response.write("Eryqa  Flores  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Eryqa"
	g.lname="Flores"
	g.email="" 
	g.address="2329 Thompson Place" 
	g.city="Santa Clara" 
	g.phone="() " 
	g.ntrp="F" 
	g.mtype="RS" 
	g.put()
#67 

	selfobj.response.write("Anne  Giannini  rudyannie@aol.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Anne"
	g.lname="Giannini"
	g.email="rudyannie@aol.com" 
	g.address="430 Laurel Ave." 
	g.city="Millbrae" 
	g.phone="(650) 678-8812" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#68 

	selfobj.response.write("Karthi  Gopalan  karthigopalan@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Karthi"
	g.lname="Gopalan"
	g.email="karthigopalan@yahoo.com" 
	g.address="1616 Hope Drive 423" 
	g.city="Santa Clara" 
	g.phone="(408) 910-5127" 
	g.ntrp="F4.0" 
	g.mtype="RS" 
	g.put()
#69 

	selfobj.response.write("Allan  Greenberg  allgreen@ucla.edu")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Allan"
	g.lname="Greenberg"
	g.email="allgreen@ucla.edu" 
	g.address="550 Moreland Way Apt 2403" 
	g.city="Santa Clara" 
	g.phone="(310) 576-1310" 
	g.ntrp="M4.0" 
	g.mtype="RS" 
	g.put()
#70 

	selfobj.response.write("Vikas  Gupta  vikasait@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Vikas"
	g.lname="Gupta"
	g.email="vikasait@gmail.com" 
	g.address="3480 Granada Ave. #268" 
	g.city="Santa Clara" 
	g.phone="(571) 230-2377" 
	g.ntrp="M3.0" 
	g.mtype="RS" 
	g.put()
#71 

	selfobj.response.write("Dah-Young  Hahn  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Dah-Young"
	g.lname="Hahn"
	g.email="" 
	g.address="2926 Roma Ct." 
	g.city="Santa Clara" 
	g.phone="() " 
	g.ntrp="F" 
	g.mtype="RS" 
	g.put()
#72 

	selfobj.response.write("Hyeok  Hahn  hhahn00@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Hyeok"
	g.lname="Hahn"
	g.email="hhahn00@yahoo.com" 
	g.address="2926 Roma Ct." 
	g.city="Santa Clara" 
	g.phone="(408) 249-6456" 
	g.ntrp="M3.5" 
	g.mtype="RS" 
	g.put()
#73 

	selfobj.response.write("Julie  Hahn  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Julie"
	g.lname="Hahn"
	g.email="" 
	g.address="2926 Roma Ct." 
	g.city="Santa Clara" 
	g.phone="() " 
	g.ntrp="F" 
	g.mtype="RS" 
	g.put()
#74 

	selfobj.response.write("Lucy  Harendza  lharendza@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Lucy"
	g.lname="Harendza"
	g.email="lharendza@yahoo.com" 
	g.address="267 Cahill Pk Dr" 
	g.city="San Jose" 
	g.phone="(408) 888-2447" 
	g.ntrp="F3.0" 
	g.mtype="NRS" 
	g.put()
#75 

	selfobj.response.write("Norah  Hibbits  norellha@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Norah"
	g.lname="Hibbits"
	g.email="norellha@yahoo.com" 
	g.address="1091 Essex Ave." 
	g.city="Sunnyvale" 
	g.phone="(301) 580-8329" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#76 

	selfobj.response.write("Jeanette  Hoggatt  queenb_95051@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Jeanette"
	g.lname="Hoggatt"
	g.email="queenb_95051@yahoo.com" 
	g.address="3070 Dibble Court" 
	g.city="Santa Clara" 
	g.phone="(408) 243-4381" 
	g.ntrp="F3.5" 
	g.mtype="RF" 
	g.put()
#77 

	selfobj.response.write("Herta  Hoggatt  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Herta"
	g.lname="Hoggatt"
	g.email="" 
	g.address="3070 Dibble Court" 
	g.city="Santa Clara" 
	g.phone="(408) 243-4381" 
	g.ntrp="F" 
	g.mtype="RF" 
	g.put()
#78 

	selfobj.response.write("Pamela  Hoggatt  pnhoggatt@hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Pamela"
	g.lname="Hoggatt"
	g.email="pnhoggatt@hotmail.com" 
	g.address="3070 Dibble Court" 
	g.city="Santa Clara" 
	g.phone="(408) 243-4381" 
	g.ntrp="F3.0" 
	g.mtype="RF" 
	g.put()
#79 

	selfobj.response.write("Rosemary  Hopkins  rosemarh@hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Rosemary"
	g.lname="Hopkins"
	g.email="rosemarh@hotmail.com" 
	g.address="920 Laurel Glen Dr." 
	g.city="Palo Alto" 
	g.phone="(650) 948-0827" 
	g.ntrp="F" 
	g.mtype="NRS" 
	g.put()
#80 

	selfobj.response.write("Emi  Iizuka  wellbng@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Emi"
	g.lname="Iizuka"
	g.email="wellbng@gmail.com" 
	g.address="319 N. Murphy Ave." 
	g.city="Sunnyvale" 
	g.phone="(408) 306-6516" 
	g.ntrp="F" 
	g.mtype="NRS" 
	g.put()
#81 

	selfobj.response.write("Akari  Ikeda  aikeda14@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Akari"
	g.lname="Ikeda"
	g.email="aikeda14@yahoo.com" 
	g.address="3765 Tamarack Ln #280" 
	g.city="Santa Clara" 
	g.phone="(408) 916-7875" 
	g.ntrp="F4.5" 
	g.mtype="RS" 
	g.put()
#82 

	selfobj.response.write("Nicole  Isaacson  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Nicole"
	g.lname="Isaacson"
	g.email="" 
	g.address="513 Hickory Pl" 
	g.city="Santa Clara" 
	g.phone="(408) 247-0343" 
	g.ntrp="F" 
	g.mtype="RF" 
	g.put()
#83 

	selfobj.response.write("Alice  Isaacson  aliceisaacson@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Alice"
	g.lname="Isaacson"
	g.email="aliceisaacson@yahoo.com" 
	g.address="513 Hickory Pl" 
	g.city="Santa Clara" 
	g.phone="(408) 247-0343" 
	g.ntrp="F3.5" 
	g.mtype="RF" 
	g.put()
#84 

	selfobj.response.write("Matthew  Isaacson  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Matthew"
	g.lname="Isaacson"
	g.email="" 
	g.address="513 Hickory Pl" 
	g.city="Santa Clara" 
	g.phone="(408) 247-0343" 
	g.ntrp="M" 
	g.mtype="RF" 
	g.put()
#85 

	selfobj.response.write("Mark  Isaacson  mji1422@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Mark"
	g.lname="Isaacson"
	g.email="mji1422@yahoo.com" 
	g.address="513 Hickory Pl" 
	g.city="Santa Clara" 
	g.phone="(408) 247-0343" 
	g.ntrp="M" 
	g.mtype="RF" 
	g.put()
#86 

	selfobj.response.write("Taryn  Ishida  tarynishida@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Taryn"
	g.lname="Ishida"
	g.email="tarynishida@gmail.com" 
	g.address="95 Hobson St #3A" 
	g.city="San Jose" 
	g.phone="(408) 247-0807" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#87 

	selfobj.response.write("Karthik  Jayaraman Raghuram  jrk1982@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Karthik"
	g.lname="Jayaraman Raghuram"
	g.email="jrk1982@gmail.com" 
	g.address="900 Pepper Tree Lane Apt 618" 
	g.city="Santa Clara" 
	g.phone="(805) 245-4504" 
	g.ntrp="M3.5" 
	g.mtype="RS" 
	g.put()
#88 

	selfobj.response.write("Pallavi  Jeewanker  abhi.ncsu@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Pallavi"
	g.lname="Jeewanker"
	g.email="abhi.ncsu@gmail.com" 
	g.address="900 Pepper Tree Ln. #121" 
	g.city="Santa Clara" 
	g.phone="(919) 449-8369" 
	g.ntrp="F" 
	g.mtype="RS" 
	g.put()
#89 

	selfobj.response.write("Victoria  Jew  vcjew@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Victoria"
	g.lname="Jew"
	g.email="vcjew@yahoo.com" 
	g.address="10260 Calvert Dr" 
	g.city="Cupertino" 
	g.phone="(650) 208-7746" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#90 

	selfobj.response.write("Robert  Jiang  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Robert"
	g.lname="Jiang"
	g.email="" 
	g.address="460 Norweed Circle" 
	g.city="Santa Clara" 
	g.phone="() " 
	g.ntrp="M" 
	g.mtype="RS" 
	g.put()
#91 

	selfobj.response.write("Tom  Jiang  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Tom"
	g.lname="Jiang"
	g.email="" 
	g.address="460 Norweed Circle" 
	g.city="Santa Clara" 
	g.phone="() " 
	g.ntrp="M" 
	g.mtype="RS" 
	g.put()
#92 

	selfobj.response.write("Adam  Jiang  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Adam"
	g.lname="Jiang"
	g.email="" 
	g.address="460 Norweed Circle" 
	g.city="Santa Clara" 
	g.phone="() " 
	g.ntrp="M" 
	g.mtype="RS" 
	g.put()
#93 

	selfobj.response.write("Nancy  Jing  nancyyj@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Nancy"
	g.lname="Jing"
	g.email="nancyyj@yahoo.com" 
	g.address="10810 S Blaney Ave" 
	g.city="Cupertino" 
	g.phone="(510) 589-9999" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#94 

	selfobj.response.write("Elko  Johnson  elkoj@earthlink.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Elko"
	g.lname="Johnson"
	g.email="elkoj@earthlink.net" 
	g.address="18112 Daves Ave" 
	g.city="Monte Sereno" 
	g.phone="(408) 354-1261" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#95 

	selfobj.response.write("Vanessa  Jordan  vincalifornia@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Vanessa"
	g.lname="Jordan"
	g.email="vincalifornia@gmail.com" 
	g.address="1700 N. 1st St." 
	g.city="San Jose" 
	g.phone="(214) 392-3609" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#96 

	selfobj.response.write("Steve  Jow  steven.jow@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Steve"
	g.lname="Jow"
	g.email="steven.jow@gmail.com" 
	g.address="88 Bush St. Unit #2135" 
	g.city="San Jose" 
	g.phone="(408) 390-7728" 
	g.ntrp="M4.5" 
	g.mtype="NRS" 
	g.put()
#97 

	selfobj.response.write("Marie  Jue  msfan00@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Marie"
	g.lname="Jue"
	g.email="msfan00@yahoo.com" 
	g.address="10989 Ronald Wy" 
	g.city="Cupertino" 
	g.phone="(408) 332-6026" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#98 

	selfobj.response.write("Jacqueline  Kerkhove  jkerkhove@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Jacqueline"
	g.lname="Kerkhove"
	g.email="jkerkhove@gmail.com" 
	g.address="755 Santa Paula Ave" 
	g.city="Sunnyvale" 
	g.phone="(408) 499-6233" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#99 

	selfobj.response.write("Tiang  Khoo  tkhoo@mac.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Tiang"
	g.lname="Khoo"
	g.email="tkhoo@mac.com" 
	g.address="" 
	g.city="Sunnyvale" 
	g.phone="() " 
	g.ntrp="M4.5" 
	g.mtype="" 
	g.put()
#100 

	selfobj.response.write("Amy  Kim  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Amy"
	g.lname="Kim"
	g.email="" 
	g.address="3750 Miraverde Ct" 
	g.city="Santa Clara" 
	g.phone="() " 
	g.ntrp="F" 
	g.mtype="RS" 
	g.put()
#101 

	selfobj.response.write("Kevin  Kim  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Kevin"
	g.lname="Kim"
	g.email="" 
	g.address="3750 Miraverde Ct" 
	g.city="Santa Clara" 
	g.phone="() " 
	g.ntrp="M" 
	g.mtype="RS" 
	g.put()
#102 

	selfobj.response.write("Sanggyum  Kim  sanggyum.kim@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Sanggyum"
	g.lname="Kim"
	g.email="sanggyum.kim@gmail.com" 
	g.address="3750 Miraverde Ct" 
	g.city="Santa Clara" 
	g.phone="(510) 926-2837" 
	g.ntrp="M4.5" 
	g.mtype="RS" 
	g.put()
#103 

	selfobj.response.write("Sayaka  Kishino  ksh_kishino@hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Sayaka"
	g.lname="Kishino"
	g.email="ksh_kishino@hotmail.com" 
	g.address="1173 Susan Way" 
	g.city="Sunnyvale" 
	g.phone="(408) 773-0659" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#104 

	selfobj.response.write("Kazuhiro  Kishino  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Kazuhiro"
	g.lname="Kishino"
	g.email="" 
	g.address="1173 Susan Way" 
	g.city="Sunnyvale" 
	g.phone="(408) 773-0651" 
	g.ntrp="M4.5" 
	g.mtype="NRS" 
	g.put()
#105 

	selfobj.response.write("Sayaka  Kobayashi  sayaka.kobayashi0325@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Sayaka"
	g.lname="Kobayashi"
	g.email="sayaka.kobayashi0325@gmail.com" 
	g.address="25 Rio Robles East #428" 
	g.city="San Jose" 
	g.phone="(408) 489-3357" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#106 

	selfobj.response.write("Shyang  Kong  skkong_98@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Shyang"
	g.lname="Kong"
	g.email="skkong_98@yahoo.com" 
	g.address="1085 Tasman Dr. #549" 
	g.city="Sunnyvale" 
	g.phone="(858) 337-7509" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#107 

	selfobj.response.write("Ryan  Koo  tennisclinic@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Ryan"
	g.lname="Koo"
	g.email="tennisclinic@gmail.com" 
	g.address="3655 N. First St." 
	g.city="San Jose" 
	g.phone="(408) 420-4181" 
	g.ntrp="M4.5" 
	g.mtype="NRS" 
	g.put()
#108 

	selfobj.response.write("Jack  Koo  jackkoo@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Jack"
	g.lname="Koo"
	g.email="jackkoo@sbcglobal.net" 
	g.address="6554 Whitbourne Dr." 
	g.city="San Jose" 
	g.phone="(408) 824-4882" 
	g.ntrp="M4.5" 
	g.mtype="NRS" 
	g.put()
#109 

	selfobj.response.write("Fran  Kristofferson  franmavia@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Fran"
	g.lname="Kristofferson"
	g.email="franmavia@yahoo.com" 
	g.address="4 Rosevelt Circle" 
	g.city="Palo Alto" 
	g.phone="() " 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#110 

	selfobj.response.write("Ben  Le  Mlebin@msn.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Ben"
	g.lname="Le"
	g.email="Mlebin@msn.com" 
	g.address="4129 George Ave. #4" 
	g.city="San Mateo" 
	g.phone="(650) 483-9565" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#111 

	selfobj.response.write("Brandon  Lee  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Brandon"
	g.lname="Lee"
	g.email="" 
	g.address="4558 Cheeney St" 
	g.city="Santa Clara" 
	g.phone="(408) 506-2089" 
	g.ntrp="M" 
	g.mtype="RS" 
	g.put()
#112 

	selfobj.response.write("Nathan M  Lee  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Nathan M"
	g.lname="Lee"
	g.email="" 
	g.address="4558 Cheeney St" 
	g.city="Santa Clara" 
	g.phone="(408) 506-2089" 
	g.ntrp="M" 
	g.mtype="RS" 
	g.put()
#113 

	selfobj.response.write("Hang  Lee  lee.hang@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Hang"
	g.lname="Lee"
	g.email="lee.hang@yahoo.com" 
	g.address="4558 Cheeney St" 
	g.city="Santa Clara" 
	g.phone="(408) 506-2089" 
	g.ntrp="M3.5" 
	g.mtype="RS" 
	g.put()
#114 

	selfobj.response.write("Lisa  Lee  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Lisa"
	g.lname="Lee"
	g.email="" 
	g.address="4558 Cheeney St" 
	g.city="Santa Clara" 
	g.phone="(408) 506-2089" 
	g.ntrp="F" 
	g.mtype="RS" 
	g.put()
#115 

	selfobj.response.write("Brook  Lee  bm.lee@verizon.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Brook"
	g.lname="Lee"
	g.email="bm.lee@verizon.net" 
	g.address="1172 Morse Ave" 
	g.city="Sunnyvale" 
	g.phone="(408) 745-7088" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#116 

	selfobj.response.write("Scott  Lenz  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Scott"
	g.lname="Lenz"
	g.email="" 
	g.address="5938 Country Club Pkwy" 
	g.city="San Jose" 
	g.phone="(408) 531-1699" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#117 

	selfobj.response.write("Joy  Lenz  jlenz77@hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Joy"
	g.lname="Lenz"
	g.email="jlenz77@hotmail.com" 
	g.address="5938 Country Club Pkwy" 
	g.city="San Jose" 
	g.phone="(408) 531-1699" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#118 

	selfobj.response.write("Austin  Lenz  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Austin"
	g.lname="Lenz"
	g.email="" 
	g.address="5938 Country Club Pkwy" 
	g.city="San Jose" 
	g.phone="(408) 531-1699" 
	g.ntrp="M4.5" 
	g.mtype="NRS" 
	g.put()
#119 

	selfobj.response.write("Colman  Leung  uciengr@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Colman"
	g.lname="Leung"
	g.email="uciengr@yahoo.com" 
	g.address="609 N. Capitol Ave. #137" 
	g.city="San Jose" 
	g.phone="(415) 312-3908" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#120 

	selfobj.response.write("Jianling  Li  jlee_19711@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Jianling"
	g.lname="Li"
	g.email="jlee_19711@yahoo.com" 
	g.address="3270 Saint Ignatius Place" 
	g.city="Santa Clara" 
	g.phone="(847) 224-9820" 
	g.ntrp="F3.5" 
	g.mtype="RS" 
	g.put()
#121 

	selfobj.response.write("Martin F  Lim  martin998899@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Martin F"
	g.lname="Lim"
	g.email="martin998899@gmail.com" 
	g.address="2368 Susan Dr" 
	g.city="Santa Clara" 
	g.phone="(408) 246-4137" 
	g.ntrp="M3.0" 
	g.mtype="RS" 
	g.put()
#122 

	selfobj.response.write("Leila  Linke  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Leila"
	g.lname="Linke"
	g.email="" 
	g.address="1285 Main Street" 
	g.city="Santa Clara" 
	g.phone="() " 
	g.ntrp="F" 
	g.mtype="RF" 
	g.put()
#123 

	selfobj.response.write("Cleo  Linke  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Cleo"
	g.lname="Linke"
	g.email="" 
	g.address="1285 Main Street" 
	g.city="Santa Clara" 
	g.phone="() " 
	g.ntrp="F" 
	g.mtype="RF" 
	g.put()
#124 

	selfobj.response.write("Mina  Linke  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Mina"
	g.lname="Linke"
	g.email="" 
	g.address="1285 Main Street" 
	g.city="Santa Clara" 
	g.phone="() " 
	g.ntrp="F" 
	g.mtype="RF" 
	g.put()
#125 

	selfobj.response.write("Erin  Linke  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Erin"
	g.lname="Linke"
	g.email="" 
	g.address="1285 Main Street" 
	g.city="Santa Clara" 
	g.phone="() " 
	g.ntrp="F" 
	g.mtype="RF" 
	g.put()
#126 

	selfobj.response.write("Al  Linke  alinke@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Al"
	g.lname="Linke"
	g.email="alinke@yahoo.com" 
	g.address="1285 Main Street" 
	g.city="Santa Clara" 
	g.phone="(408) 892-1718" 
	g.ntrp="M4.0" 
	g.mtype="RF" 
	g.put()
#127 

	selfobj.response.write("Darren  Lo  darrenlo@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Darren"
	g.lname="Lo"
	g.email="darrenlo@yahoo.com" 
	g.address="19500 Pruneridge Ave #10101" 
	g.city="Cupertino" 
	g.phone="(949) 439-5645" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#128 

	selfobj.response.write("Robin  Lutgert  robinlutgert@msn.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Robin"
	g.lname="Lutgert"
	g.email="robinlutgert@msn.com" 
	g.address="170 Cuesta de los Gatos" 
	g.city="Los Gatos" 
	g.phone="(239) 860-1600" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#129 

	selfobj.response.write("Marshall  Madamba  mmadamba@redshift.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Marshall"
	g.lname="Madamba"
	g.email="mmadamba@redshift.com" 
	g.address="350 E Taylor St #6114" 
	g.city="San Jose" 
	g.phone="(408) 691-5758" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#130 

	selfobj.response.write("Chris  Madsen  teachmetennis@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Chris"
	g.lname="Madsen"
	g.email="teachmetennis@gmail.com" 
	g.address="1560 Camden Village Cir" 
	g.city="San Jose" 
	g.phone="(408) 489-3993" 
	g.ntrp="M4.5" 
	g.mtype="NRS" 
	g.put()
#131 

	selfobj.response.write("Jordan  Madsen  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Jordan"
	g.lname="Madsen"
	g.email="" 
	g.address="1560 Camden Village Cir" 
	g.city="San Jose" 
	g.phone="(408) 489-3993" 
	g.ntrp="M" 
	g.mtype="NRS" 
	g.put()
#132 

	selfobj.response.write("Cindy  Madsen  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Cindy"
	g.lname="Madsen"
	g.email="" 
	g.address="1560 Camden Village Cir" 
	g.city="San Jose" 
	g.phone="(408) 489-3993" 
	g.ntrp="F3.0" 
	g.mtype="NRS" 
	g.put()
#133 

	selfobj.response.write("Kayla  Madsen  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Kayla"
	g.lname="Madsen"
	g.email="" 
	g.address="1560 Camden Village Cir" 
	g.city="San Jose" 
	g.phone="(408) 489-3993" 
	g.ntrp="F" 
	g.mtype="NRS" 
	g.put()
#134 

	selfobj.response.write("Kayleen  Madsen  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Kayleen"
	g.lname="Madsen"
	g.email="" 
	g.address="1560 Camden Village Cir" 
	g.city="San Jose" 
	g.phone="(408) 489-3993" 
	g.ntrp="F" 
	g.mtype="NRS" 
	g.put()
#135 

	selfobj.response.write("Ronald  Mah  ronaldmah@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Ronald"
	g.lname="Mah"
	g.email="ronaldmah@sbcglobal.net" 
	g.address="2495 Tasso St" 
	g.city="Palo Alto" 
	g.phone="(650) 303-7114" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#136 

	selfobj.response.write("Sujatha  Mandava  sjt_m@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Sujatha"
	g.lname="Mandava"
	g.email="sjt_m@yahoo.com" 
	g.address="862 Bremerton Drive" 
	g.city="Sunnyvale" 
	g.phone="(4108) 832-2315" 
	g.ntrp="F3.0" 
	g.mtype="NRS" 
	g.put()
#137 

	selfobj.response.write("Reza  Manion  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Reza"
	g.lname="Manion"
	g.email="" 
	g.address="2504 Benton St." 
	g.city="Santa Clara" 
	g.phone="() " 
	g.ntrp="" 
	g.mtype="RS" 
	g.put()
#138 

	selfobj.response.write("Ali  Manion  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Ali"
	g.lname="Manion"
	g.email="" 
	g.address="2504 Benton St." 
	g.city="Santa Clara" 
	g.phone="() " 
	g.ntrp="" 
	g.mtype="RS" 
	g.put()
#139 

	selfobj.response.write("Sara  Manion  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Sara"
	g.lname="Manion"
	g.email="" 
	g.address="2504 Benton St." 
	g.city="Santa Clara" 
	g.phone="() " 
	g.ntrp="" 
	g.mtype="RS" 
	g.put()
#140 

	selfobj.response.write("Manjid  Manion  Majidmanion@att.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Manjid"
	g.lname="Manion"
	g.email="Majidmanion@att.net" 
	g.address="2504 Benton St." 
	g.city="Santa Clara" 
	g.phone="(408) 208-5752" 
	g.ntrp="M" 
	g.mtype="RS" 
	g.put()
#141 

	selfobj.response.write("Luzmaria  Martinez  katsulas@aol.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Luzmaria"
	g.lname="Martinez"
	g.email="katsulas@aol.com" 
	g.address="350 E Taylor St #6114" 
	g.city="San Jose" 
	g.phone="(408) 691-5758" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#142 

	selfobj.response.write("Helen  Matsumoto  geetennis@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Helen"
	g.lname="Matsumoto"
	g.email="geetennis@yahoo.com" 
	g.address="1247 Redoaks Dr" 
	g.city="San Jose" 
	g.phone="(408) 248-7922" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#143 

	selfobj.response.write("Ted  Matsushita  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Ted"
	g.lname="Matsushita"
	g.email="" 
	g.address="3375 Mauricia Ave." 
	g.city="Santa Clara" 
	g.phone="(408) 554-6592" 
	g.ntrp="M3.5" 
	g.mtype="RF" 
	g.put()
#144 

	selfobj.response.write("Laurie  Matsushita  lbjsmom@comcast.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Laurie"
	g.lname="Matsushita"
	g.email="lbjsmom@comcast.net" 
	g.address="3375 Mauricia Ave." 
	g.city="Santa Clara" 
	g.phone="(408) 554-6592" 
	g.ntrp="F4.0" 
	g.mtype="RF" 
	g.put()
#145 

	selfobj.response.write("Lindsey  Matsushita  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Lindsey"
	g.lname="Matsushita"
	g.email="" 
	g.address="3375 Mauricia Ave." 
	g.city="Santa Clara" 
	g.phone="(408) 554-6592" 
	g.ntrp="F" 
	g.mtype="RF" 
	g.put()
#146 

	selfobj.response.write("Brad  Matsushita  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Brad"
	g.lname="Matsushita"
	g.email="" 
	g.address="3375 Mauricia Ave." 
	g.city="Santa Clara" 
	g.phone="(408) 554-6592" 
	g.ntrp="M" 
	g.mtype="RF" 
	g.put()
#147 

	selfobj.response.write("Jenny  Matsushita  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Jenny"
	g.lname="Matsushita"
	g.email="" 
	g.address="3375 Mauricia Ave." 
	g.city="Santa Clara" 
	g.phone="(408) 554-6592" 
	g.ntrp="F" 
	g.mtype="RF" 
	g.put()
#148 

	selfobj.response.write("Dee  Mayer  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Dee"
	g.lname="Mayer"
	g.email="" 
	g.address="1143 Alice Dr" 
	g.city="Santa Clara" 
	g.phone="(408) 243-9768" 
	g.ntrp="F2.5" 
	g.mtype="RF" 
	g.put()
#149 

	selfobj.response.write("Jim  Mayer  mayertenn@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Jim"
	g.lname="Mayer"
	g.email="mayertenn@sbcglobal.net" 
	g.address="1143 Alice Dr" 
	g.city="Santa Clara" 
	g.phone="(408) 243-9768" 
	g.ntrp="M3.0" 
	g.mtype="RF" 
	g.put()
#150 

	selfobj.response.write("Colleen  McCullough  collmcc1999@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Colleen"
	g.lname="McCullough"
	g.email="collmcc1999@yahoo.com" 
	g.address="713 Astor Ct." 
	g.city="Mountain View" 
	g.phone="(650) 996-0432" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#151 

	selfobj.response.write("Sally  McElravey  samcelravey@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Sally"
	g.lname="McElravey"
	g.email="samcelravey@gmail.com" 
	g.address="12486 Brookglen Dr." 
	g.city="Saratoga" 
	g.phone="(408) 255-3248" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#152 

	selfobj.response.write("Lubica  Michalek  lubicaus@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Lubica"
	g.lname="Michalek"
	g.email="lubicaus@gmail.com" 
	g.address="10025 Crescent Rd" 
	g.city="Cupertino" 
	g.phone="(408) 582-3101" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#153 

	selfobj.response.write("Yuko  Mihara  miharayuko@hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Yuko"
	g.lname="Mihara"
	g.email="miharayuko@hotmail.com" 
	g.address="20208 Northwest Square" 
	g.city="Cupertino" 
	g.phone="(408) 393-5333" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#154 

	selfobj.response.write("Vivian  Miller  millervivian7@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Vivian"
	g.lname="Miller"
	g.email="millervivian7@gmail.com" 
	g.address="" 
	g.city="Sunnyvale" 
	g.phone="(805) 215-8011" 
	g.ntrp="F3.0" 
	g.mtype="NRS" 
	g.put()
#155 

	selfobj.response.write("Mio  Mizutani  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Mio"
	g.lname="Mizutani"
	g.email="" 
	g.address="119 Arcadia Ave." 
	g.city="Santa Clara" 
	g.phone="() " 
	g.ntrp="F" 
	g.mtype="RS" 
	g.put()
#156 

	selfobj.response.write("Tohru  Mizutani  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Tohru"
	g.lname="Mizutani"
	g.email="" 
	g.address="119 Arcadia Ave." 
	g.city="Santa Clara" 
	g.phone="() " 
	g.ntrp="M4.0" 
	g.mtype="RS" 
	g.put()
#157 

	selfobj.response.write("Akiyo  Mizutani  kxb00454@nifty.ne.jp")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Akiyo"
	g.lname="Mizutani"
	g.email="kxb00454@nifty.ne.jp" 
	g.address="119 Arcadia Ave." 
	g.city="Santa Clara" 
	g.phone="(408) 418-3441" 
	g.ntrp="F3.0" 
	g.mtype="RS" 
	g.put()
#158 

	selfobj.response.write("Gil  Molina  molinateam@comcast.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Gil"
	g.lname="Molina"
	g.email="molinateam@comcast.com" 
	g.address="64 Starbush Dr." 
	g.city="Sunnyvale" 
	g.phone="(408) 209-6549" 
	g.ntrp="M" 
	g.mtype="NRS" 
	g.put()
#159 

	selfobj.response.write("Roy  Molseed  roy.molseed@vta.org")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Roy"
	g.lname="Molseed"
	g.email="roy.molseed@vta.org" 
	g.address="2550 Blue rock Ct" 
	g.city="San Jose" 
	g.phone="(408) 580-6396" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#160 

	selfobj.response.write("Gayle  Moore  tennissenior@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Gayle"
	g.lname="Moore"
	g.email="tennissenior@yahoo.com" 
	g.address="3115 Mauricia Ave." 
	g.city="Santa Clara" 
	g.phone="(408) 246-5129" 
	g.ntrp="F3.0" 
	g.mtype="RS" 
	g.put()
#161 

	selfobj.response.write("Yukiko  Nara  yucco2250@live.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Yukiko"
	g.lname="Nara"
	g.email="yucco2250@live.com" 
	g.address="19702" 
	g.city="Saratoga" 
	g.phone="(408) 217-8424" 
	g.ntrp="F3.0" 
	g.mtype="NRS" 
	g.put()
#162 

	selfobj.response.write("Shiv  Natarajan  shiv.natarajan@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Shiv"
	g.lname="Natarajan"
	g.email="shiv.natarajan@yahoo.com" 
	g.address="4813 Verbena Way" 
	g.city="San Jose" 
	g.phone="(408) 480-1044" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#163 

	selfobj.response.write("Sara  Neill  saraknoh@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Sara"
	g.lname="Neill"
	g.email="saraknoh@yahoo.com" 
	g.address="767 N Fair Oaks Ave. #5" 
	g.city="Sunnyvale" 
	g.phone="(408) 505-2606" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#164 

	selfobj.response.write("Lloyd  Ngo  lloydngo@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Lloyd"
	g.lname="Ngo"
	g.email="lloydngo@yahoo.com" 
	g.address="3399 Victoria Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 891-1154" 
	g.ntrp="M3.5" 
	g.mtype="RS" 
	g.put()
#165 

	selfobj.response.write("Kristina  Ngo  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Kristina"
	g.lname="Ngo"
	g.email="" 
	g.address="3399 Victoria Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 945-1724" 
	g.ntrp="F3.0" 
	g.mtype="RS" 
	g.put()
#166 

	selfobj.response.write("Thi  Nguyen  baothiy2k@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Thi"
	g.lname="Nguyen"
	g.email="baothiy2k@yahoo.com" 
	g.address="1925 White Oaks Rd" 
	g.city="Campbell" 
	g.phone="(408) 879-9677" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#167 

	selfobj.response.write("Christian  Nguyen  christian.nguyen@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Christian"
	g.lname="Nguyen"
	g.email="christian.nguyen@yahoo.com" 
	g.address="1350 Sajak Ave." 
	g.city="San Jose" 
	g.phone="(510) 396-2992" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#168 

	selfobj.response.write("Leslie  Nguyen  leslie@uniquesolutions.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Leslie"
	g.lname="Nguyen"
	g.email="leslie@uniquesolutions.net" 
	g.address="1436 Leaftree Circle" 
	g.city="San Jose" 
	g.phone="(408) 219-3674" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#169 

	selfobj.response.write("Nancy  Nii  udderniis@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Nancy"
	g.lname="Nii"
	g.email="udderniis@yahoo.com" 
	g.address="1838 Montemar Way" 
	g.city="San Jose" 
	g.phone="(408) 559-0747" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#170 

	selfobj.response.write("Martha  Norberg  martea92@aol.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Martha"
	g.lname="Norberg"
	g.email="martea92@aol.com" 
	g.address="3727 La Calle Ct" 
	g.city="Palo Alto" 
	g.phone="(650) 644-6131" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#171 

	selfobj.response.write("Yuri  Oda  yurijudy123@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Yuri"
	g.lname="Oda"
	g.email="yurijudy123@yahoo.com" 
	g.address="17265 Grosvenor Ct" 
	g.city="Monte Sereno" 
	g.phone="(408) 399-7466" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#172 

	selfobj.response.write("Wendy  Oei  wkawamoto@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Wendy"
	g.lname="Oei"
	g.email="wkawamoto@yahoo.com" 
	g.address="902 Arrowrock Pl." 
	g.city="Sunnyvale" 
	g.phone="(408) 773-9639" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#173 

	selfobj.response.write("Roger  Okamoto  tennis.mutt@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Roger"
	g.lname="Okamoto"
	g.email="tennis.mutt@gmail.com" 
	g.address="1349 Mariposa Ave" 
	g.city="San Jose" 
	g.phone="(408) 993-9515" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#174 

	selfobj.response.write("Ally  Okazaki  ally.taylor81@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Ally"
	g.lname="Okazaki"
	g.email="ally.taylor81@gmail.com" 
	g.address="2851 Homestead Rd. # 308" 
	g.city="Santa Clara" 
	g.phone="(763) 607-7449" 
	g.ntrp="F4.5" 
	g.mtype="RS" 
	g.put()
#175 

	selfobj.response.write("Matt  Okazaki  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Matt"
	g.lname="Okazaki"
	g.email="" 
	g.address="2851 Homestead Rd. # 308" 
	g.city="Santa Clara" 
	g.phone="() " 
	g.ntrp="M2.0" 
	g.mtype="RS" 
	g.put()
#176 

	selfobj.response.write("Ken  Okazaki  okaken1@aol.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Ken"
	g.lname="Okazaki"
	g.email="okaken1@aol.com" 
	g.address="814 Daffodil Way" 
	g.city="San Jose" 
	g.phone="(408) 984-7697" 
	g.ntrp="M4.0" 
	g.mtype="NRS" 
	g.put()
#177 

	selfobj.response.write("Rachel  Okazaki  japanesegrace@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Rachel"
	g.lname="Okazaki"
	g.email="japanesegrace@gmail.com" 
	g.address="814 Daffodil Way" 
	g.city="San Jose" 
	g.phone="(408) 984-7697" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#178 

	selfobj.response.write("Deanna  Okuno  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Deanna"
	g.lname="Okuno"
	g.email="" 
	g.address="3410 Laguna" 
	g.city="Santa Clara" 
	g.phone="(408) 739-3989" 
	g.ntrp="F" 
	g.mtype="RF" 
	g.put()
#179 

	selfobj.response.write("Chester  Okuno  chesterokuno@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Chester"
	g.lname="Okuno"
	g.email="chesterokuno@gmail.com" 
	g.address="3410 Laguna" 
	g.city="Santa Clara" 
	g.phone="(408) 739-3989" 
	g.ntrp="M4.0" 
	g.mtype="RF" 
	g.put()
#180 

	selfobj.response.write("Cheryl  Okuno  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Cheryl"
	g.lname="Okuno"
	g.email="" 
	g.address="3410 Laguna" 
	g.city="Santa Clara" 
	g.phone="(408) 739-3989" 
	g.ntrp="F3.0" 
	g.mtype="RF" 
	g.put()
#181 

	selfobj.response.write("Dylan  Okuno  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Dylan"
	g.lname="Okuno"
	g.email="" 
	g.address="3410 Laguna" 
	g.city="Santa Clara" 
	g.phone="(408) 739-3989" 
	g.ntrp="M" 
	g.mtype="RF" 
	g.put()
#182 

	selfobj.response.write("Noriko  Osawa  noriko_osawa@hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Noriko"
	g.lname="Osawa"
	g.email="noriko_osawa@hotmail.com" 
	g.address="157 Kensington Way" 
	g.city="Los Gatos" 
	g.phone="(408) 401-9977" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#183 

	selfobj.response.write("Hye-Yoon  Paik  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Hye-Yoon"
	g.lname="Paik"
	g.email="" 
	g.address="2926 Roma Ct." 
	g.city="Santa Clara" 
	g.phone="() " 
	g.ntrp="F2.5" 
	g.mtype="RS" 
	g.put()
#184 

	selfobj.response.write("Vickie  Panova  Vickie200555@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Vickie"
	g.lname="Panova"
	g.email="Vickie200555@yahoo.com" 
	g.address="979 La Mesa Terr. Apt D" 
	g.city="Sunnyvalae" 
	g.phone="(408) 755-3922" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#185 

	selfobj.response.write("BoAe  Park  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="BoAe"
	g.lname="Park"
	g.email="" 
	g.address="3750 Miraverde Ct" 
	g.city="Santa Clara" 
	g.phone="() " 
	g.ntrp="F" 
	g.mtype="RS" 
	g.put()
#186 

	selfobj.response.write("Christine  Peters  ck.peters@sbcglobal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
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
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Elisapeta"
	g.lname="Peterson"
	g.email="peta.peterson@sbcglobal.net" 
	g.address="13970 Saratoga Ave." 
	g.city="Saratoga" 
	g.phone="(408) 867-6947" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#188 

	selfobj.response.write("Bettye  Pham-Vo  bettyediem@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Bettye"
	g.lname="Pham-Vo"
	g.email="bettyediem@gmail.com" 
	g.address="3657 Lisbon Ct" 
	g.city="San Jose" 
	g.phone="(408) 250-5658" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#189 

	selfobj.response.write("Jagannath  Rallapallli  rallapalli_jagan@hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Jagannath"
	g.lname="Rallapallli"
	g.email="rallapalli_jagan@hotmail.com" 
	g.address="807 Batista Dr" 
	g.city="San Jose" 
	g.phone="(408) 978-7576" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#190 

	selfobj.response.write("Aditya  Rawat  ad.rawat30@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Aditya"
	g.lname="Rawat"
	g.email="ad.rawat30@gmail.com" 
	g.address="4301 Renaissance Dr. #306" 
	g.city="San Jose" 
	g.phone="(219) 964-5051" 
	g.ntrp="M3.5" 
	g.mtype="NRS" 
	g.put()
#191 

	selfobj.response.write("David  Reed  dwreed06@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="David"
	g.lname="Reed"
	g.email="dwreed06@gmail.com" 
	g.address="2250 Monroe St. Apt 193" 
	g.city="Santa Clara" 
	g.phone="(310) 968-5478" 
	g.ntrp="M4.0" 
	g.mtype="RS" 
	g.put()
#192 

	selfobj.response.write("Bridget  Rinek  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Bridget"
	g.lname="Rinek"
	g.email="" 
	g.address="80 Gilbert Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 248-3088" 
	g.ntrp="F2.5" 
	g.mtype="RS" 
	g.put()
#193 

	selfobj.response.write("Larry  Rinek  lrinek@aol.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Larry"
	g.lname="Rinek"
	g.email="lrinek@aol.com" 
	g.address="80 Gilbert Ave" 
	g.city="Santa Clara" 
	g.phone="(408) 248-3088" 
	g.ntrp="M3.5" 
	g.mtype="RS" 
	g.put()
#194 

	selfobj.response.write("Jennifer  Roberts  jennroberts2006@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Jennifer"
	g.lname="Roberts"
	g.email="jennroberts2006@gmail.com" 
	g.address="23863 Mountain Charlie Rd." 
	g.city="Los Gatos" 
	g.phone="(408) 410-5457" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#195 

	selfobj.response.write("Betty  Rooker  tenisbetty@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Betty"
	g.lname="Rooker"
	g.email="tenisbetty@gmail.com" 
	g.address="1042 Williams Way" 
	g.city="Mountain View" 
	g.phone="(650) 776-1771" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#196 

	selfobj.response.write("Jeff  Rosenberg  usta@stinky-webisaur.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Jeff"
	g.lname="Rosenberg"
	g.email="usta@stinky-webisaur.com" 
	g.address="463 Juanita Drive" 
	g.city="Santa Clara" 
	g.phone="(408) 242-9889" 
	g.ntrp="M3.5" 
	g.mtype="RS" 
	g.put()
#197 

	selfobj.response.write("Sabrina  Rumford  rumford.sabrina@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Sabrina"
	g.lname="Rumford"
	g.email="rumford.sabrina@gmail.com" 
	g.address="3836 Shasta Drive" 
	g.city="Santa Clara" 
	g.phone="(859) 492-0030" 
	g.ntrp="F3.5" 
	g.mtype="RS" 
	g.put()
#198 

	selfobj.response.write("Atsuko  Saito  atsuko.iwako@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Atsuko"
	g.lname="Saito"
	g.email="atsuko.iwako@gmail.com" 
	g.address="20380 Stevens Creek Blvd. #321" 
	g.city="Cupertino" 
	g.phone="(408) 505-5034" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#199 

	selfobj.response.write("Dolores  Salazar  kddsalazar@comcast.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Dolores"
	g.lname="Salazar"
	g.email="kddsalazar@comcast.net" 
	g.address="3376 Solano Court" 
	g.city="Santa Clara" 
	g.phone="(408) 296-2379" 
	g.ntrp="F2.5" 
	g.mtype="RS" 
	g.put()
#200 

	selfobj.response.write("Ken  Salazar  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Ken"
	g.lname="Salazar"
	g.email="" 
	g.address="3376 Solano Court" 
	g.city="Santa Clara" 
	g.phone="(408) 296-2379" 
	g.ntrp="M" 
	g.mtype="RS" 
	g.put()
#201 

	selfobj.response.write("Cecilia  Santillanes  cicigirl56@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Cecilia"
	g.lname="Santillanes"
	g.email="cicigirl56@yahoo.com" 
	g.address="1405 McDaniel Ave. #4" 
	g.city="San Jose" 
	g.phone="(408) 334-5776" 
	g.ntrp="F" 
	g.mtype="NRS" 
	g.put()
#202 

	selfobj.response.write("Louis  Satrijo  Lsatrijo@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Louis"
	g.lname="Satrijo"
	g.email="Lsatrijo@yahoo.com" 
	g.address="2007 Heather Glen Dr." 
	g.city="San Jose" 
	g.phone="(408) 507-8064" 
	g.ntrp="M3.0" 
	g.mtype="NRS" 
	g.put()
#203 

	selfobj.response.write("Mei  See  meisee68@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Mei"
	g.lname="See"
	g.email="meisee68@yahoo.com" 
	g.address="1913 Magdalena Cir. #109" 
	g.city="Santa Clara" 
	g.phone="(408) 480-1880" 
	g.ntrp="F" 
	g.mtype="RS" 
	g.put()
#204 

	selfobj.response.write("Ami  Shah  amishah73@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Ami"
	g.lname="Shah"
	g.email="amishah73@gmail.com" 
	g.address="1001 Laurel St. #407" 
	g.city="San Carlos" 
	g.phone="(925) 339-0606" 
	g.ntrp="F3.0" 
	g.mtype="NRS" 
	g.put()
#205 

	selfobj.response.write("Cynthia  Shannon  cyn.tennis@sbcgloal.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Cynthia"
	g.lname="Shannon"
	g.email="cyn.tennis@sbcgloal.net" 
	g.address="97 Waterside Circle" 
	g.city="Redwood City" 
	g.phone="(650) 598-9822" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#206 

	selfobj.response.write("William  Shiau  shiauwh@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="William"
	g.lname="Shiau"
	g.email="shiauwh@gmail.com" 
	g.address="60 Descanso Drive Apt 1411" 
	g.city="San Jose" 
	g.phone="(971) 242-9032" 
	g.ntrp="M3.0" 
	g.mtype="NRS" 
	g.put()
#207 

	selfobj.response.write("Carol  Shields  carolsf37@aol.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Carol"
	g.lname="Shields"
	g.email="carolsf37@aol.com" 
	g.address="104 Plazoleta" 
	g.city="Los Gatos" 
	g.phone="(408) 374-4299" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#208 

	selfobj.response.write("Shirley  Silveria  shirlsil@hotmc.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Shirley"
	g.lname="Silveria"
	g.email="shirlsil@hotmc.com" 
	g.address="14670 Matilija" 
	g.city="Los Gatos" 
	g.phone="(408) 395-3541" 
	g.ntrp="F3.5" 
	g.mtype="NRS" 
	g.put()
#209 

	selfobj.response.write("Wanda  Soon  wsoon8@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Wanda"
	g.lname="Soon"
	g.email="wsoon8@yahoo.com" 
	g.address="130 Barneson Ave. #8" 
	g.city="San Mateo" 
	g.phone="(415) 298-7098" 
	g.ntrp="F3.0" 
	g.mtype="NRS" 
	g.put()
#210 

	selfobj.response.write("Richard  South  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Richard"
	g.lname="South"
	g.email="" 
	g.address="253 Redwood Ave." 
	g.city="Santa Clara" 
	g.phone="(408) 248-7876" 
	g.ntrp="M3.5" 
	g.mtype="RF" 
	g.put()
#211 

	selfobj.response.write("Ruth  South  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Ruth"
	g.lname="South"
	g.email="" 
	g.address="253 Redwood Ave." 
	g.city="Santa Clara" 
	g.phone="(408) 248-7876" 
	g.ntrp="F2.5" 
	g.mtype="RF" 
	g.put()
#212 

	selfobj.response.write("Brooke  South  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Brooke"
	g.lname="South"
	g.email="" 
	g.address="253 Redwood Ave." 
	g.city="Santa Clara" 
	g.phone="(408) 248-7876" 
	g.ntrp="F2.5" 
	g.mtype="RF" 
	g.put()
#213 

	selfobj.response.write("Kent  South  rksouth@aol.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Kent"
	g.lname="South"
	g.email="rksouth@aol.com" 
	g.address="253 Redwood Ave." 
	g.city="Santa Clara" 
	g.phone="(408) 248-7876" 
	g.ntrp="M3.5" 
	g.mtype="RF" 
	g.put()
#214 

	selfobj.response.write("Patti  Stetak  pattistetak@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Patti"
	g.lname="Stetak"
	g.email="pattistetak@gmail.com" 
	g.address="1048 Keeble Court" 
	g.city="San Jose" 
	g.phone="(408) 373-9655" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#215 

	selfobj.response.write("Elizabeth (Betty)  Symonds  bsym2000@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Elizabeth (Betty)"
	g.lname="Symonds"
	g.email="bsym2000@yahoo.com" 
	g.address="1556 Rosecrest Terrace" 
	g.city="San Jose" 
	g.phone="(408) 287-7807" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#216 

	selfobj.response.write("Tomoe  Tajima  tomoetajima@earthlink.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Tomoe"
	g.lname="Tajima"
	g.email="tomoetajima@earthlink.net" 
	g.address="" 
	g.city="" 
	g.phone="() " 
	g.ntrp="F4.0" 
	g.mtype="" 
	g.put()
#217 

	selfobj.response.write("Janet  Tallett  jttallett@comcast.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Janet"
	g.lname="Tallett"
	g.email="jttallett@comcast.net" 
	g.address="6 Daffodil Lane" 
	g.city="San Carlos" 
	g.phone="(650) 28-2655" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#218 

	selfobj.response.write("Lourdes  Thevanayagan  namunaka@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Lourdes"
	g.lname="Thevanayagan"
	g.email="namunaka@yahoo.com" 
	g.address="1035A Alta Mira Drive" 
	g.city="Santa Clara" 
	g.phone="(408) 246-0039" 
	g.ntrp="F3.0" 
	g.mtype="RS" 
	g.put()
#219 

	selfobj.response.write("Thomas  Truong  thomas_g_troung@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Thomas"
	g.lname="Truong"
	g.email="thomas_g_troung@yahoo.com" 
	g.address="2167 Weston Place" 
	g.city="Santa Clara" 
	g.phone="(408) 219-2377" 
	g.ntrp="M4.0" 
	g.mtype="RS" 
	g.put()
#220 

	selfobj.response.write("Katie  Truong  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Katie"
	g.lname="Truong"
	g.email="" 
	g.address="2167 Weston Place" 
	g.city="Santa Clara" 
	g.phone="(408) 219-2377" 
	g.ntrp="F" 
	g.mtype="RS" 
	g.put()
#221 

	selfobj.response.write("Ryan  Truong  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Ryan"
	g.lname="Truong"
	g.email="" 
	g.address="2167 Weston Place" 
	g.city="Santa Clara" 
	g.phone="(408) 219-2377" 
	g.ntrp="M" 
	g.mtype="RS" 
	g.put()
#222 

	selfobj.response.write("Paula  Tsukida  pjtsukida@aol.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Paula"
	g.lname="Tsukida"
	g.email="pjtsukida@aol.com" 
	g.address="1555 Shaw Dr." 
	g.city="San Jose" 
	g.phone="(408) 265-6756" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#223 

	selfobj.response.write("Julie  Tsutsui  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Julie"
	g.lname="Tsutsui"
	g.email="" 
	g.address="32 Wistaria Way" 
	g.city="Santa Clara" 
	g.phone="(408) 206-0496" 
	g.ntrp="F2.5" 
	g.mtype="RS" 
	g.put()
#224 

	selfobj.response.write("John  Tsutsui  john.tsutsui@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="John"
	g.lname="Tsutsui"
	g.email="john.tsutsui@gmail.com" 
	g.address="32 Wistaria Way" 
	g.city="Santa Clara" 
	g.phone="(408) 206-0496" 
	g.ntrp="M4.0" 
	g.mtype="RS" 
	g.put()
#225 

	selfobj.response.write("Cary  Tucker  carywtucker@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Cary"
	g.lname="Tucker"
	g.email="carywtucker@gmail.com" 
	g.address="980 Kiely Blvd #323" 
	g.city="Santa Clara" 
	g.phone="(408) 239-7329" 
	g.ntrp="M2.5" 
	g.mtype="RS" 
	g.put()
#226 

	selfobj.response.write("Tracy  VanDenBerg  vandenberg.tl@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Tracy"
	g.lname="VanDenBerg"
	g.email="vandenberg.tl@gmail.com" 
	g.address="714 Astor Ct." 
	g.city="Mountain View" 
	g.phone="(408) 242-0925" 
	g.ntrp="F3.0" 
	g.mtype="NRS" 
	g.put()
#227 

	selfobj.response.write("Hank  Wang  lorddct@animedrd.net")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Hank"
	g.lname="Wang"
	g.email="lorddct@animedrd.net" 
	g.address="12223 Candy Ln" 
	g.city="Saratoga" 
	g.phone="(408) 455-2666" 
	g.ntrp="M4.5" 
	g.mtype="NRS" 
	g.put()
#228 

	selfobj.response.write("Susan  Weiner  sweiner@hotmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Susan"
	g.lname="Weiner"
	g.email="sweiner@hotmail.com" 
	g.address="18581 Decatur Rd." 
	g.city="Los Gatos" 
	g.phone="(408) 354-7855" 
	g.ntrp="F4.0" 
	g.mtype="NRS" 
	g.put()
#229 

	selfobj.response.write("Xie  Xing  Y@")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Xie"
	g.lname="Xing"
	g.email="Y@" 
	g.address="3270 Saint Ignatius Place" 
	g.city="Santa Clara" 
	g.phone="() F" 
	g.ntrp="4" 
	g.mtype="RS" 
	g.put()
#230 

	selfobj.response.write("Hideko  Yashiro  jojoo.kao@gmail.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Hideko"
	g.lname="Yashiro"
	g.email="jojoo.kao@gmail.com" 
	g.address="15595 Old Japanese Rd" 
	g.city="Los Gatos" 
	g.phone="(617) 905-2369" 
	g.ntrp="F4.5" 
	g.mtype="NRS" 
	g.put()
#231 

	selfobj.response.write("Jenny  Yip  jenny_rex@yahoo.com")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Jenny"
	g.lname="Yip"
	g.email="jenny_rex@yahoo.com" 
	g.address="1275 Green Oak Lane" 
	g.city="Los Altos" 
	g.phone="(650) 210-8883" 
	g.ntrp="F3.0" 
	g.mtype="NRS" 
	g.put()
#232 

	selfobj.response.write("Lynda  Zhang  @")
	selfobj.response.write("<br> ") 
	g = MEMBER(key=ndb.Key(MEMBER,"1386687600")) 
	g.year=2013
	g.fname="Lynda"
	g.lname="Zhang"
	g.email="" 
	g.address="460 Norweed Circle" 
	g.city="Santa Clara" 
	g.phone="(208) 939-2835" 
	g.ntrp="F4.0" 
	g.mtype="RS" 
	g.put()
