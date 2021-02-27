import random

tarot = {1: "The Magician", 2: "The High Priestess", 3: "The Empress", 4: "The Emperor", 5: "The Hierophant",
         6: "The Lovers", 7: "The Chariot", 8: "Strength", 9: "The Hermit", 10: "Wheel of Fortune", 11: "Justice",
         12: "The Hanged Man", 13: "Death", 14: "Temperance", 15: "The Devil", 16: "The Tower", 17: "The Star",
         18: "The Moon", 19: "The Sun", 20: "Judgement", 21: "The World", 22: "The Fool"}

# spread = {}

# spread.update({'past': tarot.pop(13)})
# spread.update({'present': tarot.pop(22)})
# spread.update({'future': tarot.pop(10)})

# for key, val in spread.items():
    # print('Your {key} is the {value} card.'.format(key=key, value=val))


# tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}

# spread = {}

# spread.update({"past": tarot.pop(13), "present": tarot.pop(22), "future": tarot.pop(10)})

# for keys, values in spread.items():
    # print('Your {keys} is the {values} card.'.format(keys=keys, values=values))

## Bonus problem: Make 8.2.10 give you a random draw every time you run it

random_list = [random.randint(1, 22) for i in range(3)]

def is_unique(lst):
    for number in lst:
        if lst.count(number) > 1:
            return False
    return True

while not is_unique(random_list):
    random_list = [random.randint(1, 22) for i in range(3)]

spread = {}
spread.update({"past": tarot.pop(random_list[0]), "present": tarot.pop(random_list[1]), "future": tarot.pop(random_list[2])})

for keys, values in spread.items():
    print('Your {keys} is the {values} card.'.format(keys=keys, values=values))

print(random_list)

"""from random import randint

tarot = {1: "The Magician", 2: "The High Priestess", 3: "The Empress", 4: "The Emperor", 5: "The Hierophant",
         6: "The Lovers", 7: "The Chariot", 8: "Strength", 9: "The Hermit", 10: "Wheel of Fortune", 11: "Justice",
         12: "The Hanged Man", 13: "Death", 14: "Temperance", 15: "The Devil", 16: "The Tower", 17: "The Star",
         18: "The Moon", 19: "The Sun", 20: "Judgement", 21: "The World", 22: "The Fool"}

times = ['past', 'present', 'future']
cards = [randint(1, 22) for i in range(3)]

while len(cards) != len(set(cards)):
    cards = [randint(1, 22) for i in range(3)]

spread = {time: tarot[card] for time, card in zip(times, cards)}

for key, val in spread.items():
    print('Your {key} is the {value} card.'.format(key=key, value=val))"""

"""rand_list = [0, 0]

while len(rand_list) != len(set(rand_list)):  # Regenerate random card selection if values are not unique
    rand_list = [randint(1, 10) for i in range(10)]

print(rand_list)"""

"""from random import randint

rand_list = []

while len(rand_list) < 3:
    rand = randint(1, 22)
    if rand not in rand_list:
        rand_list.append(rand)

print(rand_list)"""