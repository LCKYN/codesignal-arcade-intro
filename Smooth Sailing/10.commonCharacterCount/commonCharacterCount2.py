def commonCharacterCount(s1, s2):
    result = 0
    for x in set(s1):
        result += min(s1.count(x), s2.count(x))
    return result
