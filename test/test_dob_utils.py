from datetime import date

from utils import Utils



def test_calculate_dob_from_age():
    """Test the calculate_dob_from_age function."""

    today = date(2025, 7, 30)
    ages = [25, 30, 18, 40, 50]

    for age in ages:
        dob = Utils.calculate_dob_from_age(age, today)
        min_dob = today.replace(year=today.year - age)
        max_dob = date(today.year - age + 1, 7, 30)
        assert min_dob <= dob < max_dob, f"DOB {dob} not in range {min_dob} - {max_dob} for age {age}"