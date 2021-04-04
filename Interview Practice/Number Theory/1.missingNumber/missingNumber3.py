def missingNumber(arr):
    res = 0
    for i,v in enumerate(arr):
        res ^= (i + 1) ^ v
    return res