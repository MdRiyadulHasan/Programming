def BubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j+1]<arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr

if __name__ == '__main__':
    nums = [30,15,20,40,22,17]
    result = BubbleSort(nums)
    print(result)