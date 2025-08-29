class Car:

    # __init__ is python's version of a constructor.
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    # methods
    def drive(self):
        print("This car is driving")

    def stop(self):
        print("This car is stopped")

