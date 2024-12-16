from sortedcontainers import SortedList
from bisect import bisect_left
class MyCalendar:
   

    def __init__(self):
        self.bookings = SortedList()  

    def book(self, startTime: int, endTime: int) -> bool:
        idx = self.bookings.bisect_left((startTime, endTime))
        if idx>0 and self.bookings[idx-1][1]>startTime:
            return False
        if idx<len(self.bookings) and self.bookings[idx][0]<endTime:
            return False
        self.bookings.add((startTime, endTime))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)