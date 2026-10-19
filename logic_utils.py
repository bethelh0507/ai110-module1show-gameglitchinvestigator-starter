def get_range_for_difficulty(difficulty: str):
    """Return the number range for each difficulty."""
    if difficulty == "Easy":
        return 1, 20
    elif difficulty == "Normal":
        return 1, 100
    elif difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """Convert user input into a valid whole number."""
    try:
        guess = int(raw)
        return True, guess, None
    except (ValueError, TypeError):
        return False, None, "Please enter a valid whole number."


def check_guess(guess, secret):
    """Compare the player's guess with the secret number."""
    if guess == secret:
        return "Win", "🎉 Correct!"
    elif guess > secret:
        return "Too High", "📈 Go LOWER!"
    else:
        return "Too Low", "📉 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update the player's score based on their guess."""
    if outcome == "Win":
        points = 100 - 10 * attempt_number

        if points < 10:
            points = 10

        return current_score + points

    if outcome == "Too High":
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score