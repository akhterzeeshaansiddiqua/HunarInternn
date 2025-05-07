import random
def get_computer_choice():
    options = ['rock', 'paper', 'scissors']
    return random.choice(options)
def get_user_choice():
    choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Try again.")
        choice = input("Enter your choice (rock, paper, scissors): ").lower()
    return choice
def determine_winner(user, computer):
    print(f"You chose: {user}")
    print(f"Computer chose: {computer}")
    
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "You win!"
    else:
        return "You lose!"
def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    print(result)
play_game()
