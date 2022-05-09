from heapq import heappush, heappop
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
def minMeetingRooms(slots):
    if(len(slots) == 0):
        return 0
    sorted_slots = sorted(slots, key= lambda slot:(slot.start, slot.end))
    count = 0
    heap = []
    for it in sorted_slots:
        start, end = it.start, it.end
        while heap and heap[0] <= start:
            heappop(heap)
        heappush(heap, end)
        count =  max(len(heap), count)
    return count

print(minMeetingRooms([Interval(0,30),Interval(6,80),Interval(5,10)]))