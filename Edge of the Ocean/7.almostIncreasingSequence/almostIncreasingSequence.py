def almostIncreasingSequence(sequence):
    found = 0
    
    # Two elements are always true.
    if(len(sequence) == 2): return True
    
    # found at the first element
    if(sequence[0] >= sequence[1]):
        found += 1
    
    for i in range(1, len(sequence) - 1):   
        
        # found non-increasing    
        if(sequence[i] >= sequence[i+1]):
            found += 1
            if(found == 2):
                return False
            
            # remove i
            if(sequence[i-1] < sequence[i+1]):
                continue
                
            # last element     
            if(i+2 >= len(sequence)):
                return True
                
            # remove i + 1   
            if(sequence[i] < sequence[i+2]) :
                continue
            return False
    return True