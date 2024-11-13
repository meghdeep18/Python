def list_statistics(numbers):
    if not numbers:
        return None  
    
    largest = max(numbers)
    smallest = min(numbers)
    total_sum = sum(numbers)
    
    return largest, smallest, total_sum

# Example usage:
numbers = [3, 1, 4, 1, 5, 9, 2]
largest, smallest, total_sum = list_statistics(numbers)
print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")
print(f"Sum of all numbers: {total_sum}")
