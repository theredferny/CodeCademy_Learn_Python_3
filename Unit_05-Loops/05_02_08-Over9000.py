def over_nine_thousand(lst):
    sum_9000 = 0
    for i in lst:
        sum_9000 += i
        if sum_9000 > 9000 or i == lst[-1]:
            break
    return sum_9000

print(over_nine_thousand([8000, 900, 120, 5000]))
print(over_nine_thousand([]))
print(over_nine_thousand([1]))