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
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
if choice == 0:
  print(rock)
elif choice == 1:
  print(paper)
else:
  print(scissors)
print("computer_chose: ")
computer_chose = random.randint(0,2)
print(computer_chose)
if computer_chose == 0:
  print(rock)
elif computer_chose == 1:
  print(paper)
else:
  print(scissors)

if choice == 0 and computer_chose == 0 or choice == 1 and computer_chose == 1 or choice == 2 and computer_chose == 2:
  print("Draw match. Try again! ")
elif choice == 0 and computer_chose == 1 or  choice == 1 and computer_chose == 2 or choice == 2 and computer_chose == 0:
  print("You lose! ")
else:
  print("You win! ")