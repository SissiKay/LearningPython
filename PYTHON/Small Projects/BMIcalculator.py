# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI= round(weight/(height**2))


if BMI < 18.5:
    print ("underweight")
elif 18.5<BMI<25:
    print ("normal weight")
elif 25<BMI<30:
    print("ouff slightly overweight")
elif 30<BMI<35:
    print("obese")
else :
    print("fat piece of shit")