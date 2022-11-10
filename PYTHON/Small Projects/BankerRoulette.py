# Import the random module here
import random 
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

x= len(names)
print(x)

payee=random.randint(0,x)

chosen_one= names[payee]

print(f"{chosen_one} is going to buy the meal today!")