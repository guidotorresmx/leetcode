class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        
        I, J = len(matrix), len(matrix[0])
        for i in range(I-1):
            for j in range(i+1, J):
                matrix[j][i], matrix[i][j] =  matrix[i][j], matrix[j][i]
                
        for i in range(I):
            for j in range(J//2):
                matrix[i][j], matrix[i][J-1-j] =  matrix[i][J-1-j], matrix[i][j]

        
        
        
        
        """
        I, J = len(matrix), len(matrix[0])
        data = {}
        for i, row in enumerate(matrix[:len(matrix)//2 + len(matrix)%2]):
            for j, col in enumerate(row[:len(row)//2 + len(row)%2]):
                matrix[j][I-1-i], matrix[i][j] =  matrix[i][j], matrix[j][I-1-i]
        """     