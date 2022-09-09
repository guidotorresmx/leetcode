class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        zeroesPos = []
        
        M = len(matrix)
        N = len(matrix[0])
        
        for i in range(M):
            for j in range(N):
                if not matrix[i][j]:
                    zeroesPos.append([i, j])
        
        column = [0]*M
        for column, row in zeroesPos:
            for index in range(N):
                matrix[column][index] = 0
            for index in range(M):
                matrix[index][row] = 0
            
        #print(zeroesPos)
        #print(matrix)