import math
from statistic_functions import *
def zeroValue(x):
    if x==0:
        print("For this case it`s not possible to choose 0")
        return True
    return False
def chooseValue():
    x = input("Input value:\t")
    x = float(x)
    return x
def checkPerc():
    x = input("Input percentage between 0 and 100 without %:\t")
    x = float(x)
    if x<0 and x>100:
        print("Your value", x, "is not supported")
        return None
    return x


def calculator():
    vr=0
    op=input("Choose level of functions\n"
             "A  for advanced\n"
             "B  for basic ones\n")
    if op == "B":
        op = input("Choose operation \n"
                   "+   for addition\n"
                   "-   subtraction\n"
                   "*   for multiplication\n"
                   "/   for division\n"
                   "s   for square of number\n"
                   "r   for root of number\n"
                   "f   for factorial of number\n"
                   "S   for sine of the number\n"
                   "C   for cosine of the number\n"
                   "T   for tangent of the number\n")
        if op == "r":
            vr = chooseValue()
            vr = math.sqrt(vr)

        elif op == "s":
            vr = chooseValue()
            vr=str(vr)
            x = input("Choose power for your value " + vr + ":\t")
            x = float(x)
            vr=float(vr)
            vr = math.pow(vr, x)
        else:
            if op == "+":
                x = chooseValue()
                y = chooseValue()
                vr = x + y
            elif op == "*":
                x = chooseValue()
                y = chooseValue()
                vr = x * y
            elif op == "-":
                x = chooseValue()
                y = chooseValue()
                vr = x - y
            elif op == "/":
                x = chooseValue()
                y = chooseValue()
                if zeroValue(y)==True:
                    return None
                vr = x / y
            elif op == "f":
                x=chooseValue()
                x=round(x)
                vr=math.factorial(x)
            elif op == "S":
                x=chooseValue()
                vr=math.sin(x)
            elif op == "C":
                x=chooseValue()
                vr=math.cos(x)
            elif op == "T":
                x=chooseValue()
                vr=math.tan(x)
            else:
                print("Your value", op, "is not supported")
                return None
    elif op =="A":
        op=input("Choose operation\n"
            "% when you know two percentage values and return value for one of them\n"
            "!% when you know two return values and percentage for one of them\n")
        if op == "%":
            print("Enter percentage for which you know return value\n")
            x1=checkPerc()
            if zeroValue(x1)==True:
                return None
            print("Enter return value of percetage ",x1,"\n")
            y=chooseValue()
            print("Enter percentage for which you don`t know return value\n")
            x2=checkPerc()
            vr = (x2*y) / x1
        elif op=="!%":
            print("Enter percentage for which you know return value\n")
            x = checkPerc()
            print("Enter return value of percetage ", x,"\n")
            y1 = chooseValue()
            if zeroValue(y1)==True:
                return None
            print("Enter return value for percetage you don`t know\n")
            y2 = chooseValue()
            vr=(x*y2)/y1
            if vr>100:
                print("Percentages cannot be greater than 100%")
                return None
            vr=str(vr)
            vr=vr+"%"
        else:
            print("Your value",op,"is not supported")
            return None
    else:
        print("Your value",op,"is not supported")
        return None

    return vr
print(calculator())
