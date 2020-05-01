from math import sqrt
##print the line
def printLine(n):
    for i in range((n+4)*3):
          print("-", end='')
    print()
##print the board
def printBoard(board, rowSum, colSum):
    listboard=[n for a in board for n in a]
    print(" ", end="")
    for i in range(len(board)):
        print(" |", i + 1, end='')
    print(" | ")
    for i in range(len(board)):
        printLine(len(board))
        print(i+1, "|", end="")
        for j in range(len(board)):
            print("", listboard[i * len(board)+j], "|", end='')
        print("",rowSum[i],end='')
        print()
    printLine(len(board))
    print("  |", end='')
    for i in range(len(board)):
        print("", colSum[i], "|", end='')
##Convert one-dimensional list to two-dimensional list
def  list2board(L):
    board=[]
    n=int(sqrt(len(L)))
    for i in range(n):
       board1=[]
       for j in range(n):
          board1.append(L[n*i+j])
       board.append(board1)
    return board
##Determine whether the conditions are met
def isSolution(board, rowSum, colSum):
    for i in range(len(board)):
        row=[]
        for j in range(len(board)):
               if board[i][j]==1:
                   row.append(j+1)
        if rowSum[i] != sum(row):
            return "False"
    for i in range(len(board)):
        col=[]
        for j in range(len(board)):
               if board[j][i]==1:
                   col.append(j+1)
        if colSum[i] != sum(col):
            return "False"
    return "True"
#Sum is a fixed value algorithm
def get_val(x, i, has, val, result):
    if i > len(x) - 1:
        return
    if has + list[i] == val:
        x[i] = 1
        result.append([])
        for j in range(len(x)):
            result[len(result) - 1].append(x[j])
        x[i] = 0
    x[i] = 1  #If satisfied
    get_val(x, i + 1, has + list[i], val, result)
    x[i] = 0  #If not satisfied
    get_val(x, i + 1, has, val, result)
#combination
def RecursionFunc(arr1, arrList):
    if (arrList):
        string = []
        for x in arr1:
            for y in arrList[0]:
                string.append(x + y)
        result = RecursionFunc(string, arrList[1:])
        return result
    else:
        return arr1
#Solution
def backtrack(rowSum, colSum):
    candirow = []
    for i in range(len(rowSum)):
        result = []
        get_val(x, 0, 0, rowSum[i], result)
        candirow.append(result)
    caseslist = RecursionFunc(candirow[0], candirow[1:])
    #  each case
    for ele in caseslist:
        board = list2board(ele)
        if isSolution(board, rowSum, colSum) == "True":  #Because only the first solution needs to be found
            return board
    return 0

if __name__ == '__main__':
    # L = [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1]
    # board = list2board(L)
    # rowSum = [6, 0, 6, 14, 12]
    # colSum = [1, 7, 9, 12, 10]
    # #print(board)
    # #printBoard(board, rowSum, colSum)
    # print(isSolution(board, rowSum, colSum))

    rowSum = [4, 5, 3, 5]
    colSum = [10, 3, 1, 6]
    list = [i+1 for i in range(len(rowSum))]
    x = [0 for i in range(len(rowSum))]
    board = backtrack(rowSum, colSum)
    printBoard(board, rowSum, colSum)
