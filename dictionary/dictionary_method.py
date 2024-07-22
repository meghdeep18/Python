mydict = {
            "name" : "meghdeep",
            "role" : "developer",
            "marks": [15,20,25,30]
}

print(mydict.keys()) # prints the keys of the dictionary 
print(mydict.values()) # prints the values of the dictionary 
print(mydict.items())#prints out the pairs of key and value in a form of tuple 
updated_dic = {
    "friend":"abhishek"
}
mydict.update(updated_dic)# adds the key and value to the dict
print(mydict)
