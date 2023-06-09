# def count_arr_elems_recursive_func(arr):
#     if not arr:
#         return 0
#     arr.pop(0)
#     return 1 + count_arr_elems_recursive_func(arr)

def count(arr):
    if not arr:
        return 0
    return 1 + count(arr[1:])


# print(count_arr_elems_recursive_func([1, 2, 3, 4, 5]))
print(count([1, 2, 3, 4, 5]))
