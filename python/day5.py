#loops and running loops on lists 

# for loops 


import random

sample=[1,2,3,4,5,6,7,8,9]
heights=[]
for s in sample:
    height='1'
    height+=str(sample [random.randint(0,len(sample)-1)])
    height+=str(sample[ random.randint(0,len(sample)-1)])
    heights.append(int(height))  

sum=0
count=1
for j in heights:
    sum+=j
    count+=1


print(f"Average height: {round(sum/count)}")
print(f"Max height : {max(heights)}")
print(f"Min height : {min(heights)}")



# python range function 

sum=0
for a in range(0,101,1): # including 1 and not including 322
    sum+=a

print(sum)




# fizz buzz program 
#RULES
# if number divisible by 3 then fizz 5 then buzz if both 3 and 5 then fizz buzz


for a in range(1,101):
    if(a%3==0):
        if(a%5==0):
            print("Fizz Buzz")
        else:
            print("Fizz")
    elif(a%5==0):
        print("Buzz")
    else:
        print(a)



a='a'
alphabets=[]
alphabets.append(a)
numbers=[]
for i in range(1,26):
    alpha=chr(ord(a)+i)
    alphabets.append(alpha)
    numbers.append(i)
print(alphabets)
numbers=numbers[0:9]
print(numbers)

symbols=['!','@','#','$','%','^','&','*','(',')','-']

# noa=int(input("Please enter password length "))
# nos=int(input("enter number of symbols "))
# non=int(input('enter number of numbers '))


# for a in range(0,noa):
#     d=randint(1,3)

print(random.shuffle())