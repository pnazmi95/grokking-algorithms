def binary_search_recursive(arr, searched_item):
    if not arr:
        return -1

    low_index = 0
    high_index = len(arr) - 1
    mid_index = (high_index - low_index) // 2

    if arr[mid_index] == searched_item:
        return mid_index
    elif arr[mid_index] > searched_item:
        return binary_search_recursive(arr[:mid_index], searched_item)
    else:
        return binary_search_recursive(arr[mid_index + 1:], searched_item)


print(binary_search_recursive([6, 7, 8, 9, 10], 8))
print(binary_search_recursive([6, 7, 8, 9, 10], 6))
