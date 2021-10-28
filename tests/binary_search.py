def binary_search(nums: list, target: int) -> int:
    mid = int(len(nums) / 2)
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = int((start + end) / 2)

        if nums[mid] == target:
            return mid

        if nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return -1


def test_binary_search():
    nums = [4, 5, 7, 9, 10, 14, 16, 20]

    index = binary_search(nums, 4)
    assert index == 0

    index = binary_search(nums, 20)
    assert index == 7
