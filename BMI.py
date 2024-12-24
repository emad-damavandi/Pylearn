weight = float(input())
height_cm = float(input())

height_m = height_cm / 100

bmi = weight / (height_m ** 2)

print("BMI:",bmi)

if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 25:
    print("Normal Weight")
elif 25 <= bmi < 30:
    print("Overweight")
elif 30 <= bmi < 35:
    print("Obesity")
elif 35 <= bmi < 39.9:
    print("Extreme Obesity")
else:
    print("Super Obesity!")