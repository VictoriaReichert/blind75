from collections import defaultdict
from typing import List, Tuple


# 1.
def hasDuplicate(nums: List[int]) -> bool:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False


def hasDup(nums: List[int]) -> bool:
    return len(set(nums)) < len(nums)


# 2.
def isAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


def isAn(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    countS, countT = {}, {}
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
        # print(countS[s[i]])
        # print(countS.get(s[i], 0))
    # print(countS)
    return countS == countT


# 3. 27.01
def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def twoS(nums: List[int], target: int) -> tuple[int, int]:
    dif = {}
    for i in range(len(nums)):
        if not (i in dif):
            dif[target - nums[i]] = i
        if nums[i] in dif and i != dif.get(nums[i]):
            return i, dif.get(nums[i])


# 4. 04.02
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    res = defaultdict(list)
    for s in strs:
        sortedS = ''.join(sorted(s))
        res[sortedS].append(s)
    return list(res.values())


# 5. 6.02
def freqNum(nums: List[int], k: int) -> List[int]:
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)  # 0 is default (WHAT)
    print(count)
    for n, c in count.items():  # returns pairs of key - value
        freq[c].append(n)
    print(freq)

    res = []
    for i in range(len(freq)-1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res


# 1. Поиск дубликата
# answer = hasDup([1, 0, 0, 3])
# print(answer)
# 2. Анаграмма
# sort = isAn("current", "version")
# print(sort)
# 3. Сумма
# two = twoS([3, 5, 7, 5], 10)
# print(two)
# 4. Группа анаграм
# group = groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"])
# print(group)
# 5. Топ элементов
print(freqNum([2, 1, 2, 2, 3, 5, 56], 2))
