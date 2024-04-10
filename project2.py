import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("please type a number larger than 0 nest time.")
        quit()


random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("please type a next time.")
        continue

    if user_guess == random_number:
        print("you got it!")
        break    
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")    

print("You got it on", guesses, "guesses")
