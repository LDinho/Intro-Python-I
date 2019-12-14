# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE


def is_even(number):
    if number % 2 == 0:
        return True
    elif number % 2 == 1:
        return False
    else:
        return "try again"

# Read a number from the keyboard


num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

if is_even(num):
    print('Even')
else:
    print('odd')

