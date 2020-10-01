import random


def randomNumber():
    random_number = random.randrange(0, 10)

    user_input = int(input("select a random number from 1-10 "))

    while True:
        if random_number == user_input:
            print("You guessed it right, the number is " + str(random_number))
        else:
            print("Wrong! Try again.")

        return False


randomNumber()
