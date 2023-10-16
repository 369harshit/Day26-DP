def isSubsetSum(nums, target):
    def backtrack(index, current_sum):
        # Base case: subset with the current_sum equal to the target is found
        if current_sum == target:
            return True
        
        # Explore all possible subsets
        for i in range(index, len(nums)):
            # Include the current number in the subset
            if backtrack(i + 1, current_sum + nums[i]):
                return True
            
            # Exclude the current number from the subset
            if backtrack(i + 1, current_sum):
                return True
        
        # No subset found
        return False
    
    # Start the backtracking from the first index with the initial sum of 0
    return backtrack(0, 0)

# Example usage:
nums = [1,2,3,4]
target = 4

result = isSubsetSum(nums, target)
print("Subset with sum equal to target exists:", result)
