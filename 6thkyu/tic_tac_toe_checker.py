def is_solved(board):
    if horizontal(board, 2) == True:
        return 2
    if vertical(board, 2) == True:
        return 2
    
    if diagonal(board, 2) == True:
        return 2
    
    if reverse_diagonal(board, 2) == True:
        return 2
    
    if reverse_diagonal(board, 1) == True: 
        return 1
    if diagonal(board, 1) == True: 
        return 1
    
    if vertical(board, 1) == True:
        return 1
    
    if horizontal(board, 1) == True:
        return 1
    
    if is_draw(board) == True:
        return 0
    
    else:
        return -1

   
# horizonally, checks each row
def horizontal(board, marker):
    curr_row = 0
    
    while curr_row <= 2:     
        if board[curr_row][0] == marker and board[curr_row][1] == marker and board[curr_row][2] == marker:
            return True
        # check the next row
        curr_row += 1
        
    return False

# vertical, checks each column
def vertical(board, marker):
    curr_col = 0
    
    while curr_col <= 2:     
        if board[0][curr_col] == marker and board[1][curr_col] == marker and board[2][curr_col] == marker:
            return True
        # check the next col
        curr_col += 1
        
    return False

# diagonal
def diagonal(board, marker):
    return board[0][0] == marker and board[1][1] == marker and board[2][2] == marker

# reverse diagonal
def reverse_diagonal(board, marker):
    return board[0][2] == marker and board[1][1] == marker and board[2][0] == marker
    
# each position needs to be taken up without a winner  
def is_draw(board):
    for row in board:
        for pos in row:
            if pos == 0:
                return False
            
    return True