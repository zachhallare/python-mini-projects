import random
import time

def welcomeMessage():
    name = input("What's your name?: ")
    print("Welcome " + name.capitalize() + "!")
    return name.capitalize()

def mainMenu():
    choice = 0
    while choice < 1 or choice > 6:
        print("\n===== MINI GAME HUB =====")
        print("1. Rock, Paper, Scissors")
        print("2. Number Guessing")
        print("3. Dice Roller")
        print("4. Multiplication Table Generator")
        print("5. Utilities")
        print("6. Quit")
        try:
            choice = int(input("Choose an option (1-6) : "))
        except:
            print("Invalid input, please enter a number.")
            choice = 0
    return choice


def rockPaperScissors():
    playerScore = 0
    computerScore = 0
    playAgain = "y"

    choices = ["rock", "paper", "scissors"]
    print("Welcome to Rock, Paper, Scissors!")

    while playAgain == "y":
        userChoice = ""
        while userChoice not in choices:
            userChoice = input("You chose: ").lower()
            if userChoice not in choices:
                print("Invalid choice, try again!\n")

        computerChoice = random.choice(choices)
        print("Computer chose: " + computerChoice)
        time.sleep(1)

        if ((userChoice == "rock" and computerChoice == "scissors") or
            (userChoice == "scissors" and computerChoice == "paper") or
            (userChoice == "paper" and computerChoice == "rock")):
            playerScore += 1
            print("Result: You win this round!")
        elif userChoice == computerChoice:
            print("Result: It's a draw!")
        else:
            computerScore += 1
            print("Result: Computer wins this round!")
        
        print("\nScores:")
        print("Player: " + str(playerScore))
        print("Computer: " + str(computerScore))
        playAgain = input("Play again? (y/n): ").lower()
        print()

    return



def numGuessingGame():
    playAgain = "y"

    while playAgain == "y":
        numOfAttempts = 3
        randomNumber = random.randint(1, 20)

        print("I am thinking of a number between 1 and 20...")
        print("You have 3 tries to guess it!\n")

        while numOfAttempts > 0:
            try:
                userGuess = int(input("Enter your guess: "))
                if userGuess == randomNumber:
                    print("Correct! The number was " + str(randomNumber) + ".\n")
                    break
                elif userGuess < randomNumber:
                    print("Too low!\n")
                else:
                    print("Too high!\n")
                
                numOfAttempts -= 1

                if numOfAttempts == 0:
                    print("Out of attempts! The number was " + str(randomNumber) + " .\n")
            except ValueError:
                print("Please enter a valid number!\n")

        playAgain = input("Do you want to play again? (y/n): ").lower()
        print()

    return



def diceRoller():
    playAgain = "y" 

    while playAgain == "y":
        deckOfCards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "K", "Q", "J"]

        print("Welcome to the Randomizer!")
        print("1. Roll a Dice")
        print("2. Shuffle Cards")

        userChoice = 0
        while userChoice not in range(1, 3):
            try:
                userChoice = int(input("Choose an option: "))
                if userChoice == 1:
                    print("\nRolling a die...")
                    time.sleep(1)
                    print("You rolled: " + str(random.randint(1, 6)))
                elif userChoice == 2:
                    print("\nShuffling cards...")
                    time.sleep(1)
                    random.shuffle(deckOfCards)
                    print("Here's the shuffled deck:\n" + str(deckOfCards))
                else:
                    print("Invalid choice, try again!\n")
            except ValueError:
                print("Please enter a valid number!\n")

        playAgain = input("Do you want to play again? (y/n): ").lower()
        print()

    return



def multiplicationGen():
    playAgain = "y"

    while playAgain == "y":
        print("Welcome to the Multiplication Table Generator!")
        try: 
            chosenNumber = int(input("Enter a number: "))
        except ValueError:
            print("Invalid number!\n")
            continue

        print("\nHere's the multiplication table for " + str(chosenNumber))
        for i in range(1, 11):
            print("{:>3} x {:<2} = {}".format(chosenNumber, i, chosenNumber * i))

        playAgain = input("Do you want to play again? (y/n): ").lower()
        print()

    return



def hello(**kwargs):
    print("Hello", end=" ")
    for key, value in kwargs.items():
        if key == "middle":
            print(value[0] + ".", end=" ")
        elif key == "last":
            print(value + "!")
        else:
            print(value, end=" ")
    print("\n")

    

def utilities(username):
    choice = 0

    while choice < 1 or choice > 3:
        print("Welcome to the Utilities!")
        print("1. Age Calculator")
        print("2. Unique Word Counter")
        print("3. Greeting Generator")
        try:
            choice = int(input("Choose (1-3): "))
        except:
            print("Invalid input, try again.\n")
            choice = 0

    if choice == 1:
        try: 
            age = int(input("How old are you " + username + "?: "))
            print("You will be " + str(age + 1) + " next year!")
        except ValueError:
            print("Please enter a valid number!")
    elif choice == 2:
        sentence = input("Enter a sentence: ")
        words = set(sentence.split())
        print("Unique words (" + str(len(words)) + "):", words)
    elif choice == 3:
        middleName = input("Enter your middle name: ")
        lastName = input("Enter your last name: ")
        hello(title="Mr.", first=username, middle=middleName, last=lastName)


def spacer():
    print("\n=========================\n")


def Funbox():
    username = welcomeMessage()
    selectedChoice = 0

    while True: 
        selectedChoice = mainMenu()

        if selectedChoice == 1:
            spacer()
            rockPaperScissors()
        elif selectedChoice == 2:
            spacer()
            numGuessingGame()
        elif selectedChoice == 3:
            spacer()
            diceRoller()
        elif selectedChoice == 4:
            spacer()
            multiplicationGen()
        elif selectedChoice == 5:
            spacer()
            utilities(username)
        elif selectedChoice == 6:
            spacer()
            print("Thanks for playing, " + username + "! See you again.")
            break        


Funbox()



