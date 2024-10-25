def count_occurrences(input_string):
    occurrences = {}
    for char in input_string:

        if char in occurrences:
            occurrences[char] += 1  # Increment the count
        else:
            occurrences[char] = 1  # Set initial count to 1
    return occurrences

text = input("please enter any sentence :")
occurrences = count_occurrences(text)
print(occurrences)  
 
 