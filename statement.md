# Hangman Game - Project Statement

## Introduction

Hangman is a classic word-guessing game that has entertained players for generations. This project implements a fully functional, interactive command-line version of the traditional Hangman game in Python. The application provides an engaging gaming experience while demonstrating fundamental programming concepts such as string manipulation, control flow, random selection, and user input validation. Whether you're a beginner learning Python or someone looking for a fun game to play, this Hangman implementation offers both educational value and entertainment.

## Problem Statement

The challenge addressed by this project is to create an engaging and interactive word-guessing game that maintains the spirit of the classic Hangman gameplay while providing a smooth, user-friendly experience in a terminal environment. The implementation needs to handle game logic effectively, manage player attempts fairly, provide clear visual feedback through ASCII art, and ensure robust input validation to create a seamless gaming experience. Additionally, the game must be easily playable with the ability to play multiple rounds without restarting the program.

## Scope of the Project

This project encompasses the following deliverables:

**Core Functionality:**
- A random word selection system from a predefined list of words
- A turn-based guessing mechanism where players attempt to identify letters in the hidden word
- A limited number of attempts (six tries) before the game ends in defeat
- Comprehensive input validation to ensure only valid letters are accepted
- Win and loss conditions with appropriate feedback messages

**User Experience:**
- ASCII art visualization of the hangman figure that progresses with each incorrect guess
- Real-time display of the word completion status and remaining attempts
- Clear prompts and informative messages to guide the player through gameplay
- Replay functionality allowing players to start new games without restarting the program

**Constraints:**
- The game is limited to a predefined word list (easily expandable for future versions)
- Gameplay is restricted to a command-line interface
- The word set contains common English words of varying lengths

## Explanation of Key Aspects of the Code

### Core Components

**Word Selection Module:**
The game maintains a list of ten fruit-themed words. At the start of each game, a word is randomly selected using Python's `random.choice()` function, ensuring variety and unpredictability across multiple playthroughs.

**Main Game Loop:**
The central `game()` function orchestrates the entire gameplay experience. It maintains several critical variables throughout the session: the selected word, the number of remaining tries, a list of previously guessed letters, and a dynamic representation of word completion showing correctly guessed letters and blanks for unguessed ones.

**Input Validation System:**
Before processing any guess, the program validates that user input is exactly one character and is alphabetic. This prevents invalid entries from affecting game state and ensures clean, predictable gameplay. Additionally, the system tracks previously guessed letters to prevent duplicate attempts.

**Letter Matching and Word Completion:**
When a valid letter is submitted, the program checks if it exists in the target word. Correct guesses reveal all instances of that letter in the word, while incorrect guesses consume one attempt. The word completion string is dynamically updated using list comprehension, displaying both revealed letters and remaining blanks in an easily readable format.

**Visual Feedback System:**
The `display_hangman()` function manages a series of seven ASCII art stages representing the hangman figure. As players make incorrect guesses and attempts dwindle, progressively more detailed hangman illustrations are displayed, creating visual tension and providing immediate feedback on game status.

**Game State Management:**
The program continuously checks two conditions in its main loop: whether attempts remain and whether all letters have been guessed. Once either condition fails, the game concludes with appropriate messaging revealing the solution if the player lost or congratulating them on their victory.

**Replay Mechanism:**
After each game concludes, players are prompted whether they wish to play again. This outer loop allows seamless replaying without program termination, returning to the main function for a fresh game instance.

## Benefits of the Program

**Educational Value:**
This implementation serves as an excellent learning resource for Python beginners, demonstrating essential programming constructs including functions, loops, conditional statements, list operations, and string manipulation in a practical, engaging context.

**Entertainment:**
The game provides genuine entertainment through engaging gameplay mechanics, visual ASCII art feedback, and the inherent challenge of word-guessing that has made Hangman popular for decades.

**Extensibility:**
The code structure is clean and modular, making it simple to enhance with additional features such as difficulty levels, larger word databases, custom categories, or graphical user interfaces.

**Immediate Playability:**
With no external dependencies beyond Python's standard library, the game runs immediately on any system with Python installed. There are no setup complexities or installation requirements.

**Accessibility:**
The command-line interface makes the game accessible to users with varying technical backgrounds while remaining lightweight and responsive.

## Target Users

**Primary Audience:**
- Python beginners and students learning programming fundamentals
- Teachers seeking engaging programming examples for classroom instruction
- Casual gamers interested in classic word games with nostalgic appeal
- Developers looking to understand game loop implementation and state management

**Secondary Audience:**
- Experienced programmers interested in quickly refactoring or extending the codebase
- Contributors to open-source projects seeking beginner-friendly codebases to enhance
- Anyone seeking a quick, no-nonsense command-line game for entertainment during breaks

## High-Level Features

**1. Intelligent Word Management**
The game maintains a curated list of words and employs random selection for varied gameplay across multiple sessions.

**2. Robust Attempt System**
Players receive six attempts to guess the word, with each incorrect guess visually tracked and managed transparently.

**3. Dynamic Word Visualization**
The current state of the word being guessed updates in real-time, clearly showing which letters have been correctly identified and which positions remain unknown.

**4. Progressive ASCII Art**
The hangman figure evolves through seven distinct stages, providing engaging visual progression and immediate feedback on game status.

**5. Smart Input Handling**
The system intelligently validates all user input, rejecting invalid entries and preventing players from repeating previous guesses through duplicate detection.

**6. Clear Feedback Messaging**
Every player action generates informative feedback, from confirmation of correct guesses to warning messages about invalid input or repeated guesses.

**7. Replay Capability**
Players can seamlessly play multiple consecutive games without restarting the program, with each new game offering a fresh word selection and full attempt allocation.

**8. Win/Loss Detection**
The game automatically detects both victory and defeat conditions, displaying appropriate messages and revealing the answer when the player loses.

---

### Getting Started

*   To Install the code on your personal computer please download the files from github.
*   Open the file on your desired IDE.
*   Please ensure you have Python installed on your personal computer.
*   Run the following command to run the program.

          python hangman_main.py

*   Enter *y* to start the program else enter *n*.
*   Guess the letters of the word in the given nmber of tries.
*   If you manage to predict the letters of the word before tries end, you win the game else you lose.
*   You may play again by entering *y* else enter *n* to close the program.

### Future Enhancements

Potential improvements for future versions include expanding the word database, implementing difficulty levels with word length or category filters, adding a scoring system, integrating a graphical user interface, or creating multiplayer modes for competitive gameplay.
