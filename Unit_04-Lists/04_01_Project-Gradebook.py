## Gradebook ##

# Starting data to the gradebook
subjects = ["physics", "calculus", "poetry", "history"]
grades = [90, 97, 85, 88]

# Creating a list with previous datas
gradebook = list(zip(subjects, grades))

# Additions to the lists
subjects.append("computer science")
grades.append(100)
gradebook.append(("visual arts", 93))

# Adding the new gradebook to the previous one
last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]
full_gradebook = last_semester_gradebook + gradebook

# Output
print(gradebook)
