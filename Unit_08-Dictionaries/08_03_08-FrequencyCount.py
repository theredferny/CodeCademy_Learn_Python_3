"""
Write a function named frequency_dictionary that takes a list of elements named words as a parameter. The function
 should return a dictionary containing the frequency of each element in words
"""

# Write your frequency_dictionary function here:


def frequency_dictionary(words):
    dict = {}
    for element in words:
        dict.update({element: words.count(element)})
    return dict


def frequency_dictionaries(lst):
    return {element: lst.count(element) for element in set(lst)}


# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}
