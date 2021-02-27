## Len's Slices ##

# Menu of pizza toppings and prices
toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']
prices = [2, 6, 1, 3, 2, 7, 2]

# Creating a variable that contains all sorts of pizzas and orders them
num_pizzas = len(toppings)
pizzas = list(zip(prices, toppings))
pizzas.sort()

# Variables to organise pizzas according to their characteristics
cheapest_pizza = pizzas[0]
priciest_pizza = pizzas[-1]
three_cheapest = pizzas[:3]
num_two_dollar_slices = prices.count(2)

# Outputs
print(pizzas)
print("We sell " + str(num_pizzas) + " different kinds of pizza!")
print(three_cheapest)
print(num_two_dollar_slices)
