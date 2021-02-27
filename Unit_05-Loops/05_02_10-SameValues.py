def same_values(lst1, lst2):
    same_index_same_value = []
    for i in range(len(lst1)):
        if lst1[i] == lst2[i]:
            same_index_same_value.append(i)
    return same_index_same_value

print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))