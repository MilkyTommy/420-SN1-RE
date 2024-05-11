def draw1(board):
    print("-------------")
    print("|",board[0],"|",board[1],"|",board[2],"|")
    print("-------------")
    print("|",board[3],"|",board[4],"|",board[5],"|")
    print("-------------")
    print("|",board[6],"|",board[7],"|",board[8],"|")
    print("-------------")

def draw2(board):
    for row in board :
        for cell in row :
            print("|",cell, end='')

        print("|")

board1 = [
    "X"," "," ",
    " ","O","X",
    "O","X"," "
    ]
board2 = [["X"," ","O"],
          ["X","X","O"],
          ["O","X"," "]]

# board1[6]
# board2[2][0]
draw1(board1)
draw2(board2)
