def mergeOverlappingIntervals(intervals):
	intervals.sort(key=lambda x:x[0])
	print(intervals)
	copyIntervals = []
	copyIntervals.append(intervals[0])
	point = 0
	for i in range(1, len(intervals)):
		if(copyIntervals[point][1] >= intervals[i][0] and copyIntervals[point][1] >= intervals[i][1]):
			continue
		elif(copyIntervals[point][1] >= intervals[i][0]):
			copyIntervals[point] = copyIntervals[point][0], intervals[i][1]
		else:
			copyIntervals.append(intervals[i])
			point += 1
	return copyIntervals

def mergeOverlappingIntervals(intervals):
				intervals.sort()
				mergedList = []
				currPtr = intervals[0]
				mergedList.append(currPtr)
				for lst in intervals[1:]:
					if lst[0] <= currPtr[1]:
						currPtr[1] = max(currPtr[1], lst[1])
					else:
						mergedList.append(lst)
						currPtr = lst
				return mergedList