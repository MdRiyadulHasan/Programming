class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        result = []
        for i in range(len(number)):
            if number[i]==digit:
                result.append(number[:i]+number[i+1:])
        return max(result)
number = "1231"
digit = "1"
# Output: "231"