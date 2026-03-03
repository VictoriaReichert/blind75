from typing import List


# brute force O(n*n)
def twoSum(numbers: List[int], target: int) -> List[int]:
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
    return []


# two pointers O(n)
# array is sorted, so it works without any prep
def twoSum2(numbers: List[int], target: int) -> List[int]:
    l, r = 0, len(numbers) - 1
    while l < r:
        curSum = numbers[l] + numbers[r]
        if curSum > target:
            r -= 1
        elif curSum < target:
            l += 1
        else:
            return [l+1, r+1]
    return []


print(twoSum2([1, 2, 3, 4], 7))
