import csv

compromised_users = []

with open('passwords.csv') as password_file:
    password_csv = csv.DictReader(password_file)
    for dict in password_csv:
        compromised_users.append(dict['Username'])
    print(compromised_users)


with open('compromised_users.txt', 'w') as compromised_users_files:
    for user in compromised_users:
        compromised_users_files.write(user + '\n')
