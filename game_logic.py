
def game_logic(player_pick, computer_choice):
    """Output winner given the player and computer choice. """
    
    if player_pick == computer_choice:
        print(f"You picked: {player_pick}")
        print(f"Computer picked: {computer_choice}")
        print("It's a tie!\n")
        return "It's a tie"

    elif player_pick == "Rock" and computer_choice == "Scissor":
        print(f"You picked: {player_pick}")
        print(f"Computer picked: {computer_choice}")
        print("You Won!")
        return "You Won!"

    elif player_pick == "Paper" and computer_choice == "Rock":
        print(f"You picked: {player_pick}")
        print(f"Computer picked: {computer_choice}")
        print("You Won!")
        return "You Won!"

    elif player_pick == "Scissor" and computer_choice == "Paper":
        print(f"You picked: {player_pick}")
        print(f"Computer picked: {computer_choice}")
        print("You Won!")
        return "You Won!"

    elif player_pick == "Paper" and computer_choice == "Scissor":
        print(f"You picked: {player_pick}")
        print(f"Computer picked: {computer_choice}")
        print("Computer Won!")
        return "Computer Won!"

    elif player_pick == "Rock" and computer_choice == "Paper":
        print(f"You picked: {player_pick}")
        print(f"Computer picked: {computer_choice}")
        print("Computer Won!")
        return "Computer Won!"

    elif player_pick == "Scissor" and computer_choice == "Rock":
        print(f"You picked: {player_pick}")
        print(f"Computer picked: {computer_choice}")
        print("Computer Won!")
        return "Computer Won!"
