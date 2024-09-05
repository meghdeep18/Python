def common_data(list1, list2):
    for x in list1:
        for y in list2:
            if x == y:
                return True
    return False

# Example usage:
a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
print(common_data(a, b))  # Output: True

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9]
print(common_data(a, b))  # Output: False
