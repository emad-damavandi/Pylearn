print("Enter second:")
input_second = int(input())

hour = input_second // 3600
minute = input_second % 3600 // 60
second = input_second % 60

print(str(hour).zfill(2),":",str(minute).zfill(2),":",str(second).zfill(2))