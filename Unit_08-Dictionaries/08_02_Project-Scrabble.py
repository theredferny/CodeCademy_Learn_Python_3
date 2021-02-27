letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Dictionaries
letter_to_points = {letters: points for letters, points in list(zip(letters, points))}
letter_to_points.update({" ": 0})

player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"],
                   "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

player_to_points = {}


# Total points of a word
def score_word(word):
    point_total = 0
    for letter in word:
        point_total += letter_to_points.get(letter, 0)
    return point_total


# Adding words and/or players and adding their points
def play_word():
    player = input("Type your username: ")
    word = input("Type your word: ").upper()
    if player not in player_to_words:
        return "ERROR. Player not found."
    elif player in player_to_words:
        player_to_words[player].append(word)
    update_point_totals()


# Updating the player points based on the words played
def update_point_totals():
    for player, words in player_to_words.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
        player_to_points.update({player: player_points})


play_word()

# Checks
print(letter_to_points)
print(player_to_points)
print(player_to_words)
