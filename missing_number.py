# lc : https://leetcode.com/problems/missing-number/description/
# youtube : https://youtu.be/lyUu92oQQBw
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # my solution
        # missing = -1
        # length = len(nums)
        # missing_array = [0] * (length + 1)
        #
        # for i in nums:
        #     missing_array[i] = 1
        #
        # for i in range(len(missing_array)):
        #     if missing_array[i] == 0:
        #         missing = i
        #         break
        # return missing

        # efficient solution
        # length = len(nums)
        # missing_array = [0] * (length + 1)
        #
        # for i in nums:
        #     missing_array[i] = 1
        #
        # return missing_array.index(0)

        # more efficient solution
        # res = 0
        # for i in range(len(nums)):
        #     res = res + i + 1 - nums[i]
        #
        # return res

        # more efficient solution
        nums.sort()
        for i in range(0, len(nums)):
            if nums[i] != i:
                return i
        return len(nums)


test = Solution()
print(test.missingNumber([3, 0, 2]))

#