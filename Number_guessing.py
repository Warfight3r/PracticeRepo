import random

top_of_range = input("Enter the top of range: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please enter a number greater than 0.")
        quit()
else:
    print("Please enter a number next time.")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    user_guess = input("Make a guess: ")
    guesses += 1
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter a number next time.")
        continue
    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You got it wrong.")
        print("You were above the number.")
    elif user_guess < random_number:
        print("You got it wrong.")
        print("You were below the number.")
        
print("You got it in %s guesses." % guesses)