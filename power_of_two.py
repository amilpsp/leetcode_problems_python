from math import log10


def isPowerOfTwo(n: int) -> bool:
    while n != 0 or n < 0:
        return (log10(n) / log10(2)) % 1 == 0
