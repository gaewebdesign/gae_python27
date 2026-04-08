from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db

import re,os,cgi,datetime,datastore,library,types,random

class Theme:
   file=""
   name = ""
   sel = ""

class MembershipCard:
   fname = ""
   lname = ""
   long = False
   left = False
   right = False
   image = ""
   page=True


def Host():
    url = "http://"+os.environ["SERVER_NAME"]
    if (re.search("localhost",url )): url = "http://localhost:8080"
    return url


theme = [ ('southflorida.png','Fishing'),('fishschool.png','FishSchol'),
          ('fishinggirl.png','FishingGirl'),('bassfishing.png','BassFishing')
        ]

class LettersHandler(webapp.RequestHandler):


    def get(self):

        cards = []

        year=2012
        cards=[]
        count=1
        once=False
        name = ( 
                 ("Carson","Armstrong"), 
                 ("Aaron","Black"), 
                 ("Mary","Brown"), 
                 ("Cindy","Corson"), 
                 ("Augue","Danbury"), 
                 ("Cheryl","Jackson"), 
                 ("Eric","Jones"), 
                 ("Audrey","Kern"), 
                 ("Lily", "Long"),
                 ("Iris", "Lopez"),
                 ("Dawn", "Musser"),
                 ("Tosh", "Otsubo"),
                 ("Jason", "Mar") ,
                 ("Tak", "Noda") ,
                 ("Bob", "Ward") ,
                 ("Elaine", "Young") ,

               )



        for e in name:

           mc = MembershipCard()           
           mc.fname=e[0]
           mc.lname = e[1]
           mc.long=False
           mc.year = 2012
           mc.left=False
           mc.right=False
           mc.page=False
           if( len(e[0])+len(e[1])>13 ): mc.long=True
           if( count%2==1): mc.left=True
           if( count%2==0): mc.right=True           
           if( count%8==0): mc.page=True

           count = count + 1

           n = random.randrange(0,20)%len(theme)
           mc.image=theme[n][0]

           cards.append( mc )

        template_values = {
               'site'      : Host(),
               'Cards'     : cards,
               'image'     : 'lincecum1.jpg'
        }

        path = os.path.join(os.path.dirname(__file__), 'club.html' )
        self.response.out.write(template.render(path, template_values))


application = webapp.WSGIApplication(
                                     [('/club', LettersHandler),
                                     ],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":

#   print __file__
#   print __name__

    main()
