import random
pace=0
cace=0
player=[]
computer=[]
deck=[11,2,3,4,5,6,7,8,9,10,10,10,10]

player.append(random.choice(deck))
player.append(random.choice(deck))
computer.append(random.choice(deck))
computer.append(random.choice(deck))
pa='sample'
pc='sample'
psum=0
print("Player has cards",end=" ")
game=True
while(game):
    for i in range(len(player)):
        if(sum(player)>=21):
            print("the player has got an ace")
            player[player.index(11)]=1
    
        print(f"{player[i]}",end=" ")
    print(f"\nThe sum of player cards :{sum(player)}")
    
    print("computer has cards",end=" ")
    
    for i in range(len(computer)-1):
        print(computer[i],end=" ")
    
    break

    

    
    