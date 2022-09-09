class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        anagramGroups = {}
        M = len(obstacleGrid)
        N = len(obstacleGrid[0])
        
        # [1, , ]
        # [ , , ]
        # [ , , ]
        obstacleGrid[0][0] = 0 if obstacleGrid[0][0] else 1 

        
        # [1,1,1]
        # [ , , ]
        # [ , , ]
        carrier = obstacleGrid[0][0]
        for i in range(1, M):
            if obstacleGrid[i][0]:
                carrier = 0
            obstacleGrid[i][0] = carrier

        # [1,1,1]
        # [1, , ]
        # [1, , ]
        carrier = obstacleGrid[0][0]            
        for j in range(1, N):
            if obstacleGrid[0][j]:
                carrier = 0
            obstacleGrid[0][j] = carrier
        
        # [1,1,1]
        # [1,2,3]
        # [1,3,6]
        for i in range(1, M):
            for j in range(1, N):
                if obstacleGrid[i][j]:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i][j-1] + obstacleGrid[i-1][j] 
                
        print(obstacleGrid)

        return obstacleGrid[-1][-1]