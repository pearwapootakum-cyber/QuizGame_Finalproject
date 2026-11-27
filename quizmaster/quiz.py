import random
from collections.abc import Iterator

from quizmaster.player import Player
from quizmaster.question import Question


class Quiz:
    """Manage quiz questions, selection, answers, and scoring."""

    def __init__(self, questions: list[Question]):
        """Initialize a quiz with a collection of questions."""

        if not questions:
            raise ValueError("A quiz must contain at least one question.")

        for question in questions:
            if not isinstance(question, Question):
                raise TypeError("All items must be Question objects.")

        self.questions = list(questions)

    def select_questions(
        self,
        category: str | None = None,
        difficulty: str | None = None,
        amount: int | None = None,
    ) -> list[Question]:
        """Filter questions and return them in random order."""

        selected = self.questions

        if category is not None:
            filtered_questions = []

            for question in selected:
                if question.category.casefold() == category.strip().casefold():
                    filtered_questions.append(question)

            selected = filtered_questions

        if difficulty is not None:
            filtered_questions = []

            for question in selected:
                if question.difficulty.casefold() == difficulty.strip().casefold():
                    filtered_questions.append(question)

            selected = filtered_questions

        if not selected:
            raise ValueError("No questions match your selection.")

        if amount is not None:
            if not isinstance(amount, int) or isinstance(amount, bool):
                raise ValueError("Amount must be an integer.")

            if amount <= 0:
                raise ValueError("Amount must be greater than zero.")

            if amount > len(selected):
                raise ValueError("Not enough questions available.")

            return random.sample(selected, amount)

        return random.sample(selected, len(selected))

    def iter_questions(
        self,
        category: str | None = None,
        difficulty: str | None = None,
        amount: int | None = None,
    ) -> Iterator[Question]:
        """Generate selected questions one at a time."""

        yield from self.select_questions(category, difficulty, amount)

    def check_answer(self, question: Question, answer: str) -> bool:
        """Check whether an answer to a quiz question is correct."""

        if question not in self.questions:
            raise ValueError("Question does not belong to this quiz.")

        if not isinstance(answer, str):
            raise TypeError("Answer must be a string.")

        return question.is_correct(answer)

    def play_question(
        self,
        question: Question,
        answer: str,
        player: Player,
    ) -> bool:
        """Check the player's answer and award points if correct."""

        if not isinstance(player, Player):
            raise TypeError("Player must be a Player object.")

        if self.check_answer(question, answer):
            player.add_points(question.points)
            return True

        return False