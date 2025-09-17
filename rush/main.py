#!/usr/bin/env python3

from checkmate import checkmate

# --- Test ---
# checkmate(
#     "........",
#     "....Q...",
#     "........",
#     "...K....",
#     "........",
#     "........",
#     "........",
#     "........"
# )  # should print Success
# print()

# checkmate(
#     "........",
#     "...R....",
#     "...P....",
#     "...K....",
#     "........",
#     "........",
#     "........",
#     "........"
# ) # should print Success


def main():
    board = """\
.....K
......
...P..
......
......
......\
"""
    checkmate(board)

    board = """\
R...
.K..
....
....\
"""
    checkmate(board)

    board = """\
....
.K..
..Q.
....\
"""
    checkmate(board)

    
    board = """\
R...
.K..
..P.
....\
"""
    checkmate(board)

    board = """\
...K.
.....
..B..
.....
.Q...\
"""
    checkmate(board)

    board = """\
R...B..Q
.P......
........
........
.K...P..
..Q.....
....R...
........\
"""
    checkmate(board)

    board = """\
..
..\
"""
    checkmate(board)
    board = """\
K..
. .
...\
"""
    checkmate(board)
    board = """\
..
K..\
"""
    checkmate(board)
    board = """\
.........
.........
.........
.........
.......K.
.........
.........
.........
.........\
"""
    checkmate(board)


if __name__ == "__main__":
    main()
