from google.appengine.ext import ndb

#   timestamp = ndb.DateTimeProperty(verbose_name="MTime",auto_now=True)

class League(ndb.Model):
     name = ndb.StringProperty()  #M4.0,M4.5, etc.

class RosterList(ndb.Model):
     fname = ndb.StringProperty()
     lname = ndb.StringProperty()
     rdate = ndb.StringProperty()
     city = ndb.StringProperty()
     ntrp = ndb.StringProperty()
     timestamp = ndb.DateProperty()   # the actual date (for sorting)

#
#     teamid=ndb.IntegerProperty()
#     usta = ndb.StringProperty()
#     gender = ndb.StringProperty()
#     rating = ndb.StringProperty()
#     city = ndb.StringProperty()
#     ctc = ndb.StringProperty()
#     csc = ndb.StringProperty()

class Team(ndb.Model):
     position = ndb.IntegerProperty()
     captain = ndb.StringProperty()
     teamid = ndb.IntegerProperty()
     name = ndb.StringProperty()
     level = ndb.StringProperty()
     timestamp = ndb.DateTimeProperty()
     roster  = ndb.StructuredProperty( RosterList , repeated=True)




