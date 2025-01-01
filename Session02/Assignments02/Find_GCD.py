a = int(input())
b = int(input())

gcd = 1

for i in range(1,a+1):
    if a % i == 0 and b % i == 0:
        gcd = i
print(gcd)