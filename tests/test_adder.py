from src.debugkit import run_away


def test_run_away():
    result = run_away()
    assert result == "goodbye"
