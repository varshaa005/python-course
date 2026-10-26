for i in range(1,101):
  if i%7 == 0 and i%9 == 0:
    print(i)
    break

for i in range(1,31):
  if i%3 == 0:
    continue
  print(i)
  
for i in range(1,21):
  if i%2 != 0:
    continue
  if i>15:
    break
  print(i)