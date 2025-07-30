"""Utility functions for the notebooks"""

import random
from pathlib import Path
from datetime import date, timedelta


class Utils:
    """Utility class for common operations."""

    @staticmethod
    def project_root_path() -> Path:
        """
        Returns the root path of the project.
        """
        return Path(__file__).parent.parent

    @staticmethod
    def calculate_dob_from_age(age: int, today: date | None = None) -> date:
        """
        Calculate the date of birth from the given age.
        Return random month and day in the year of birth.

        Args:
            age (int): The age in years.

        Returns:
            date: The calculated date of birth.
        """
        if today is None:
            today = date.today()
            
        year = today.year - age
        
        
        
        start_date = today.replace(year=year) + timedelta(days=1)      
        end_date = today.replace(year=year + 1) - timedelta(days=1)
        # The date will be between today +1 until this day next year -1
        delta_days = (end_date - start_date).days
        random_days = random.randint(0, delta_days)
        dob = start_date + timedelta(days=random_days)
        return dob
