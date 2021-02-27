import random

# Collect user data
name = input("What is your name? ")
question = input("Ask me your questions. Yes or no answers only. ")

# Available answers
answer_1 = "Yes - definitely."
answer_2 = "It is decidedly so."
answer_3 = "Without a doubt."
answer_4 = "Reply hazy, try again."
answer_5 = "Ask again later."
answer_6 = "Better not tell you now."
answer_7 = "My sources say no."
answer_8 = "Outlook not so good."
answer_9 = "Very doubtful."

# Pick a random answer
random_number = random.randint(1, 9)

if random_number == 1:
    answer = answer_1
elif random_number == 2:
    answer = answer_2
elif random_number == 3:
    answer = answer_3
elif random_number == 4:
    answer = answer_4
elif random_number == 5:
    answer = answer_5
elif random_number == 6:
    answer = answer_6
elif random_number == 7:
    answer = answer_7
elif random_number == 8:
    answer = answer_8
elif random_number == 9:
    answer = answer_9
else:
    answer = "Error"

# Print out the answers
if question == "":
    print("No question provided. Try again.")
elif name == "":
    print("Question: " + question)
    print("Magic 8-Ball's answer: " + answer)
else:
    print(name + " asks: " + question)
    print("Magic 8-Ball's answer: " + answer)
