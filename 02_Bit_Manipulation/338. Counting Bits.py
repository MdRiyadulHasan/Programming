from typing import List 
def countBits(num: int) -> List[int]:
    counter = [0]
    for i in range(1, num+1):
        counter.append(counter[i >> 1] + i % 2)
    return counter
n = 5 
result =countBits(n)
print("Result:", result)
