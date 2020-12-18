# Import current month,year,day:
import datetime

x=datetime.datetime.now()
print(x.month)
print(x.year)
print(x.strftime("%A"))

#Import the datetime module and display the current date:

import datetime

x = datetime.datetime.now()

print(x)
