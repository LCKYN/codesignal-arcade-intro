def isLucky(n):
    result = 0
    digit = int(math.log10(n)) + 1
    digit //= 2
    
    l = n % 10**(digit)
    r = n // 10**(digit)
    
    while(l > 0 or r > 0):
        result = result + l % 10 - r % 10
        
        l //= 10
        r //= 10
        
    return(result == 0) 