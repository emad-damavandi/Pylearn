a = float(input())
b = float(input())
c = float(input())

if a + b > c and b + c > a and c + a > b:
    print("Yes it is possible")
else:
    print("No")