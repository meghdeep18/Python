import random

def game():
        choices = ["stone", "paper", "scissors"]
        computer_choice = random.choice(choices)

        user_choice = input("Enter your choice (stone, paper, scissors): ")
        while user_choice not in choices:
            print("Invalid input, please try again.")
            user_choice = input("Enter your choice (stone, paper, scissors): ")

        print("Computer chose: ", computer_choice)

        if user_choice == computer_choice:
            return "It's a tie!"
        elif user_choice == "stone" and computer_choice == "scissors":
            return "Congratulations, you win!"
        elif user_choice == "paper" and computer_choice == "stone":
            return "Congratulations, you win!"
        elif user_choice == "scissors" and computer_choice == "paper":
            return "Congratulations, you win!"
        else:
            return "Sorry, you lose. Better luck next time!"

print(game())