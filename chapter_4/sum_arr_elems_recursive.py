# def recursive_sum_arr_elems_func(arr):
#     if len(arr) == 0:
#         return 0
#     elif len(arr) == 1:
#         return arr[0]
#     elif len(arr) >= 2:
#         first = arr[0]
#         arr.pop(0)
#         return first + recursive_sum_arr_elems_func(arr)

def recursive_sum_arr_elems_func(arr):
    if not arr:
        return 0
    return arr[0] + recursive_sum_arr_elems_func(arr[1:])


print(recursive_sum_arr_elems_func([1, 2, 3, 4]))
