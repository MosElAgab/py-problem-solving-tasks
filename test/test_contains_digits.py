from src.contains_digits import contains_digits
import pytest

def test_it_only_accept_integers_by_throwing_TypeError():
    with pytest.raises(TypeError, match='input object must be an instance of integer'):
        contains_digits('', 100)
    with pytest.raises(TypeError, match='input object must be an instance of integer'):
        contains_digits(5, '')

def test_it_returns_instance_of_list():
    result = contains_digits(0, 1)
    expected = []
    assert isinstance(result, list)
    assert result == expected
    

def test_it_returns_a_list_with_single_match_when_only_one_match_exist():
    result = contains_digits(1, 9)
    expected = [1]
    assert result == expected
    result = contains_digits(5, 9)
    expected = [5]
    assert result == expected
    result = contains_digits(10, 9)
    expected = []
    assert result == expected

def test_evaluates_numerals_units_position():
    expected = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    result = contains_digits(0, 100)
    assert result == expected

def test_evaluates_numerals_all_positions():
    expected = [9, 19, 29, 39, 49, 59, 69, 79, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
    result = contains_digits(9, 100)

    assert result == expected