import csv

with open('books.csv') as books_csv:
  books_reader = csv.DictReader(books_csv, delimiter='@')
  isbn_list = []
  for element in books_reader:
    isbn_list.append(element['ISBN'])

#  The possibility of a new line escaped by a \n character in our data is why we
#  pass the newline='' keyword argument to the open() function.
