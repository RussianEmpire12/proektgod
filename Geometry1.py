# conversion_module.py

def celsius_to_fahrenheit(celsius):
    if isinstance(celsius, (int, float)):
        return (celsius * 9/5) + 32
    return None


def fahrenheit_to_celsius(fahrenheit):
    if isinstance(fahrenheit, (int, float)):
        return (fahrenheit - 32) * 5/9
    return None


def hours_to_seconds(hours):
    if isinstance(hours, (int, float)):
        return hours * 3600
    return None


def seconds_to_hours(seconds):
    if isinstance(seconds, (int, float)):
        return seconds / 3600
    return None
