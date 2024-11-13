def convertTuple(tup):
       
    str = ''
    for item in tup:
        str = str + item
    return str

tuple = ('m', 'e', 'g', 'h','d','e','e','p')
str = convertTuple(tuple)
print(str)