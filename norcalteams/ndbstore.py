from google.appengine.ext import ndb

#   timestamp = ndb.DateTimeProperty(verbose_name="MTime",auto_now=True)



class Team( ndb.Model):
     order = ndb.IntegerProperty()

     teamid = ndb.StringProperty()
     teamname = ndb.StringProperty()

     captain = ndb.StringProperty()
     captainid = ndb.StringProperty()

#    leagueid = ndb.StringProperty()    
     area = ndb.StringProperty()    

     win = ndb.IntegerProperty()    
     loss = ndb.IntegerProperty()    

     date = ndb.DateTimeProperty()

     playoff = ndb.StringProperty()

     def __del__(self):
       n=2
#      print("__del__")


# ------------------------------------------


class Player( ndb.Model):
     id = ndb.StringProperty()  # teamid_playerid combination


     name = ndb.StringProperty()
     rating = ndb.StringProperty()
     winloss = ndb.StringProperty()


#     teams = ndb.StructuredProperty(IDList, repeated=True )
#     timestamp = ndb.DateTimeProperty(verbose_name="Player",auto_now=True)
#    count = ndb.IntegerProperty()
#    current = ndb.IntegerProperty()

class Flight( ndb.Model):
      teams = ndb.StructuredProperty( Team , repeated=True)
      players = ndb.StructuredProperty( Player, repeated=True)

class Flight2( ndb.Model):
      players = ndb.StructuredProperty( Player, repeated=True)


class USTAID(ndb.Model):
     fname  = ndb.StringProperty()
     lname  = ndb.StringProperty()
     username  = ndb.StringProperty()
     password  = ndb.StringProperty()


class User( ndb.Model):
     id  = ndb.StringProperty()
     fname  = ndb.StringProperty()
     lname  = ndb.StringProperty()


class IDList( ndb.Model ):
     id = ndb.StringProperty()
     desc = ndb.StringProperty()


class MatchList( ndb.Model):
     desc = ndb.StringProperty()
     date = ndb.DateTimeProperty()

#  ADDED to match main.py description of MatchList
     status = ndb.StringProperty()           # Completed/Scheduled
     match  = ndb.StringProperty()           # Week/Playoff/Districts/Sectionals
     scorecard_id  = ndb.StringProperty()    # ID of scorecard of completed match
     opponent    = ndb.StringProperty()      # Opponent
     opponent_id = ndb.StringProperty()      # Opponents team ID
     where    = ndb.StringProperty()         # Home/Away 
#  *******************************************************

#class Player(db.Model):
#   name = db.StringProperty()
#   teams = db.StringListProperty()
#   dates = db.ListProperty(datetime.date)




# Only used in Admin.py for display
class USTA( Player):
     ustaid = ndb.StringProperty()




class Roster( ndb.Model):
     teamid = ndb.StringProperty()
     name  = ndb.StringProperty()
     alias = ndb.StringProperty()
     color = ndb.StringProperty()

     confirmed = ndb.StructuredProperty( MatchList , repeated=True)
     scheduled = ndb.StructuredProperty( MatchList , repeated=True)

#    completed = ndb.StructuredProperty( MatchList , repeated=True)
#    active = ndb.StructuredProperty( MatchList , repeated=True)

# IDList is a generic (id,name) list
     players = ndb.StructuredProperty( IDList, repeated =True)
     teams = ndb.StructuredProperty(IDList, repeated=True)

#    players = ndb.StructuredProperty(Player, repeated=True)
#    teams = ndb.StructuredProperty(Team, repeated=True)



class PTeam( Roster ):
     pass

