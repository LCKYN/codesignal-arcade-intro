def arrayPacking(a):
    result = 0
    for i in range(len(a)):
         result |= a[i] << 8*i
    return result