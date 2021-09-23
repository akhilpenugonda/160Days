def bubbleSort(array):
	isSorted = False
	counter = 0
	while not sorted:
		isSorted = True
		for i in range(len(array) - 1 - counter):
    			if(array[i] > array[i+1]):
					swap(array[i], array[i+1])
					#Found a swap so mark flag and proceed to next traversal also
					isSorted = False
		counter += 1
	return sorted(array)

def swap(i,j,array):
    	array[i], array[j] = array[j], array[i]
