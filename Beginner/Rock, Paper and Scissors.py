import random

while True:
    user_input = input("Choose Your Option (Rock / Paper / Scissors) or 'quit' to exit: ").lower()
    
    if user_input == "quit":
        print("Thanks for playing!")
        break
    
    if user_input not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please choose Rock, Paper, or Scissors.")
        continue
    
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {computer_choice}")
    
    if user_input == computer_choice:
        print("It's a tie!")
    elif (user_input == "rock" and computer_choice == "scissors") or \
         (user_input == "paper" and computer_choice == "rock") or \
         (user_input == "scissors" and computer_choice == "paper"):
        print(f"You win! {user_input.title()} beats {computer_choice.title()}.")
    else:
        print(f"You lose! {computer_choice.title()} beats {user_input.title()}.")
    
    print()