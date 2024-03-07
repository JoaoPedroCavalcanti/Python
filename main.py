import random
from hangman_art import stages, logo
from hangman_words import word_list


#Chose a random word in the word_list
word_choosen = random.choice(word_list)
#initialize two lists
display_list = []
guess_list = []

#Put a "_" on each lettler of the choosen word
for lettler in word_choosen:
    display_list.append("_")
    
print(logo)
print("Welcome to the Hangmans Game!")
print("You have 6 lifes")
print("Your Word is:\n")
print(f"{display_list} \n", stages[6])

life = 6
blank_spaces = len(word_choosen)
counter_aux = blank_spaces

while blank_spaces > 0:
    
    #Get a lettler
    guess = input("Guess a lettler: ").lower()
    #Check if the lettler has already been used
    while guess in guess_list:
        print("You already choose this lettler, try another one.")
        guess = input("Guess a lettler: ").lower()
    #Add the lettler to the list of lettler that had been used
    guess_list.append(guess)
    
    #Will check if the lettler given exists in the word.
    #If exists, will put this lettler in the respective space in the display_list
    index = -1
    for lettler in word_choosen:
        index += 1
        
        if guess == lettler:
            display_list[index] = guess
            blank_spaces -= 1 
    
    #check if the blank_spaces got decresed(If not got decresed, it means
    # the user didn't get the right lettler)    
    if blank_spaces == counter_aux:
        life -= 1
        print(f"You have {life} lifes")
    else:
        counter_aux -= 1
        
    print(f"\n{display_list}\n", stages[life])
    
    #If the life is less than 0, you lost
    if not life > 0:
        print("You lost!")
        print(f"The word was: {word_choosen}")
        break
#If there isn't any "_" on the display_list, means you win
if not "_" in display_list:
    print("You win!")
            
