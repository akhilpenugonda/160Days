import heapq
from heapq import heappop, heappush



def calculateMax(pairs):
    pairs.sort(key = lambda e: e[0])
    pq = [] # store end time of open events
    count = 0
    i, n = 0, len(pairs)
    d = 0  # current day
    
    while i < n or pq:
        if not pq:
            d = pairs[i][0]
        while i < n and d >= pairs[i][0]: 
            heappush(pq, pairs[i][1])
            i += 1
        heappop(pq)  # attend this one event
        count += 1
        d += 1
        while pq and pq[0] < d: 
            heappop(pq)
        
    return count


class meeting:
	
	def __init__(self, start, end, pos):
		
		self.start = start
		self.end = end
		self.pos = pos

def maxMeeting(l, n):
	ans = []
	max = 0
	l.sort(key = lambda x: x.end)
	ans.append(l[0].pos)
	time_limit = l[0].end
	for i in range(1, n): 
		if l[i].start > time_limit:
			ans.append(l[i].pos)
			time_limit = l[i].end
	for i in ans:
		max += 1
	print(max)
if __name__ == '__main__':
	n = int(input())
	start = []
	end = []
	for i in range(n):
    		start.append(int(input()))
	for i in range(n):
    		end.append(int(input()))
	l = []
	for i in range(n):
		l.append(meeting(start[i], end[i], i))
	maxMeeting(l, n)
