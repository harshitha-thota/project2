# test_custom_datetime.py
import pytest
from custom_datetime import CustomDateTime

# Test creating CustomDateTime with specific arguments
def test_constructor_with_arguments():
    dt = CustomDateTime(2023, 1, 1, 12, 30, 45)
    assert dt.year == 2023
    assert dt.month == 1
    assert dt.day == 1
    assert dt.hour == 12
    assert dt.minute == 30
    assert dt.second == 45

# Test creating CustomDateTime with no arguments (defaults to current date and time)
def test_constructor_defaults():
    dt = CustomDateTime()
    now = CustomDateTime.from_iso_format(CustomDateTime().to_iso_format())
    assert dt.to_iso_format().startswith(now.to_iso_format())


# Test to_iso_format method
def test_iso_format():
    dt = CustomDateTime(2023, 1, 1, 12, 30, 45)
    assert dt.to_iso_format() == "2023-01-01T12:30:45"

# Test to_human_readable_format method
def test_human_readable_format():
    dt = CustomDateTime(2023, 1, 1, 12, 30, 45)
    assert dt.to_human_readable_format() == "2023-01-01 12:30:45"

# Test validate_date class method
def test_validate_date():
    assert CustomDateTime.validate_date(2023, 1, 1) == True
    assert CustomDateTime.validate_date(2023, 2, 30) == False

# Test date_difference class method
def test_date_difference():
    dt1 = CustomDateTime(2023, 1, 1)
    dt2 = CustomDateTime(2023, 1, 10)
    assert abs(CustomDateTime.date_difference(dt1, dt2, unit='days')) == 9


# Test date_from_string static method
def test_date_from_string():
    dt_str = "2023-03-15 08:45:30"
    dt = CustomDateTime.date_from_string(dt_str)
    assert dt.to_human_readable_format() == "2023-03-15 08:45:30"
