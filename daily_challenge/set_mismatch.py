# link : https://leetcode.com/problems/set-mismatch/
# video : https://www.youtube.com/watch?v=NkwtLIgnv70&list=PLP446CXRka0UXaJDzvvKG3dxYvt60YQpm&index=61
from typing import List


class Solution:

    def findErrorNums(self, nums: List[int]) -> List[int]:

        # solution 1 - naive approach
        len_nums = len(nums)
        unique_nums = set(nums)
        sum_nums = (len_nums * (len_nums + 1)) / 2
        sum_unique_nums = sum(unique_nums)
        missing = int(abs(sum_unique_nums - sum_nums))
        duplicate = sum(nums) - sum_unique_nums

        # return [missing, duplicate]

        # solution 2 - super naive approach - brute force

        for i in range(len(nums)):
            count = 0

            for j in nums:
                if i == j:
                    count = count + 1

            if count == 0:
                missing = i
            if count == 2:
                duplicate = i
            return [missing, duplicate]

        # solution 3 - using sorting
        # duplicate - numbers close to each other
        # missing - if diff between consecutive numbers == 1

        # solution 4 - using map - hashmap -
        # collection.Counter() in python
        # missing = looping over n and checking which number isnt present
        # duplicate = key whole value is more than 1

        # solution 5 - using diff array and not map , updating array value at position i with no of times it occurs
        # optimized solution of hashmap - since hashmap needs 2 entries for each key

        # solution 6 - using array and not map , but updating the input
        # the same array but not recommended coz its messes up the input space
        for i in nums:
            if nums[abs(i)-1] < 0:
                duplicate = abs(i)
            else:
                nums[abs(i)-1] = nums[abs(i)-1]*(-1)

        for i in range(len(nums)):
            if nums[i] > 0:
                missing = i+1

        return [missing, duplicate]







test = Solution()
test.findErrorNums([1, 2, 2, 4])
