import webapp2    # Python 2.7


from google.appengine.api import urlfetch

from google.appengine.api.urlfetch import urllib2

from google.appengine.ext import ndb

from google.appengine.ext.webapp import template
# new Python 2.7 imports


import urllib,  os,re,cgi,calendar,string,types
import datetime,time,sys

from ndbstore import *

#import SystemProperty

def ENVIRONMENT(self):

      self.response.out.write("<p>")
      self.response.out.write('ENVIRONMENT')
      self.response.out.write("<br>")


      for key in os.environ:
       self.response.out.write( key + " -->  " + str(os.environ[key]) + "<br>" )

      self.response.out.write( os.environ['CURRENT_VERSION_ID'])


      self.response.out.write('ENVIRONMENT')
      self.response.out.write("<p>")

class VersionHandler( webapp2.RequestHandler):

     def get(self):
      self.response.out.write("<p>")
      self.response.out.write('ENVIRONMENT<br>')
      self.response.out.write( os.environ['CURRENT_VERSION_ID'])
      self.response.out.write("<br>")
      self.response.out.write( sys.version )
      self.response.out.write("<p>")

      for key in os.environ:
       self.response.out.write( key + " -->  " + str(os.environ[key]) + "<br>" )



class TestHandler( webapp2.RequestHandler):

   def ENVRONMENT(selfj):

      for key in os.environ:
       self.response.out.write( key + " -->  " + str(os.environ[key]) + "<br>" )



   def get(self):

      print("TestHandler")

      url = "https://www.ustanorcal.com/teaminfo.asp?id=52981"



      url = "https://www.ustanorcal.com/teaminfo.asp?id=81742"
      url = "https://www.ustanorcal.com/organization.asp?id=2423"

      url = "https://www.ustanorcal.com/organization.asp?id=2423"
      url = "http://www.sctennisclub.org"


#     req = urllib2.Request( url )
      req = urlfetch.fetch(url=url, method = urlfetch.GET,  validate_certificate=True)

      self.response.out.write( "** SYS ***" )
      self.response.out.write( "<br>" ) 
      self.response.out.write( sys.version )
      self.response.out.write( "<br>" )
      self.response.out.write( "*** SYS ***" )
      self.response.out.write( "<br>" )



      self.response.out.write(  "<br>"  )

#      self.response.out.write(  "get_full_url() <br>"  )
#      self.response.out.write(  req.get_full_url()  )
#      self.response.out.write(  "<p>get_method()<br>"  )
#      self.response.out.write(  req.get_method()  )
#      self.response.out.write(  "<p>get_data()<br>"  )
#      self.response.out.write(  req.get_data()  )
#      self.response.out.write(  "<p>"  )
#      self.response.out.write(  dir(req)  )

      self.response.out.write(  url  )
      self.response.out.write(  "<br>"  )


      self.response.out.write(  req  )
      self.response.out.write(  "<br>"  )

      response = urllib2.urlopen( url )
      scraped = response.read()

      self.response.out.write(  scraped )


class TestHandler2( webapp2.RequestHandler):


   def get(self):

      print("TestHandler")
      
      ENVIRONMENT(  self )


      print( dir(urllib)   )
      print( "#"*50   )

      print( "urlfetch "*5   )
      print( dir(urlfetch)   )
      self.response.out.write( "urlfetch <br>"   )
      self.response.out.write( dir(urlfetch)   )
      self.response.out.write( "<p>"   )

      self.response.out.write( "urlfetch.httplib <br>"   )
      self.response.out.write( dir(urlfetch.httplib)   )
      self.response.out.write( "<p>"   )

      print( "^"*50   )


      print( dir(urlfetch)   )

      print( "urlfetch.urllib2 "*5   )
      print( dir(urlfetch.urllib2)   )
      self.response.out.write( "urlfetch.urllib2 <br>"   )
      self.response.out.write( dir(urlfetch.urllib2)   )
      print( "^"*50   )

      print( "urlfetch.urllib2.Request "*5   )
#      print( dir(urlfetch.urllib2.Request)   )
      self.response.out.write("<p>"  )
      self.response.out.write("urlfetch.urllib2.Request <br>"  )
      self.response.out.write( dir(urlfetch.urllib2.Request)   )
      print( "%"*50   )

      idx = "113"
      url = "http://www.ustanorcal.com/organization.asp?id=" + idx


      u = "http://www.marthastewart.com"
      u = "http://www.sctennisclub.org"

      u = "https://www.ustanorcal.com/teaminfo.asp?id=52981"

      self.response.out.write( "<br>")
      self.response.out.write( "*"*30)
      self.response.out.write( "<br>")

      self.response.out.write( "<br>")
      self.response.out.write( "*"*30)


#      urlfetch.Fetch(url, payload=None, method = 1, headers={}, allow_truncated=False,
#          follow_redirects=True, deadline=None, validate_certificate=True)

      response= ""
      self.response.out.write( " <p> ")
      self.response.out.write( " TRY " + u   )

      result = urllib2.urlopen( u )
      self.response.write( result.read() )

      return

      user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36',
      head = {'User-Agent': user_agent}

      response = urlfetch.Fetch(url=u, 
                       method = urlfetch.GET,  
                       headers = head,
                       validate_certificate=True,

           )

#     response = urlfetch.fetch(u )

      self.response.out.write( "response  "    )
      self.response.out.write( response.status_code  )
      self.response.out.write( response.content  )
      self.response.out.write( response.headers  )
      self.response.out.write( "length "  )
      self.response.out.write( len(response.content)  )
#      self.response.out.write( response.getheaders()  )
      self.response.out.write( "response  "    )


      return

      try:
        response = urlfetch.Fetch(url=u, method = urlfetch.GET,  validate_certificate=True)
        self.response.out.write( response )

      except :
        self.response.out.write( "EXCEPTION: " + str( sys.exc_info()[0])  )
#        self.response.out.write( "EXCEPTION: " , sys.exc_info()[0]   )

#      finally:
#        self.response.out.write( "finally " )


      self.response.out.write( " DONE... "   )     
      self.response.out.write(  response    )     


#      response =  urlfetch.urllib2.urlopen( url ) 
#      html = response.read()

#      self.response.out.write( html )

#      result = urlfetch.fetch(url)
#     scraped = result.content



app = webapp2.WSGIApplication(
                                     [
                                      ('/test', TestHandler2),
                                      ('/version', VersionHandler),

                                     ],
                                      debug=True)

