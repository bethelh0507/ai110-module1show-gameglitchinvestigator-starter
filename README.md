# 🎮 Game Glitch Investigator: The Impossible Guesser

🚨 The Situation

This project is a number guessing game built using Python and Streamlit. The goal is to guess a randomly generated secret number within a limited number of attempts.

The original AI-generated game contained several bugs that made it difficult to play correctly. My task was to investigate the problems, fix the code, test the game, and document how I used AI during the debugging process.

🛠️ Setup

Install dependencies: pip install -r requirements.txt

Run the application: python -m streamlit run app.py

Open the local Streamlit URL displayed in the terminal.

Choose a difficulty level and start guessing.

🕵️‍♂️ My Mission

During this project, I investigated and fixed several issues:

Incorrect hints: The game sometimes told players to guess higher when they needed to guess lower. I corrected the comparison logic.

Attempt counter: The game did not always track attempts correctly. I updated the session-state initialization.

Scoring problems: Incorrect guesses could produce incorrect score changes. I fixed the update_score() function.

Display updates: Attempts, scores, and guess history sometimes displayed outdated information. I corrected when the information was refreshed.

Code organization: I moved the game logic into logic_utils.py so it could be tested separately from the Streamlit interface.

📝 Document Your Experience

Game's purpose: The game challenges players to guess a secret number using higher/lower hints before running out of attempts.

Bugs discovered: I found incorrect hints, problems with attempts and scoring, and outdated information displayed on the screen.

Fixes applied: I corrected the game logic, improved session-state handling, separated the functions into logic_utils.py, and added automated tests.

I used ChatGPT to help understand the code and troubleshoot the bugs. I also tested the changes myself to make sure the game behaved correctly.

📸 Demo Walkthrough

The following is an example of a completed game on Easy difficulty.

The player selects Easy, which generates a secret number between 1 and 20 and allows 6 attempts.

The secret number is 4, and the player enters 5. The game displays "Go LOWER!", and the score decreases to -5.

The player enters 3. The game displays "Go HIGHER!", and the score decreases to -10.

The player enters 4, matching the secret number. The game displays "Correct!" and the winning message.

The game awards 70 points for winning on the third attempt, resulting in a final score of 60.

The player can click New Game to reset the attempts, score, and secret number.

🧪 Test Results

I used pytest to test the game logic, including correct guesses, incorrect guesses, scoring, and input validation.

Paste the actual output from your latest successful pytest run here:

platform win32 -- Python 3.12.0, pytest-9.1.1, pluggy-1.7.0 -- C:\Users\user\ai110-module1show-gameglitchinvestigator-starter\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\user\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.15.1
collected 5 items                                                                                                            

tests/test_game_logic.py::test_winning_guess PASSED                                                                    [ 20%]
tests/test_game_logic.py::test_guess_too_high PASSED                                                                   [ 40%]
tests/test_game_logic.py::test_guess_too_low PASSED                                                                    [ 60%]
tests/test_game_logic.py::test_scoring PASSED                                                                          [ 80%]
tests/test_game_logic.py::test_invalid_input PASSED                                                                    [100%]

===================================================== 5 passed in 0.02s =====================================================
PS C:\Users\user\ai110-module1show-gameglitchinvestigator-starter> 

🚀 Stretch Features

No optional stretch challenges completed.

💡 What I Learned

This project taught me that AI-generated code can contain mistakes even when it looks correct. I learned how Streamlit session state works, how to separate game logic from the interface, and how to use automated tests to verify changes. I also learned that debugging works better when I investigate one problem at a time and test each solution before moving forward.