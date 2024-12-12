class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        vowel_list = [char for char in s if char in vowels]
        vowel_list.sort()
        print(vowel_list)
        vowel_index = 0
        result = []
        for ch in s:
            if ch in vowels:
                result.append(vowel_list[vowel_index])
                vowel_index+=1
                
            else:
                result.append(ch)
        return "".join(result)
