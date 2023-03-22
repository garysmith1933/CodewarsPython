def digital_root(n):
    if n < 10:
        return n 
    
    sum = 0

    #conver to string for iteration
    n = str(n)
    
    # iterate over n 
    for digit in n:
        #converting digit back to num for addition
        sum += int(digit)
    
    if sum < 10:
        return sum
    
    return digital_root(sum)