from google.appengine.ext import blobstore
from google.appengine.ext import db

import datetime,time

#
#import urllib
#import sys
#import httplib
#import re
#import string


#          g = datastore.FacilityTeam( key_name= team[0] )

# Scheduled match dates for a team
class Team( db.Model):
   id = db.IntegerProperty()
   created = datetime.date
   home_id = db.StringProperty()    # home facility
   home_name = db.StringProperty()    # home facility
   name = db.StringProperty()
   nickname = db.StringProperty()
   active = db.ListProperty(datetime.date)   
   completed = db.ListProperty(datetime.date)   
   players = db.StringListProperty()
   teams = db.StringListProperty()

class Roster( Team ):
   pass



class Player(db.Model):

   name = db.StringProperty()
   teams = db.StringListProperty()
   dates = db.ListProperty(datetime.date)



class Nickname( db.Model):
   name = db.StringProperty()
   nickname = db.StringProperty()   
