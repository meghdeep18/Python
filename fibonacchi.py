def fibonacci_series(n):
    fib_series = []
    a, b = 0, 1
    for i in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

# Taking user input for the range
range_limit = int(input("Enter the range for the Fibonacci series: "))

# Generating the Fibonacci series within the given range
fibonacci_result = fibonacci_series(range_limit)

print(f"Fibonacci series within the range of {range_limit}:")
print(fibonacci_result)

    
   
