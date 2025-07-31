import random

# Generate a random number between 1 and 100;

secret_num = random.randint(1,100)
print("Welcome to the number guessing game!")
print("I chosen a number between 1 and 100 . Can you guess it ?")


attempts = 0

while True:
    guess = input("Enter your guess number (or type 'quit' to exit): ")
    if guess.lower() == 'quit':
        print(f"You gave up! The secret number was {secret_num}")
        break
    try:
        guess = int(guess)
    except ValueError:
        print('Please enter a valid number: ')
        continue
    
    attempts += 1
    
    
    
    if guess == secret_num:
        print(f"Congralutions! you guessed the number in {attempts}.")
        break
    elif guess < secret_num :
        print('Too low! Try again.')
      
    else:
        print('Too high! Try again.')    
    
    
    
    