import unittest
import random
from makeheap import makeheap, makeheap_n_log_n


def is_min_heap(a):
    n = len(a)
    for i in range(n):
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and a[i] > a[l]:
            return False
        if r < n and a[i] > a[r]:
            return False
    return True


def extract_all_min(a):
    res = []
    b = a[:]
    out = []
    while b:
        m = min(b)
        out.append(m)
        b.remove(m)
    return out


class TestMakeHeap(unittest.TestCase):
    def test_empty_and_single(self):
        self.assertEqual(makeheap([]), [])
        self.assertEqual(makeheap_n_log_n([]), [])
        self.assertEqual(makeheap([1]), [1])
        self.assertEqual(makeheap_n_log_n([1]), [1])

    def test_small_cases(self):
        a = [3, 2, 1, 5, 6, 4]
        b = a[:]
        self.assertTrue(is_min_heap(makeheap(a)))
        self.assertTrue(is_min_heap(makeheap_n_log_n(b)))
        self.assertEqual(extract_all_min(a), sorted(b))

    def test_with_duplicates_and_negatives(self):
        a = [5, 3, 5, -1, 0, -1, 2]
        b = a[:]
        self.assertTrue(is_min_heap(makeheap(a)))
        self.assertTrue(is_min_heap(makeheap_n_log_n(b)))
        self.assertEqual(extract_all_min(a), sorted(b))

    def test_random(self):
        random.seed(0)
        for _ in range(20):
            arr = [random.randint(-1000, 1000) for _ in range(100)]
            a = arr[:]
            b = arr[:]
            self.assertTrue(is_min_heap(makeheap(a)))
            self.assertTrue(is_min_heap(makeheap_n_log_n(b)))
            self.assertEqual(extract_all_min(a), sorted(arr))


if __name__ == '__main__':
    unittest.main()
