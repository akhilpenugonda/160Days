def binarySearch(array, target):
    length = len(array)
    if(length == 0):
		return -1
    l = 0
    r = length - 1
    mid = (l+r)//2
    while l <= r:
		mid = (l+r)//2
		match = array[mid]
		if(target == match):
			return mid
		if(target > match):
			l = mid + 1
		else:
			r = mid -1
    return -1
