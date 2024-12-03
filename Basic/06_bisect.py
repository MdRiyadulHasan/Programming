from bisect import bisect_left, bisect_right

# Sorted list
data = [1, 3, 3, 3, 5, 7, 9]

# Element to find
x = 3

# Using bisect_left
left = bisect_left(data, x)
print(f"bisect_left: {left}")  # Output: 1 (index of the first occurrence of 3)

# Using bisect_right
right = bisect_right(data, x)
print(f"bisect_right: {right}")  # Output: 4 (index after the last occurrence of 3)

# Insert positions
print(f"Insert {x} to the left: {data[:left] + [x] + data[left:]}")
print(f"Insert {x} to the right: {data[:right] + [x] + data[right:]}")
