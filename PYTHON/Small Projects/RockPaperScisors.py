from random import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

choices=[rock,paper,scissors]

#user
print(f"{rock}\n{paper}\n{scissors}")
user=int(input("Chose your weapon: type 0 for rock, 1 for paper or 2 for scissors?\n"))


if user >= 3 or user < 0: 
    
    print("You typed an invalid number, you lose!") 
    

else:
    user_image= choices[user]
    print(user_image)
    #computers random answer
    computer= random.randint(0,2)
    print(f"Computer chose:\n{computer}")
    computer_image= choices[computer]
    print(computer_image)

    #then we compare

    if user == 0 and computer == 2:
        print("You win!")
    elif computer == 0 and user == 2:
        print("You lose")
    elif computer > user:
        print("You lose")
    elif user > computer:
        print("You win!")
    elif computer == user:
        print("It's a draw")
