#!/usr/bin/env python3

def find_position(board, char):
    """Find first occurrence of char on board, return (row, col)."""
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == char:
                return (i, j)
    return None


def in_bounds(x, y, n):
    return 0 <= x < n and 0 <= y < n


def is_king_in_check(*rows):
    try:
        board = [list(r) for r in rows]
        n = len(board)

        king_pos = find_position(board, "K")
        if not king_pos:
            print("No king found!")
            return
        kx, ky = king_pos

        # Directions for rays
        rook_dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        bishop_dirs = [(-1,-1),(-1,1),(1,-1),(1,1)]
        queen_dirs = rook_dirs + bishop_dirs

        # Pawn attacks (assuming pawns go DOWN the board, i.e. from top to bottom)
        pawn_attacks = [(-1,-1),(1,-1)]

        # Scan all pieces
        for y in range(n):
            for x in range(n):
                piece = board[y][x]
                if piece == "." or piece == "K":
                    continue

                dx, dy = kx - x, ky - y

                if piece == "Q":
                    dirs = queen_dirs
                elif piece == "R":
                    dirs = rook_dirs
                elif piece == "B":
                    dirs = bishop_dirs
                elif piece == "P":
                    dirs = pawn_attacks
                else:
                    dirs = []

                # Handle ray pieces
                if piece in "QRB":
                    for ddx, ddy in dirs:
                        cx, cy = x+ddx, y+ddy
                        while in_bounds(cx, cy, n):
                            if board[cy][cx] != ".":
                                if (cx, cy) == (kx, ky):
                                    print("Fail1")
                                    return
                                break
                            else:
                                board[cy][cx] = "*"
                            cx += ddx
                            cy += ddy

                # Handle pawn
                elif piece == "P":
                    for ddx, ddy in pawn_attacks:
                        board[y+ddy][x+ddx] = "*"
                        if (x+ddx, y+ddy) == (kx, ky):
                            print("Fail2")
                            return


        print("Success")

        for row in board:
            print(" ".join(row))

    except Exception as e:
        print(f"Error: {e}")
        return


# --- Test ---
is_king_in_check(
    "........",
    "....Q...",
    "........",
    "...K....",
    "........",
    "........",
    "........",
    "........"
)  # should print Success
print()

is_king_in_check(
    "........",
    "...R....",
    "...P....",
    "...K....",
    "........",
    "........",
    "........",
    "........"
) # should print Success



