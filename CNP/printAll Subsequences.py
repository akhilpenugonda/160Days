from http.client import NETWORK_AUTHENTICATION_REQUIRED


def printSubs(s, o):
    if(len(s) == 0):
        print(o)
        return
    printSubs(s[1:], o)
    newOutput = o + s[0]
    printSubs(s[1:], newOutput)
    