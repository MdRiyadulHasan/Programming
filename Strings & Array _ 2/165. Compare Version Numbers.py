class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1_list = list(map(int, version1.split("."))) 
        version2_list = list(map(int, version2.split(".")))
        max_length = max(len(version1_list), len(version2_list))
        for i in range(max_length):
            val1 = version1_list[i] if i<len(version1_list) else 0
            val2 = version2_list[i] if i<len(version2_list) else 0
            if val1<val2:
                return -1
            elif val1>val2:
                return 1
        return 0
# Input: version1 = "1.01", version2 = "1.001"

# Output: 0

