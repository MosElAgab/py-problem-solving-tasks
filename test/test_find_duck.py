from src.find_duck import (find_duck)

def test_finds_lonesome_duck():
    expected = 1
    result = find_duck('🦆')

    assert result == expected


def test_finds_duck_in_the_queue():
    expected = 3
    result = find_duck('🐄 🐖 🦆 🐑 🦙')

    assert result == expected


def test_handles_non_existant_duck():
    expected = -1
    result = find_duck('🐄 🐖 🐑 🦙')

    assert result == expected