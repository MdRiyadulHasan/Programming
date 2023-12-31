# https://leetcode.com/problems/integer-to-english-words/

class Solution:
    def numberToWords(self, num: int) -> str:
        dic = {
          1000000000: 'Billion',
          1000000: 'Million',
          1000: 'Thousand',
          100: 'Hundred',
          90: 'Ninety',
          80: 'Eighty',
          70: 'Seventy',
          60: 'Sixty',
          50: 'Fifty',
          40: 'Forty',
          30: 'Thirty',
          20: 'Twenty',
          19: 'Nineteen',
          18: 'Eighteen',
          17: 'Seventeen',
          16: 'Sixteen',
          15: 'Fifteen',
          14: 'Fourteen',
          13: 'Thirteen',
          12: 'Twelve',
          11: 'Eleven',
          10: 'Ten',
          9: 'Nine',
          8: 'Eight',
          7: 'Seven',
          6: 'Six',
          5: 'Five',
          4: 'Four',
          3: 'Three',
          2: 'Two',
          1: 'One'
        }
        if num==0:
            return "Zero"
        result=""
        
        for k, v in dic.items():
            count=0
            if num>=k:
               count=num//k
               num%=k
               if count>1 or k>=100:
                   result= result+" "+self.numberToWords(count)+" "+v
               else:
                   result+=" "+v
        result=result[1:]
        return result
           #returning answer removing the last blank space
ob = Solution()
num = 75234567
result = ob.numberToWords(num)
print(result) 
