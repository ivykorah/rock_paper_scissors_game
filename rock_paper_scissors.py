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


game_images = [rock, paper, scissors]

print("Welcome to the rock, paper, scissors game!\n\n")


my_choice = int(input("Rock, paper, scissors.\nWhat do you choose?\nType 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if my_choice >= 3 or my_choice < 0:
  print("Invalid entry, You lose.\nPlease select enter 0, 1 or 2")
else:
  print(f"You chose {my_choice}")
  print(game_images[my_choice])

  computer_choice = random.randint(0, 2)
  print(f"Computer chose: {computer_choice}")
  print(game_images[computer_choice])


  if (my_choice >= 3) or (my_choice) < 0:
    print("Invalid entry, You lose.\nPlease select enter 0, 1 or 2")
  elif my_choice == 0 and computer_choice == 2:
    print("You win!")
  elif my_choice < computer_choice:
    print("You lose, oomputer wins!")
  elif my_choice == computer_choice:
    print("Draw! Nobody wins.")
  elif my_choice == 2 and computer_choice == 0:
    print("You lose! Computer wins.")
  elif my_choice > computer_choice:
    print("You win!")
