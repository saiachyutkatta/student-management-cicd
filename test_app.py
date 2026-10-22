
import pytest
from app import calculate_average


def test_average():
    assert calculate_average([80, 90, 70]) == 80


def test_single_mark():
    assert calculate_average([95]) == 95


def test_empty_marks():
    with pytest.raises(ValueError):
        calculate_average([])
