def sum_no_duplicates(l):
    from collections import Counter
    sum = 0
    
    hash = Counter(l)
    for num,count in hash.most_common():
        if count < 2:
            sum += num
            
    return sum



