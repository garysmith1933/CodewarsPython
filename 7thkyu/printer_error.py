def printer_error(s):
    length = len(s)
    accepted = 'abcdefghijklm'
    errors = 0
    
    for char in s:
        if char not in accepted:
            errors += 1
    
    return f'{errors}/{length}'