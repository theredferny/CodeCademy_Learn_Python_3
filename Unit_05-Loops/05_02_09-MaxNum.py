## Function to calculate the time it takes to run any function
import time


# def command_time(func, *args):
    # begin = time.time()
    # func(*args)
    # finish = time.time()
    # total_time = finish - begin
    # print("Command '{}' completed in: {}".format(func, total_time))
##

## Long way
def max_numero(nums):
    nums.sort() # inefficient
    return nums[-1]

print(max_numero([50, -10, 0, 75, 20]))

## Short way
def max_num(nums):
    biggest_num = nums[0]
    for i in nums:
        if i > biggest_num:
             biggest_num = i
    return biggest_num

## Test
print(max_num([-50, -10, -23, -75, -200]))

#### Cat's Function

import random
import time


def num_mais_grande(lst):
    lst_sorted = sorted(lst)
    return lst_sorted[-1]


def max_num(lst):
    biggest = lst[0]
    for num in lst:
        if num > biggest:
            biggest = num
    return biggest


def command_time(func, *args):
    begin = time.time()
    func(*args)
    finish = time.time()
    total_time = finish - begin
    print("Command '{}' completed in: {}".format(func, total_time))


rand_lst = [random.randint(-10_000_000, 10_000_000) for i in range(10_000_000)]

proceed = input("List generated. Continue? (Y/n): ")

if proceed.lower() == 'y' or proceed == '':
    proceed = input("Which max_num method would you like to run?\n"
                    "1) Sort list and select last element\n"
                    "2) Compare current maximum to each element and store if larger\n"
                    "Selection: ")
    if int(proceed) == 1:
        command_time(num_mais_grande, rand_lst)
    elif int(proceed) == 2:
        command_time(max_num, rand_lst)
    else:
        print("Invalid selection")
        exit()
else:
    exit()