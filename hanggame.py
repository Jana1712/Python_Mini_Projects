import random

def hangman():
    words = ['python', 'java', 'swift', 'javascript']
    word = random.choice(words)
    guessed = "_" * len(word)
    word = list(word)
    guessed = list(guessed)
    attempts = 6
    guessed_letters = []

    while attempts > 0:
        print(' '.join(guessed))
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
            if "_" not in guessed:
                print("Congratulations! You won!")
                break
        else:
            attempts -= 1
            print(f"Wrong guess. You have {attempts} attempts left.")
        guessed_letters.append(guess)

    if attempts == 0:
        print(f"You lost! The word was {''.join(word)}.")

hangman()