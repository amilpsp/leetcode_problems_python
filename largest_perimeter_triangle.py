from typing import List


def largestPerimeter(nums: List[int]) -> int:
    #    perimeter = 0
    #    List.sort(nums)
    #    List.reverse(nums)
    nums.sort(reverse=True)         # Useful!

    for i in range(len(nums) - 2):
        a, b, c = nums[i: i + 3]    # <--  Unpacking!
        #        a = nums[i]
        #        b = nums[i + 1]
        #        c = nums[i + 2]
        #        if a + b > c and b + c > a and a + c > b and a + b + c > perimeter:
        #            perimeter = a + b + c
        if a >= (b + c):
            continue
        else:
            return a + b + c
    return 0
