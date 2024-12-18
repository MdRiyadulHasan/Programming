from typing import List 
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []
        for person, start, end in trips:
            events.append((start, person))
            events.append((end, -person))
        events.sort()
        total_person = 0
        for location, person in events:
            total_person+=person
            if total_person>capacity:
                return False
        return True