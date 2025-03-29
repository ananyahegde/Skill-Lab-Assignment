def count_set_bits(n):
    count = 0        
    while n > 0:  
        count = count + (n & 1) 
        n = n >> 1 
    return count

def sort_by_set_bits(arr):
    sorted_arr = sorted(arr, key=count_set_bits, reverse=True)
    return sorted_arr  
arr = [5, 3, 7, 10, 14]
sorted_arr = sort_by_set_bits(arr)
print("Sorted array by set bits:", sorted_arr)


