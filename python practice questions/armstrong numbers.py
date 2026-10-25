

for i in range (101,1000):
  p = len(str(i))
  sum = 0

  for char in str(i): 
    sum += int(char)**p
  if sum == i:
    print(i)