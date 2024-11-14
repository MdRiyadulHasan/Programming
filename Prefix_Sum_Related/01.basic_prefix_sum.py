def prefix_sum(arr):
    prefix = [0] * len(arr)
    prefix[0] = arr[0]
    for i in range(1, len(arr)):
        prefix[i] = arr[i]+prefix[i-1]
    return prefix

def range_sum(prefix, l, r):
    if l==0:
        return prefix[r]
    else:
        return prefix[r] - prefix[l-1]
arr = [3, 2, 1, 4, 5]
print(prefix_sum(arr))
print(range_sum(prefix, 1, 3))