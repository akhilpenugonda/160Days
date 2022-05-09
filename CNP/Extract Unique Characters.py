def uniqueChar(s): 
    dict = {}
    resp = ""
    for i in s:
        if i not in dict:
            dict[i] = 1
            resp+=i
    return resp
# Main 
s=input() 
print(uniqueChar(s))