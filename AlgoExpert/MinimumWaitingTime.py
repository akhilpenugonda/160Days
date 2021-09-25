def minimumWaitingTime(queries):
    	queries.sort()
	presentWaitingTime = 0
	totalWaitTime = 0
	for i in range(1, len(queries)):
		presentWaitingTime += queries[i-1]
		totalWaitTime += presentWaitingTime
	return totalWaitTime
		
		
