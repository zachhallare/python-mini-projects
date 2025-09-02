class Student:
    def __init__(self, name, grade):
        self.__name = name    # private attribute
        self.__grade = grade    # private attribute
        # if its "protected" use only 1 underscore

    # getter methods
    def getName(self):
        return self.__name
        
    def getGrade(self):
        return self.__grade
        
    # setter method
    def setGrade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print("Invalid grade!")

    
student = Student("Zach", 95)

print(student.getName())
print(student.getGrade())

student.setGrade(100)
print(student.getGrade())

