n = int(input("Enter number to print pattern :"))
for i in range(1, n+1):
    # internal loop run for i times
    for k in range(1, i+1):
        print("*", end="")
    print()
