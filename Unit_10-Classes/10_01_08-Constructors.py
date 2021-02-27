"""
__init__() method (note the two underscores before and after the word “init”).
This method is used to initialize a newly created object.
It is called every time the class is instantiated.
"""


class Circle:
    pi = 3.14

    # Add constructor here:
    def __init__(self, diameter):
        print("New circle with diameter: {diameter}".format(diameter=diameter))


teaching_table = Circle(36)
