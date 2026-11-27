import pytest

from quizmaster.question import Question


def make_question(difficulty="Easy"):
    """Create a sample question for testing."""

    return Question(
        "What is the capital of Thailand?",
        ["Bangkok", "Tokyo", "Seoul", "Beijing"],
        "A",
        "Geography",
        difficulty,
    )


def test_question_creation():
    question = make_question()

    assert question.text == "What is the capital of Thailand?"
    assert question.category == "Geography"


def test_question_points():
    assert make_question("Easy").points == 1
    assert make_question("Medium").points == 2
    assert make_question("Hard").points == 3


def test_correct_answer():
    question = make_question()

    assert question.is_correct("A") is True
    assert question.is_correct("a") is True
    assert question.is_correct("B") is False


def test_invalid_number_of_options():
    with pytest.raises(ValueError):
        Question("Question?", ["One", "Two"], "A", "Test", "Easy")


def test_invalid_difficulty():
    with pytest.raises(ValueError):
        make_question("Impossible")


def test_empty_question_text():
    with pytest.raises(ValueError):
        Question("", ["A", "B", "C", "D"], "A", "Test", "Easy")

def test_invalid_correct_answer():
    with pytest.raises(ValueError):
        Question("Question?", ["A", "B", "C", "D"], "E", "Test", "Easy")
