import random

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    # rock: 0, paper: 1, scissors: 2

    computer_pick = options[random_number]

    print("Computer picked %s." % computer_pick)

    if user_input == "paper" and computer_pick == "rock":
        print("You win!")
        user_wins += 1
    elif user_input == "rock" and computer_pick == "scissors":
        print("You win!")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You win!")
        user_wins += 1
    elif user_input == "rock" and computer_pick == "rock":
        print("It's a draw!")
    elif user_input == "scissors" and computer_pick == "scissors":
        print("It's a draw!")
    elif user_input == "paper" and computer_pick == "paper":
        print("It's a draw!")
    else:
        print("computer wins!")
        computer_wins += 1

print("You won %s times." % user_wins)
print("Computer_won %s times." % computer_wins)   
print("Good Bye!")