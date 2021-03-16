"""
Great job! You’ve created two classes and defined their interactions. This is object-oriented programming!
From here you could:

    Write a Grade method .is_passing() that returns whether a Grade has a passing .score.
    Write a Student method get_average() that returns the student’s average score.
    Add an instance variable to Student that is a dictionary called .attendance,
    with dates as keys and booleans as values that indicate whether the student attended school that day.
    Write your own classes to do whatever logic you want!
"""


class Circle:
    pi = 3.14

    def __init__(self, diameter):
        self.radius = diameter / 2

    def area(self):
        return self.pi * self.radius ** 2

    def circumference(self):
        return self.pi * 2 * self.radius

    def __repr__(self):
        return 'Circle with radius {radius}'.format(radius=self.radius)


medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza)
print(teaching_table)
print(round_room)
