import random

computer_number = random.randint(0,100)
attempts = 0
while True:
    attempts += 1
    print("Guess the number:")
    user_number = int(input())
    if user_number == computer_number:
        print("Congratulations!")
        break
    elif user_number < computer_number:
        print("Try Again! You guessed too high")
    elif user_number > computer_number:
        print("Try Again! You guessed too small")
    
    
print("your try:",attempts)