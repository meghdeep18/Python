# User efine function are the kind of funtion which are created by the user 
# some example of user deined function are down below
def mySum(num1, num2):
    return num1 + num2
# s = mySum(5,55)
# print(s) #other method

print("Enter two numbers:")
x = int(input())
y = int(input())

result = mySum(x, y)
print("The sum is : ", result)

# In above code we have defined a new function named "mySum" which takes two arguments and returns their sum. Then we called this function with two number entered by the user and print