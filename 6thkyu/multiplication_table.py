def multiplication_table(size):
    table = []
    current_row = []
    base = 1
    prev_num = 0
    
    # while length of table is less than size
    while len(table) < size:
        num = prev_num + base
        
        # if length of current row does not equal to size 
        if len(current_row) != size:
            # push into current row
            current_row.append(num)
            prev_num = num
        
        # else we push current row into table, reset the row, increment base, reset prev num to 0
        else:
            table.append(current_row)
            prev_num = 0 
            base += 1
            current_row = []
                
    return table