# Use the collections library counter function for counting unique letters per word
from collections import Counter

def most_repeating_word(words):
  # Use dictionary to store results
  tmp = {}
  # Iterate thorugh and store word plus most common letter frequency in dictionary
  for word in words:
    c = Counter(word).most_common(1)
    print(c, "Printed C")
    tmp[word] = c[0][1]
  # Return dict key with highest value
  print(tmp, max(tmp, key = tmp.get))
  return max(tmp, key = tmp.get)
words = ['this', 'is', 'an', 'elementary', 'test', 'example']
most_repeating_word(words)

def productExceptSelf(a, n):
      
    prod = 1
    flag = 0
  
    for i in range(n):
  
        # Counting number of elements
        # which have value
        # 0
        if (a[i] == 0):
            flag += 1
        else:
            prod *= a[i]
  
    # Creating a new array of size n
    arr = [0 for i in range(n)]
  
    for i in range(n):
  
        # If number of elements in
        # array with value 0
        # is more than 1 than each
        # value in new array
        # will be equal to 0
        if (flag > 1):
            arr[i] = 0
  
        # If no element having value
        # 0 than we will
        # insert product/a[i] in new array
        elif (flag == 0):
            arr[i] = (prod // a[i])
  
        # If 1 element of array having
        # value 0 than all
        # the elements except that index
        # value , will be
        # equal to 0
        elif (flag == 1 and a[i] != 0):
            arr[i] = 0
  
        # If(flag == 1 && a[i] == 0)
        else:
            arr[i] = prod
  
    return arr
  
  
# Driver Code
n = 5
array = [10, 3, 5, 6, 2]
ans = productExceptSelf(array, n)
print(*ans)

def productArray(arr, n):
      
    # Base case
    if n == 1:
        print(0)
        return
  
    i, temp = 1, 1
  
    # Allocate memory for the product array
    prod = [1 for i in range(n)]
  
    # Initialize the product array as 1
  
    # In this loop, temp variable contains product of
    # elements on left side excluding arr[i]
    for i in range(n):
        prod[i] = temp
        temp *= arr[i]
  
    # Initialize temp to 1 for product on right side
    temp = 1
  
    # In this loop, temp variable contains product of
    # elements on right side excluding arr[i]
    for i in range(n - 1, -1, -1):
        prod[i] *= temp
        temp *= arr[i]
  
    # Print the constructed prod array
    for i in range(n):
        print(prod[i], end=" ")
  
    return
  
  
# Driver Code
arr = [10, 3, 5, 6, 2]
n = len(arr)
print("The product array is: n")
productArray(arr, n)

def printNonrepeated(string):
     
    # Calculating frequencies
    # using Counter function
    freq = Counter(string)
 
    # Traverse the string
    for i in string:
        if(freq[i] == 1):
            print(i)
            break
# Driver code
string = "geeksforgeeks"
 
# passing string to printNonrepeated function
printNonrepeated(string)