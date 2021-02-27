# Write your function here
def every_three_nums(start):
    return list(range(start, 101, 3))

# Uncomment the line below when your function is done
print(every_three_nums(91))

# Write your function here
def remove_middle(lst, start, end):
    return lst[0:start] + lst[end + 1:]

# Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

# Write your function here
def more_frequent_item(lst, item1, item2):
    if lst.count(item1) >= lst.count(item2):
        return item1
    elif lst.count(item2) > lst.count(item1):
        return item2
    else:
        return "ERROR"

# Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

# Write your function here
def double_index(lst, index):
    if index >= len(lst):
        return lst
    elif index < len(lst):
        new_lst = lst[0:index]
        new_lst.append(lst[index] * 2)
        new_lst = new_lst + lst[index + 1:]
        return new_lst
    else:
        return "ERROR"

# Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))

# Write your function here
def middle_element(lst):
    if len(lst) % 2 == 0:
        return int((lst[int(len(lst) / 2)] + lst[int(len(lst) / 2) - 1]) / 2)
    elif len(lst) % 2 != 0:
        return lst[int(len(lst) / 2)]
    else:
        return "ERROR"


# Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))

