a = int(input("enter a side: "))
b = int(input("enter b side: "))
c = int(input("enter c side: "))

if a+b>c and b+c>a and c+a>b:
  print("valid triangle")
  if a == b == c:
    print("equilateral")
  elif a == b != c or b == c != a or c == a != b:
    print("Isosceles")
  else:
    print("scalene")
else:
  print("not valid")