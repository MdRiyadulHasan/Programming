from typing import List 
class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:

        event1Start = event1[0].split(':')
        event1End = event1[1].split(':')

        event2Start = event2[0].split(':')
        event2End = event2[1].split(':')

        return False if event2Start > event1End or event1Start > event2End else True    