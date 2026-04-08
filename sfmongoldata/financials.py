import webapp2


from google.appengine.ext.webapp import template
from datetime import timedelta

import urllib,re,datetime,string,sys,os

#import mysession
#import logging

class RedirectHandler(webapp2.RequestHandler):

    def get(self):

      self.response.write("Financials")
#     self.redirect("/financials/index.html")

      template_values = {

      }

#      path = os.path.join(os.path.dirname(__file__), '_ggtc/financials','index.html')

      path = os.path.join(os.path.dirname(__file__), '_ggtc/financials/website','2018pairnetworks_bill.pdf')


      self.response.out.write(template.render(path, template_values))


app = webapp2.WSGIApplication(
                                     [
                                      ('/financials', RedirectHandler)
                                     ],
                                      debug=True)
