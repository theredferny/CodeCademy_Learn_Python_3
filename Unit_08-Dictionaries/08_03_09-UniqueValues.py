"""
Create a function named unique_values that takes a dictionary named my_dictionary as a parameter. The function should
 return the number of unique values in the dictionary.
"""

# Write your unique_values function here:


def unique_values(my_dictionary):
    unique_lst = []
    for value in my_dictionary.values():
        if value not in unique_lst:
            unique_lst.append(value)
    return len(unique_lst)


def unique_value(my_dict):
    return len(set(my_dict.values()))

# Uncomment these function calls to test your  function:
print(unique_values({0: 3, 1: 1, 4: 1, 5: 3}))
# should print 2
print(unique_values({0: 3, 1: 3, 4: 3, 5: 3}))
# should print 1
