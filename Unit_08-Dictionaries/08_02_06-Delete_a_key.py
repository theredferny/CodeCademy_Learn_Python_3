""".pop() doesn't just delete something
It returns the value in the process
And when you access a dictionary by a key, it returns that key's value
dictionaries are kinda like lists of variables
key: value can be thought of like key = value
So if you return key (say, "cake of the cure"), you get its value (5)
so items.pop('cake') resolves to 5
It just also removes that element in the process"""

available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

health_points += available_items.pop("stamina grains", 0)
health_points += available_items.pop("power stew", 0)
health_points += available_items.pop("mystic bread", 0)

print(available_items, health_points)
