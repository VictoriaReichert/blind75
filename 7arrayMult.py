from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    numsMult = 1
    numsMultZero = 1
    for n in nums:
        numsMult *= n
        if n != 0:
            numsMultZero *= n

    output = []
    for n in nums:
        if numsMult == 0 and n != 0:
            output.append(0)
        elif numsMult == 0 and n == 0:
            output.append(numsMultZero)
        elif numsMult != 0:
            output.append(int(numsMult/n))
    return output


def multExcludeI(nums: List[int], i: int) -> int:
    numMult = 1
    for j in range(len(nums)):
        if j != i:
            numMult *= nums[j]
    return numMult


def productExceptSelf2(nums: List[int]) -> List[int]:
    output = []
    for i in range(len(nums)):
        output.append(multExcludeI(nums, i))
    return output


def productExceptSelf3(nums: List[int]) -> List[int]:
    n = len(nums)
    output = []
    pref = 1
    suff = 1
    for i in range(n):
        output.append(pref)
        pref *= nums[i]
    #print(output)
    for i in range(n-1, -1, -1):
        #print(i)
        output[i] *= suff
        suff *= nums[i]
    return output


print(productExceptSelf3([1,2,3,4]))