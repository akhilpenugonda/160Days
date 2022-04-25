import random
count = 0
def selectRandom(x):
     
    global res
    global count
    count += 1;
    if (count == 1):
        res = x;
    else:
        i = random.randrange(count);
        if (i == count - 1):
            res = x;
    return res;
 
stream = [1, 2, 3, 4];
n = len(stream);

for i in range (n):
    print("Random number from first",
         (i + 1), "numbers is",
          selectRandom(stream[i]));