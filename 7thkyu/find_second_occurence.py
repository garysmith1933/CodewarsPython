def second_symbol(s, symbol):
    count_of_symbol = 0
    
    for i in range(len(s)):
        if s[i] == symbol:
            count_of_symbol += 1
        
        if count_of_symbol == 2: 
            return i
    
    return -1