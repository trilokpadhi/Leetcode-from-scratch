def twoSum(nums, target):
    # Create a dictionary to store the indices of numbers
    num_indices = {}
    
    # Iterate through the array
    for i, num in enumerate(nums):
        # Calculate the complement (number needed to reach target)
        complement = target - num
        
        # Check if the complement is already in the dictionary
        if complement in num_indices:
            # If found, return the indices of current number and its complement
            return [num_indices[complement], i]
        
        # Otherwise, add the current number to the dictionary with its index
        num_indices[num] = i
    
    # If no solution is found, return an empty list
    return []

# Example usage:
nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))  # Output: [0, 1]
