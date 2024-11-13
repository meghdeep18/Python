# How will you remove last object from a list?
# Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]?

l1 = [2,33,222,14,25]
print(l1[-1]) #prints  the last index of the list 

l1.pop()
print(l1)  #pop removes the last character in list by default if u dont give index 