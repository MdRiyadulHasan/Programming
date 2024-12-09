def reverseStr(s: str, k: int) -> str:
    s = list(s)
    for i in range(0, len(s), 2 * k):
        # Reverse the first k characters in every 2k block
        s[i:i+k] = reversed(s[i:i+k])
    return ''.join(s)
# Input: s = "abcdefg", k = 2
# Output: "bacdfe