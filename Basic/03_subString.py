def substrings(s):
    n = len(s)
    result = []
    for i in range(n):
        for j in range(i, n):
            result.append(s[i:j+1])
    return result

s = "hello world"
print("Substrings:", substrings(s))