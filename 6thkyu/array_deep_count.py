def deep_count(a):
    count = 0
    for el in a:
        if isinstance(el, list):
            count += deep_count(el)
            count += 1
        
        else:
           count += 1
    return count 