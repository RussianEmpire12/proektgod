# conversion_module.py

def celsius_to_fahrenheit(celsius):
    try:
        celsius = float(celsius)
        return (celsius * 9/5) + 32
    except ValueError:
        return None


def fahrenheit_to_celsius(fahrenheit):
    try:
        fahrenheit = float(fahrenheit)
        return (fahrenheit - 32) * 5/9
    except ValueError:
        return None


def hours_to_seconds(hours):
    try:
        hours = float(hours)
        return hours * 3600
    except ValueError:
        return None


def seconds_to_hours(seconds):
    try:
        seconds = float(seconds)
        return seconds / 3600
    except ValueError:
        return None