import pytest

from average import average


def test_average_multiple_numbers():
    assert average([1, 2, 3, 4]) == 2.5


def test_average_single_number():
    assert average([5]) == 5


def test_average_negative_numbers():
    assert average([-1, 0, 1]) == 0


def test_average_empty_sequence_raises():
    with pytest.raises(ValueError):
        average([])
