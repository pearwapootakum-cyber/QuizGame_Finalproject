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

The game uses only the Python standard library, so you can run it right
away. The setup below is only needed to run the tests and the linter.

### Windows (Command Prompt or PowerShell)

Run the game:

```bat
py main.py
```

Set up the development tools (optional):

```bat
py -m venv .venv
.venv\Scripts\activate
pip install -e ".[dev]"
```

### macOS (Terminal)

Run the game:

```bash
python3 main.py
```

Set up the development tools (optional):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

Inside an activated virtual environment, `python` works on both systems.

## How to Play

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
python -m pytest
```

## Linting

```bash
python -m ruff check .
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
