import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "user"
    else:
        return "computer"

def display_result(user_choice, computer_choice, winner):
    print(f"\nUser choice: {user_choice}")
    print(f"Computer choice: {computer_choice}")
    
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
    else:
        print("Computer wins!")

def main():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock-Paper-Scissors Game!")
    
    while True:
        print("\nPlease choose:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        user_choice = input("Enter your choice (1/2/3): ").strip()
        
        if user_choice not in ['1', '2', '3']:
            print("Invalid choice, please try again.")
            continue
        
        choices = {'1': 'rock', '2': 'paper', '3': 'scissors'}
        user_choice = choices[user_choice]
        
        computer_choice = get_computer_choice()
        winner = get_winner(user_choice, computer_choice)
        
        display_result(user_choice, computer_choice, winner)
        
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1
        
        print(f"\nScores:")
        print(f"User: {user_score}")
        print(f"Computer: {computer_score}")
        
        play_again = input("\nDo you want to play another round? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break

    print("\nThank you for playing! Goodbye.")

if __name__ == "__main__":
    main()
