"""
This style is especially useful when we have an object for which it might not matter
which class the object is an instance of.
Instead, we’re interested in whether that object can perform a given task.

When two classes have the same method names and attributes, we say they implement the same interface.
An interface in Python usually refers to the names of the methods and the arguments they take.
Other programming languages have more rigid definitions of what an interface is,
but it usually hinges on the fact that different objects from different classes can perform the same operation
(even if it is implemented differently for each class).
"""


class InsurancePolicy:
    def __init__(self, price_of_item):
        self.price_of_insured_item = price_of_item


class VehicleInsurance(InsurancePolicy):
    def get_rate(self):
        return self.price_of_insured_item * .001


class HomeInsurance(InsurancePolicy):
    def get_rate(self):
        return self.price_of_insured_item * .00005
