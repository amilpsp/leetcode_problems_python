from typing import List
#LINK TO PROBLEM -----> https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/


def canMakeArithmeticProgression(arr: List[int]) -> bool:
    arr.sort()
    constant = arr[1] - arr[0]
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] != constant:
            return False
    return True


def better_runtime_to_learn_from(arr: List[int]) -> bool:
    arr = sorted(arr)
    diff = arr[1] - arr[0]
    for i, item in enumerate(arr): # <--- THIS IS IT
        if i == 0:
            continue
        if item - arr[i - 1] == diff:
            continue
        else:
            return False
    return True