str1 = "varshakollu"

for i in range(len(str1)):
  if str1[i] in str1[:i]:
    print(str1[i])
    break

