def max_subarray_sum(arr):
    max_so_far = float('-inf')  # Stores the maximum sum encountered
    max_ending_here = 0  # Stores the current sum of the subarray
    
    for num in arr:
        max_ending_here += num
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0  # Reset if negative
    
    return max_so_far

# Example usage
arr = [-2, -3, 4, -1, -2, 1, 5, -3]
print("Largest Sum of Contiguous Subarray:", max_subarray_sum(arr))
