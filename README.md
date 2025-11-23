# Project Title: HANGMAN

This is the famous Hnagman game where one has to guess the letters of a word. If a player guesses an incorrect letter a small section of the Hangman appears, else nothing happens. If a player is able to guess the word before the completion of the Hangman, he/she wins else the player loses the game on completion of the Hangman.


## Overview of the project

*   The program is a game called Hangman.
*   The project will help students relieve stress and enjoy while at the same time learn new words and brainstorm to win the game.
*   I have used Python programming language and it's basic functions to create this game.
*   I encountered a problem while trying to put the correctly guessed alphabets in their right places because a correctly guesserd letter can occur more than        once in a word and therefore identifying them and putting '_' on the rest of the missing letters was a problem that I encountered and overcame.


## Table of Contents
*   [Features](#features)
*   [Technologies/Tools Used](#technologies)
*   [Steps to install & run the project](#steps)
*   [Instructions for testing](#instructions)
*   [License](#license)


## Features

*   Random Word Selection:

     The game program randomly chooses a secret word from a predefined list or text file of words. The random module in Python is commonly used for this function.

*   Limited Guesses (Lives):

     The player is given a fixed, limited number of incorrect guesses before losing the game. Each wrong guess results in the loss of a life/attempt.

*   Progressive Visual Feedback:

     A visual representation (often ASCII art in a console-based game, or a simple graphic in a GUI version) of the "hangman" is progressively displayed as the player makes incorrect guesses.

*   Word Display with Placeholders:

     The secret word is displayed as a series of underscores or blanks, with correct letters filled in as they are guessed. This shows the player the length of the word and their progress.

*   User Input and Validation:

     The game prompts the user to input a single letter per turn. The input is validated to ensure it is a single alphabetical character and has not been guessed previously.

*   Tracking Guessed Letters:

     The game keeps track of all letters that have been guessed, both correct and incorrect, and often displays them to the player to prevent repetition.

*   Win/Loss Conditions:

     The game loop ends when one of two conditions is met:
      *   __Win:__ The player correctly guesses all the letters in the word before running out of lives.
      *   __Loss:__ The player runs out of lives before the word is fully guessed, and the full hangman figure is drawn.

*   Game Loop and Replayability:

The features are wrapped in a game loop that continues until the game ends, after which the player is typically given the option to play again or exit. 


## Technologies/Tools Used

**Core Technologies and Tools (Text-Based)**

For a basic command-line/terminal Hangman game, the core Python language and its standard library modules are sufficient. 

*   Python Programming Language:

     The foundation for the game's logic, control flow (loops, conditional statements), and data manipulation (strings, lists, sets).

*   Built-in Functions:

     *   __input():__ To get the player's letter guesses from the command line.
     *   __print():__ To display the game's progress, the hangman (using ASCII art), the hidden word (using underscores), and game messages.

*   Standard Library Modules:

      *   __random:__ Specifically the random.choice(words) function, is used to select a word randomly from a predefined list of words called _words_.
      *   __string:__ The string.ascii_lowercase or string.ascii_uppercase objects can be used for input validation to ensure the player enters a valid                    letter.

*   Data Structures:

      *   String list to store the words.
      *   List to efficiently track letters that have already been guessed.

## Steps to install & run the project

*   To Install the code on your personal computer please download the files from github.
*   Open the file on your desired IDE.
*   Please ensure you have Python installed on your personal computer.
*   Run the following command to run the program.
     *     python hangman_main.py
*   Enter *y* to start the program else enter *n*.
*   Guess the letters of the word in the given nmber of tries.
*   If you manage to predict the letters of the word before tries end, you win the game else you lose.
*   You may play again by entering *y* else enter *n* to close the program.

## Instructions for testing

*   Run the following command to run the program.
     *     python hangman_main.py
*   Enter *y* to start the program else enter *n*.
*   Guess the letters of the word in the given nmber of tries.
*   If you manage to predict the letters of the word before tries end, you win the game else you lose.
*   You may play again by entering *y* else enter *n* to close the program.

## License

*   This program is free to use for everyone.
