import pytest

import wages_per_day_calculation


def test_wages_per_day_calculator():
    assert wages_per_day_calculation.return_wage(80) == 45_000


def test_wages_below_fifty_percent():
    assert wages_per_day_calculation.return_wage(25) == 9000


def test_wages_above_fifty_percent():
    assert wages_per_day_calculation.return_wage(55) == 16_000


def test_wages_above_sixty_percent():
    assert wages_per_day_calculation.return_wage(65) == 21_250


def test_wages_above_seventy_percent():
    assert wages_per_day_calculation.return_wage(75) == 42_500


def test_enter_percentage_above_hundred():
    with pytest.raises(RuntimeError):
        wages_per_day_calculation.return_wage(1000)


def test_enter_percentage_below_zero():
    with pytest.raises(RuntimeError):
        wages_per_day_calculation.return_wage(-1000)


def test_enter_zero_percentage():
    with pytest.raises(RuntimeError):
        wages_per_day_calculation.return_wage(0)
