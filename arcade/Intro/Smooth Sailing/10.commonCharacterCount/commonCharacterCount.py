def commonCharacterCount(s1, s2):
    ch = [False] * len(s2)
    result = 0
    
    for i in s1:
        for j in range(len(s2)):
            if(i == s2[j] and not ch[j]):
                result += 1
                ch[j] = True
                break
    return result
