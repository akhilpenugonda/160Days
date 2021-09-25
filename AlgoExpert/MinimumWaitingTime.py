def minimumWaitingTime(queries):
    	queries.sort()
	presentWaitingTime = 0
	totalWaitTime = 0
	for i in range(1, len(queries)):
		presentWaitingTime += queries[i-1]
		totalWaitTime += presentWaitingTime
	return totalWaitTime
		
		
def minimumWaitingTime(queries):
    	queries.sort()
	totalWait = 0
	for idx, value in enumerate(queries):
		queriesLeft = len(queries) - (idx + 1)
		totalWait += value * queriesLeft
	return totalWait
