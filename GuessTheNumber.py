print("WELCOME")
import random
random_number = random.randint(1, 100)
while True:
    user_guess = int(input("Guess a number between 1 and 100: "))
    if user_guess == random_number:
            print("Congratulations! You  won ! You guessed the correct number:", random_number)
            break       
    elif user_guess < random_number:
            print("it's low guess, guess again!")
    elif user_guess > random_number:
            print("it's high guess, guess again!")
    else:
            print("Sorry, you guessed the wrong number")
