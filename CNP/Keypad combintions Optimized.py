## Read input as specified in the question.
## Print output as specified in the question.
def getString(d):
    if(d == 2):
        return "abc"
    if(d==3):
        return "def"
    if(d==4):
        return "ghi"
    if(d == 5):
        return "jkl"
    if(d==6):
        return "mno"
    if(d==7):
        return "pqrs"
    if(d==8):
        return "tuv"
    if(d==9):
        return "wxyz"
    return " "
def PrintKeyPadOpt(n, outPutSofar):
    if(n == 0):
        print(outPutSofar)
        return
    smallNumber = n // 10
    lastDigit = n % 10
    lastDigitCharacters = getString(lastDigit)
    for ch in lastDigitCharacters:
        newOutput = ch + outPutSofar
        PrintKeyPadOpt(smallNumber, newOutput)
    return
number = int(input())
PrintKeyPadOpt(number, "")