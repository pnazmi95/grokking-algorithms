def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less_array = [item for item in arr[1:] if item <= pivot]
        greater_array = [item for item in arr[1:] if item > pivot]

        return quick_sort(less_array) + [pivot] + quick_sort(greater_array)


print(quick_sort([1, 10, -5, -4, 2]))
