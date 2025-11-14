def _sift_up(heap, idx):
    while idx > 0:
        parent = (idx - 1) // 2
        if heap[idx] < heap[parent]:
            heap[idx], heap[parent] = heap[parent], heap[idx]
            idx = parent
        else:
            break


def _sift_down(heap, idx, size):
    while True:
        left = 2 * idx + 1
        right = 2 * idx + 2
        smallest = idx

        if left < size and heap[left] < heap[smallest]:
            smallest = left
        if right < size and heap[right] < heap[smallest]:
            smallest = right

        if smallest != idx:
            heap[idx], heap[smallest] = heap[smallest], heap[idx]
            idx = smallest
        else:
            break


def makeheap_n_log_n(arr):
    heap = []
    for x in arr:
        heap.append(x)
        _sift_up(heap, len(heap) - 1)
    arr[:] = heap
    return arr


def makeheap(arr):
    n = len(arr)
    for i in range((n // 2) - 1, -1, -1):
        _sift_down(arr, i, n)
    return arr
