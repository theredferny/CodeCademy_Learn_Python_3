"""
Overriding methods is really useful in some cases
but sometimes we want to add some extra logic to the existing method.
In order to do that we need a way to call the method from the parent class.
Python gives us a way to do that using super().

super() gives us a proxy object.
With this proxy object, we can invoke the method of an object’s parent class
(also called its superclass).
We call the required function as a method on super():
"""


class PotatoSalad:
    def __init__(self, potatoes, celery, onions):
        self.potatoes = potatoes
        self.celery = celery
        self.onions = onions


class SpecialPotatoSalad(PotatoSalad):
    def __init__(self, potatoes, celery, onions):
        self.raisins = 40
        super().__init__(potatoes, celery, onions)
