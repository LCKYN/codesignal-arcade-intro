def phoneCall(min1, min2_10, min11, s):
    
    result = 0
    
    if( s < min1):
        return 0
    
    result += 1
    s -= min1
    
    if(s < min2_10 * 9):
        return result + s // min2_10
    
    result += 9
    s -= min2_10 * 9
    
    result += s // min11
    
    return result