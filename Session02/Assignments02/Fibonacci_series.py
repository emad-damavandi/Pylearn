while True:
    print("Enter number:")
    number = int(input())
    if number <= 0:
        print("please enter a positive number!")
    else:
        a = 0
        b = 1
        i = 0
        print(a , end=" , ")
        print(b , end=" , ")
        while i < number - 2:
            next_number = a+b
            print(next_number , end = " , ")
            a = b
            b = next_number
            i += 1
        break # this break to check while is a positive number