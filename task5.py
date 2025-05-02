import random
randomNum = random.randint(0,50)
attempt = 0
winnerDeclared = False
while (attempt <5):
    usrInput = int(input("Guess the Number: "))
    if(usrInput==randomNum):
        winnerDeclared= not(winnerDeclared)
        break
    elif(usrInput> randomNum):
        print("Guess Lower!")
    else:
        print("Guess Higher")
    attempt+=1
if(winnerDeclared):
    print("You won the game😊!, in ",attempt,"attempts.")
else:
    print("You loose the game😒!, the number was ",randomNum)