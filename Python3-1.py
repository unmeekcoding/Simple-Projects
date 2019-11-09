import random

guessesTaken = 0

print("I am thinking of a number! Take a guess at what it is.")

randomNumber = random.randint(0, 20)

while guessesTaken < 3:
    userGuess = input()
    userGuess = int(userGuess)
    
    guessesTaken = guessesTaken + 1
    
    if randomNumber < userGuess:
        print("You guessed too high!")
    if randomNumber > userGuess:
        print("You guessed too low")
    if randomNumber == userGuess:
        print("You got it!")
        break
    
if userGuess == randomNumber:
    guessesTaken = str(guessesTaken)
    print('Good job! You guessed my number in ' + guessesTaken + ' guesses!')

if userGuess != randomNumber:
    randomNumber = str(randomNumber)
    print('Sorry. Better luck next time! The number I was thinking of was ' + randomNumber)
        