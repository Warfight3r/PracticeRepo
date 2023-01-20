print("Welcome to my quiz game. We hope you would like our fried chicken.")
playing = input("Do you want to proceed? ")
print(playing)

if playing != "yes":
    quit()

print("Alright then. We begin our game. Yeah Mr.White!")
score = 0

answer = input("What is the best place is to store your product in a truck? You know what I mean here. ").lower()

if answer == "in the batter":
    print("That is correct! Remember to check the patches on the boxes of batter first.")
    score += 1
else:
    print("You got it wrong. Please don't get involved with transportation.")

answer = input("If a customer keeps asking to meet the owner, what do you do? ").lower()

if answer == "call the given number":
    print("Correct! I will be there for my customers whenever they need me.")
    score += 1
else:
    print("No. You directly call me if the customer repeatedly insists.")

answer = input("Yo bitch. Answer this. What do you call a place where cows live? ").lower()

if answer == "cowhouse":
    print("Yeah bitch! Give me five! There you go Mr.White. I told you its a cow house.")
    score += 1
elif answer == "barn":
    print("That's some bullshit Mr.white taught you. It's not called a barn!")
else:
    print("Wrong, Bitch!")

answer = input("Now I will ask you a question. *a man standing in a black jacket and a black hat*. What is my name? Say it. ").lower()

if answer == "heisenberg":
    print("You're goddamn right.")
    score += 1
else:
    print("You are wrong and this is not meth! *booom*")

print("You answered " + str(score) + " questions correctly.")

if score <= 2:
    print("Your performance did not meet to our standards. Mike will take you back to your home.")
elif score == 3:
    print("You seem to be a good choice for our organisation. Meet me at the factory tomorrow morning at 9 A.M .")
else:
    print("We are impressed with your performance. Stay on our side and I believe you will find it very fruitful. ")
