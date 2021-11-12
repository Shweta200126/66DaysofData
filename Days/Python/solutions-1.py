#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 13:04:18 2019

@author: Giles
"""

'''
Question 1
Write code that asks the user to input a number between 1 and 5 inclusive.
The code will take the integer value and print out the string value. So for
example if the user inputs 2 the code will print two. Reject any input that
is not a number in that range
'''
#Solution
# num = int(input("Enter any integer from 1 to 5:\n>>>"))

# if num == 1:
#     print("You entered one")
# elif num == 2:
#     print("You entered two")
# elif num == 3:
#     print("You entered three")
# elif num == 4:
#     print("You entered four")
# elif num == 5:
#     print("You entered five")
# else:
#     print("Out of range")


'''
Question 2
Repeat the previous task but this time the user will input a string and the
code will ouput the integer value. Convert the string to lowercase first.
'''
#Solution:
# num = input("Enter any integer from one to five:\n>>>")
# num = num.lower()
# if num == 'one':
#     print(1)
# elif num == 'two':
#     print(2)
# elif num == 'three':
#     print(3)
# elif num == 'four':
#     print(4)
# elif num == 'five':
#     print(5)
# else:
#     print("Out of range")


'''
Question 3
Create a variable containing an integer between 1 and 10 inclusive. Ask the
user to guess the number. If they guess too high or too low, tell them they
have not won. Tell them they win if they guess the correct number.
'''
# num = 5
# guess = input("Guess a number from 1 to 10\n>>>")

# if guess.isdigit():
#     guess = int(guess)
#     if guess == num:
#         print("You won!")
#     elif guess < num and guess >0:
#         print("Too low")
#     elif guess > num and guess < 11:
#         print("Too high")
#     else:
#         print("Out of range")
# else:
#     print("This isn't a number")


'''
Question 4
Ask the user to input their name. Check the length of the name. If it is
greater than 5 characters long, write a message telling them how many characters
otherwise write a message saying the length of their name is a secret
'''

#Solution:

# name = input("Enter you name:\n>>>")

# len_name = len(name)

# if len_name > 5:
#     print("You name has", len_name, "letter")
# else:
#     print("You name length is a secret")
    


'''
Question 5
Ask the user for two integers between 1 and 20. If they are both greater than
15 return their product. If only one is greater than 15 return their sum, if
neither are greater than 15 return zero
'''

#Solution:

# x = int(input("Enter a number b/w 1 and 20\n>>>"))
# y = int(input("Enter a number b/w 1 and 20\n>>>"))

# if x > 15 and y > 15:
#     product = x*y
#     print("Product of", x, "and", y, "is", product)
# elif x > 15 or y > 15:
#     sum = x + y
#     print("Sum of", x, "and", y, "is", sum)
# else:
#     print(0)



'''
Question 6
Ask the user for two integers, then swap the contents of the variables. So if
var_1 = 1 and var_2 = 2 initially, once the code has run var_1 should equal 2
and var_2 should equal 1.
'''

#Solution:

# var_1 = int(input("Enter an integer\n>>>"))
# var_2 = int(input("Enter another interger\n>>>"))
# var_1, var_2 = var_2, var_1


# print("\nSwapped numbers are\n\t1.", var_1, "\n\t2.", var_2)


