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



