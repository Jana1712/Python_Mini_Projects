import random

def rps_game():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")
    print(f"Computer chose: {computer_choice}")


rps_game()



#OUTPUT

Choose rock, paper, or scissors: scissors
You lose!
Computer chose: rock

Choose rock, paper, or scissors: paper
You lose!
Computer chose: scissors

Choose rock, paper, or scissors: rock
You win!
Computer chose: scissors
