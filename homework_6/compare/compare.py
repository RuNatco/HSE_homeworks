import random
import time


def time_it(func):
    def wrapper(*args, **kwargs):
        if not hasattr(wrapper, "_last_duration"):
            wrapper._last_duration = None
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        wrapper._last_duration = end_time - start_time
        print(f"Function {func.__name__} took {wrapper._last_duration:.6f} seconds in total")
        return result
    return wrapper


def _mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        _mergesort(left_half)
        _mergesort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr


@time_it
def mergesort(arr):
    return _mergesort(arr)


def _quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return _quicksort(left) + middle + _quicksort(right)


@time_it
def quicksort(arr):
    return _quicksort(arr)
