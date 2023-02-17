def sum_cubes(n):
    sum = 0 
    num = 1
    
    while num <= n:
        sum += num ** 3
        num += 1
        
    return sum

# Time: O(N) 
# Space: O(1)
