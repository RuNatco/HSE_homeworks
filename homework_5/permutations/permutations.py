from homework_5.tracer.tracer import trace_recursive

@trace_recursive
def permute(nums):
    if not nums:
        return [[]]

    results = set()
    if len(nums) == 1:
        return [nums[:]]
    for i in range(len(nums)):
        n = nums.pop(0)
        perms = permute(nums)

        for perm in perms:
            perm.append(n)
        results.update(tuple(p) for p in perms)
        nums.append(n)
    return sorted([list(p) for p in results])
