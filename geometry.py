def factorial(n):
    if n < 0:
        return "Факториал не определен для отрицательных чисел"
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
import random
def generate_random_number(start, end):
    return random.randint(start, end)