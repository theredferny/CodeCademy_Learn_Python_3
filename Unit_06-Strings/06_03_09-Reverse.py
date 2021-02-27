"""
Write a function named reverse_string that takes a string as a parameter. The function should return word in reverse.
"""

# Write your reverse_string function here:


def reverse_string(string):
    reverse = ''
    for i in range(len(string)):
        reverse += string[-i - 1]
    return reverse

def reverse_strings(string): # Cat's version
    gnirts = ''
    for index in range(1, len(string) + 1):
        gnirts = gnirts + string[-index]
    return gnirts

# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print

# Challenge: Try with list slicing


def gnirts_esrever(string):
    return string[::-1]


# Challenge: Try without slicing or range()


def reverser(string):
    reverse_string = ''
    for letter in string:
        reverse_string = letter + reverse_string
    return reverse_string