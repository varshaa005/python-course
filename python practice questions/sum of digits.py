# Count the digits of a number and find the sum of its digits.

no = 43356

count = 0
sum = 0
for char in str(no):
  count += 1
  sum += int(char)
print(count)
print(sum)