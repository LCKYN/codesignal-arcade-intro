def adjacentElementsProduct(a):
    res = a[0] * a[1]
    
    for i in range(1,len(a) - 1):
        if res < a[i] * a[i+1]:
            res = a[i] * a[i+1]
    
    return res