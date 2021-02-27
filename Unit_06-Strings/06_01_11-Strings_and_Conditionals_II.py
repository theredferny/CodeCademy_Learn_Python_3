def contains(big_string, little_string):
    return little_string in big_string


print(contains("watermelon", "melon"))
print(contains("watermelon", "berry"))


def common_letters(string_one, string_two):
    list_of_same_letters = []
    for letter_one in string_one:
        for letter_two in string_two:
            if letter_one == letter_two and letter_one not in list_of_same_letters:
                list_of_same_letters.append(letter_one)
    return list_of_same_letters


print(common_letters("banana", "cream"))
