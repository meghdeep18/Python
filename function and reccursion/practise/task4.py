def outerfunc(a,b):
    def innerfunc(a,b):
        return a+b

    inn = innerfunc(a,b)

    return inn + 5

result =  outerfunc(5,10)
print(result)