import pytest
from spam_scoring import score_message, classify, filter_inbox, inbox_status

#Example test cases:
def test_plain_message_scores_zero():
    assert score_message("hello there", False, 0) == 0

def test_low_score_is_clean():
    assert classify(1) == "clean"

#Write the rest of the test cases so that the code is 90- 100% covered.

def test_spam_word_scores_two():
    assert score_message("free offer", False, 0) == 2

def test_uppercase_word_scores_one():
    assert score_message("HELLO", False, 0) == 1

def test_many_links_add_four():
    assert score_message("hello", False, 4) == 4

def test_some_links_add_one():
    assert score_message("hello", False, 1) == 1

def test_known_sender_score_does_not_go_negative():
    assert score_message("hello", True, 0) == 0

def test_high_score_is_spam():
    assert classify(8) == "spam"

def test_medium_score_is_suspicious():
    assert classify(4) == "suspicious"

def test_filter_inbox_counts_messages():
    messages = [
        ("free winner prize urgent", False, 0),
        ("hello", False, 4),
        ("hello there", False, 0)
    ]

    result = filter_inbox(messages)

    assert result == {
        "spam": 1,
        "suspicious": 1,
        "clean": 1
    }

def test_empty_inbox_status():
    counts = {"spam": 0, "suspicious": 0, "clean": 0}
    assert inbox_status(counts) == "empty"

def test_flooded_inbox_status():
    counts = {"spam": 6, "suspicious": 2, "clean": 2}
    assert inbox_status(counts) == "flooded"

def test_noisy_inbox_status():
    counts = {"spam": 3, "suspicious": 3, "clean": 4}
    assert inbox_status(counts) == "noisy"

def test_healthy_inbox_status():
    counts = {"spam": 1, "suspicious": 3, "clean": 6}
    assert inbox_status(counts) == "healthy"

