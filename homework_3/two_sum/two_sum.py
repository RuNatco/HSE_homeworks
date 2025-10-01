def two_sum(arr, k):
    if len(arr) < 2:
        raise ValueError("Array must contain at least two elements.")
    index_map = {}
    for i, num in enumerate(arr):
        complement = k - num
        if complement in index_map:
            return tuple(sorted((index_map[complement], i)))
        index_map[num] = i
