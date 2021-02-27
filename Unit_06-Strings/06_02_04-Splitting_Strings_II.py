authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(',')
last_names = []
author_last_names = []

for names in author_names: # split the strings inside the list into substrings
    last_names += names.split(' ')

for i in range(len(last_names)): # create another variable with only the odd index elements
    if i % 2 != 0:
        author_last_names.append(last_names[i])

print(author_names)
print(last_names)
print(author_last_names)

authors2 = "Samuel Taylor Coleridge,Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Edgar Allen Poe,Adrienne Rich,Nikki Giovanni"

author_names2 = authors2.split(',')

print(author_names2)
last_name = []

for name in author_names2:
    split_name = name.split(' ')
    last_name.append(split_name[-1])

print(last_name)

# author_last_names = [name.split()[-1] for name in author_names]
## Cat's code

