import random

def hangman():
    # List of words to choose from
    word_list = ["python", "programming", "hangman", "challenge", "algorithm"]
    
    # Randomly select a word
    selected_word = random.choice(word_list)
    
    # Initialize variables
    guessed_word = ["_" for _ in selected_word]  # Placeholder for the word
    guessed_letters = set()  # Set of guessed letters
    attempts_remaining = 6  # Maximum number of incorrect guesses

    print("Welcome to Hangman!")
    print("You have to guess the word one letter at a time.")

    # Main game loop
    while attempts_remaining > 0 and "_" in guessed_word:
        print("\n" + " ".join(guessed_word))
        print(f"Attempts remaining: {attempts_remaining}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")

        guess = input("Guess a letter: ").lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please guess a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        # Add the guess to the set of guessed letters
        guessed_letters.add(guess)

        # Check if the guessed letter is in the word
        if guess in selected_word:
            print(f"Good guess! '{guess}' is in the word.")
            for i, letter in enumerate(selected_word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            print(f"Wrong guess. '{guess}' is not in the word.")
            attempts_remaining -= 1

    # End of game
    if "_" not in guessed_word:
        print("\nCongratulations! You guessed the word:", "".join(guessed_word))
    else:
        print("\nGame over! The word was:", selected_word)

# Run the game
if __name__ == "__main__":
    hangman()
