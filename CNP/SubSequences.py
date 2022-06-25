

def subsequences(string):
    if(len(string) == 0):
        output = []
        output.append("")
        return output
    smallerString = string[1:]
    smallerOutput = subsequences(smallerString)
    
    output = []
    for st in smallerOutput:
        output.append(st)
    for st in smallerOutput:
        appendedString = string[0] + st
        output.append(appendedString)
    return output

string = input()
ans = subsequences(string)
for ele in ans:
    print(ele)






