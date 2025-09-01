class Car:
    wheels = 4  # class variable (you can change this outside the class)

    # __init__ is python's version of a constructor.
    def __init__(self, make, model, year, color):
        self.make = make        # instance variable
        self.model = model      # instance variable
        self.year = year        # instance variable
        self.color = color      # instance variable

    # methods
    def drive(self):
        print("This car is driving")

    def stop(self):
        print("This car is stopped")

