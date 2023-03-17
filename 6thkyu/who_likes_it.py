def likes(names):
    if not names:
        return "no one likes this"
    
    match len(names):
        case 1:
            return f'{names[0]} likes this'
        
        case 2:
            return f'{names[0]} and {names[1]} like this'
            
        case 3:
            return f'{names[0]}, {names[1]} and {names[2]} like this'
        
        case 4:
            return f'{names[0]}, {names[1]} and 2 others like this'
        
        case _:
            return f'{names[0]}, {names[1]} and {len(names) - 2} others like this'