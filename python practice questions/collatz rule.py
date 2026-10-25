n = 6
count = 0

while n != 1:
  count += 1
  if n%2 == 0:
    n = n//2   
  else:
    n = n*3 + 1
  print(n)    
print("steps: ",count)
