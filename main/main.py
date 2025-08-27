# import math

# name = input("What's your name?: ")
# print("Hello " + name.capitalize() + "!")

# age = int(input("How old are you " + name + "?: "))
# age += 1;
# print("You are " + str(round(age)) + " years old next year!")


# name = "Zach Hallare"

# firstName = name[0:name.find(' ')]
# lastName = name[name.find(' ')+1:len(name)]
# reversedName = name[::-1]

# print(firstName)
# print(lastName)
# print(reversedName)

# website = "http://google.com"
# slice = slice(7, -4)
# print(website[slice])

# import time
# for i in range(5, 0, -1):
#     print(i)
#     time.sleep(1)
# print("Happy birthday!")

# # matrix
# num = 1
# row = int(input("Enter the number of rows: "))
# column = int(input("Enter the number of column: "))

# for i in range(row):
#     for j in range(column):
#         print(str(num) + " ", end="")  #end="" tells python to not end in a newline
#         num += 1
#     print()

# #pass statement
# for i in range(1, 10):
#     if i == 5:
#         pass
#     else:
#         print(i)




# #lists
# people = ["Yamal", "Pedri", "Ferran"]
# people[0] = "Balde"
# people.append("Hector")
# people.insert(0, "Kounde")

# for i in people:
#     print(i)

# print()
# people.sort()

# for i in people:
#     print(i)



# # #tuples
# student = ("Zach", 19, "Male")
# print(student.count("Male"))
# print(student.index("Zach"))

# for i in student:
#     print(i)



# # sets - unordered, unindexed, no duplicates
# utensils = {"fork", "spoon", "knife", "napkin"}
# dishes = {"bowl", "plate", "cup", "napkin"}
# dinnerTable = utensils.union(dishes)

# for i in dinnerTable:
#     print(i)

# print()
# print(utensils.difference(dishes))  # what does utensil have that dishes dont?
# print(dishes.difference(utensils))
# print(utensils.intersection(dishes))



# # dictionary ("key":"value") = it uses hashing
# capitals = {"USA":"Washington D.C.",
#            "India":"New Dehli",
#            "China":"Beijing",
#            "Russia":"Moscow"}

# print(capitals.get("USA"))
# capitals.update({"Germany":"Berlin"})
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())

# for key, value in capitals.items():
#     print(key, value)



# # functions
# def hello(firstName, lastName):
#     print("Hello " + firstName + " " + lastName + "!")

# hello("Zach", "Hallare")
# hello(lastName="Ngo", firstName="Meggie")


# # *args (method/function overloading for python)
# # the parameters can have different data types
# def add(*args):     # it doesnt have to be named args, but put the *
#     sum = 0
#     for i in args:
#         sum += i
#     return sum

# print(add(1, 2, 3, 4, 5, 6))


# # **kwargs (same as args but it puts it in a dictionary, you use keywords)
# def hello(**kwargs):     # it doesnt have to be named kwargs, but put the **
#     # print("Hello " + kwargs["first"] + " " + kwargs["middle"][0] + ". " + kwargs["last"])
#     print("Hello", end=" ")
#     for key, value in kwargs.items():
#         if key == "middle":
#             print(value[0], end=". ")
#         elif key == "last":
#             print(value, end="! ")
#         else:
#             print(value, end=" ")

# hello(title="Mr.", first="Zach Benedict", middle="Isleta", last="Hallare")



# # string formatting
# print("The {animal} jumped over the {item}".format((animal="cow", item="moon"))    

# # Aligning
# name = "Zach"
# print("Hello, {:<10}. Nice to meet you".format(name))
# print("Hello, {:^10}. Nice to meet you".format(name))
# print("Hello, {:>10}. Nice to meet you".format(name))

# pi = 3.14159
# print("The number pi is {:.3f}".format(pi))

# number = 1000
# print("The number is {:,}".format(number))
# print("The number is {:b}".format(number))
# print("The number is {:o}".format(number))
# print("The number is {:X}".format(number))



# random module
import random

x = random.randint(1, 6)
print(x)

y = random.random()
print(y)

myList = ["rock", "paper", "scissors"]
z = random.choice(myList)
print(z)

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K", "A"]
random.shuffle(cards)
print(cards)

