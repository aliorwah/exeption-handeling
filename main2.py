try:
    num1 = int(input("please enter a number:"))
    num2 = int(input("please enter a number:"))
    result= num1/num2
    print ("this is the result:", result)

except ZeroDivisionError:
    print("you cant divide by zero")

except ValueError as ex:
    print("please enter a valid number", ex)

except NameError as ex:
    print("name error", ex)

except:
    print("something went wrong")

finally:
    print("i will always excute")