"""
Python offers a whole suite of magic methods a class can implement that will allow us to use the same syntax
as Python’s built-in data types. You can write functionality that allows custom defined types to behave like lists

"""


class LawFirm:
    def __init__(self, practice, lawyers):
        self.practice = practice
        self.lawyers = lawyers

    def __len__(self):
        return len(self.lawyers)

    def __contains__(self, lawyer):
        return lawyer in self.lawyers


d_and_p = LawFirm("Injury", ["Donelli", "Paderewski"])
