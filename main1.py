try:
    num = int(input("please enter a number:"))
    print (num)
    
except ValueError as ex:
    print("exeption:", ex)

    print("enter a valid number")
    