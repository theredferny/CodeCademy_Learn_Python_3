"""
In Python __main__ means “this current file that we’re running”
and so one could read the output from type() to mean “the class Facade that was defined here,
in the script you’re currently running."
"""

class Facade:
  pass

facade_1 = Facade()
facade_1_type = type(facade_1)
print(facade_1_type)  # this will print the type of the object
#  in this case, the output will be <class '__main__.Facade'>

