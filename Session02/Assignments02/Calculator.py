import math

while True:
    print("Select the calculator operation:")
    operator = input()


    if operator == "+":
        a = int(input())
        b = int(input())
        result = a + b
    elif operator == "-":
        a = int(input())
        b = int(input())
        result = a - b
    elif operator == "*":
        a = int(input())
        b = int(input())
        result = a * b
    elif operator == "/":
        a = int(input())
        b = int(input())
        if b != 0:
            result = a / b
        else:
            result = "You can not divide by zero!"
    elif operator == "^":
        a = int(input())
        b = int(input())
        # result = a ** b
        result = math.pow(a,b)
    elif operator == "kmm":
        a = int(input())
        b = int(input())
        result = math.lcm(a,b)
    elif operator == "sin":
        a = int(input())
        radian = a * math.pi / 180
        result = math.sin(radian)
        
    elif operator == "cos":
        a = int(input())
        radian = a * math.pi / 180
        result = math.cos(radian)

    elif operator == "tan":
        a = int(input())
        radian = a * math.pi / 180
        result = math.tan(radian)

    elif operator == "cot":
        a = int(input())
        radian = a * math.pi / 180
        result = math.cos(radian) / math.sin(radian)

    elif operator == "sqrt":
        a = int(input())
        b = int(input())
        result = a ** ( 1 / b )
    elif operator == "factorial":
        a = int(input())
        result = math.factorial(a)
    elif operator == "exit":
        break
    else:
        result = "This operator not supported!"


    print(result)