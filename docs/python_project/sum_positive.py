def sum_positive(numbers):
    total = 0
    for num in numbers:
        if num < 0:
            raise ValueError("Negative number detected")
        total += num
    return total
