first_name = "Reiko"
last_name = "Matsuki"

def password_generator(first_name, last_name):
  new_password = first_name[len(first_name) - 3:] + last_name[len(last_name) - 3:]
  return new_password

temp_password = password_generator("Reiko", "Matsuki")