# 6 задача
from typing import List


def encode(strs: List[str]) -> str:
    newStr = ''
    newStr = ';'.join(strs)
    #print(newStr)

    if len(strs) == 0:
        return []
    oldStr = ''
    oldStr = newStr.split(';')
    return oldStr


print(encode([]))
