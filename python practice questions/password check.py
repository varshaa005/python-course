password = "V029K"
# entered_password = input("Enter Password: ")

# while (entered_password != password):
#   print("wrong! try again.")
#   entered_password = input("Enter Password: ")
# print("you're logged in")

attempts = 0

while attempts < 3:
  entered_password = input("Enter Password: ")
  attempts += 1

  if password == entered_password:
    print("correct")
    break
  else:
    print("wrong")

if attempts == 3 and entered_password != password:
  print("max attempts reached")