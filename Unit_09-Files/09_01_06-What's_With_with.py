with open('fun_file.txt') as close_this_file:
    setup = close_this_file.readline()  # read each line
    punchline = close_this_file.readline()
    print(setup)
    print(punchline)

"""
fun_file.txt


What did the pirate say when he turned 80?

Aye Matey.
"""
