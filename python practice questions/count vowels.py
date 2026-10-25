sentence = "Coding in Python is fun"

vowel = ['a','e','i','o','u','A','E','I','O','U']
count = 0

for char in sentence:
  if(char in vowel):
    print(char)
    count+=1
print(count)