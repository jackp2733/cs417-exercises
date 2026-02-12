from datetime import datetime


def days_between(date1: str, date2: str) -> int:
    fmt = "%Y-%m-%d"
    d1 = datetime.strptime(date1, fmt)
    d2 = datetime.strptime(date2, fmt)
    return abs((d2 - d1).days)


def is_weekend(date_str: str) -> bool:
    fmt = "%Y-%m-%d"
    dt = datetime.strptime(date_str, fmt)
    return dt.weekday() >= 5