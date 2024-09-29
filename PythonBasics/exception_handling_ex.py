num1 = input("enter number 1 - ")
num2 = input("enter number 2 - ")

def arthimetic_Except():
    try:
        res = int(num1) / int(num2)
        print(f"res is {int(res)}")
        if( int(res)*int(num2)==int(num1)):
            return {
                "status":"success"
                 }
    except ZeroDivisionError as zde:
        return {
            "status":"fail",
            "Reason":zde
        }
    except TypeError as e:
        print('Type error exception')
        res = None

print(arthimetic_Except())

