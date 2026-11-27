import pytest

from quizmaster.player import Player
from quizmaster.question import Question
from quizmaster.quiz import Quiz


def make_questions():
    """Create sample questions for testing."""

    return [
        Question(
            "Capital of Thailand?",
            ["Bangkok", "Tokyo", "Seoul", "Beijing"],
            "A",
            "Geography",
            "Easy",
        ),
        Question(
            "Chemical symbol for gold?",
            ["Ag", "Fe", "Au", "Cu"],
            "C",
            "Science",
            "Medium",
        ),
        Question(
            "Closest planet to the Sun?",
            ["Venus", "Earth", "Mars", "Mercury"],
            "D",
            "Science",
            "Hard",
        ),
    ]


def test_quiz_creation():
    quiz = Quiz(make_questions())

    assert len(quiz.questions) == 3


def test_category_filter():
    quiz = Quiz(make_questions())

    questions = quiz.select_questions(category="Science")

    assert len(questions) == 2

    for question in questions:
        assert question.category == "Science"


def test_difficulty_filter():
    quiz = Quiz(make_questions())

    questions = quiz.select_questions(difficulty="Hard")

    assert len(questions) == 1
    assert questions[0].difficulty == "Hard"


def test_question_amount():
    quiz = Quiz(make_questions())

    questions = quiz.select_questions(amount=2)

    assert len(questions) == 2


def test_invalid_question_amount():
    quiz = Quiz(make_questions())

    with pytest.raises(ValueError):
        quiz.select_questions(amount=10)


def test_play_question():
    questions = make_questions()
    quiz = Quiz(questions)
    player = Player("Nut")

    result = quiz.play_question(questions[0], "A", player)

    assert result is True
    assert player.score == 1


def test_wrong_answer():
    questions = make_questions()
    quiz = Quiz(questions)
    player = Player("Nut")

    result = quiz.play_question(questions[0], "B", player)

    assert result is False
    assert player.score == 0


def test_question_generator():
    quiz = Quiz(make_questions())

    generated = list(quiz.iter_questions(amount=2))

    assert len(generated) == 2