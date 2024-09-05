def get_unique_elements(input_list):
    # Using a set to store unique elements
    unique_elements = list(set(input_list))
    return unique_elements

# Example usage
original_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = get_unique_elements(original_list)
print(unique_list)  # Output: [1, 2, 3, 4, 5]