#Take three numbers and print the largest without using max()

a = 8
b = 8
c = 3
if(a == b and b == c):
  print("all are equal")
elif(a>=b and a>=c):
  print("a: ",a)
elif(b>=a and b>=c):
  print("b: ",b)
else:
  print("c: ",c)

#print(max(a,b,c))