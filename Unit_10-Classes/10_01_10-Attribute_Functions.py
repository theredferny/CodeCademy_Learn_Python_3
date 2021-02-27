"""
Instance variables and class variables are both accessed similarly in Python.
This is no mistake, they are both considered attributes of an object.
If we attempt to access an attribute that is neither a class variable nor an instance variable of the object
Python will throw an AttributeError.


What if we aren’t sure if an object has an attribute or not?
hasattr() will return True if an object has a given attribute and False otherwise.
If we want to get the actual value of the attribute, getattr() is a Python function
that will return the value of a given object and attribute.
In this function, we can also supply a third argument that will be the default if the object does not have the given attribute.

The syntax and parameters for these functions look like this:

hasattr(object, “attribute”) has two parameters:

    object : the object we are testing to see if it has a certain attribute
    attribute : name of attribute we want to see if it exists

getattr(object, “attribute”, default) has three parameters (one of which is optional):

    object : the object whose attribute we want to evaluate
    attribute : name of attribute we want to evaluate
    default : the value that is returned if the attribute does not exist (note: this parameter is optional)

"""

can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for element in can_we_count_it:
  if hasattr(element, "count") == True:
    print(str(type(element)) + " has the count attribute!")
  else:
    print(str(type(element)) + " does not have the count attribute :(")
