from typing import List


def getLastMoment(n: int, left: List[int], right: List[int]) -> int:
    if len(left) == 0:
        return n - min(right)
    elif len(right) == 0:
        return max(left)
    elif n - min(right) < max(left) or len(left) == 0:
        return n - min(right)
    else:
        return max(left)
