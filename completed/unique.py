def get_unique_elements(input_list):

    unique = list(set(input_list))

    return unique

li = [1,2,3,1,2]
unique_list = get_unique_elements(li)
print(unique_list)  