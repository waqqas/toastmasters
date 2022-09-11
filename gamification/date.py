from datetime import date


def start_of_month(initial_date: date) -> date:
    """Return the start of month of a given date"""
    return initial_date.replace(day=1)
