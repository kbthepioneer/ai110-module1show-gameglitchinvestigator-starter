# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation
You asked an AI to build a simple "Number Guessing Game" using Streamlit. It wrote the code, ran away, and now the game is unplayable.

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Run the app: `python -m streamlit run app.py`

## 📝 Document Your Experience

**Game Purpose:**
A number guessing game where the player tries to guess a randomly generated secret number within a limited number of attempts. The player receives hints after each guess and earns points based on how quickly they guess correctly.

**Bugs Found:**
- The hints were backwards — guessing too high said "Go HIGHER" and too low said "Go LOWER"
- Every other attempt converted the secret number to a string, causing broken comparisons
- The secret number would reset on every button click due to a Streamlit session state issue
- The scoring formula used the wrong multiplier, making a first-attempt win worth less than 100 points

**Fixes Applied:**
- Swapped the hint messages in `check_guess()` in `logic_utils.py`
- Removed the string conversion bug that used `str(st.session_state.secret)` on even attempts
- Fixed session state initialization so the secret only generates once per game
- Fixed scoring formula to `max(10, 110 - 10 * attempt_number)` so first attempt awards full points

## 📸 Demo Walkthrough
1. User opens the app — a secret number between 1 and 100 is generated (visible in Developer Debug Info)
2. User enters a guess of 40 and clicks "Submit Guess"
3. Game returns "📈 Go HIGHER!" — score decreases by 5
4. User enters a guess of 70 and clicks "Submit Guess"
5. Game returns "📉 Go LOWER!" — score decreases by 5
6. User enters a guess of 55 and clicks "Submit Guess"
7. Game returns "🎉 Correct!" — balloons appear, final score displayed
8. User clicks "New Game" to reset and play again with a new secret number

## 🧪 Test Results
```
python -m pytest tests/
============================= test session starts ==============================
platform win32 -- Python 3.14.5, pytest-9.0.3, pluggy-1.6.0
rootdir: C:\Users\kbayona\ai110-module1show-gameglitchinvestigator-starter
collected 21 items

tests\test_game_logic.py .....................                            [100%]
============================== 21 passed in 0.25s ==============================
```

## 🚀 Stretch Features
- Completed Challenge 1: Advanced Edge-Case Testing — added 7 additional pytest cases covering negative numbers, very large numbers, None input, and boundary values (1 and 100)