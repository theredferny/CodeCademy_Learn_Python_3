def del_starting_evens(lst):  # This version looks for the first odd element and makes a new list that starts there
    i = 0
    while i <= len(lst):
        if i == len(lst):
            return []
        elif lst[i] % 2 == 1:
            i += 1
            break
        else:
            i += 1
            continue
    new_list = lst[i-1:]
    return new_list

def delete_starting_evens(lst):
    while len(lst) != 0 and lst[0] % 2 == 0:
        lst = lst[1:]
    return lst

# Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))