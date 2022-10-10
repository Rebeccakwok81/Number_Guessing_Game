import random
import time

print("Hi! Welcome to the guessing game. I am going to pick a number between 1 and 10.")
time.sleep(3)
print("Picking a number...")
time.sleep(2)
guess = int(input("What is your guess?: "))
correct_num = random.randint(1,10)
guess_count = 1

while guess != correct_num:
    guess_count += 1
    if guess < correct_num:
        guess = int(input("Wrong. Guesses higher num. What is your guess?: "))
    else:
        guess = int(input("Wrong. Guesses lower num. What is your guess?: "))

print(f"You got it!:), the right answer was {correct_num}.It took you {guess_count} guesses.")