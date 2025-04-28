from geometry import factorial
from geometry import generate_random_number
from Geometry1 import celsius_to_fahrenheit
from Geometry1 import fahrenheit_to_celsius
from Geometry1 import hours_to_seconds
from Geometry1 import seconds_to_hours
n = 6
start = 1
end = 100
celsius = 25
fahrenheit = 10
hours = 2
seconds = 7200
print(factorial(n))
print(generate_random_number(start, end))
print('°F:', celsius_to_fahrenheit(celsius))
print('°C:', fahrenheit_to_celsius(fahrenheit))
print(hours, 'часа =', hours_to_seconds(hours), 'секунд')
print(seconds, 'секунд =', seconds_to_hours(seconds), 'часа')
