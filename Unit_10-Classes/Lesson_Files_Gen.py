"""
Goal: create .py files.

- First part of files names: unit number
- Second part: lesson number
- Third part: exercise number
- Then: "-Name_of_the_Exercise"

"""

unit_number = '10'  # add wanted data
lesson_number = '02'  # add wanted data
exercise_number = 1
file_contents = '"""\n\n"""\n\n\n'

with open('exercises_list.txt') as exercises_list:
    for name in exercises_list.readlines():
        file_name = "{unit}_{lesson}_{exercise}-{name}.py".format(unit=unit_number, lesson=lesson_number,
                                                                  exercise=str(exercise_number).zfill(2),
                                                                  name=name.replace(' ', '_').replace('\n', ''))
        with open(file_name, 'w') as py_file:
            py_file.write(file_contents)
        exercise_number += 1
