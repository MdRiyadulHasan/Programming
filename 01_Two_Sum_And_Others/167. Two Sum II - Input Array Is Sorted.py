def twoSum(numbers, target):
    l = 0
    r = len(numbers) - 1
    while l < r:
        currentSum = numbers[l] + numbers[r]
        if currentSum == target:
            return [l + 1, r + 1]
        elif currentSum < target:
            l = l + 1
        else:
            r = r - 1
numbers = [2, 7, 11, 15]
target = 9
result = twoSum(numbers, target)
print(result)
