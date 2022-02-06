import random
import hangmanArt as art
import hangmanWords as words
#choosing a random word
print(art.logo)
choosen = random.choice(words.word_list)
print(choosen)

lives=6
# filling the blanks 
word =[]

for i in range(len(choosen)):
    word.append("_")

print(word)
gameOn=True
while(gameOn):
    choice=input("Please enter a letter").lower()
    for i in range(len(choosen)):
        if(choice==choosen[i]):
            word[i]=choice
    if choice not in choosen:
        lives-=1
        print(art.stages[lives])
    if(lives<=0):

        print("Opps Game over")
        gameOn=False

    print(word)

        








hh=[1,2,3,243,35,43,43,43]
print(hh.index(43))
