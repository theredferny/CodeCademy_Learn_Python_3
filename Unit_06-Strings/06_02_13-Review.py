"""
.upper(), .title(), and .lower() adjust the casing of your string.
    .split() takes a string and creates a list of substrings.
    .join() takes a list of strings and creates a string.
    .strip() cleans off whitespace, or other noise from the beginning and end of a string.
    .replace() replaces all instances of a character/string in a string with another character/string.
    .find() searches a string for a character/string and returns the index value that character/string is found at.
    .format() allows you to interpolate a string with variables.
"""





highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925," \
    "Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871," \
    "Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965," \
    "Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

highlighted_poems_stripped = []
highlighted_poems_details = []
titles = []
poets = []
dates = []

highlighted_poems_list = highlighted_poems.split(',')

for string in highlighted_poems_list:
    highlighted_poems_stripped.append(string.strip(' '))

for details in highlighted_poems_stripped:
    highlighted_poems_details.append(details.split(':'))

for elements in highlighted_poems_details:
    titles.append(elements[0])
    poets.append(elements[1])
    dates.append(elements[2])

for i in range(len(highlighted_poems_details)):
    print("The poem {titles} was published by {poets} in {dates}.".format(titles=titles[i], poets=poets[i], dates=dates[i]))

# print(highlighted_poems)
# print(highlighted_poems_list)
# print(highlighted_poems_stripped)
# print(highlighted_poems_details)


## Cat's code
# highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela " \
                    # "Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold " \
                    # "Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico " \
                    # "City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, " \
                    # "Dreamwood:Adrienne Rich:1987 "

# highlighted_poems_list = highlighted_poems.split(',')
# highlighted_poems_stripped = [poem.strip() for poem in highlighted_poems_list]
# highlighted_poems_details = [poem.split(':') for poem in highlighted_poems_stripped]

# titles, poets, dates = zip(*[(detail[0], detail[1], detail[2]) for detail in highlighted_poems_details])

# for poem in highlighted_poems_details:
    # print('The poem {title} was published by {poet} in {date}.'.format(title=poem[0], poet=poem[1], date=poem[2]))