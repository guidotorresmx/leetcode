class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        I, J = len(matrix), len(matrix[0])
        data = {}
        for i, row in enumerate(matrix):
            for j, col in enumerate(row):
                data[(i,j)] = matrix[i][j]
        for i,j in data.keys():
            matrix[j][I-1-i] = data[(i,j)]
                