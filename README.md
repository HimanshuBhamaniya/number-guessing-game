# 🎲 Number Guessing Game (CLI)

A fun **Command Line Interface (CLI)** based number guessing game built in Python.  
This project is inspired by the [roadmap.sh Number Guessing Game project](https://roadmap.sh/projects/number-guessing-game) and is designed to help beginners practice Python basics, loops, conditionals, and user input handling.

---

## 📖 Overview
The game picks a random number between **1 and 100**.  
Your goal is to guess the secret number within a limited number of chances, based on the difficulty level you choose.

---

## ⚙️ Features
- Randomly generated secret number between 1 and 100
- Three difficulty levels:
  - **Easy** → 10 chances
  - **Medium** → 5 chances
  - **Hard** → 3 chances
- Feedback after each guess:
  - Too low
  - Too high
  - Correct guess
- Tracks number of attempts and displays success/failure message

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone <https://github.com/HimanshuBhamaniya/number-guessing-game.git>
cd number-guessing-game
```
### 2. Create a virtual environment
```bash
python -m venv venv
```
#### Activate it:
```bash
source venv/Scripts/activate
```

### 3. Run the game
```bash
python number_guessing_game.py
```

# 🛠️ Gameplay Example
```code
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have 5 chances to guess the correct number.
Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)

Enter your choice > 2
Great! You have selected the 2 difficulty level. Let's start the game!
Enter your guess > 50
Incorrect! Your guess is too low.
Enter your guess > 75
Incorrect! Your guess is too high.
Enter your guess > 63
Good job! You got it in 3 guesses.
```