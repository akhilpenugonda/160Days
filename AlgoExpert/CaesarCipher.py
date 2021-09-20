def caesarCipherEncryptor(string, key):
    lst = list(string)
    ret = []
    newkey = key% 26
    for i in lst:
        ret.append(chr(getOriginalLetter(ord(i), newkey)))
    return "".join(ret)
def getOriginalLetter(letter, key):
    if(letter + key < 123):
        return letter + key
    else:
        return (96 + (letter+key) % 122)


def caesarCipherEncryptor(string, key):
    newLetters = []
    newKey = key % 26
    alphabet = list("abcdefghijklmnoprstuvwxyz")
    for i in string:
        newLetters.append(getNewLetter(i, newKey, alphabet))
    return "".join(newLetters)

def getNewLetter(letter, newKey, alphabelt):
    newLetterCode = alphabelt.index(letter) + newKey
    return alphabelt[newLetterCode % 26]
