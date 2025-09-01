class Animal:
    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")
    

# inherits Animal class
class Rabbit(Animal):
    def run(self):
        print("This rabbit is running")

class Fish(Animal):
    def swim(self):
        print("This fish is swimming")

class Hawk(Animal):
    def fly(self):
        print("This hawk is flying")
    # method overriding
    def sleep(self):
        print("This animal is now awake")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
hawk.fly()
hawk.sleep()
