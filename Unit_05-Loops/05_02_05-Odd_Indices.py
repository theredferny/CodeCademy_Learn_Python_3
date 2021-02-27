def odd_indices(lst):
    new_lst = [lst[i] for i in range(len(lst)) if i % 2 == 1]
    return new_lst


def odd_indices(lst):
    new_lst = [lst[i] for i in range(1, len(lst), 2)]
    return new_lst

print(odd_indices([4, 3, 7, 10, 11, -2, 1]))