import random
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]

def main():
    wrd_selected = random.choice(words)
    tries = 6
    print("Welcome to Hangman!")
    game(wrd_selected, tries)

def game(word, tries):
    print("Guess the word before the hangman is complete!")
    guessed_letters = []
    word_completion = " _ " * len(word)
    while tries > 0 and "_" in word_completion:
        print(display_hangman(tries))
        print(word_completion)
        guess = input("Please enter a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
        guessed_letters.append(guess)
        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
            word_completion = ''.join([letter if letter in guessed_letters else ' _ ' for letter in word])
        else:
            tries -= 1
            print(f"Sorry, '{guess}' is not in the word. You have {tries} tries left.")
        print(display_hangman(tries))
        print(word_completion)
    if "_" not in word_completion:
        print("Congratulations! You've guessed the word!")
    else:
        print(f"Game over! The word was '{word}'.")

def display_hangman(tries):
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      
           |      
           |      
           |     
           -
        """
    ]
    return stages[tries]
while True:
    w = input("Do you want to play Hangman? (y/n): ")
    if w in ['y', 'Y']:
        main()
    else:
        print("Thank you for playing Hangman. Goodbye!")
        break