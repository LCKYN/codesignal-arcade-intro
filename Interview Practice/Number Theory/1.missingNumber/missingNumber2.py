def missingNumber(arr):
    n = len(arr)
    return n*(n+1)/2 - sum(arr)