# print("hello world")
# print("hello ")
# print("world")
# print("ctrl+/")

# name = "varsha"
# age = 21
# cgpa = 8.6

# #typecasting

# a = "34"
# c = int(a)
# print(type(a))
# print(type(c))

# a = int(input("Enter a number: "))
# b = int(input("enter no: "))
# sum = a + b
# print(sum)

# print("varsha" ,"21" , "hello" , sep=", ")
# print("hello", "world", end="/")

# operators : Arithmetic = add +, sub -, mul *, div /, mod %, floor div //, exp **  
#             Comparision = true or false(<,>,==,!=,<=,>=)
#             Logical = OR, AND, NOT

# name = "Varsha"
# age = 21
# height = 152.6
# is_student = False

# print("The name of the person is " + name + ". She is " + str(age) + " years old. " + "She is " + str(height) + "cms tall. " +  "Student: " + str(is_student))

# num = "45"
# print(int(num) + 10)

# food = input("tell your fav food: ")
# print("Wow! I also like "+ food)

# a = int(input("enter a number: "))

# print("square= ", a**2)
# print("cube= ", a**3)
# b = int(input("enter 2nd number: "))

# print("sum = " , a+b)
# print("diff = " , a-b)
# print("mul = " , a*b)
# print("quot = " , a/b)

# age = int(input("enter your age: "))

# if(age>18):
#   print("you can drive")
# elif(age == 18):
#   print("get licence")
# else:
#   print("you can't drive")

# a = int(input("enter a number: "))

# match a:
#   case 1:
#     print("hi")
#   case 3:
#     print("hello")
#   case 6:
#     print("hola")
#   case _:
#     print("bye")

# i = 1
# for i in range(1,11):
#   if i == 5:
#       break #cancel the exec of the loop
#   print(i)

# i = 1
# for i in range(1,11):
#   if i == 5:
#     continue #continue the loop for the next iteraton here itself
#   print(i)

# if i == 32:
#   pass #basically does nothing

# i = int(input("no: "))
# if(i == 0):
#     print("zero")
# elif(i > 0):
#     print("positive")
# else:
#     print("negative")

# age = int(input("age: "))
# if(age >= 18):
#   print("Can Vote")
# else:
#   print("cant")

# day = int(input("enter day of the week: "))

# match day:
#   case 1:
#     print("monday")
#   case 2:
#     print("tuesday")
#   case 3:
#     print("wednesday")
#   case 4:
#     print("thursday")
#   case 5:
#     print("friday")
#   case 6:
#     print("saturday")
#   case 7:
#     print("sunday")

# n = int(input("enter num: "))

# for i in range(1,11):
#   print(n , "X", i, "=", n*i)


# sum = 0
# for i in range(1,101):
#   sum += i
# print(sum)


# num = 6523
# print(int(str(num)[::-1]))


#Strings
# a = 'Hello' #Single quoted
# b = "Hello" #double qu..
# c = '''Hello''' #triple qu..  """Hello"""
# c = '''hello
# hi
#    bye'''
# print(c)

# d = '"hello"'  ??
# print(d)  

# name = "Varsha0123456789"
# print(name[0:10])
# print(name[0:10:2]) #[0:10:n] skips n-1 chars
# print(name[::3]) #replaces first empty number with 0 #name[:4]
#                  # and second empty number with length #name[1:]

#Strings are immutable(not changeable)

# s = "hello woRld"

# print(s.upper())
# print(s.lower())
# print(s.capitalize())
# print(s.title())

# text ="  hello world  "
# print(text.strip())
# print(text.lstrip())
# print(text.rstrip())

# text = "python is fun is fun"
# print(text.find("is"))
# print(text.replace("fun","awesome"))

# text = "Apples,Bananas,Berries"
# print(text.split(","))
# print(",".join(['Apples', 'Bananas', 'Berries']))

# text ="Python123"
# print(text.isalpha()) 
# print(text.isdigit()) 
# print(text.isalnum()) 
# print(text.isspace())

# name = "varsha"
# age = 21
# print(f"my name is {name}. I'm {age}")


#string practise set

# name = "Varsha Kollu"
# print(name[0])
# print(name[-1])
# print(len(name))

# str1 = "hello"
# str2 = "world"
# print(str1 +" "+ str2)
# print(str1,str2)

#text = "Python Programming"

# print(text[0:7])
# print(text[-6:])
# print(text[1::2])

#print(text[::-1])

# text = " i love python programming "
# print(text.strip())
# print(text.title())
# print(text.count("o"))

# str1 = "123abc"
# print(str1.isalnum())

# sentence = "Coding in Python is fun"
# new = sentence.replace("fun","awesome")
# print(new)
# index = sentence.index("Python")
# print(index)
# print(sentence.upper())



