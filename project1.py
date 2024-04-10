name = input(" What's your name: ")
print("Hello", name, "welcome to my quiz!")

playing = input("Are you ready? ")

if playing.lower() != "yes":
    print("Maybe nextime. Goodbye! ")
    quit()

print("Okay let's go!")    
score = 0

answer = input("In which year did World War I begin? 1923, 1938 or 1914. ")
if answer.lower() == "1914":
    print("Correct! ")
    score += 1
else:
 print("Incorrect. ")

answer = input("In which country was Adolf Hitler born? Germany, France or Austria. ")
if answer.lower() == "Austria":
    print("Correct! ")
    score += 1
else:
 print("Incorrect. ")

answer = input("Where was John F. Kennedy assassinated? New York, Dallas, Austin or Miami.  ")
if answer.lower() == "Dallas":
    print("Correct! ")
    score += 1
else:
 print("Incorrect. ")

answer = input("The disease that ravaged and killed a third of Europe's population in the 14th century is known as: Plague, Smallpox or Malaria. ")
if answer.lower() == "Plague":
    print("Correct! ")
    score += 1
else:
 print("Incorrect. ")

 answer = input("In which year did Albert Einstein get the Nobel Prize? 1935, 1922 or 1929. ")
if answer.lower() == "Plague":
    print("Correct! ")
    score += 1
else:
 print("Incorrect. ")

 print("You got " + str(score) + " questions correct!" )
 print("That's a " + str((score / 5) * 100) + " %" " score." )       
