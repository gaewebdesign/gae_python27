import re

_date="align=left nowrap bgcolor=white> 09/22/13 "

rxp  = r"([\d]{1,2})\/([\d]{1,2})\/([\d]{1,2})"

m = re.search(rxp , _date)


print( "check ",_date,len(_date)  )
print( "rxp ",rxp)
print( m.group() )



