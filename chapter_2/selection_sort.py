def find_min(arr):
    smallest_element = arr[0]
    smallest_element_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest_element:
            smallest_element = arr[i]
            smallest_element_index = i
    return smallest_element_index


def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest_element_index = find_min(arr)
        new_arr.append(arr.pop(smallest_element_index))
    return new_arr


print(selection_sort([5, 3, 6, 2, 10]))

# # Finds the smallest value in an array
# def findSmallest(arr):
#     # Stores the smallest value
#     smallest = arr[0]
#     # Stores the index of the smallest value
#     smallest_index = 0
#     for i in range(1, len(arr)):
#         if arr[i] < smallest:
#             smallest_index = i
#             smallest = arr[i]
#     return smallest_index
#
#
# # Sort array
# def selectionSort(arr):
#     newArr = []
#     for i in range(len(arr)):
#         # Finds the smallest element in the array and adds it to the new array
#         smallest = findSmallest(arr)
#         newArr.append(arr.pop(smallest))
#     return newArr
#
#
# print(selectionSort([5, 3, 6, 2, 10]))
