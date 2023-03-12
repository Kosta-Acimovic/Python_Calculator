import math

pi = math.pi


def chooseValue():
    x = input("Input value:\t")
    x1 = x.isdigit()
    if not x1:
        while not x1:
            print("You entered a wrong value, please try again\n")
            x = input("Input value:\t")
            x1 = x.isdigit()
    x = float(x)
    return x


def circle_area():
    r = chooseValue()
    vr = 2 * r * pi
    return vr


def square_area():
    r = chooseValue()
    vr = float(r)
    vr = math.pow(vr, 2)
    return vr


def rectangle_area():
    a = chooseValue()
    b = chooseValue()
    a = float(a)
    b = float(b)
    vr = a * b
    return vr


def right_triangle_area():
    op = input("Firstly you need to choose how you will find this area, options are\n"
               "Enter   1   if you have two sides of triangle (not hypotenuse)\n"
               "Enter   2   if you have hypotenuse and height\n")
    if op == "1":
        print("FIRST SIDE\n")
        a = chooseValue()
        a = float(a)
        print("SECOND SIDE\n")
        b = chooseValue()
        b = float(b)
        vr = (a * b) / 2
        return vr
    elif op == "2":
        print("HYPOTENUSE\n")
        c = chooseValue()
        c = float(c)
        print("HEIGHT")
        hc = chooseValue()
        hc = float(hc)
        vr = (c * hc) / 2
        return vr
