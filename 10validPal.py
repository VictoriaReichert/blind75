
def isPalindrome(s: str) -> bool:
    s = s.lower()
    cleanS = ""
    for c in s:
        if c.isalnum():
            cleanS += c

    l = len(cleanS)
    print(cleanS)
    for i in range(l//2):
        j = l-1 - i
        #print(cleanS[i], "|", cleanS[j])
        if cleanS[i] != cleanS[j]:
            return False
    return True


print(isPalindrome("Was it a car or a cat I saw?"))
# wasitacaroracatisaw