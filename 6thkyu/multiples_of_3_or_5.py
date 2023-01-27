def solution(number):
    #if the number is negative return 0
    if number < 0: return 0

    sum = 0
    
    # from 1 to number add numbers to the list that is divisible by 3 or 5
    multiples = [num for num in range(1, number) if num % 3 == 0 or num % 5 == 0]
    
    # iterate over the list of divisible numbers
    for num in multiples: 
        #add the values of each one to the sum
        sum += num
    
    return sum