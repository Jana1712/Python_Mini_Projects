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
    
    
    

# output:

PS C:\Users\Janakiraman B\Downloads\Udemy Certificates\Projects\python mini projects> & "C:/Users/Janakiraman B/AppData/Local/Microsoft/WindowsApps/python3.13.exe" "c:/Users/Janakiraman B/Downloads/Udemy Certificates/Projects/python mini projects/numberguessinggame.py"
Welcome to the number guessing game!
I chosen a number between 1 and 100 . Can you guess it ?
Enter your guess number (or type 'quit' to exit): 45
Too high! Try again.
Enter your guess number (or type 'quit' to exit): 5
Too low! Try again.
Enter your guess number (or type 'quit' to exit): 20
Too high! Try again.
Enter your guess number (or type 'quit' to exit): 17
Too high! Try again.
Enter your guess number (or type 'quit' to exit): 14
Too low! Try again.
Enter your guess number (or type 'quit' to exit): 15
Too low! Try again.
Enter your guess number (or type 'quit' to exit): 16
Congralutions! you guessed the number in 7.


