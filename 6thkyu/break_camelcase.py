def solution(s):
    i = 0
    res = ''
    
    while i != len(s):
        if s[i] == s[i].upper():
            res += ' '
            res += s[i]
        
        else:
            res += s[i]
           
        i += 1
    
    return res