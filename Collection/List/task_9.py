def have_one_common(list1,list2):
    for items in list1: 
        if items in list2:
            return True
        return False

list1 = [1,2,3]
list2 = [2,3,4]

print(have_one_common(list1,list2))