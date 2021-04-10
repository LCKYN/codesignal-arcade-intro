def allLongestStrings(inputArray):
    longestLen = max(len(i) for i in inputArray)
    allLongest = [i for i in inputArray if longestLen == len(i)]
    return allLongest
