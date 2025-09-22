def max_sum_divisible_by_2(numbers):
    if not all(isinstance(num, int) and num >= 0 for num in numbers):
        raise ValueError("Числа должны быть неотрицательными целыми")
    total_sum = sum(numbers)
    if total_sum % 2 == 0:
        return total_sum
    min_odd = float('inf')
    for num in numbers:
        if num % 2 != 0:
            min_odd = min(min_odd, num)
    return total_sum - min_odd if min_odd != float('inf') else 0
