# 💭 Reflection: Game Glitch Investigator

## 1. What was broken when you started?

When I first ran the game, the hints were completely backwards — guessing a number that was too high would tell me to go higher, and guessing too low would tell me to go lower, making it impossible to win by following the hints. The secret number also kept resetting every time I clicked Submit, so even if I somehow guessed correctly, the target would change before it could register as a win. There was also a bug where every other attempt compared my integer guess against a string version of the secret number, causing unpredictable behavior on even-numbered attempts.

**Bug Reproduction Log**

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess of 30 when secret was 50 | "Go HIGHER" hint | "Go LOWER" hint shown | none |
| Guess of 70 when secret was 50 | "Go LOWER" hint | "Go HIGHER" hint shown | none |
| Clicking Submit multiple times | Secret stays the same | Secret changed every click | none |
| Winning on first attempt | Score of 100 | Score of 80 | none |

---

## 2. How did you use AI as a teammate?

I used Claude as my AI coding assistant throughout this project. Claude helped me identify all four bugs by reading through the code and explaining what each line was doing wrong. One example of a correct suggestion was fixing the backwards hints in `check_guess()` — Claude pointed out that `"Go HIGHER"` and `"Go LOWER"` were swapped, I verified it by checking the debug info panel and confirming the hints now matched expectations. One example where I had to think critically was the scoring fix — Claude suggested several different approaches before landing on the correct formula `max(10, 110 - 10 * attempt_number)`, and I had to test each one manually in the game to confirm it actually gave 100 points on a first-attempt win.

---

## 3. Debugging and testing your fixes

I decided a bug was fixed by both running pytest and manually testing the game in the browser. For the hints bug, I opened the Developer Debug Info to see the secret number, then made guesses above and below it to confirm the hints now said the correct direction. I ran `python -m pytest tests/` after every change and used the 21 test cases — including edge cases for negative numbers, very large numbers, None input, and boundary values — to confirm nothing broke. Claude helped me generate the edge case tests by suggesting inputs that might trip up the logic, which I then verified made sense before adding them.

---

## 4. What did you learn about Streamlit and state?

Streamlit reruns the entire Python script from top to bottom every single time the user interacts with anything — clicks a button, changes a dropdown, types in a box. This means any regular variable you create gets wiped out on every interaction. Session state (`st.session_state`) is like a persistent backpack that survives these reruns — you store important values like the secret number in it so they don't get reset. The bug in this project happened because the input field's key was tied to the difficulty setting, which caused Streamlit to treat it as a brand new input and reinitialize everything including the secret number.

---

## 5. Looking ahead: your developer habits

One habit I want to carry forward is committing after each meaningful change rather than doing one big commit at the end — it creates a clear history of what changed and why, which makes debugging easier later. Next time I work with AI on a coding task, I would test each suggestion immediately in isolation before moving on, rather than applying multiple fixes at once and then trying to figure out which one caused an issue. This project changed how I think about AI-generated code — I used to assume it was probably correct since it came from an AI, but now I treat it the same way I would treat code from any other source: read it carefully, test it, and verify it actually does what it claims to do.