class Solution:
    def trap(self, height: List[int]) -> int:
        def getNextIndex(i,k, way=1):
            walls = 0
            water = 0
            j = i if way == 1 else k
            firstHeight = height[j]
            while True:
                #print(f"{i=} {j=} {k=}" , f"{way=} {height[j]=}")
                j += way
                if i<=j<=k and height[j] <= firstHeight :
                    pass
                else:
                    break
                walls = height[j]
                water += firstHeight - min(walls, firstHeight)
                #print(f"{water=} {walls=}<<<<<")
            return j, walls, water

        water = 0
        i , k = 0, len(height)-1
        while i < k:
            #print(f"{i=} {k=} {height[i]=} {height[k]=} ************")
            if height[i] <= height[k]:
                i, _, tempWater = getNextIndex(i, k, way=1)
                water+=tempWater
            else:
                k, _, tempWater = getNextIndex(i, k, way=-1)
                water+=tempWater
        return water
