# Use Cases of Sliding Window Technique:
# 1. To find the maximum sum of all subarrays of size K:
# Given an array of integers of size ‘n’, Our aim is to calculate the maximum sum of ‘k’ 
# consecutive elements in the array.


def max_sum(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i] + arr[i+1]
        if window_sum > max_sum:
            max_sum = window_sum

    return window_sum


# Given an array arr[] of integers and a number X, the task is to find the smallest subarray with a sum 
# greater than the given value.
# https://www.geeksforgeeks.org/smallest-window-contains-characters-string/
def smallest_subarray(arr, x):
    left = 0
    window_sum = arr[0]
    min_len = len(arr)
    for right in range(1, len(arr)):
        window_sum = window_sum + arr[right]
        if window_sum >= x:
            break
    while right < len(arr):
        min_len = min(min_len, right - left + 1)
        window_sum = window_sum - arr[left]
        left = left + 1
    
    # min_len = right - left + 1
    return min_len

# arr = [1, 4, 45, 6, 0, 19]
# x = 51
arr = [1, 11, 100, 1, 0, 200, 3, 2, 1, 250]
x = 280
print(smallest_subarray(arr, x))

# Smallest window that contains all characters of string itself
# Given a string, find the smallest window length with all distinct characters 
# of the given string. For eg. str = “aabcbcdbca”, then the result would be 4 as of the smallest window will be “dbca” .
# https://www.geeksforgeeks.org/smallest-window-contains-characters-string/
# def smallest_window_with_distinct_characters(s):

    
    
    