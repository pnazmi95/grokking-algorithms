def binary_search(input_list, item):
    low_index = 0
    high_index = len(input_list) - 1

    while low_index <= high_index:
        mid_index = (low_index + high_index) // 2
        guess = input_list[mid_index]
        if guess == item:
            return mid_index
        elif guess > item:
            high_index = mid_index - 1
        else:
            low_index = mid_index + 1

    return None


print(binary_search([1, 3, 5, 7, 9], 3))
print(binary_search([1, 3, 5, 7, 9], -1))
