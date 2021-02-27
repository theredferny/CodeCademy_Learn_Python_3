#Write your function here
def add_greetings(names):
    each_greeting = []
    each_greeting = ["Hello, " + name for name in names]
    return each_greeting

#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))