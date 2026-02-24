from typing import List


def longestConsecutiveDraft(nums: List[int]) -> int:
    min = nums[0]
    index = 0
    for i in range(len(nums)):
        if nums[i] < min:
            min = nums[i]
            index = i
    return min


def find(parent: {}, x: int) -> int:
    if parent[x] != x:
        return find(parent, parent[x])
    else:
        return x


def countGraph(parent: {}, x: int, count: int) -> int:
    count += 1
    if parent[x] != x:
        return countGraph(parent, parent[x], count)
    else:
        return count


def longestConsecutive(nums: List[int]) -> int:
    graph = {}
    for i in range(len(nums)):
        graph[nums[i]] = nums[i]

    for n in graph.keys():
        if n+1 in graph.keys():
            graph[n+1] = n

    #print(graph)
    count = 0
    for n in graph.keys():
        c = countGraph(graph, n, 0)
        if c > count:
            count = c
    return count


print(longestConsecutive([0,3,2,5,4,6,1,1]))