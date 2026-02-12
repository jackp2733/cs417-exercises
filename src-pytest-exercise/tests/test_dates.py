import pytest
from timeutils.dates import days_between, is_weekend

def test_days_between_same_day():
    assert days_between("2025-03-15", "2025-03-15") == 0


def test_days_between_one_week():
    assert days_between("2025-03-01", "2025-03-08") == 7


def test_days_between_order_independent():
    assert days_between("2025-01-01", "2025-06-15") == days_between("2025-06-15", "2025-01-01")


def test_is_weekend_saturday():
    assert is_weekend("2025-03-15") is True


def test_is_weekend_weekday():
    assert is_weekend("2025-03-17") is False


def test_days_between_invalid_format():
    with pytest.raises(ValueError):
        days_between("not-a-date", "2025-03-15")
