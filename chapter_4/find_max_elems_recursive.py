def find_max_elems_func(arr):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    temp_max = find_max_elems_func(arr[1:])
    return arr[0] if arr[0] > temp_max else temp_max


print(find_max_elems_func([1, 2, -2, 3, 10]))

