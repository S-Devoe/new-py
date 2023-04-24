import random

print("================================================================")
# get players choice 
def get_choice():
    player_choice =input('Enter a choice (rock, scissors, paper): ')
    options = ['paper', 'rock', 'scissors']
    computer_choice = random.choice(options)
    choices = {'player': player_choice, 'computer': computer_choice}
    return choices

# check for win or lose 
def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == 'scissors':
            return "Rock smashes scissors!, You win!" 
        else:
            return "Paper covers rock!, You lose."
    elif player == 'paper':
        if computer == 'rock':
            return "Paper covers rock!, You win!"
        else :
            return "Scissors destroys paper, You lose."
    elif player == "scissors":
        if computer == 'paper':
            return "Scissors destroys paper! You win!"
        else: 
            return "Rock smashes scissors! You lose."

start_game = get_choice()
result = check_win(start_game["player"], start_game["computer"])

print(result)
