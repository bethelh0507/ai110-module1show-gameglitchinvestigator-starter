# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  
  When I first ran the game, it looked like a normal number guessing game where I could select a difficulty and enter guesses, but some features were not working correctly. One problem was that the hints were backwards, so the game sometimes told me to guess higher when I needed to guess lower. I also noticed problems with the attempt counter and scoring system, which made it difficult to track my progress accurately. After looking through the code, I found that some of these problems were caused by incorrect conditions and logic in the game functions.



**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Secret number: 4, guess: 5| Display "Too High" and tell the player to go lower|The hint incorrectly directed the player higher |Incorrect hint displayed; no console error recorded |check_guess()
| Start a new game| Attempts should begin at 0|Attempt counter started with an attempt already used |Incorrect attempt count; no console error recorded |app.py, session-state initialization
|Enter an incorrect guess | Score should decrease by 5 points| Score increased instead of decreasing|ncorrect score displayed; no console error recorded |update_score()

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

I used ChatGPT to help me understand the Python code, identify bugs, and figure out how to correct them. One helpful suggestion was to fix the conditions in check_guess() so that guesses higher than the secret number displayed the correct hint, which I verified by testing different guesses in the game. AI also helped me investigate why the attempts, score, and history were displaying outdated information. Before submitting, I need to add a specific example of an AI suggestion I changed or did not accept as written, including why and how I tested my alternative.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I tested the game after making changes to see whether the bugs were actually fixed instead of assuming the code was correct. For example, when the secret number was 4, I guessed 5 and received the correct instruction to go lower, then guessed 3 and received the instruction to go higher. When I guessed 4, the game displayed the winning message and the correct final score of 60. ChatGPT helped me understand what results to expect and how to check whether the guessing logic, scoring system, and attempt counter were working correctly.

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

I learned that Streamlit reruns the Python script whenever a user interacts with the application, such as submitting a guess or clicking a button. Session state allows the game to remember information like the secret number, attempts, score, and previous guesses between reruns. Without session state, the game could lose important information whenever the page updated. I also learned that the order of the code matters because displaying information before processing a guess can make the screen show outdated values.

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
One habit I want to continue using is testing my code after each small change instead of changing everything at once. Next time I work with AI, I would ask it to explain the cause of a bug before suggesting a solution so I can better understand what I am changing. This project helped me realize that AI-generated code is not always correct, even when it looks reasonable. I learned that developers still need to review, test, and understand the code instead of relying completely on AI.