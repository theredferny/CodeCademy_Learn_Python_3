def larger_sum(lst1, lst2):
    total1 = 0
    total2 = 0
    for i in lst1:
        total1 += i
    for i in lst2:
        total2 += i
    if total1 >= total2:
        return lst1
    elif total1 < total2:
        return lst2
    else:
        return "ERROR"

print(larger_sum([1, 9, 5], [2, 3, 7]))


# cheating way
def larger_sum(lst1, lst2):
    if sum(lst1) >= sum(lst2):
        return lst1
    else:
        return lst2