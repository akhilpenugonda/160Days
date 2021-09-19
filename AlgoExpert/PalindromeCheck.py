def isPalindrome(string, i = 0):
    j = len(string) - 1 -i
    return True if i > j else string[i] == string[j] and isPalindrome(string, i+1)

def isPalindrome(string):
    return string == string[::-1]

def isPalindromeUsingIndexes(string):
    lIx = 0
    rIdx = len(string) -1
    while lIx < rIdx:
        if(string[lIx] != string [rIdx]):
            return False
        else:
            lIx += 1
            rIdx -=1
    return True
