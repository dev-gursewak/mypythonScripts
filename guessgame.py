#this program is to guess a number between 1 to 20.
print("Hello!, what is your name?")
name = input() #asking of persons name.


import random
secretNumber = random.randint(1, 20) # random number b/w 1 to 20
print("well " + str(name) + ", I was thinking of number between 1 to 20.")


for guessNumber in range(1, 7):
    print("Guess the number.")
    guess = int(input())
    if secretNumber > guess:
        print("Your number is too low") #for greater secret no. than guess no.
    elif secretNumber < guess:
        print("Your number is too high") #for smaller secret no. than guess no.
    else:
        break   #for correct guess.


if guess == secretNumber:
   print("whooooo, you guess the correct number:). You take only " + str(guessNumber) + " guess")
else:
   print("You are out of guesses as you already did " + str(guessNumber) + ' gusses')
     
