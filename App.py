import random

print("***** WELCOME AND GOOD LUCK *****")

options = ["Rock", "Paper", "Scissor"]


print("1) Rock")
print("2) Papper")
print("3) Scissor \n")

computer_choice = random.choice(options)

player_choice = int(input("Please enter the number of your choice: "))

player_pick = options[player_choice - 1]

# print(player_pick)
# print(computer_choice)

if player_pick == computer_choice:
    print(f"You picked: {player_pick}")
    print(f"Computer picked: {computer_choice}")
    print("It's a tie!\n")
elif player_pick == "Rock" and computer_choice == "Scissor":
    print(f"You picked: {player_pick}")
    print(f"Computer picked: {computer_choice}")
    print("You Won!")
elif player_pick == "Paper" and computer_choice == "Rock":
    print(f"You picked: {player_pick}")
    print(f"Computer picked: {computer_choice}")
    print("You Won!")
elif player_pick == "Scissor" and computer_choice == "Paper":
    print(f"You picked: {player_pick}")
    print(f"Computer picked: {computer_choice}")
    print("You Won!")
elif player_pick == "Paper" and computer_choice == "Scissor":
    print(f"You picked: {player_pick}")
    print(f"Computer picked: {computer_choice}")
    print("Computer Won!")
elif player_pick == "Rock" and computer_choice == "Paper":
    print(f"You picked: {player_pick}")
    print(f"Computer picked: {computer_choice}")
    print("Computer Won!")
elif player_pick == "Scissor" and computer_choice == "Rock":
    print(f"You picked: {player_pick}")
    print(f"Computer picked: {computer_choice}")
    print("Computer Won!")




