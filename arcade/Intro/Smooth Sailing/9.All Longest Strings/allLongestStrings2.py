def allLongestStrings(inputArray):
    return (list(filter(lambda x: len(x) == len(max(inputArray, key=len)), inputArray)))

