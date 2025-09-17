#!/usr/bin/env python3
def check_king_in_check(*rows):
    try:
        # Build the board as a list of lists
        board = [list(r) for r in rows]
        n = len(board)

        # Find the king's position
        king_pos = None
        for i in range(n):
            for j in range(n):
                if board[i][j] == 'K':
                    king_pos = (i, j)
                    break
            if king_pos:
                break

        if not king_pos:
            print("Error: No King found")
            return

        ki, kj = king_pos

        # Directions for rook/queen (straight lines)
        straight_dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        # Directions for bishop/queen (diagonals)
        diag_dirs = [(1,1), (1,-1), (-1,1), (-1,-1)]
        # Knight moves
        knight_moves = [
            (2,1), (2,-1), (-2,1), (-2,-1),
            (1,2), (1,-2), (-1,2), (-1,-2)
        ]
        # Pawn attacks (assuming pawns move DOWN the board)
        pawn_moves = [(1,-1), (1,1)]

        def scan_dirs(directions, attackers):
            for di, dj in directions:
                x, y = ki+di, kj+dj
                while 0 <= x < n and 0 <= y < n:
                    cell = board[x][y]
                    board[x][y] = "x"
                    if cell != '.':  # found a piece
                        if cell in attackers:
                            return True
                        else:
                            break  # blocked
                    x += di
                    y += dj
            return False

        # Check rook/queen
        if scan_dirs(straight_dirs, {'R','Q'}):
            print("Success")
            return
        # Check bishop/queen
        if scan_dirs(diag_dirs, {'B','Q'}):
            print("Success")
            return
        # Check knights
        for di, dj in knight_moves:
            x, y = ki+di, kj+dj
            if 0 <= x < n and 0 <= y < n and board[x][y] == 'N':
                print("Success")
                return
        # Check pawns
        for di, dj in pawn_moves:
            x, y = ki+di, kj+dj
            if 0 <= x < n and 0 <= y < n and board[x][y] == 'P':
                print("Success")
                return

        # If no attackers found
        print("Fail")

        # --- Print the board nicely ---
        for row in board:
            print(" ".join(row))
        print() 

    except Exception:
        # In case something goes wrong (weird board, bad input, etc.)
        return
    
check_king_in_check(
    "........",
    "....Q...",
    "........",
    "...K....",
    "........",
    "........",
    "........",
    "........"
)
