from typing import List
# LINK TO PROBLEM ----->  https://leetcode.com/problems/two-sum/


def two_sum(nums: List[int], target: int) -> List[int]:
    num_map = {}  # dictionaries in python work like hashmaps in java (?)
    solution = []
    for i in range(0, len(nums)):
        if target - nums[i] in num_map:
            solution.append(num_map.get(target - nums[i]))
            solution.append(i)
            return solution
        num_map[nums[i]] = i
    return solution


# O(n) Solution
numbers = [3, 3]
print(two_sum(numbers, 6))

# Success

#    for i in range(0, len(nums)):
#        for j in range(i + 1, len(nums)):
#            if nums[i] + nums[j] == target:
#                return i, j
#            j += 1
#        i += 1

#    First try, failed, struggling
#    i = 1
#    for number in nums:
#        while i in range(nums.index(number) + 1, len(nums)-1):
#            num2 = nums[i]
#            if number + num2 == target:
#                return nums.index(number), i
#            else:
#                i += 1
