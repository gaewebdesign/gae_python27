from google.appengine.ext import ndb

#class Team(db.Model):
class FacilityTeam(db.Model):
  position = db.IntegerProperty()
  facility = db.IntegerProperty()
  teamid = db.IntegerProperty()
  name = db.StringProperty()
  captain = db.StringProperty()
#  page = db.TextProperty()
  updated= db.DateTimeProperty()
#  xrosterkey=db.ListProperty(db.Key)


#class Roster(db.Model):
class FacilityRoster(db.Model):
  facility = db.IntegerProperty()
  teamid = db.IntegerProperty()
  playerid = db.IntegerProperty()
  fname = db.StringProperty()
  lname = db.StringProperty()
  roster= db.StringProperty()
  date= db.DateProperty()
  city = db.StringProperty()
  gender = db.StringProperty()
  rating = db.StringProperty()


class IDList( ndb.Model ):
     id = ndb.StringProperty()
     desc = ndb.StringProperty()


class Author( db.Model):
  name = db.StringProperty()

#http://www.terminally-incoherent.com/blog/2011/03/28/student-webspace-in-the-cloud-google-app-engine/

class BlobKey(db.Model):
  name = db.StringProperty()
  mykey = blobstore.BlobReferenceProperty( )
  date= db.DateProperty()

#class Player(db.Model):
class FacilityPlayer(db.Model):
  id = db.StringProperty()
  facility = db.IntegerProperty()
  usta = db.StringProperty()
  fname = db.StringProperty()
  lname = db.StringProperty()
  gender = db.StringProperty()
  rating = db.StringProperty()
  city = db.StringProperty()
  ctc = db.StringProperty()
  csc = db.StringProperty()
