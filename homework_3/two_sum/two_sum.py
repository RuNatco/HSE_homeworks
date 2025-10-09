def two_sum(arr, k):
    if len(arr) < 2:
        raise ValueError("Array must contain at least two elements.")
    indexes = {}
    for i, num in enumerate(arr):
        dif = k - num
        if dif in indexes:
            return tuple(sorted((indexes[dif], i)))
        indexes[num] = i
    print("No solution found")
    return None
