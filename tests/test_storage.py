from quizmaster.player import Player
from quizmaster.storage import JsonStorage


def test_save_and_load_players(tmp_path):
    file_path = tmp_path / "leaderboard.json"
    storage = JsonStorage(file_path)

    players = [
        Player("Nut", 10),
        Player("Alex", 15),
    ]

    assert storage.save_players(players) is True

    loaded_players = storage.load_players()

    assert len(loaded_players) == 2
    assert loaded_players[0].name == "Nut"
    assert loaded_players[0].score == 10


def test_missing_file_returns_empty_list(tmp_path):
    storage = JsonStorage(tmp_path / "missing.json")

    assert storage.load_players() == []


def test_corrupted_json_returns_empty_list(tmp_path):
    file_path = tmp_path / "broken.json"
    file_path.write_text("{broken json", encoding="utf-8")

    storage = JsonStorage(file_path)

    assert storage.load_players() == []


def test_invalid_entries_are_skipped(tmp_path):
    file_path = tmp_path / "leaderboard.json"
    file_path.write_text(
        '[{"name": "Nut", "score": 10}, {"name": "", "score": -1}]',
        encoding="utf-8",
    )

    storage = JsonStorage(file_path)
    players = storage.load_players()

    assert len(players) == 1
    assert players[0].name == "Nut"

def test_save_failure_returns_false(tmp_path):
    blocker = tmp_path / "not_a_folder"
    blocker.write_text("", encoding="utf-8")

    storage = JsonStorage(blocker / "leaderboard.json")

    assert storage.save_players([Player("Nut", 10)]) is False
