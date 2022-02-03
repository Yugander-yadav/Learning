# hangman project 
from ctypes.wintypes import PINT
import random


wordsList = ["apple",'bananna','control']

selected=random.choice(wordsList)
guess=[]
for i in range(len(selected)):
    guess.append("_")

points=0
while(1):
    charGuess=input("Please enter a character").lower()
    for i in range(len(selected)):
            if(charGuess==selected[i]):
                guess[i]=charGuess
                points+=1
            print(guess[i],end=" ")
    else:
        print("You won the game")
        

