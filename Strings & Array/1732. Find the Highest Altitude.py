from typing import List 
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        currentSum = 0
        max_altitude = 0
        for n in gain:
            currentSum+=n
            max_altitude = max(max_altitude, currentSum)
        return max_altitude
gain = [-4,-3,-2,-1,4,3,2]