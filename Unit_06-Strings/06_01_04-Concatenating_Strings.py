first_name = "Julie"
last_name = "Blevins"

def account_generator(first_name, last_name):
  new_acc_name = first_name[:3] + last_name[:3]
  return new_acc_name

new_account = account_generator("Julie", "Blevins")