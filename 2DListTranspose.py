""" print transpose of 2d grid """


grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


grid = [[1,1,1,1,1],
      [2,2,2,2,2],
      [3,3,3,3,3],
      [4,4,4,4,4],
      [5,5,5,5,5]]

def print2dListTranspose(twoDList):
    numOfEmbeddedList, lengthOfEmbeddedList = 0,0
    numOfEmbeddedList = len(twoDList)
    lengthOfEmbeddedList = len(grid[0])

    for i in range(lengthOfEmbeddedList) :
        for j in range(numOfEmbeddedList):
            print(grid[j][i], end="")
        print("")


        
print2dListTranspose(grid)
