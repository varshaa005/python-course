year = int(input("enter an year: "))

if(year%4 == 0):
  print("a leap year")
elif(year%400):
  print("a leap year")
else:
  print("not a leap year")