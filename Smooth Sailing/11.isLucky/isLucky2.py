def isLucky(n):
    n = str(n)
    
    l = n[:len(n)//2]
    r = n[len(n)//2:]
    
    l = sum([int(i) for i in l])
    r = sum([int(i) for i in r])
    
    return not (l - r)