# lc :https://leetcode.com/problems/distribute-candies/
# video link :https://www.youtube.com/watch?v=_h0srmz41Gw&list=PLP446CXRka0UXaJDzvvKG3dxYvt60YQpm&index=62
import collections
from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:

        # my solution - 54 seconds
        n = len(candyType)
        # candy_types = {}
        # for i in candyType:
        #     if i in candy_types.keys():
        #         candy_types[i] = candy_types[i] + 1
        #     else:
        #         candy_types[i] = 1
        # unique_candies = int(len(candy_types.keys()))
        # if n / 2 > unique_candies:
        #     print(int(unique_candies))
        # else:
        #     print(int(n / 2))

        # solution 1 from Programming live with Larry - 39 seconds
        # return min(len(collections.Counter(candyType)), n // 2)

        # solution 2 from Programming live with Larry - 41 seconds
        # return min(len(set(candyType)), n//2)

        # my solution optimized using dict
        candy_types = {}
        for i in candyType:
            if i in candy_types.keys():
                candy_types[i] = candy_types[i] + 1
            else:
                candy_types[i] = 1

            unique_candies = int(len(candy_types.keys()))
            if unique_candies > n // 2:
                return n // 2

        # my solution optimized using set

test = Solution()
print(test.distributeCandies([1, 2, 3, 2, 5, 2]))
