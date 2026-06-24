from logic_utils import check_guess, parse_guess, get_range_for_difficulty, update_score


# --- check_guess tests ---
def test_correct_guess():
    outcome, message = check_guess(42, 42)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, message = check_guess(80, 42)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, message = check_guess(10, 42)
    assert outcome == "Too Low"

def test_hint_too_high_says_lower():
    outcome, message = check_guess(80, 42)
    assert "LOWER" in message

def test_hint_too_low_says_higher():
    outcome, message = check_guess(10, 42)
    assert "HIGHER" in message


# --- parse_guess tests ---
def test_parse_valid_number():
    ok, val, err = parse_guess("50")
    assert ok and val == 50

def test_parse_empty_string():
    ok, val, err = parse_guess("")
    assert not ok

def test_parse_non_number():
    ok, val, err = parse_guess("abc")
    assert not ok

def test_parse_decimal():
    ok, val, err = parse_guess("7.9")
    assert ok and val == 7


# --- get_range_for_difficulty tests ---
def test_range_easy():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1 and high == 20

def test_range_normal():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1 and high == 100

def test_range_hard():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1 and high == 50


# --- update_score tests ---
def test_score_increases_on_win():
    new_score = update_score(0, "Win", 1)
    assert new_score > 0

def test_score_decreases_on_wrong_guess():
    new_score = update_score(50, "Too High", 1)
    assert new_score < 50


# --- Edge Case Tests ---
def test_negative_guess_too_low():
    outcome, message = check_guess(-5, 42)
    assert outcome == "Too Low"

def test_very_large_guess_too_high():
    outcome, message = check_guess(99999, 42)
    assert outcome == "Too High"

def test_parse_negative_number():
    ok, val, err = parse_guess("-5")
    assert ok and val == -5

def test_parse_very_large_number():
    ok, val, err = parse_guess("99999")
    assert ok and val == 99999

def test_parse_none():
    ok, val, err = parse_guess(None)
    assert not ok

def test_guess_boundary_low():
    outcome, _ = check_guess(1, 1)
    assert outcome == "Win"

def test_guess_boundary_high():
    outcome, _ = check_guess(100, 100)
    assert outcome == "Win"