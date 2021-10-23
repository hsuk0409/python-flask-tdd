def quick_sort_recursive(nums: list, start: int, end: int) -> None:
    if start <= end:
        pivot = partition(nums, start, end)

        quick_sort_recursive(nums, start, pivot - 1)
        quick_sort_recursive(nums, pivot + 1, end)


def partition(nums: list, start: int, end: int) -> int:
    pivot = start

    for i in range(pivot, end):
        if nums[i] < nums[end]:
            tmp = nums[i]
            nums[i] = nums[pivot]
            nums[pivot] = tmp
            pivot += 1

    tmp = nums[pivot]
    nums[pivot] = nums[end]
    nums[end] = tmp

    return pivot


def test_quick_sort_recursive():
    nums = [8, 4, 5, 2, 0, 12, 1, 10]
    result = [0, 1, 2, 4, 5, 8, 10, 12]

    print(nums)
    quick_sort_recursive(nums, 0, len(nums) - 1)
    print(nums)

    for idx, num in enumerate(nums):
        assert num == result[idx]
