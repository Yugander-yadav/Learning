# conditional statements logical operators , code blocks with scope
a=1

# indentation is important in python 


if(a==0):
    print("hello world")
elif a==1:
    print("yo")
else:
    print("what up")

## odd or even assignment 


b=3

if(b%2==0):
    print("even")
else:
    print("odd")


## and or not 



if(1):
    print("true")
else:
    print("false")




# leap year problem 


year=2100

if(year%4==0 and year %400==0):
    print("leap year")
else:
    print("not a leap year")

print("eeeeeeeeeeeeee".count('e')) # to know the character occurence 



# Treasure Island Program


print("welcome to the Treasure Island ")

a=input("which direction you want to take  left or right ").lower()

if(a=='left'):
    a=input("what do you want to do swim or wait ").lower()
    if(a=='wait'):
        a=input("which door you want to take red blue or yellow").lower()
        if(a=='blue'):
            print("you won")
        else:
            print("Game over")
    else:
        print("Game over")
else:
    print("game over")