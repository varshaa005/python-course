marks = int(input("enter marks: "))
print("Grade: ")
if marks >= 90:
  print("A")
elif marks <= 89 and marks >=75:
  print("B")
elif marks <= 74 and marks >=50:
  print("C")
else:
  print("Fail")