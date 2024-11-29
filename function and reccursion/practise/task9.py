# menu driven program
while True:
    print("1.addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division")
    print("5 exit")
    choice = int(input("please enter your choice"))

    num1 = int(input("please enter any 1 number"))
    num2 = int(input("please enter 2 number"))

    if choice == 1:
        print("addition",num1+num2)
    elif choice == 2:
        print("subtraction",num1-num2)
    elif choice ==  3 :
        print("multiplication",num1*num2)
    elif choice == 4:
        print("division",num1/num2) 
    elif choice == 5:
        break
    else:
        print("invalid choice")
        break

        if choice == 5:
            break
        

