# Variables
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# Defining functions
def f_to_c(temp_f):
    c_temp = (temp_f - 32) * 5/9
    print(round(c_temp, 2))

def c_to_f(c_temp):
    f_temp = c_temp * (9/5) + 32
    print(round(f_temp, 2))

def get_force(mass, acceleration):
    return mass * acceleration

def get_energy(mass, c=3*10**8):
    return mass * c * c

def get_work(mass, acceleration, distance):
    return get_force(mass, acceleration) * distance

# Variables
f100_in_celcius = f_to_c(100)
c0_in_fahrenheit = c_to_f(0)
train_force = get_force(train_mass, train_acceleration)
bomb_energy = get_energy(bomb_mass)
train_work = get_work(train_mass, train_acceleration, train_distance)

# Results
print(train_force)
print("The GE train supplies " + str(train_force) + " Newtons of force.")
print("A 1kg bomb suppies " + str(bomb_energy) + " Joules.")
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")