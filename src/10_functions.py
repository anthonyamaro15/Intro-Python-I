# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

# Read a number from the keyboard
num = input("Enter a number: ")
value = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"


def checker(num):
    if (num % 2) == 0:
        print('even')
    else:
        print('Odd')


checker(value)

# YOUR CODE HERE
