# Write a Python program to find the second smallest number in a list
def list_statistics(numbers):
    if not numbers:
        return None  
        
    smallest = min(numbers)

    return  smallest


numbers = [3, 1, 4, 1, 5, 9, 2]
smallest = list_statistics(numbers)
print(f"Smallest number: {smallest}")

