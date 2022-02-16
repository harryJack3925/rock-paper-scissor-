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

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print("Your Choice:")
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer Choice:")
print(game_images[computer_choice])

def if_win(computer, user):
    if user >= 3 or user < 0: 
        print("You typed an invalid number, you lose!")
    elif user == 0 and computer == 2: 
        print("You win!")
    elif computer == 0 and user == 2:
        print("You lose")
    elif computer > user:
        print("You lose")
    elif user > computer:
        print("You Won!")
    elif computer == user:
        print("It's a draw")

if_win(computer_choice, user_choice)

  


