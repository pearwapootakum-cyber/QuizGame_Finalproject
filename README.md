# QuizMaster

A terminal-based multiple-choice quiz game where players answer questions,
earn points, and compete for the highest score.

## Features

- Player registration
- Multiple question categories
- Three difficulty levels: Easy, Medium, Hard
- Randomized questions
- Multiple-choice answers (A-D)
- Difficulty-based scoring
- Input validation
- Persistent JSON leaderboard
- Custom question generator

## Requirements

- Python 3.12 or newer
- pip

## Installation

Clone the repository:

```bash
git clone https://github.com/pearwapootakum-cyber/QuizGame_Finalproject.git
cd QuizGame_Finalproject
```

(Optional) create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
```

Install the project with the development tools:

```bash
pip install -e ".[dev]"
```

## How to Play

Run the game:

```bash
python main.py
```

1. Enter your name.
2. Choose a category and a difficulty:
   - **Ranked game:** pick *All Categories* and *All Difficulties*. You get
     10 random questions, and your score goes on the leaderboard.
   - **Practice game:** pick a specific category or difficulty, then choose
     how many questions to answer. Practice scores are not saved.
3. Answer each question by typing A, B, C, or D.
4. See your final score and the top 5 players on the leaderboard.

Press Ctrl+C at any time to quit.

## Scoring

| Difficulty | Points |
|------------|--------|
| Easy       | 1      |
| Medium     | 2      |
| Hard       | 3      |

Every ranked game is the same length, so leaderboard scores are fair to
compare. Ranked scores are saved to `data/leaderboard.json`. If you play again
with the same name (case-insensitive), the leaderboard keeps your best score.

## Running Tests

```bash
pytest
```

## Linting

```bash
ruff check .
```

## Project Structure

```
QuizGame_Finalproject/
├── main.py               # Terminal interface and game loop
├── quizmaster/
│   ├── question.py       # Question model and validation
│   ├── player.py         # Player model and scoring
│   ├── quiz.py           # Question selection and answer checking
│   ├── leaderboard.py    # Ranking players
│   └── storage.py        # JSON save/load
└── tests/                # pytest test suite
```
