import threading
import time

# def eatBreakfast():
#     time.sleep(3)
#     print("You eat breakfast")

# def drinkCoffee():
#     time.sleep(4)
#     print("You drank coffee")

# def study():
#     time.sleep(5)
#     print("You finish studying")

# x = threading.Thread(target=eatBreakfast, args=())
# x.start()

# y = threading.Thread(target=drinkCoffee, args=())
# y.start()

# z = threading.Thread(target=study, args=())
# z.start()


def timer():
    print()
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for: ", count, " seconds")

x = threading.Thread(target=timer, daemon=True)
x.start()

answer = input("Do you wish to exit?")