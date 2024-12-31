import random

# Function to get the computer's choice
def get_computer_choice():
    """Returns a random choice from rock, paper, or scissors for the computer."""
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

# Function to determine the winner of the game
def determine_winner(user_choice, computer_choice):
    """Compares user and computer choices and returns the result."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

# Function to display the score
def display_score(user_score, computer_score):
    """Displays the current score of the game."""
    print(f"Score: You - {user_score}, Computer - {computer_score}")

# Main game loop
def play_game():
    """The main function that runs the Rock-Paper-Scissors game."""
    user_score = 0
    computer_score = 0

    while True:
        # User input
        print("\nWelcome to Rock-Paper-Scissors!")
        print("Choose: rock, paper, or scissors")
        user_choice = input("Your choice: ").lower()

        # Validate user input
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        # Computer makes a choice
        computer_choice = get_computer_choice()

        # Show choices
        print(f"Computer's choice: {computer_choice}")

        # Determine and display the result of the game
        result = determine_winner(user_choice, computer_choice)
        print(result)

        # Update scores based on the result
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        # Display the current score
        display_score(user_score, computer_score)

        # Ask user if they want to play again
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            print("Thanks for playing!")
            break

# Run the game
if __name__ == "__main__":
    play_game()
