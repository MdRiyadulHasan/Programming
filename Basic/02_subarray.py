def subarrays(nums):
    n = len(nums)
    result = []
    for i in range(n):
        for j in range(i,n):
            result.append(arr[i:j+1])
    return result


arr = [1, 2, 3, 4]
print("Subarrays:", subarrays(arr))