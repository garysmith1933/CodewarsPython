def to_camel_case(text):
    delimiters = ['-', '_']
    idx = 0
    str = ''

    while idx != len(text):
        value = text[idx]
        
        if value in delimiters:    
            value = text[idx + 1].upper()
            
            str += value
            
            idx += 2
            continue
        
        else:
            str += value
            idx += 1
                     
    return str