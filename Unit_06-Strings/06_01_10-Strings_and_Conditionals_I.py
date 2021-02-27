def letter_check(word, letter):
    for i in word:
        if letter == i:
            return True
    return False

print(letter_check("bee", "b"))
print(letter_check("john", "n"))
print(letter_check("john", "y"))