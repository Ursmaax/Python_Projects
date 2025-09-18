# Concept - Ternary Operator
# num = 3
# print("Even" if num % 2 == 0 else "Odd")
# print("Positive" if num > 0 else "Negative")
# from os import access
#
# from pandas.core.interchange.from_dataframe import primitive_column_to_ndarray
from pandas.core.interchange.from_dataframe import primitive_column_to_ndarray

# n = 6
# m = 10
# print("n is big" if n > m else "m is big")

# user_role ="admin"
# access_limits = "limited Access" if user_role != "admin" else "Full Access"
# print(access_limits)

# problem :
# validate user input exercise
#1. username is no more than 12 characters
#2. username must not contain spaces
#3. username must not contain digits . . . . . . . .

# username = input("Enter your username here : ")
# spaces = username.find(" ")
# digit = username.isdigit()
# if len(username) > 12 :
#     print("invalid : Your username is more than 12 characters !!!")
# else :
#     if spaces > 0 :
#         print("invalid : Your username contain spaces !!!")
#     else :
#         if digit :
#             print("invalid : Your username contains digits !!!")
#         else :
#             print(f"Welcome {username}")


# Concept - indexing : accessing elements of a sequence using [] (indexing operator ).
# [start : end : step]
# phone_number = "9849072215"
# print(phone_number[0 : 5 ])
# print(phone_number[ : 5 ])
# print(phone_number[0 : 5 : 2 ])
# print(phone_number[::-1])
# print(phone_number[5: ])
# print(phone_number[-1])
# print(phone_number[ : : 2 ])
# last_digits = phone_number[-2:]
# print(f"XXXXX XXX{last_digits}")


#Concept - Format specifiers = {:flags} format a value based on what flags are inserted
#.(number)f = round to that many decimal places (fixed point)
#: (number) = allocate that many spaces
#:03 = allocate and zero pad that many spaces
#:< = left justify
# :> = right justify
#:^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
#: = insert a space before positive numbers
#:, = comma separator
# Practice :
#
# area_of_circle1 = 3005.141516
# area_of_circle2 = 97654.123134234
# area_of_circle3 = 243525.90508217311
# #Float precision
# print(f"Area of Circle 1 = {area_of_circle1 :.2f}") #Area of Circle 1 = 3.14
# print(f"Area of Circle 2 = {area_of_circle2 :.3f}") #Area of Circle 1 = 3.14
# print(f"Area of Circle 3 = {area_of_circle3 :.4f}") #Area of Circle 3 = 8.9051
# #Arraged to exact 15 spaces :
# print(f"Area of Circle 1 = {area_of_circle1 :15}")#Area of Circle 1 =        3.141516
# print(f"Area of Circle 2 = {area_of_circle2 :15}")#Area of Circle 2 =     9.123134234
# print(f"Area of Circle 3 = {area_of_circle3 :15}")#Area of Circle 3 =   8.90508217311
# #default values at spaces - zeros :
# print(f"Area of Circle 1 = {area_of_circle1 :015}")#Area of Circle 1 = 00000003.141516
# print(f"Area of Circle 2 = {area_of_circle2 :015}")#Area of Circle 2 = 00009.123134234
# print(f"Area of Circle 3 = {area_of_circle3 :015}")#Area of Circle 3 = 008.90508217311
# #default right
# print(f"Area of Circle 1 = {area_of_circle1 :>10}") #Area of Circle 1 =   3.141516
# print(f"Area of Circle 2 = {area_of_circle2 :>10}") #Area of Circle 2 = 9.123134234
# print(f"Area of Circle 3 = {area_of_circle3 :>10}") #Area of Circle 3 = 8.90508217311
# #default left
# print(f"Area of Circle 1 = {area_of_circle1 :<10}") #Area of Circle 1 = 3.141516
# print(f"Area of Circle 2 = {area_of_circle2 :<10}") #Area of Circle 2 = 9.123134234
# print(f"Area of Circle 3 = {area_of_circle3 :<10}") #Area of Circle 3 = 8.90508217311
# #Center
# print(f"Area of Circle 1 = {area_of_circle1 :^10}") #Area of Circle 1 =  3.141516
# print(f"Area of Circle 2 = {area_of_circle2 :^10}") #Area of Circle 2 = 9.123134234
# print(f"Area of Circle 3 = {area_of_circle3 :^10}") #Area of Circle 3 = 8.90508217311
# #defautl separtor thousands , hundreds , tens and ones
# print(f"Area of Circle 1 = {area_of_circle1 :,}") #Area of Circle 1 = 3,005.141516
# print(f"Area of Circle 2 = {area_of_circle2 :,}") #Area of Circle 2 = 97,654.123134234
# print(f"Area of Circle 3 = {area_of_circle3 :,}") #Area of Circle 3 = 243,525.90508217312
# #using multiple flags
# print(f"Area of Circle 1 = {area_of_circle1 :,.2f}") #Area of Circle 1 = 3,005.14
# print(f"Area of Circle 2 = {area_of_circle2 :,.2f}") #Area of Circle 2 = 97,654.12
# print(f"Area of Circle 3 = {area_of_circle3 :,.2f}") #Area of Circle 3 = 243,525.90

# Concept - While loop : Execute some code WHILE some condition remain true

# name = input("Enter your name here : ")
# while name == "" :
#     print("You didn't enter the name / name can't be empty")
#     name = input("Enter your name here : ")
# print(f"Hello {name} !!!")

# age = int(input("Enter your age here : "))
# while age < 0 :
#     print("Age can't be negative")
#     age = int(input("Enter your age here : "))
# print(f"Your age : {age}")

# food = input("Enter the food item you want (q to quit) : ").lower()
# while not  food  == "q" :
#     food = input("Enter the food item you want (q to quit ) :")
# print("Bye")

# Concept - For Loop = Execute a block of code a fixed number of times .
#                      You can iterate over a range , string , sequence etc ...

# for x in reversed(range (0, 11)) : # it prints in reversed order ex : 10 , 9 , 8 ,7 .....
#     print(x)
# print("Happy Birthday Divya 😍 !!!")
#
# for i in range(0 , 11, 2) :
#     print(i)

# Concept : Break and Continue statements

# for x in range(0,11):
#      if x == 5 :
#          print("This number is picked ")
#          continue
#      else :
#          print(x)

# for x in range(1, 6):
#      if x == 3 :
#          break
#      else :
#          print(x)

# Concept : Time Module :

# import time
# my_time = int(input(f"Enter Time in Seconds : "))
# for x in reversed(range(0,my_time)):  # for x in range(my_time , 0 , -1) this logic will also done same thing ... it increments reversly
#     seconds = x % 60 #→ remainder after dividing by 60 → because 11 is less than 60, it’s basically x itself here.
#     minutes = int(x / 60) % 60
#     hours = x / 3600
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1) # This will delay for 1 second for each iteration ....
# print("Happy Birthday My Dear 🦋 Butterfly 🦋 Gaaru ")

# Concept : Nested Loops - A loop inside another loop (outer, inner)
#             outer loop:
#                 inner loop :

# for x in range(1, 10) :
#     print(x, end=" ")

# for x in range(4) :
#     for y in range(1, 10):
#         print(y, end=" ")
#     print()

# rows = int(input("Enter number of  rows : "))
# columns = int(input("Enter number of columns : "))
# symbol = input("Enter the symbol :" )
# for row in range(rows):
#     for column in range(columns):
#         print(symbol , end=" ")
#     print()

#Concept -  Collections  = Single "variable" used to store multiple values.
#          1. List - [] = Ordered and changeable, Duplicates OK
#          2. Set  - {} = Unordered and immutable, but Add/Remove OK. NO duplicates
#          3. Tuple- () = Ordered and unchangeable, Duplicates OK, FASTER

#List :
# colours = ["Green" , "Orange" , "Pink" , "violet" , "Yellow" ]
# print(colours) #['Green', 'Orange', 'Pink', 'violet', 'Yellow'] - Ordered 
# print(colours[0:5])    #index starts from 0
# print(colours[::-1])   #prints all in reverse order
# print(colours[0:])     # Prints all from zero on words
# print(colours[ : :3])  #['Green', 'violet']
# print(colours[-2])     #violet

# for colour in colours :
#     print(colour , end="\n")
# colours = ["Green" , "Orange" , "Pink" , "violet" , "Yellow" ]
# xs = dir(colours) # It will return what are the different types of operations that we can perform on list collections , we can also print like this : print(dir(colurs))
# for x in xs :
#     print(x)
# print(help(colours))
# print(len(colours)) # returns length of the list
# print("Green" in colours) # This method checks whether Green present inthe list or not and returns boolean value in this case output will look like = True
# colours[1] = "Blue" # lists can be modified
# print(colours[1])   #Blue

# colours = ["Green" , "Orange" , "Pink" , "violet" , "Yellow" ]
# colours.append("Blue") # this method adds blue into the list at last
# print(colours) # ['Green', 'Orange', 'Pink', 'violet', 'Yellow', 'Blue']

# colours = ['Green', 'Orange', 'Pink', 'violet', 'Yellow', 'Blue']
# colours.remove("Green") # it removes that element from the list completely
# print(colours)          # ['Orange', 'Pink', 'violet', 'Yellow', 'Blue']

# colours = ['Green', 'Orange', 'Pink', 'violet', 'Yellow', 'Blue']
# colours.insert(0 ,"Pink") # it inserts a value at any position
# print(colours) #['Pink', 'Green', 'Orange', 'Pink', 'violet', 'Yellow', 'Blue']

# colours = ['Pink', 'Green', 'Orange', 'Pink', 'violet', 'Yellow', 'Blue']
# colours.sort() #it sorts the entire list in alphabetical order
# print(colours) #['Blue', 'Green', 'Orange', 'Pink', 'Pink', 'Yellow', 'violet']

# colours = ['Pink', 'Green', 'Orange', 'Pink', 'violet', 'Yellow', 'Blue']
# colours.reverse() #it arranges our entire list in reverse order according to index not alphabetical as default
# print(colours) #['Blue', 'Yellow', 'violet', 'Pink', 'Orange', 'Green', 'Pink']

# colours = ['Pink', 'Green', 'Orange', 'Pink', 'violet', 'Yellow', 'Blue']
# colours.clear() #it clears entire list and makes it empty
# print(colours) # []

# colours = ['Pink', 'Green', 'Orange', 'Pink', 'violet', 'Yellow', 'Blue']
# print(colours.index("Orange")) # 2 ... it will return the index of the specific element if it is in the list ...

# colours = ['Pink', 'Green', 'Orange', 'Pink', 'violet', 'Yellow', 'Blue']
# print(colours.count("Pink"))   # 2 ... this method will tell you how many elements are these with same name her pink is there 2 times in the list ...

#Concept = 2. Set  - {} = Unordered and immutable, but Add/Remove OK. NO duplicates :

# animals = {"Dog" , "Cat" , "Goat" , "Sheep" ,"Elephant" ,"Cow" , "Butterfly" , "Peacock"}
#print(animals) # Unordered _ {'Goat', 'Cat', 'Butterfly', 'Elephant', 'Cow', 'Dog', 'Peacock', 'Sheep'}
#print(type(animals)) #<class 'set'>
#UNCGANGABLE

#Concept =  3. Tuple- () = Ordered and unchangeable, Duplicates OK, FASTER

animals = ("Dog 🐶" , "Cat 😼" , "Goat 🐐" , "Sheep 🐏" ,"Elephant 🐘" ,"Cow 🐄" , "Butterfly 🦋" , "Peacock 🦚" , "Cat 😼")
# print(animals) #('Dog', 'Cat', 'Goat', 'Sheep', 'Elephant', 'Cow', 'Butterfly', 'Peacock')
# print(animals.index("Cat")) #1

# print(animals[::-1])
# for animal in animals :
#     print(animal , end="\n")
# print(animals.count("Cat 😼"))

