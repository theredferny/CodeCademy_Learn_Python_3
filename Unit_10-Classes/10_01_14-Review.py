"""

"""


class Student:

    def __init__(self, name, year, attendance):
        self.name = name
        self.year = year
        self.grades = []
        self.attendance = {}

    def add_grade(self, grade):
        if type(grade) == Grade:
            self.grades.append(grade)

    def get_average(self):
        grades_sum = 0
        for grade in self.grades:
            grades_sum += grade.score
        return grades_sum / len(self.grades)


roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)


class Grade:
    minimum_passing = 65

    def __init__(self, score):
        self.score = score

    def is_passing(self):
        return self.score >= self.minimum_passing


new_grade = Grade(100)
pieter.add_grade(new_grade)

sum_grades1 = Grade(100)
sum_grades2 = Grade(99)
sum_grades3 = Grade(98)
sum_grades4 = Grade(97)
sum_grades5 = Grade(1)
roger.add_grade(sum_grades1)
roger.add_grade(sum_grades2)
roger.add_grade(sum_grades3)
roger.add_grade(sum_grades4)
roger.add_grade(sum_grades5)

# print(new_grade.score)
print(roger.get_average())
# print(type(sum_grades5))


