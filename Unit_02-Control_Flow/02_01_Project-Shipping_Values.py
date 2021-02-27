# Collect weight data
weight = float(input("Please type the weight of your package: "))

# Normal Ground Shipping values
normal_flat_charge = 20.00
normal_price_1 = weight * 1.50
normal_price_2 = weight * 3.00
normal_price_3 = weight * 4.00
normal_price_4 = weight * 4.75

if weight <= 2:
    normal_cost = normal_price_1 + normal_flat_charge
elif 2 < weight <= 6:
    normal_cost = normal_price_2 + normal_flat_charge
elif 6 < weight <= 10:
    normal_cost = normal_price_3 + normal_flat_charge
elif weight > 10:
    normal_cost = normal_price_4 + normal_flat_charge
else:
    print("ERROR. Value not supported.")

# Premium Ground Shipping values
premium_cost = 125.00

# Drone Shipping values
drone_flat_charge = 0
drone_price_1 = weight * 4.50
drone_price_2 = weight * 9.00
drone_price_3 = weight * 12.00
drone_price_4 = weight * 14.25

if weight <= 2:
    drone_cost = drone_price_1 + drone_flat_charge
elif 2 < weight <= 6:
    drone_cost = drone_price_2 + drone_flat_charge
elif 6 < weight <= 10:
    drone_cost = drone_price_3 + drone_flat_charge
elif weight > 10:
    drone_cost = drone_price_4 + drone_flat_charge
else:
    print("ERROR. Value not supported.")

# Total shipping costs
print("Normal Ground Shipping costs $" + str(round(normal_cost, 2)))
print("Premium Ground Shipping costs $" + str(round(premium_cost, 2)))
print("Drone Shipping costs $" + str(round(drone_cost, 2)))

# Pick cheapest shipping cost
if normal_cost <= premium_cost and normal_cost <= drone_cost:
    print("The cheapest shipping option is Normal Ground Shipping.1")
elif premium_cost <= normal_cost and premium_cost <= drone_cost:
    print("The cheapest shipping option is Premium Ground Shipping.")
elif drone_cost <= normal_cost and drone_cost <= premium_cost:
    print("The cheapest shipping option is Drone Shipping.")
else:
    print("ERROR. The cheapest option wasn't found. Try again.")
