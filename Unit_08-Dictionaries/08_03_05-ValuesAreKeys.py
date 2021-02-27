"""
Create a function named values_that_are_keys that takes a dictionary named my_dictionary as a parameter. This function
 should return a list of all values in the dictionary that are also keys.
"""


# Write your values_that_are_keys function here:


def values_that_are_keys(my_dictionary):
    key_values = []
    for key, value in my_dictionary.items():
        if value in my_dictionary.keys():
            key_values.append(value)
    return key_values


# Uncomment these function calls to test your  function:
print(values_that_are_keys({1: 100, 2: 1, 3: 4, 4: 10}))
# should print [1, 4]
print(values_that_are_keys({"a": "apple", "b": "a", "c": 100}))
# should print ["a"]


def values_that_are_key(my_dict):  # Cat's version
    return [key for key in my_dict if key in my_dict.values()]
