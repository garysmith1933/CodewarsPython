def find_even_index(arr):
    idx = 0
  
    while idx != len(arr):
        if has_equal_sides(arr, idx) == True:
            return idx
        
        else:
            idx += 1
            
    return -1

def has_equal_sides(arr, idx):
    left_sum = 0
    right_sum = 0
    
    left, right = 0, len(arr)-1
    
    while left != idx:
            left_sum += arr[left]
            left += 1
 
    while right != idx:
            right_sum += arr[right]
            right -= 1
       
    return left_sum == right_sum