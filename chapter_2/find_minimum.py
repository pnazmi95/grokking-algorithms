def find_min(arr):
    smallest_element = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest_element:
            smallest_element = arr[i]
            smallest_index = i
    return smallest_index


print(find_min([1, -2, 3, 0, 10]))
