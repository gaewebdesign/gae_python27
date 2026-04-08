import re

import datetime,random


def find( theList, theDate ):
  return [ d for d in theList if d[0] == theDate ]


year=2013

l = []


theDate =  datetime.datetime(2012,8,24,12,30,15)
print str(theDate)

theDate =  datetime.date(2012,8,24)



s1= [theDate , 23] 
s2= [theDate , 230]

l.append( s1 )
l.append( s2 )


for i in range(1,10):
     month = random.randint(1,12)
     day   = random.randint(1,30)

     d = datetime.date( year, month, day )
     r = random.randint(100,25000)

     l.append ( [d,r] )

last = [d,r]
l.sort()
for a in l:
    print a

print "*"*25
print last

f = find( l , last[1] )
g = find( l , theDate )


print f

print g







