data = open("./day4.txt").read().split("\n\n")
bingoBoards = []
bingoNums = data[0].split(',')
for i in range(1, len(data)):
    bingoBoards.append(data[i].split())
for num in bingoNums:
    z = 0
    while z < len(bingoBoards):
        board = bingoBoards[z]
        for i, tile in enumerate(board):
            if tile == num:
                board[i] = "X"
                row, column = divmod(i,5)
                bingoRow = True
                bingoColumn = True #persume true until checked
                for x in range(0, 5):
                    if not board[column + x*5] == 'X':
                        bingoColumn = False
                        break
                for y in range(0, 5):
                    if not board[row*5 + y] == 'X':
                        bingoRow = False
                        break
                if bingoRow or bingoColumn:
                    if len(bingoBoards) == 1:
                        sum = 0 
                        for sq in bingoBoards[0]:
                            if not sq == 'X':
                                sum+=int(sq) 
                        exit()
                    bingoBoards.remove(board) 
                    z-=1
                    break
        z+=1
