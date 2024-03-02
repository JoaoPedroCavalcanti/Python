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

print("Welcome to the rock, papper, scissors game! ")
index_input = int(input("To play, type 0 to Rock, 1 to Papper and 2 to Scissors: "))
random_input = random.randint(0,2)
print("You: ")
print(game_images[index_input])
print("The computer: ")
print(game_images[random_input])

is_you_winner = True
is_draw = False

if index_input == random_input:
    is_draw = True
    
elif index_input == 0 and random_input == 1:
    is_you_winner = False
elif index_input == 1 and random_input == 2:
    is_you_winner = False
elif index_input == 2 and random_input == 0:
    is_you_winner = False

if is_draw == True:
    print("It's a draw! ")
elif is_you_winner == True:
    print("You're the winner!")
else:
    print("You're the Loser!")