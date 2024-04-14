# Challenge1 
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

""" 
Important Links: 
    1. Link to other problems which could be solved with two pointer method - https://leetcode.com/problems/remove-duplicates-from-sorted-array/solutions/3676877/best-method-100-c-java-python-beginner-friendly/
    2. Link has the solution using python and the two-pointer technique has been used in 4 ways - https://leetcode.com/problems/remove-duplicates-from-sorted-array/solutions/2107606/py-all-4-methods-intuitions-walk-through-wrong-answer-explanations-for-beginners-python/
    3. Video Solution Link: https://www.youtube.com/watch?v=oMr9lehS7Us
"""
from typing import List

def removeDuplicates(nums: List[int]) -> int:
    
    # Method 1:
    slow = 0
    fast = 1
    while fast < len(nums):
        if nums[slow] == nums[fast]:
            fast += 1
        else:
            slow += 1
            nums[slow] = nums[fast]
            fast += 1

    # return slow + 1

    # Method 2:
    # using for loop 
    """ 
    slow = 0
    for fast in range(len(nums)):
        if nums[slow] != nums[fast]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1
    """
    
    # Method 3:
    # Iterating through the list and popping the duplicates
    """ 
    for i in range(len(nums)-1, 0, -1):
        if nums[i] == nums[i-1]:
            nums.pop(i)
    """


# Challenge2
# https://leetcode.com/problems/remove-element/


def removeElement(nums: List[int], val: int) -> int:
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
    return slow

# Challenge3
# https://leetcode.com/problems/shuffle-the-array

def shuffle(nums: List[int], n: int) -> List[int]:
    res = []
    for i in range(n):
        res.append(nums[i])
        res.append(nums[i + n])
    return res

    
