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


def _merge(arr, temp, left, mid, right):
    i = left
    j = mid
    k = left
    while i < mid and j < right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1
    while i < mid:
        temp[k] = arr[i]
        i += 1
        k += 1
    while j < right:
        temp[k] = arr[j]
        j += 1
        k += 1
    for t in range(left, right):
        arr[t] = temp[t]


@time_it
def mergesort_iter(arr):
    n = len(arr)
    if n <= 1:
        return arr
    temp = arr.copy()
    size = 1
    while size < n:
        left = 0
        while left < n:
            mid = min(left + size, n)
            right = min(left + 2 * size, n)
            if mid < right:
                _merge(arr, temp, left, mid, right)
            left += 2 * size
        size *= 2
    return arr


def _partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


@time_it
def quicksort_iter(arr):
    n = len(arr)
    if n <= 1:
        return arr
    stack = [(0, n - 1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            p = _partition(arr, low, high)
            if p - 1 - low > high - (p + 1):
                stack.append((low, p - 1))
                stack.append((p + 1, high))
            else:
                stack.append((p + 1, high))
                stack.append((low, p - 1))
    return arr
