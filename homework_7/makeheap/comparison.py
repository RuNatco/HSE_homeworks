import time
import random
from makeheap import makeheap, makeheap_n_log_n

def compare_time():
    sizes = [10_000, 50_000, 100_000, 200_000]

    for n in sizes:
        arr = [random.randint(-10**6, 10**6) for _ in range(n)]

        a1 = arr[:]
        a2 = arr[:]

        t1_start = time.perf_counter()
        makeheap_n_log_n(a1)
        t1_end = time.perf_counter()

        t2_start = time.perf_counter()
        makeheap(a2)
        t2_end = time.perf_counter()

        print(f"N = {n:6d}: "
              f"makeheap_n_log_n = {t1_end - t1_start:.6f} сек, "
              f"makeheap = {t2_end - t2_start:.6f} сек")


if __name__ == "__main__":
    compare_time()
