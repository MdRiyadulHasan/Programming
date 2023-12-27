def repeatedStringMatch(A, B):
    # Calculate the minimum number of times A needs to be repeated
    times = -(-(len(B) - 1) // len(A))  # Equivalent to ceil((len(B) - 1) / len(A))

    # Check if B is a substring of A repeated 'times' times
    if B in A * times:
        return times
    elif B in A * (times + 1):
        return times + 1
    else:
        return -1

# Example usage:
A = "abcd"
B = "cdabcdab"
result = repeatedStringMatch(A, B)
print(result)


# Given two strings a and b, return the minimum number of times you should repeat string a so that string b is a substring of it. If it is impossible for b​​​​​​ to be a substring of a after repeating it, return -1.

# Notice: string "abc" repeated 0 times is "", repeated 1 time is "abc" and repeated 2 times is "abcabc".
# a = "abcd", b = "cdabcdab"
# Output: 3
# Explanation: We return 3 because by repeating a three times "abcdabcdabcd", b is a substring of it.