from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import datetime,re


class MainHandler(webapp.RequestHandler):
  def __init__(self):
    pass

  def get(self ):

# http://vancouver-webpages.com/META/FAQ.html#redirect

# http://code.google.com/appengine/docs/python/tools/webapp/redirects.html

    today = datetime.datetime.date(datetime.datetime.now())
    current = re.split('-', str(today)) 
    month = current[1]
    year  = current[0]

    self.redirect("/month/"+ month + "/" + year )



def main():
    application = webapp.WSGIApplication(
          [ ('/schedule', MainHandler),
            ('/*.', MainHandler)
          ], debug=True)
    run_wsgi_app(application)

if __name__ == '__main__':
  main()
