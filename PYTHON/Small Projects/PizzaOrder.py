# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆
bill= 0
#Write your code below this line 👇
if size=="S":
    bill+=15
elif size=="M":
    bill+=20
elif size=="L":
    bill+=25
else:
    print("Please respect the format of the letters i am asking you to input")

if add_pepperoni =="Y":
    if size=="S":
        bill+=2
    else:
        bill+= 3
if extra_cheese =="Y":
    bill+=1

print(f"Your final bill is: {bill}")