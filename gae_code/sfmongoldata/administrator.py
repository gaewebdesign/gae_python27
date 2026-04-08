import webapp2
import json   #Python 2.7


from google.appengine.ext import ndb
from google.appengine.ext.webapp import template

import collections,time
from  datetime import datetime,timedelta
import os,re,cgi,string,types

from datastore import  *
# bigwilly
# Subtact 7 hours
# https://timestamp.online/article/how-to-convert-timestamp-to-datetime-in-python
def LOCALTIME( unix):
      return time.strftime("%D ", time.localtime( unix - 7*60*60 ))
#      return time.strftime("%b %d %Y %I:%M %p", time.localtime( unix - 7*60*60 ))

def LOCALTIME_DETAIL( unix):
      return time.strftime("%b %d %Y %I:%M %p", time.localtime( unix - 7*60*60 ))

def ERROR(sobj, text):
     sobj.response.write( "<center>")
     sobj.response.write( "<h2>")
     sobj.response.write( text )
     sobj.response.write("<br>")
     sobj.response.write( "</h2>")
     sobj.response.write( "</center>")


# from from source to trash Model, deleting source
def TRASHCAN( sourceKEY ):
      g =  sourceKEY.get()
      print( "Deleting " + str(g) ) 
      unix = g.key.id() 
      print( unix )

      trashKey = ndb.Key(TRASH,str(unix))
      t = TRASH( key = trashKey)
      t.year = g.year

      t.fname = g.fname
      t.lname = g.lname
      t.address = g.address
      t.city = g.city
      t.zip = g.zip
      t.phone = g.phone

      t.email= g.email

      t.mtype= g.mtype
      t.ntrp = g.ntrp

      t.src  = g.src
      t.mtype = g.mtype
      t.zknt = g.zknt
      t.ztra = g.ztra

      print( sourceKEY.delete()  )
      print( t.put()  )

#      if( g!= None):
#               keyID.delete()

def  Abbreviate( city ):

             if( re.search("clara",city, re.IGNORECASE)): city = "SC"
             elif( re.search("jose", city, re.IGNORECASE)): city ="SJ"
             elif( re.search("mountain", city, re.IGNORECASE)): city ="MV"
             elif( re.search("sunny", city, re.IGNORECASE)): city ="SU"
             elif( re.search("altos", city, re.IGNORECASE)): city ="LA"
             elif( re.search("altos", city, re.IGNORECASE)): city ="LA"
             elif( re.search("cup", city, re.IGNORECASE)): city ="CU"
             elif( re.search("monte", city, re.IGNORECASE)): city ="MS"
             elif( re.search("milpitas", city, re.IGNORECASE)): city ="MP"
             elif( re.search("redwood", city, re.IGNORECASE)): city ="RWC"
             elif( re.search("fremont", city, re.IGNORECASE)): city ="FMT"
             elif( re.search("scotts", city, re.IGNORECASE)): city ="SV"
             elif( re.search("gato", city, re.IGNORECASE)): city ="LG"

             elif( re.search("campb", city, re.IGNORECASE)): city ="CMB"

             elif( re.search("millbrae", city, re.IGNORECASE)): city ="MilB"

             elif( re.search("menlo", city, re.IGNORECASE)): city ="MPk"
             elif( re.search("belmont", city, re.IGNORECASE)): city ="Belm"
             elif( re.search("saratoga", city, re.IGNORECASE)): city ="SRT"
             elif( re.search("palo", city, re.IGNORECASE)): city ="PA"

             elif( re.search("dublin", city, re.IGNORECASE)): city ="DB"
             elif( re.search("morgan", city, re.IGNORECASE)): city ="MH"

             elif( re.search("cameron", city, re.IGNORECASE)): city ="CPk"

             elif( re.search("bruno", city, re.IGNORECASE)): city ="SB"

             elif( re.search("burling", city, re.IGNORECASE)): city ="BG"

             return city

class AdminHandler(webapp2.RequestHandler):

     def get(self, id=None):

        YEAR=SCTC_KOTOSHI          # set in datastore.py
        if id != None :
         YEAR = int(id)

        obj = []
        d=collections.OrderedDict()

        minute = 60
        hour =   60*minute
        day =   24*hour
        month = 30*day
        year  = 12*month

        unix_now = int( time.time() )
        unix_pending = unix_now - 24*year
        unix_wait = unix_now - 24*year

        print("*"*30)
        print( unix_now ,unix_pending)
        print("NOW = " +   LOCALTIME_DETAIL(unix_now)   )
        print("PENDING  = " +   LOCALTIME_DETAIL( unix_pending )  )
        print("WAIT  = " +   LOCALTIME_DETAIL( unix_wait )  )

        print("*"*30)

# Get Waitlist

        keys = WAIT.query(WAIT.year == YEAR ).fetch(keys_only = True)
        WaitList = []
        for k in keys:

          if( int(k.id()) > unix_wait):
               p = WAIT.get_by_id( k.id () )
               print( "Wait(" + str(k.id()) + ") " + p.fname + " " + p.lname )
               unix = int( k.id() ) 
               g = GENUS( p.year ,p.fname, p.lname ,p.address , p.city,p.zip, p.email ,p.phone, p.ntrp ,p.mtype, p.src ,p.zknt,p.ztra, unix, LOCALTIME(unix)  )
               WaitList.append(g)

        WaitList.sort(key=lambda x: x.unix, reverse=True)

# Get Pending
        keys = PENDING.query(PENDING.year == YEAR ,PENDING.done!="done").fetch(keys_only = True)
              
        PendingList = []
        for k in keys:

          if( int(k.id()) > unix_pending):
               p = PENDING.get_by_id( k.id () )
               print( "Pending(" + str(k.id()) + ") " + p.fname + " " + p.lname )
               unix = int( k.id() ) 
               g = GENUS(p.year ,p.fname, p.lname ,p.address , p.city,p.zip, p.email ,p.phone, p.ntrp ,p.mtype, p.src ,p.zknt, p.ztra, unix, LOCALTIME(unix)  )
               PendingList.append(g)

        PendingList.sort(key=lambda x: x.unix, reverse=True)


# Get Members 
        abbr = {}
        abbr["jose"] = "SJ"
        abbr["sunnyvale"] = "SU"
        abbr["clara"] = "SC"



        query = MEMBER.query( MEMBER.year == YEAR)  #.order(MEMBER.lname)
        obj = []
        d=collections.OrderedDict()

        MemberList = []

        NR = R = 0

        pattern = 'Santa'
        r = re.compile(pattern ,  re.IGNORECASE)
        for key in query.iter():

             unix = int( key.key.id() )

             city = Abbreviate( key.city )

             g = GENUS( key.year ,key.fname, key.lname ,key.address , city,key.zip, key.email ,key.phone, key.ntrp ,key.mtype, key.src,key.zknt,key.ztra,unix, LOCALTIME(unix) )
             MemberList.append(g)
             if( re.search(pattern, key.city) or key.mtype == "RS" or key.mtype=="RF" or key.mtype=="RF_" ): R= R+1

        MemberList.sort(key=lambda x: x.lname, reverse=False)

        template_values = {
                         'TITLE'  :  "Santa Clara Tennis Club Administrator",
                         'KOTOSHI' : SCTC_KOTOSHI, #,2019,
                         'KYONEN'  : SCTC_KOTOSHI-1,
                         'OTOTOSHI' : SCTC_KOTOSHI-2,

                         'COLOR_WAITLIST'  :  "#f4e542",

                         'COLOR_PENDING'  :  "#ffcccc",

                         'COLOR_STRIP'      :  "#99ccff",
                         'COLOR_SCTC'      :  "#ffccff",


                         'DIR'  :  "admin",
                         'YEAR'  :  YEAR,


                         'WaitList' : WaitList,
                         'PendingList' : PendingList,
                         'MemberList' : MemberList,

                         'W' : len(WaitList),
                         'P' : len(PendingList),
                         'M' : len(MemberList),

                         "R" :  R,
                         "NR" :  len(MemberList) - R

             }


        path = os.path.join(os.path.dirname(__file__), 'templates','admin.html')
        self.response.out.write(template.render(path, template_values))


class ModifyHandler(webapp2.RequestHandler):

     def post(self, id=None):
           print("ModifyHandler (POST)" )
           _POST = cgi.escape(self.request.get('MODIFY'))


           try:
            key,model = _POST.split(",")
            print( key, model)
           except:
            ERROR(self, "WHOOPS: Select someone ")
            return


           self.modify( key, model )


     def modify(self,KEY,MODEL):

#          Edit either a Member or Pending model
           print( "Modify Handler")
           print( KEY , MODEL)

           if ( MODEL == "Pending"):
                print("deal with Pending ")
                m = PENDING.get_by_id( str(KEY) )
           elif( MODEL == "Member"):
                print("deal with Member ")
                m = MEMBER.get_by_id( str(KEY) )
           elif( MODEL == "Wait"):
                print("deal with Wait ")
                m = WAIT.get_by_id( str(KEY) )
           else:
                print("ERROR: neither Pending/Member/Wait ")


           if( m == None):
                print(" Whoops " + MODEL + " = None" )
                return
 
           print(m.fname + " " + m.lname + " " + m.address + " " + m.address )
           unix = int( int(KEY) )

           g= GENUS( m.year ,m.fname, m.lname ,m.address , m.city, m.zip ,m.email , m.phone, m.ntrp ,m.mtype, m.src ,m.zknt,m.ztra, unix, LOCALTIME(unix) )

           template_values = {
                         'YEAR' : m.year,
                         'Model': MODEL,
                         'TITLE'  :  "Modify Member",
                         'DIR'  :  "modify",
                         'Member' : g
             }


           path = os.path.join(os.path.dirname(__file__), 'templates','admin_modify.html')
           self.response.out.write(template.render(path, template_values))


     def get(self, id=None):
           print("ModifyHandler" )

class ActionHandler(webapp2.RequestHandler):
     def post(self, id=None):
       print("ActionHandler(POST)" ) 
#      self.write.response("ActionHandler(POST)" ) 

#      either 
#      Delete from Database:
#      Edit Database
#      Add to Database
       _DEL = cgi.escape(self.request.get('_DELETE'))
       _EDIT = cgi.escape(self.request.get('_EDIT'))
       _ADD = cgi.escape(self.request.get('_ADD'))

       _MODEL = cgi.escape(self.request.get('Model'))
       _UNIX = cgi.escape(self.request.get('unix'))

       print( 20*"#" )
       print(_DEL , _EDIT , _ADD )
       print(_MODEL + "(" + _UNIX + ")" )
       print( 20*"#" )


       _TITLE = "-"

#      Get values from form
       _fname  = cgi.escape(self.request.get('fname'))
       _lname  = cgi.escape(self.request.get('lname'))
       _address  = cgi.escape(self.request.get('address'))
       _city = cgi.escape(self.request.get('city'))
       _zip =  cgi.escape(self.request.get('zip'))

       _phone =  cgi.escape(self.request.get('phone'))
       _email = cgi.escape(self.request.get('email'))

       _ntrp   =  cgi.escape(self.request.get('ntrp'))
       _mtype  = cgi.escape(self.request.get('mtype'))

       _zknt =  cgi.escape(self.request.get('zknt'))

       _help = "FILL "
       _other = "FILL "
       _ip = "FILL "
       _ztra = "FILL "

       try:
          _zknt = int( _zknt)
       except:
          zknt = 0

       print(_fname + " " + _lname )
       print(_address + " " + _city + " " + _zip)
       print(_phone )


       note= ""
       g = keyID = "" 

       if( _MODEL == "Member"):
            g =  ndb.Key(MEMBER, _UNIX).get()
            keyID =  ndb.Key(MEMBER, _UNIX)
            print("Member: " + str(g) )
       elif( _MODEL == "Pending"):
            g =  ndb.Key(PENDING, _UNIX).get()
            keyID =  ndb.Key(PENDING, _UNIX)
            print("Pending: " + str(g) )
       elif( _MODEL == "Wait"):
            g =  ndb.Key(WAIT, _UNIX).get()
            keyID =  ndb.Key(WAIT, _UNIX)
            print("Wait: " + str(g) )


# do the ACTION
#      DELETE 
       if( re.search("Delete" , _DEL) ):
            _TITLE  = "DELETE"
            note = "DELETED " + g.fname + " " + g.lname
            TRASHCAN( keyID)

#      EDIT 
       elif(re.search("Edit", _EDIT) ):
            _TITLE  = "EDIT"
            print( _EDIT)

#           EDITING MODULE (either WAIT/PENDING/MEMBER)

            if( g != None):
                g.fname = _fname
                g.lname = _lname
                g.address = _address
                g.city = _city
                g.ntrp = _ntrp
                g.zip = _zip
                g.email = _email
                g.mtype = _mtype
                g.zknt = _zknt
                note = "MODIFIED " + g.fname + " " + g.lname
                g.put()

#      only a WAIT or PENDING class needs to be added to the database
       elif( re.search("Add",_ADD) ):
            if _MODEL == "Pending":
               _TITLE = "ADD from Pending List"
            elif (_MODEL == "Wait" ):
               _TITLE = "ADD from Wait Lst "
            else :
               print("ERROR: not a PENDING nor WAIT MODEL")
               return

            print( _ADD)
            # create a MEMBER, put, then trash
            p = MEMBER(
                   id = _UNIX,             
                   year= g.year,         #g.year,
                   fname = _fname,      #g.fname,
                   lname = _lname,      #g.lname,
                   address  = _address, #g.address,
                   city  = _city,       #g.city,
#                  done  = "",
                   zip  = _zip,        #g.zip,
                   phone  = _phone,     #g.phone,
                   email  = _email,     #g.email,
                   ntrp  = _ntrp,       #g.ntrp,

                   src = g.src,
                   help = g.help,        #_help,        #g.help,
                   other = g.other,      #_other       #g.other
                   ip  = g.ip,       #g.ntrp,

# ----- unique to MEMBER class (Santa Clara Tennis Club) ------------
                   mtype = _mtype,   
                   zknt = g.zknt,
                   ztra = g.ztra

            )

# Put the MEMBER
            print(" new Member ")
            print( p )
            print( type(p).__name__ )
            r=p.put()
            _MODEL = type(p).__name__  # the actual MODEL
            print( "RESULT" )
            print(  r )
            print(" new Member ")

# Then delete the old _MODEL( whether WAIT OR PENDING)
            print( "*** deleting ***" ) 
            print( "MODEL: " +  type(g).__name__ )
            TRASHCAN( keyID  )
            print( "*** deleting ***" ) 


       template_values = {

                          'TITLE': _TITLE,

                          'NOTE': note,

                          'FNAME': _fname,
                          'LNAME': _lname,

                          'ADDRESS': _address,
                          'CITY': _city,
                          'ZIP': _zip,
                          'PHONE': _phone,
                          'NTRP': _ntrp,
                          'EMAIL': _email,
                          'MTYPE': _mtype,
                          'COUNT': _zknt,

#                         'YEAR' : m.year,
                          'MODEL': _MODEL,
                          'UNIX': _UNIX,

#                         'DIR'  :  "modify",
#                         'Member' : g
             }




       path = os.path.join(os.path.dirname(__file__), 'templates','admin_action.html')
       self.response.out.write(template.render(path, template_values))


     def get(self, id=None):
       print("ActionHandler(GET)" ) 

       pass



app = webapp2.WSGIApplication(
           [
               ('/admin', AdminHandler),
               ('/admin/([\d]*)', AdminHandler),

               ('/modify', ModifyHandler),
               ('/_action', ActionHandler),


           ]


)



#
#        query = Pending.query(Pending.year == YEAR  , Pending.zknt > unix_before ) # .fetch(50)
#        query = Pending.query(Pending.year == YEAR   ).fetch(500)


#        PendingList = []
#        for p in query:
#           unix = int( p.key.id())

#           duration = unix_now - unix

#           print( "p.zknt = " + str(p.zknt)   )
#           print( datetime.timedelta( seconds = duration ) )
#           print( p.fname + " " + p.lname)

#           if( unix_now - unix > 60*100 ): continue


#           t = datetime.datetime.fromtimestamp(unix) + timedelta(hours=5)
#           dt = t.strftime("%Y-%m-%d %H:%M:%S")
#           g = GENUS( p.year ,p.fname, p.lname ,p.address , p.city,p.zip, p.email ,p.phone, p.ntrp ,p.mtype, p.src ,unix, dt )
#           PendingList.append(g)


#        PendingList.sort(key=lambda x: x.unix, reverse=True)
