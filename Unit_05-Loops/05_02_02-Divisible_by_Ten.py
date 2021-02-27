# Write your function here

def divisible_by_ten(nums):
    div_by_ten = [number for number in nums if number % 10 == 0]
    return len(div_by_ten)


# Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))