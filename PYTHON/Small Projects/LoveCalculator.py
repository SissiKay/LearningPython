# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
together_name=name1+name2

together_name=together_name.lower()


#TRUE
t=together_name.count("t")
r=together_name.count("r")
u=together_name.count("u")
e=together_name.count("e")

true= str(t+r+u+e)

#LOVE
l=together_name.count("l")
o=together_name.count("o")
v=together_name.count("v")
e=together_name.count("e")

love= str(l+o+v+e)

love_score= int(true+love)

if (love_score<10) or (love_score> 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40<(love_score<50) :
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
