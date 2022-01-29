#Randomisation and python lists


#watch psuedo random numbers from khan academy 

from math import floor
import random

import day4_import as a

print(a.a)
print(round(random.random()*5))

l=[1,2,3,34,4,54,43,43,43,43,54,43,46546]
l.append(32323)

print(l)


# string split 


name = "yugander,yadav,bala,goutham"

names = name.split(",")
print(names)

a=["11","12","13"]
b=["21","22","23"]
c=["31","33","33"]

h=[a,b,c]
print(f'{a}\n{b}\n{c}')
z=(input("Please enter a row and column number"))
d=int(z[0])-1
e=int(z[1])-1
print(h[d][e])
