from src.is_sqaure_num import (is_square_num)
import pytest


def test_it_only_accepts_num_instances_otherwise_throws_type_error():
    with pytest.raises(TypeError, match='input object must be instance of int'):
        is_square_num('')

def test_reports_false_when_not_square_number():
    assert is_square_num(2) == False
    assert is_square_num(5) == False
    assert is_square_num(12) == False

def test_reports_true_when_square_number():
    assert is_square_num(1) == True
    assert is_square_num(9) == True
    assert is_square_num(25) == True
    assert is_square_num(308025) == True