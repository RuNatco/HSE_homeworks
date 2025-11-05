import random


def kth_largest(nums, k):
    if k < 1 or k > len(nums):
        raise ValueError("k is out of bounds")

    target = len(nums) - k
    left = 0
    right = len(nums) - 1

    while True:
        if left == right:
            return nums[left]

        pivot_index = random.randint(left, right)
        pivot_value = nums[pivot_index]
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

        store_index = left
        for i in range(left, right):
            if nums[i] < pivot_value:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1

        nums[store_index], nums[right] = nums[right], nums[store_index]

        if target == store_index:
            return nums[store_index]
        elif target < store_index:
            right = store_index - 1
        else:
            left = store_index + 1
