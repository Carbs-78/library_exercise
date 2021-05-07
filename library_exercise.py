import math
import random
print("Welcome to Abdul, John & Greg's Super Amazing Awesome Python Math program!!!\n")
n = input("Please enter a number (eg. 34.56) or 'r' to generate a random number :") 

if n == "r":
    number = random.random()*100 # generate a random number
    print("Random number generated is ", number, "\n")

else:
    number = float(n) # convert user input to float

# Program for ceil() function
# this allows user to input
# x=float(input("Enter a float value: "))
# using the math module
# import math
# ceil function finds the next whole number
y = math.ceil(number)
#prints the results
print("the ceiling value of ",number," is ",y, "\n")

#Code for floor() function
y = math.floor(number)
print("The floor value of ", number, " is ", y, "\n")
