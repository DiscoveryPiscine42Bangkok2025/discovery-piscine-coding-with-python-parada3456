#!/usr/bin/env python3
def checkmate(board_raw):
    try:
        
        # board = [list(r) for r in rows]
        board = [list(row) for row in board_raw.strip().split("\n")]
        if(isBoardValid(board)):         
            
            straight_dir = [(1,0), (-1,0), (0,1), (0,-1)]
            diag_dir = [(1,1), (1,-1), (-1,1), (-1,-1)]
            pawns_dir = [(1,-1), (1,1)]
            
            for i, row in enumerate(board):
                for j, col in enumerate(row):
                    if col == "P":
                        if isFoundKingFirst((i, j), pawns_dir, board):
                            display(board)
                            print("Fail by P\n")
                            return
                    elif col == "B":
                        if isFoundKingFirst((i, j), diag_dir, board):
                            display(board)
                            print("Fail by B\n")
                            return
                    elif col == "R":
                        if isFoundKingFirst((i, j), straight_dir, board):
                            display(board)
                            print("Fail by R\n")
                            return
                    elif col == "Q":
                        if isFoundKingFirst((i, j), straight_dir + diag_dir, board):
                            display(board)
                            print("Fail by Q\n")
                            return
                    else:
                        continue

            display(board)
            print("Success\n")
            return
        
        display(board)
        print("Error: board not valid\n")
        return

    except Exception as e:
        display(board)
        print(f"Error: {e}\n")
        return
    

def isBoardValid(board):
    k_count = 0
    if 1 <= len(board) > 8 :
        return 0
    for row in board:
        if len(row) != len(board) or 1 <= len(row) > 8:
            return 0
        for col in row:
            if col == 'K':
                k_count +=1 
            if col not in "KQRPB.":
                return 0
        
    return 0 if k_count > 1 or k_count == 0 else 1

# def findPos(piece, board):
#     for i, row in enumerate(board):
#         for j, col in enumerate(row):
#             if col == piece:
#                 return (i, j)
#     return None
    
def isFoundKingFirst(piece_pos, piece_dirs, board):
    if piece_pos is None:
        return False
    
    start_r, start_c = piece_pos
    size = len(board)

    for dr, dc in piece_dirs:
        r, c = start_r + dr, start_c + dc
        while 0 <= r < size and 0 <= c < size:
            cell = board[r][c]
            if cell != ".":
                if cell == 'K':
                    return True   
                else:
                    return False  
            r += dr
            c += dc
    return False 

def display(board):
    for row in board:
        print(" ".join(row))
