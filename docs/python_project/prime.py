import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):  # Fixed loop range
        if n % i == 0:
            return False
    return True
