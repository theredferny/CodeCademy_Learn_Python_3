"""
e’ve learned so far that a class is a schematic for a data type and an object is an instance of a class,
but why is there such a strong need to differentiate the two if each object can only have the methods and class variables the class has?
This is because each instance of a class can hold different kinds of data.

The data held by an object is referred to as an instance variable.
Instance variables aren’t shared by all instances of a class — they are variables that are specific to the object they are attached to.
"""

class Store:
  pass

#We can instantiate two different objects from this class, alternative_rocks and isabelles_ices,
# and assign instance variables to these objects using the same attribute notation that was used for accessing class variables.

alternative_rocks = Store()
isabelles_ices = Store()

alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ices"

store_names = "{} {}".format(alternative_rocks.store_name, isabelles_ices.store_name)
print(store_names)
