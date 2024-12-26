"""Simple calculator program using functions"""
# x and y are the parameters that represent the 2 numbers to be used for our calculations
# This program uses integers only however we'll be using a float to accomodate any decimals 

def add(x, y):
    return x+y

def subtract(x, y):
    return x-y

def multiply(x, y):
    return x*y

def divide(x, y):
    return x/y

# Methods to use for user input
print("Choose a method of calculation:")
print('1.add')
print('2.subtract')
print('3.multiply')
print('4.divide')

choice = int(input('Enter a choice between(1,2,3,4): '))

num1 = float(input('Enter a number: '))
num2 = float(input('Enter a number: '))

# Calculation structure based on the above user inputs provided
if choice == 1:
    #choice 1 is add
    print(f'{num1}+{num2} = {add(num1, num2)}')

elif choice == 2:
    #choice 2 is subtract
    print(f'{num1}-{num2} = {subtract(num1, num2)}')

elif choice == 3:
    #choice 3 is multiply
    print(f'{num1}*{num2} = {multiply(num1, num2)}')

elif choice == 4:
    #choice 4 is divide
    print(f'{num1}/{num2} = {divide(num1, num2)}')

else:
    print(f'input not valid')