names = ['Jenny', 'Alexus', 'Sam', 'Grace']
dogs_names = ['Elphonse', 'Dr. Doggy DDS', 'Carter', 'Ralph']

names_and_dogs_names = zip(names, dogs_names)
list_of_names_and_dogs_names = list(zip(names, dogs_names))
print(list_of_names_and_dogs_names)

# A "list" with () is actually a different object called a "tuple"
# A tuple is like a list, but it is "immutable"
# Immutable (and "static") mean "unchanging"
# You can't add or modify elements of a tuple
# It will cause an error