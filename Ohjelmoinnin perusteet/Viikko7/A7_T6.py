# T6 - Rock Paper Scissors
# Video Thumbnail
# Click to play in YouTube

# Build “rock-paper-scissors” game in Python. In this game, there are two players, user and bot named “RPS-3PO”.

# Rules for the RPS game:

# Rock beats scissors
# Paper beats rock
# Scissors beat paper
# ASCII Art below for the game.

# Tab 1 Tab 2 Tab 3
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)

# In this exercise, place the following at the beginning of the code (right at the top). Setting the seed value means we are setting an initial state for the random number generator. After this, the generated numbers will follow exactly the same sequence. The random number will then depend on the number of calls to the random function.

# import random
# random.seed(1234)
# Randomize the bot’s choice in each game by calling the random.randint(1, 3) function with the given arguments. This function call returns a random integer between 1 and 3, inclusive. Implementing randomness in another way may lead to varying test results and is therefore not recommended.

# The program start by asking for the player’s name. Then, greet the player and announce the opponent. After that, inform that the game is starting.

# The menu contains 4 options, first three are game related options. If user chooses rock, paper or scissors from the menu, a round will be played.

# Display text "Rock! Paper! Scissors! Shoot!\n". Then, reveal the player’s choice first, followed by the bot’s choice. Show a decorative line of 25 hash (#) symbols between and around the choices to visually separate the player’s and the bot’s selections.

# Then check the players’ choice according to the rules of the RPS game. If both players have chosen the same option, the result is a draw ("Draw! Both players chose ____."). Otherwise, declare the winner and the reason for the victory based on the condition.

import random
random.seed(1234)

class RESULTS:
    win = 0
    lose = 0
    draw = 0

def RPS_display(Player: str,RPS: int) -> None:
    if RPS == 1:
        print("#"*25)
        print("{} chose rock.".format(Player))
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)""")
    elif RPS == 2:
        print("#"*25)
        print("{} chose paper.".format(Player))
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)""")
    elif RPS == 3:
        print("#"*25)
        print("{} chose scissors.".format(Player))
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)""")
    else:
        print('Error')

def menu() -> int:
    while True:
        print("\nOptions:\n1 - Rock\n2 - Paper\n3 - Scissors\n0 - Quit game")
        choice = input("Your choice: ")
        choice = choice.strip()
        if choice in ('1',"2","3","0"):
            break 
        else:
            print('\nInvalid choice\n')            
    return int(choice)

def RPS_game(Player: str,Opponent: str, Results: list[int]) -> None:
    player_result = RESULTS()
    player_result.win = 0
    player_result.lose = 0
    player_result.draw = 0
    opponent_result = RESULTS()
    opponent_result.win = 0
    opponent_result.lose = 0
    opponent_result.draw = 0
    RPS = [0,"rock","paper","scissors"]
    while True:
        choice = menu()
        opponent_choice = random.randint(1, 3)
        if choice == 0:
            Results.append(player_result)
            Results.append(opponent_result)
            break
        else :
            win_condition = {1:3,3:2,2:1}
            print("Rock! Paper! Scissors! Shoot!\n")
            RPS_display(Player,choice)
            print("")
            RPS_display(Opponent,opponent_choice)
            print("")
            print('#'*25)
            print("")
            if choice == opponent_choice :
                print('Draw! Both players chose {}.'.format(RPS[choice]))
                player_result.draw += 1
                opponent_result.draw += 1
            elif win_condition[choice] == opponent_choice:
                print('{} {} beats {} {}.'.format(Player,RPS[choice],Opponent, RPS[opponent_choice]))
                player_result.win += 1
                opponent_result.lose += 1
            else :
                print('{} {} beats {} {}.'.format(Opponent, RPS[opponent_choice],Player,RPS[choice]))
                player_result.lose += 1
                opponent_result.win += 1

def display_results(Player: str,Opponent: str,Results: list[int]) -> None :
    print("\nResults:")
    print(Player,'- wins ({}), loses({}), draws ({})'.format(Results[0].win,Results[0].lose,Results[0].draw))
    print(Opponent,'- wins ({}), loses({}), draws ({})'.format(Results[1].win,Results[1].lose,Results[1].draw))

def main():
    print("Program starting.")
    print("Welcome to the rock-paper-scissors game!")
    player = input("Insert players name: ")
    player = player.capitalize()
    print('Welcome {}!'.format(player))
    opponent = 'RPS-3PO'
    print('Your opponent is {}.'.format(opponent))
    results = []
    print('Game starts...')
    RPS_game(player,opponent,results)
    display_results(player,opponent,results)
    print("\nProgram ending.")
    
if __name__ == "__main__":
    main()