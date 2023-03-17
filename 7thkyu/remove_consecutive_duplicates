def remove_consecutive_duplicates(s):
    new_str = []
    prev = None
    
    for word in s.split(' '):
        if word != prev:
            new_str.append(word)
        prev = word
            
    return ' '.join(new_str)