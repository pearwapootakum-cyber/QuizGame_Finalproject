import main


def fake_input(monkeypatch, answers):
    """Make input() return the given answers in order."""

    replies = iter(answers)
    monkeypatch.setattr("builtins.input", lambda prompt="": next(replies))


def test_ask_name_rejects_empty(monkeypatch, capsys):
    fake_input(monkeypatch, ["   ", "Nut"])

    assert main.ask_name() == "Nut"
    assert "cannot be empty" in capsys.readouterr().out


def test_choose_option_rejects_invalid(monkeypatch):
    fake_input(monkeypatch, ["0", "abc", "3", "2"])

    assert main.choose_option("Pick:", ["One", "Two"]) == "Two"


def test_ask_amount_rejects_out_of_range(monkeypatch):
    fake_input(monkeypatch, ["0", "6", "x", "4"])

    assert main.ask_amount(5) == 4


def in_order(monkeypatch):
    """Stop the quiz shuffling, so questions come in bank order."""

    monkeypatch.setattr(
        "quizmaster.quiz.random.sample", lambda items, k: list(items)[:k]
    )


def test_ranked_game_is_fixed_length_and_saved(monkeypatch, tmp_path, capsys):
    monkeypatch.setattr(main, "DATA_FILE", tmp_path / "leaderboard.json")
    in_order(monkeypatch)
    questions = main.create_questions()[: main.RANKED_GAME_LENGTH]
    answers = []

    for question in questions:
        answers.append(question.correct_answer)

    fake_input(monkeypatch, ["Nut", "1", "1", *answers])

    main.main()

    output = capsys.readouterr().out
    total = 0

    for question in questions:
        total += question.points

    assert output.count("Correct!") == main.RANKED_GAME_LENGTH
    assert "Your score has been saved." in output
    assert f"1. Nut - {total} points" in output
    assert (tmp_path / "leaderboard.json").exists()


def test_practice_game_is_not_saved(monkeypatch, tmp_path, capsys):
    monkeypatch.setattr(main, "DATA_FILE", tmp_path / "leaderboard.json")
    in_order(monkeypatch)
    fake_input(monkeypatch, ["Nut", "2", "1", "1", "A"])

    main.main()

    output = capsys.readouterr().out
    assert "Practice game, so your score was not saved." in output
    assert "No scores recorded yet." in output
    assert not (tmp_path / "leaderboard.json").exists()
