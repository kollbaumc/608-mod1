#calc_max_chriskollbaum.py
"""Find the maximum of three values."""

number1 = int(input('Enter first number: '))
number2 = int(input('Enter sencond number: '))
number3 = int(input('Enter third number: '))

maximum = number1

if number2 > maximum:
    maximum = number2

if number3 > maximum:
    maximum = number3

print('Maximum value is', maximum)