import time
date = str(input('Please enter a date in the from DD/MM/YY: '))
date2 = time.strptime(date,'%d/%m/%y')
#Refer to https://docs.python.org/2/library/time.html#time.strptime for datetime syntax
hold = date2.tm_year
print(hold)
hold = date2.tm_mon
print(hold)
hold = date2.tm_mday
print(hold)
