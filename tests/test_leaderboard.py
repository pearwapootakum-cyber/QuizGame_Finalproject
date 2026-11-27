import pytest

from quizmaster.leaderboard import Leaderboard
from quizmaster.player import Player


def test_add_player():
    leaderboard = Leaderboard()
    player = Player("Nut", 10)

    leaderboard.add_player(player)

    assert len(leaderboard) == 1


def test_players_are_ranked():
    leaderboard = Leaderboard(
        [
            Player("Nut", 5),
            Player("Alex", 10),
            Player("Sam", 7),
        ]
    )

    ranked = leaderboard.top_players()

    assert ranked[0].name == "Alex"
    assert ranked[1].name == "Sam"
    assert ranked[2].name == "Nut"


def test_leaderboard_limit():
    leaderboard = Leaderboard(
        [
            Player("Nut", 5),
            Player("Alex", 10),
            Player("Sam", 7),
        ]
    )

    assert len(leaderboard.top_players(2)) == 2


def test_invalid_leaderboard_limit():
    leaderboard = Leaderboard()

    with pytest.raises(ValueError):
        leaderboard.top_players(0)

def test_returning_player_keeps_best_score():
    leaderboard = Leaderboard([Player("Nut", 10)])

    leaderboard.add_player(Player("nut", 3))
    assert len(leaderboard) == 1
    assert leaderboard.players[0].score == 10

    leaderboard.add_player(Player("Nut", 15))
    assert leaderboard.players[0].score == 15


def test_returning_player_name_uses_latest_spelling():
    leaderboard = Leaderboard([Player("nut", 10)])

    leaderboard.add_player(Player("Nut", 3))

    assert leaderboard.players[0].name == "Nut"
