"""
One way that we can introduce polymorphism to our class definitions is by using Python’s special dunder methods.

Python gives us the power to define dunder methods that define a custom-made class
to look and behave like a Python builtin.

"""


class Atom:
    def __init__(self, label):
        self.label = label

    def __add__(self, other):
        return Molecule([self, other])


class Molecule:
    def __init__(self, atoms):
        if type(atoms) is list:
            self.atoms = atoms


sodium = Atom("Na")
chlorine = Atom("Cl")
salt = Molecule([sodium, chlorine])
# salt = sodium + chlorine
