




#A) python number guessing game

import random

lowest_num = 1
highest_num = 100

answer = random.randint(lowest_num, highest_num)

guesses = 0
is_running = True

print("python number guessing game!!")
print(f"Please Selcet a number between {lowest_num} and {highest_num}")

while is_running:

    guess = input("enter your guess: ")
    if guess.isdigit():
          guess =int(guess)
          guesses += 1

          if guess < lowest_num or guess > highest_num:
             print(f"enter a number between{lowest_num} and {highest_num}")
          elif guess > answer:
             print("Too high!")
          elif guess < answer:
             print("Too low!")
          else:
             print("_____________Correct__________")
             print(f"answer was: {answer}")
             print(f"Number of try: {guesses}")
             is_running = False
    else:
        print("Invalid guess")

