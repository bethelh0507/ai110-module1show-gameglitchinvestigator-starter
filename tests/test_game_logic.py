from logic_utils import check_guess, update_score, parse_guess

def test_winning_guess():
    # If the secret is 50 and the guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If the secret is 50 and the guess is 60, hint should be Too High
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_guess_too_low():
    # If the secret is 50 and the guess is 40, hint should be Too Low
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message
def test_scoring():
    # Wrong guesses should subtract 5 points
    assert update_score(0, "Too High", 1) == -5
    assert update_score(0, "Too Low", 1) == -5

    # A correct guess on attempt 3 should earn 70 points
    assert update_score(0, "Win", 3) == 70


def test_invalid_input():
    # Letters should not be accepted as a number
    ok, guess, error = parse_guess("hello")

    assert ok is False
    assert guess is None
    assert error is not None