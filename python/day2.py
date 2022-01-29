# datatypes numbers operations type conversions f-strings 

# strings 
# integers 
# floats 
# boolean

print("hello"[1]) # subscripting 

# to separate digits in a large number we can use _ 

a = 123_456_789
print(a)


# Float

print(3.12233)


# Boolean 

print(True)


# type conversion 


# num = input("enter a number")
# print(f"the sum of number {int(num[0])+int(num[1])}")


# math operations 
print(2/1.0)

print(round(1.533223))



# // floor division operator 



## tip calculator 


bill = int(input("enter the total bill"))
tip = int(input("enter the 10 12 20 percentage of tip "))
people = int(input("enter the number of people"))
total = bill+(bill*(tip)/100)
print(f'each one have to pay {round(total/people,2)}')

