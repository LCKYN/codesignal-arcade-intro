def arrayPacking(a):
    return sum(a[i] << 8*i for i in range(len(a)))