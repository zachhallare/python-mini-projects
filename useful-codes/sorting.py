# printing the list
def printList(list):
    for i in list:
        print(i)


# 1D Array sorting
# students = ["Zach", "Benedict", "Isleta", "Hallare", "Bench"]

# # method version
# # students.sort(reverse=True)

# # function version
# sortedStudents = sorted(students, reverse=True)

# for i in students:
#     print(i)


# # 2D Array sorting
# students = [("Zach", "A", 19),
#             ("Benedict", "C", 32),
#             ("Isleta", "B", 10),
#             ("Hallare", "A", 47),
#             ("Bench", "D", 22)]

# grade = lambda grades:grades[1]
# students.sort(key=grade)
# printList(students)

# print()

# age = lambda age:age[2]
# students.sort(key=age, reverse=True)
# printList(students)



# mapping
store = [("shirt", 20.00),
         ("pants", 25.00),
         ("jacket", 50.00),
         ("socks", 10.00)]

toEuros = lambda data: (data[0], data[1]*0.82)
toDollars = lambda data: (data[0], data[1]/0.82)

storeDollars = list(map(toDollars, store))
printList(storeDollars)

print()



# filtering
goodPrice = lambda data:data[1] < 25
updatedPrices = list(filter(goodPrice, store))
printList(updatedPrices)
