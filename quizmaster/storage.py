import json
from pathlib import Path

from quizmaster.player import Player


class JsonStorage:
    """Save and load leaderboard information using JSON."""

    def __init__(self, file_path: Path):
        """Initialize storage with a JSON file path."""

        self.file_path = Path(file_path)

    def save_players(self, players: list[Player]) -> bool:
        """Save player information to a JSON file."""

        if not all(isinstance(player, Player) for player in players):
            raise TypeError("All entries must be Player objects.")

        data = [
            {
                "name": player.name,
                "score": player.score,
            }
            for player in players
        ]

        try:
            self.file_path.parent.mkdir(parents=True, exist_ok=True)

            with self.file_path.open("w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)

            return True

        except OSError:
            return False

    def load_players(self) -> list[Player]:
        """Load valid player information from a JSON file."""

        try:
            with self.file_path.open("r", encoding="utf-8") as file:
                data = json.load(file)

        except (OSError, json.JSONDecodeError):
            return []

        if not isinstance(data, list):
            return []

        players = []

        for entry in data:
            if not isinstance(entry, dict):
                continue

            try:
                player = Player(
                    name=entry["name"],
                    score=entry["score"],
                )
                players.append(player)

            except (KeyError, TypeError, ValueError):
                continue

        return players