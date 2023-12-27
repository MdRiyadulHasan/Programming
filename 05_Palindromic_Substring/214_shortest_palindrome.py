def shortestPalindrome(s):
    if not s:
        return ""

    # Concatenate the string with its reverse, separated by a special character
    combined = s + "#" + s[::-1]

    # Build the KMP table
    table = [0] * len(combined)
    j = 0
    for i in range(1, len(combined)):
        while j > 0 and combined[i] != combined[j]:
            j = table[j - 1]
        if combined[i] == combined[j]:
            j += 1
        table[i] = j

    # The length of the longest prefix that is also a suffix
    palindrome_prefix_length = table[-1]

    # The characters to be added to the beginning of the string
    addition = s[palindrome_prefix_length:][::-1]

    return addition + s

# Example usage:
s = "aacecaaa"
result = shortestPalindrome(s)
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length_s = len(s)
        rep = ''
        for i in range(length_s//2):
            rep+=s[i]
            if length_s%len(rep)==0:
                if rep*(length_s//len(rep))==s:
                    return True
        return False
print(result)
