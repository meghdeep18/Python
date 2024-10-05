import random

def game():
    choices = ["stone", "paper", "scissors"]
    
    while True:
        computer_choice = random.choice(choices)

        # Get user's choice and validate
        user_choice = input("Enter your choice (stone, paper, scissors) or 'exit' to quit: ").lower()
        if user_choice == 'exit':
            print("Thank you for playing! Exiting the game.")
            break
        while user_choice not in choices:
            print("Invalid input, please try again.")
            user_choice = input("Enter your choice (stone, paper, scissors): ").lower()
        
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        # Determine the result
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "stone" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "stone") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("Congratulations, you win!")
        else:
            print("Sorry, you lose. Better luck next time!")
        
        print()  # Blank line for separation between rounds

# Start the game
game()
