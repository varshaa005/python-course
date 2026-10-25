import datetime
currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
year = date.strftime("%Y")
name = "varsha"
yob = "2005"

print(f"my name is {name}. i'm {int(year)-int(yob)} yrs old")