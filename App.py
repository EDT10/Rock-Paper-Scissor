import random
from game_logic import game_logic

print("***** WELCOME AND GOOD LUCK *****")

options = ["Rock", "Paper", "Scissor"]


""" print("1) Rock")
print("2) Papper")
print("3) Scissor \n")

computer_choice = random.choice(options)

player_choice = int(input("Please enter the number of your choice: "))

player_pick = options[player_choice - 1] """

# print(player_pick)
# print(computer_choice)

round = 0
p_points = 0
c_points = 0

while round in range(0,3):
        round = round + 1
        print("Round:", round,"\n")
        print("1) Rock")
        print("2) Papper")
        print("3) Scissor \n")
        computer_choice = random.choice(options)

        player_choice = int(input("Please enter the number of your choice: "))

        player_pick = options[player_choice - 1]

        game_logic(player_pick, computer_choice)

        if game_logic(player_pick, computer_choice) == "It's a tie":
            p_points += 1
            c_points += 1
            print("player:",p_points,"computer:", c_points)
        elif game_logic(player_pick, computer_choice) == "You Won!":
            p_points += 1
            print("player:",p_points,)
        elif game_logic(player_pick, computer_choice) == "Computer Won!":
            c_points += 1 
            print("computer:", c_points)


        if round == 3:
            print("The End, Thanks for playing")
            play_again = input("Do you want to play again? ").lower()

            if play_again == "no":
                print("Thanks for playing, Goodbye")
                quit()
            elif play_again == "yes":
                rounds = 0
                continue




