import random
import time
from os import name as os_name

secret_number = random.randint(1, 200)

def welcome_message():
    print("May I ask you for your name? : ")
    player_name = input()
    print(player_name + ", we are going to play a game. I am thinking of a number between 1 and 200")
    time.sleep(.5)
    print("Go ahead. Guess!")

def make_guess():
    num_guesses = 0
    while num_guesses < 6:
        time.sleep(.25)
        guess_input = input("Guess: ")
        try:
            guessed_number = int(guess_input)

            if 200 >= guessed_number >= 1:
                num_guesses += 1
                if num_guesses < 6:
                    if guessed_number < secret_number:
                        print("The guess of the number that you have entered is too low")
                    if guessed_number > secret_number:
                        print("The guess of the number that you have entered is too high")
                    if guessed_number != secret_number:
                        time.sleep(.5)
                        print("Try Again!")
                if guessed_number == secret_number:
                    break
            if guessed_number > 200 or guessed_number < 1:
                print("Silly Goose! That number isn't in the range!")
                time.sleep(.25)
                print("Please enter a number between 1 and 200")

        except:
            print("I don't think that " + guess_input + " is a number. Sorry")

    if guessed_number == secret_number:
        num_guesses = str(num_guesses)
        print('Good job, ' + player_name + '! You guessed my number in ' + num_guesses + ' guesses!')

    if guessed_number != secret_number:
        print('Nope. The number I was thinking of was ' + str(secret_number))

play_again = "yes"
while play_again == "yes" or play_again == "y" or play_again == "Yes":
    welcome_message()
    make_guess()
    print("Do you want to play again? (yes/no or y/n)")
    play_again = input()
