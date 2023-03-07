def find_it(seq):
    from collections import Counter
    
    count = Counter(seq)
    
    for num in count:
        if count[num] % 2 is not 0:
            return num
