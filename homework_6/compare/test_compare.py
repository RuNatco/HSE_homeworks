import random
from compare import mergesort, quicksort


def test_basic():
    cases = [
        [],
        [1],
        [3, 1, 2],
        [42, 1, 42, 2],
        [-1, 0, -3, 2],
    ]
    for arr in cases:
        assert mergesort(arr.copy()) == sorted(arr)
        assert quicksort(arr.copy()) == sorted(arr)
    print("All basic tests passed.")

def test_sorting_algorithms():
    random.seed(0)

    arr_large_random = [random.randint(0, 1000000) for _ in range(5000)]
    mergesort(arr_large_random.copy())
    quicksort(arr_large_random.copy())
    print("Faster on random array:", "quicksort" if quicksort._last_duration < mergesort._last_duration else "mergesort")

    sorted_arr = list(range(900))
    mergesort(sorted_arr.copy())
    quicksort(sorted_arr.copy())
    print("Faster on sorted array:", "quicksort" if quicksort._last_duration < mergesort._last_duration else "mergesort")


def main():
    test_basic()
    test_sorting_algorithms()


if __name__ == "__main__":
    main()
