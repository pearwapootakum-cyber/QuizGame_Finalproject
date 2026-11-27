from dataclasses import dataclass


@dataclass
class Question:
    """Represent one multiple-choice quiz question."""

    text: str
    options: list[str]
    correct_answer: str
    category: str
    difficulty: str

    def __post_init__(self):
        """Validate and normalize question information."""

        if not isinstance(self.text, str):
            raise TypeError("Question text must be a string.")

        if not isinstance(self.options, list):
            raise TypeError("Options must be a list.")

        if not isinstance(self.correct_answer, str):
            raise TypeError("Correct answer must be a string.")

        if not isinstance(self.category, str):
            raise TypeError("Category must be a string.")

        if not isinstance(self.difficulty, str):
            raise TypeError("Difficulty must be a string.")

        self.text = self.text.strip()
        cleaned_options = []

        for option in self.options:
            if isinstance(option, str):
                cleaned_options.append(option.strip())
            else:
                cleaned_options.append("")

        self.options = cleaned_options
        self.correct_answer = self.correct_answer.strip().upper()
        self.category = self.category.strip()
        self.difficulty = self.difficulty.strip().title()

        if not self.text:
            raise ValueError("Question text cannot be empty.")

        if len(self.options) != 4:
            raise ValueError("A question must have exactly 4 options.")

        for option in self.options:
            if not option:
                raise ValueError("Options cannot be empty.")

        if self.correct_answer not in ["A", "B", "C", "D"]:
            raise ValueError("Correct answer must be A, B, C, or D.")

        if not self.category:
            raise ValueError("Category cannot be empty.")

        if self.difficulty not in ["Easy", "Medium", "Hard"]:
            raise ValueError("Invalid difficulty level.")

    @property
    def points(self) -> int:
        """Return points according to question difficulty."""

        scoring = {
            "Easy": 1,
            "Medium": 2,
            "Hard": 3,
        }

        return scoring[self.difficulty]

    def is_correct(self, answer: str) -> bool:
        """Check whether the player's answer is correct."""

        if not isinstance(answer, str):
            return False

        return answer.strip().upper() == self.correct_answer

    def __str__(self) -> str:
        """Return a readable representation of the question."""

        return self.text