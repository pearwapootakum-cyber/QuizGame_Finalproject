from quizmaster.player import Player


class Leaderboard:
    """Store players and organize them by their scores."""

    def __init__(self, players: list[Player] | None = None):
        """Initialize the leaderboard."""

        if players is not None:
            self.players = list(players)
        else:
            self.players = []

        for player in self.players:
            if not isinstance(player, Player):
                raise TypeError("Leaderboard entries must be Player objects.")

    def add_player(self, player: Player) -> None:
        """Add a player, or keep the higher of their old and new scores."""

        if not isinstance(player, Player):
            raise TypeError("Player must be a Player object.")

        for existing_player in self.players:
            if existing_player.name.casefold() == player.name.casefold():
                existing_player.name = player.name
                existing_player.score = max(existing_player.score, player.score)
                return

        self.players.append(player)

    def top_players(self, limit: int = 10) -> list[Player]:
        """Return players ranked by score from highest to lowest."""

        if not isinstance(limit, int) or isinstance(limit, bool):
            raise ValueError("Limit must be an integer.")

        if limit <= 0:
            raise ValueError("Limit must be greater than zero.")

        return sorted(
            self.players,
            key=lambda player: player.score,
            reverse=True,
        )[:limit]

    def __len__(self) -> int:
        """Return the number of leaderboard entries."""

        return len(self.players)