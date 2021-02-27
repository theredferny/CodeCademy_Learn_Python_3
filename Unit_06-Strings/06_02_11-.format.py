def poem_title_card(title, poet):
    return "The poem \"{}\" is written by {}.".format(title, poet)

# format adds variables to strings in the order of its placeholders {}

print(poem_title_card("Mundo Grande", "Carlos Drummond de Andrade"))