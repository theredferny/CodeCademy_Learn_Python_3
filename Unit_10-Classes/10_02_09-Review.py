"""
Incredible! We subclassed a Python primitive and introduced new behavior to it.

Some things to consider:

    When a SortedList gets initialized with unsorted values (say if you call SortedList([4, 1, 5]))
    those values don’t get sorted!
    How would you change SortedList so that the list is sorted right after the object gets created?
    What other Python builtins have functionality “missing”?
    Could you write a new dictionary that uses a fallback value when it tries to retrieve an item and can’t?
"""


class SortedList(list):
    def append(self, value):
        super().append(value)
        self.sort()
