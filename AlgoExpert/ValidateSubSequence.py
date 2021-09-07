#Two pointer is the Main Logic Behind
def isValidSubsequence(array, seq):
    arrIdx = 0
    seqIdx = 0
    while(arrIdx < len(array) and seqIdx < len(seq)):
        if(array[arrIdx] == seq[seqIdx]):
            seqIdx += 1
        arrIdx += 1
    return seqIdx == len(seq)



def isValidSubsequenceWithArrayDirect(array, seq):
    seqIdx = 0
    for i in array:
		if(seq[seqIdx] == i):
			seqIdx += 1
		if(seqIdx == len(seq)):
			break
    return seqIdx == len(seq)






#Trail Failed
def isValidSubsequenceTrial(array, sequence):
    seqInit = 0
    flag = False
    if(len(array) < len(sequence)):
        return False
    for i in range(len(sequence)):
        for j in range(seqInit, len(array)):
            if(array[j] == sequence[i]):
                seqInit = j + 1
                if(i + 1 == len(sequence)):
                    return True
                if(seqInit > len(array)-1):
                    return False
                continue
    if(i == len(sequence)):
        return True

print(isValidSubsequence( [5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10, 11, 11, 11, 11]))
print(isValidSubsequence( [5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 25, 6, -1, 8, 10, 12]))
print(isValidSubsequence( [5, 1, 22, 25, 6, -1, 8, 10], [5, 26, 22, 8]))
#[5, 1, 22, 25, 6, -1, 8, 10]