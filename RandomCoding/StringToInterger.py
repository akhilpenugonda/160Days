def strToInt(s, num):
    if(len(s) == 0):
        return num
    if(s=="0"):
        return 0
    if(num == 0 and s[0] == '0'):
        return strToInt(s[1:], num)
    if(num >= 0):
        num = num * 10 + int(s[0])
        return strToInt(s[1:], num)
        
print(strToInt("1099", 0))
        
        
