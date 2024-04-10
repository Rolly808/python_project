import random

# Two players face each other(user/computer), and they are going to try to make a number bond of five between them, using their fingers.
# You miss, you love.


options = ["one", "two", "three", "four"]
score = 0

while True:
    user_input = input("Type one/two/three/four or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # one: 0, two: 1, three: 2, four: 3
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "one" and computer_pick == "four":
        print("wow, You won!")
        score += 1
        
    elif user_input == "two" and computer_pick == "three":
        print("You won, try again!")
        score += 1
        
    elif user_input == "three" and computer_pick == "two":
        print("You won, try again!")
        score += 1

    elif user_input == "four" and computer_pick == "one":
        print("You won, try again!")
        score += 1      
        
    else:
        print("Game over, you lost.")
        print("Better luck next time!")
        print("You won", score, "time(s).")
        quit()


    
    