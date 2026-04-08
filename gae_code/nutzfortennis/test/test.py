import datetime,re


def matchtime( d):

   pm = "AM"
   hour = d.hour
   minute = ""
   if( d.hour == 12): 
      pm = "PM"    
   elif( d.hour > 12):
      pm = "PM"
      hour = d.hour - 12

   if( d.minute > 0):
      minute= ":"+str(d.minute)            

   return str(hour)+minute+pm




s = r"\s\tWord"
t = r"\\s\\tWord"
prog = re.compile(s)

print len(s),s
t = r"\\s"
print len(t),t

t = r"\s"
print len(t),t

t = r"\\s\\tWord"
print len(t),t
