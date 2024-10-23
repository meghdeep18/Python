def add(num):
    if num:
        return num + add(num-1)
    else:
        return 0

res = add(20)
print(res)