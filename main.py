from pathlib import Path

from quizmaster import (
    JsonStorage,
    Leaderboard,
    Player,
    Question,
    Quiz,
)


DATA_FILE = Path(__file__).parent / "data" / "leaderboard.json"
DIFFICULTY_ORDER = ["Easy", "Medium", "Hard"]
RANKED_GAME_LENGTH = 10


def create_questions() -> list[Question]:
    """Create the question bank."""

    return [
        Question(
            "What is the capital of Thailand?",
            ["Bangkok", "Tokyo", "Seoul", "Beijing"],
            "A",
            "Geography",
            "Easy",
        ),
        Question(
            "What is the chemical symbol for gold?",
            ["Ag", "Fe", "Au", "Cu"],
            "C",
            "Science",
            "Medium",
        ),
        Question(
            "Which planet is closest to the Sun?",
            ["Venus", "Earth", "Mars", "Mercury"],
            "D",
            "Science",
            "Hard",
        ),
        Question(
            "What is the largest ocean on Earth?",
            ["Atlantic", "Indian", "Pacific", "Arctic"],
            "C",
            "Geography",
            "Easy",
        ),
        Question(
            "Which gas do plants absorb during photosynthesis?",
            ["Oxygen", "Carbon dioxide", "Nitrogen", "Hydrogen"],
            "B",
            "Science",
            "Medium",
        ),
        Question(
            "What is the square root of 144?",
            ["10", "11", "12", "14"],
            "C",
            "Mathematics",
            "Easy",
        ),
        Question(
            "What is the derivative of x squared?",
            ["x", "2x", "x squared", "2"],
            "B",
            "Mathematics",
            "Hard",
        ),
        Question(
            "Which country is home to the city of Kyoto?",
            ["China", "South Korea", "Japan", "Thailand"],
            "C",
            "Geography",
            "Medium",
        ),
        Question(
            "How many sides does a hexagon have?",
            ["Five", "Six", "Seven", "Eight"],
            "B",
            "Mathematics",
            "Easy",
        ),
        Question(
            "Which organelle is responsible for producing ATP?",
            ["Nucleus", "Ribosome", "Mitochondrion", "Golgi apparatus"],
            "C",
            "Science",
            "Hard",
        ),
        Question(
            "What is the capital of Australia?",
            ["Sydney", "Melbourne", "Canberra", "Perth"],
            "C",
            "Geography",
            "Medium",
        ),
        Question(
            "What is 15 multiplied by 8?",
            ["100", "110", "120", "130"],
            "C",
            "Mathematics",
            "Medium",
        ),
    ]


def ask_name() -> str:
    """Ask for a valid player name."""

    while True:
        name = input("Enter your name: ").strip()

        if name:
            return name

        print("Name cannot be empty. Please try again.")


def choose_option(title: str, options: list[str]) -> str:
    """Display numbered options and return the player's choice."""

    print(f"\n{title}")

    number = 1

    for option in options:
        print(f"{number}. {option}")
        number += 1

    while True:
        choice = input("Choose an option: ").strip()

        if choice.isdigit():
            number = int(choice)

            if 1 <= number <= len(options):
                return options[number - 1]

        print(f"Please enter a number from 1 to {len(options)}.")


def ask_amount(maximum: int) -> int:
    """Ask how many questions to play, from 1 to maximum."""

    while True:
        choice = input(f"\nHow many questions? (1-{maximum}): ").strip()

        if choice.isdigit() and 1 <= int(choice) <= maximum:
            return int(choice)

        print(f"Please enter a number from 1 to {maximum}.")


def ask_question(
    quiz: Quiz,
    question: Question,
    player: Player,
    number: int,
) -> None:
    """Display a question, collect an answer, and update the score."""

    letters = ["A", "B", "C", "D"]

    print(f"\n{'-' * 45}")
    print(f"Question {number}: {question.text}")
    print(f"Category: {question.category}")
    print(f"Difficulty: {question.difficulty}")
    print(f"Points available: {question.points}")
    print()

    for letter, option in zip(letters, question.options):
        print(f"{letter}. {option}")

    while True:
        answer = input("\nYour answer (A/B/C/D): ").strip().upper()

        if answer in letters:
            break

        print("Invalid answer. Enter A, B, C, or D.")

    if quiz.play_question(question, answer, player):
        print(f"Correct! +{question.points} points.")
    else:
        print(f"Incorrect! The correct answer was {question.correct_answer}.")

    print(f"Your current score: {player.score}")


def display_leaderboard(leaderboard: Leaderboard) -> None:
    """Display the highest-scoring players."""

    print("\n========== LEADERBOARD ==========")

    top_players = leaderboard.top_players(5)

    if not top_players:
        print("No scores recorded yet.")
        return

    rank = 1

    for player in top_players:
        print(f"{rank}. {player.name} - {player.score} points")
        rank += 1


def main() -> None:
    """Run the QuizMaster application."""

    storage = JsonStorage(DATA_FILE)
    leaderboard = Leaderboard(storage.load_players())

    quiz = Quiz(create_questions())

    print("=" * 45)
    print("           WELCOME TO QUIZMASTER")
    print("=" * 45)

    player = Player(ask_name())

    print(f"\nWelcome, {player.name}!")

    print(
        f"\nPick 'All Categories' and 'All Difficulties' for a ranked game "
        f"of {RANKED_GAME_LENGTH} questions."
    )
    print("Any other choice is a practice game and is not saved.")

    categories = []

    for question in quiz.questions:
        if question.category not in categories:
            categories.append(question.category)

    categories.sort()

    category = choose_option(
        "Choose a category:",
        ["All Categories"] + categories,
    )

    if category == "All Categories":
        category = None

    available_questions = quiz.select_questions(category=category)

    difficulties = []

    for question in available_questions:
        if question.difficulty not in difficulties:
            difficulties.append(question.difficulty)

    difficulties.sort(key=DIFFICULTY_ORDER.index)

    difficulty = choose_option(
        "Choose a difficulty:",
        ["All Difficulties"] + difficulties,
    )

    if difficulty == "All Difficulties":
        difficulty = None

    ranked = category is None and difficulty is None

    if ranked:
        amount = RANKED_GAME_LENGTH
        print(f"\nRanked game: {amount} questions. Your score will be saved.")
    else:
        available_questions = quiz.select_questions(
            category=category,
            difficulty=difficulty,
        )
        amount = ask_amount(len(available_questions))
        print("\nPractice game: your score will not be saved.")

    print("\n========== LET'S START ==========")
    print("Easy = 1 point | Medium = 2 points | Hard = 3 points")

    questions = quiz.iter_questions(
        category=category,
        difficulty=difficulty,
        amount=amount,
    )

    number = 1

    for question in questions:
        ask_question(quiz, question, player, number)
        number += 1

    print("\n" + "=" * 45)
    print("              QUIZ COMPLETED")
    print("=" * 45)
    print(f"Player: {player.name}")
    print(f"Final score: {player.score} points")

    if ranked:
        leaderboard.add_player(player)

        if storage.save_players(leaderboard.players):
            print("Your score has been saved.")
        else:
            print("Warning: Your score could not be saved.")
    else:
        print("Practice game, so your score was not saved.")

    display_leaderboard(leaderboard)


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nQuiz cancelled. Goodbye!")