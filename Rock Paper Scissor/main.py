import random
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
#Putting the selection in a list
selection = [rock, paper, scissors]
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
computer_choice = random.randint(0,2)
#Check if user inputs anything other from the selection option. 0,1 or 2.
#Loose if user enters > 2
if user_input >= 3 or user_input < 0:
  print("You entered invalid number. You lost!")
else:
  print(f"You chose: {selection[user_input]}")
  print(f"Computer chose: {selection[computer_choice]}")
  if user_input == computer_choice:
    print("It's draw!")
  if user_input== 0 and computer_choice==2:
    print("You Won!")
  elif user_input ==2 and computer_choice == 0:
    print("You lost!")
  elif user_input < computer_choice:
    print("You Lost!")
  elif user_input > computer_choice:
    print("You Won!")