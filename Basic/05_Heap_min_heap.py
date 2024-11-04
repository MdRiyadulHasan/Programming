import heapq

# Initialize a list and convert it into a heap
min_heap = [5, 3, 8, 1, 7]
heapq.heapify(min_heap)

# Pop elements one by one and print them
while min_heap:
    smallest = heapq.heappop(min_heap)
    print(smallest)
