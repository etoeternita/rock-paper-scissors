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

game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print("Your Chose:")

if user_choice >= 3 or user_choice < 0:
  print("You typed an invalid number, you lose!")

else:
  comchose = random.randint(0,2)
  print(game_images[user_choice])
  print("Computer Chose:")
  print(game_images[comchose])

  if user_choice == 0 and comchose == 2:
     print("You win!")

  elif comchose == 0 and user_choice == 2:
    print("You lose")

  elif comchose > user_choice:
    print("You lose")

  elif user_choice > comchose:
    print("You win!")

  elif comchose == user_choice:
    print("It's a draw")

  elif user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
