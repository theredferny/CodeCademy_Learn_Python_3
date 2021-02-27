poem_title = "spring storm"
poem_author = "William Carlos Williams"

poem_title_fixed = poem_title.title()
poem_author_fixed = poem_author.upper()

print(poem_title)
print(poem_title_fixed)
print(poem_author)
print(poem_author_fixed)

#     .upper(), .title(), and .lower() adjust the casing of your string.
#     .split() takes a string and creates a list of substrings.
#     .join() takes a list of strings and creates a string.
#     .strip() cleans off whitespace, or other noise from the beginning and end of a string.
#     .replace() replaces all instances of a character/string in a string with another character/string.
#     .find() searches a string for a character/string and returns the index value that character/string is found at.
#     .format() allows you to interpolate a string with variables.