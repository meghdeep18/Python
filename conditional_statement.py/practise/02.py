sub1 = int(input("enter marks 1 :"))
sub2= int(input("enter  marks 2 :"))
sub3 = int(input("enter marks 3 "))

if(sub1<33 or sub2<33 or sub3<33):
     print("you are failed due to your marks ar lesser then 33")

elif(sub1<33 + sub2<33 + sub3<33)/3 <40:
    print("you have failed due to less total percentage then 40")

else:
    print("congratulations u have passes")
