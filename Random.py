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

import random

Choice=input("Type Rock, Paper or Scissors\n")

Computer_choice=random.randint(0,2)

print("Your choice:")

if(Choice=="Rock"):
    print(rock)
if(Choice=="Paper"):
    print(paper)
if(Choice=="Scissors"):
    print(scissors)

print("Computer choice:")

if(Computer_choice==0):
    print(rock)
if(Computer_choice==1):
    print(paper)
if(Computer_choice==2):
    print(scissors)

if(Choice=="Rock" and Computer_choice==0) or (Choice=="Paper" and Computer_choice ==1) or (Choice=="Scissors" and Computer_choice==2):
    print("Draw")
if(Choice=="Rock" and Computer_choice==1) or (Choice=="Paper" and Computer_choice==2) or(Choice=="Scissors" and Computer_choice==0):
    print("You lose")
if(Choice=="Rock" and Computer_choice==2) or (Choice=="Paper" and Computer_choice==0) or(Choice=="Scissors" and Computer_choice==1):
    print("You win")