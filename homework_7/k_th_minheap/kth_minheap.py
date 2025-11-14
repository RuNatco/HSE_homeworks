import heapq

def push_heap(heap, value):
    heap.append(value)
    idx = len(heap) - 1
    while idx > 0:
        parent = (idx - 1) // 2
        if heap[idx] < heap[parent]:
            heap[idx], heap[parent] = heap[parent], heap[idx]
            idx = parent
        else:
            break


def pop_heap(heap):
    last_item = heap.pop()
    if not heap:
        return last_item
    min_item = heap[0]
    heap[0] = last_item
    idx = 0
    n = len(heap)
    while True:
        left = 2 * idx + 1
        right = 2 * idx + 2
        smallest = idx
        if left < n and heap[left] < heap[smallest]:
            smallest = left
        if right < n and heap[right] < heap[smallest]:
            smallest = right
        if smallest != idx:
            heap[idx], heap[smallest] = heap[smallest], heap[idx]
            idx = smallest
        else:
            break
    return min_item


def kth_largest_custom_heap(nums, k):
    if k < 1 or k > len(nums):
        raise ValueError("k is out of bounds")
    heap = []
    for num in nums:
        push_heap(heap, num)
        if len(heap) > k:
            pop_heap(heap)
    return heap[0]


def kth_largest_heapq(nums, k):
    if k < 1 or k > len(nums):
        raise ValueError("k is out of bounds")
    return heapq.nlargest(k, nums)[-1]
