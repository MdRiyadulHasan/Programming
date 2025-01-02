def trap( height) -> int:
        l = 0
        lMax =0
        r = len(height)-1
        rMax = 0
        count = 0
        while l<r:
            if height[l]<=height[r]:
                if height[l]>=lMax:
                    lMax = height[l]
                else:
                    count+=lMax-height[l]
                l+=1
            else:
                if height[r]>=rMax:
                    rMax=height[r]
                else:
                    count+=rMax-height[r]
                r-=1
        return count
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))