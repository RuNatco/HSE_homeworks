import random
from iterative import mergesort_iter, quicksort_iter


def test_basic():
    cases = [
        [],
        [1],
        [3, 1, 2],
        [5, 1, 5, 3],
        [-1, 0, -3, 2],
    ]
    for arr in cases:
        assert mergesort_iter(arr.copy()) == sorted(arr)
        assert quicksort_iter(arr.copy()) == sorted(arr)
    print("All basic tests passed.")


def test_sorting_algorithms():
    random.seed(0)

    arr_large_random = [random.randint(0, 1000000) for _ in range(5000)]
    mergesort_iter(arr_large_random.copy())
    quicksort_iter(arr_large_random.copy())
    print("Faster on random array:", "quicksort" if quicksort_iter._last_duration < mergesort_iter._last_duration else "mergesort")

    sorted_arr = list(range(900))
    mergesort_iter(sorted_arr.copy())
    quicksort_iter(sorted_arr.copy())
    print("Faster on sorted array:", "quicksort" if quicksort_iter._last_duration < mergesort_iter._last_duration else "mergesort")


def main():
    test_basic()
    test_sorting_algorithms()


if __name__ == "__main__":
    main()
