# almostIncreasingSequence

Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

Note: sequence `a[0]`, `a[1]`, ..., `a[n]` is considered to be a strictly increasing if `a[0] < a[1] < ... < a[n]`. Sequence containing only one element is also considered to be strictly increasing.

## Example

* For `sequence = [1, 3, 2, 1]`, the output should be

  `almostIncreasingSequence(sequence) = false`.

  There is no one element in this array that can be removed in order to get a strictly increasing sequence.

* For `sequence = [1, 3, 2]`, the output should be
  
  `almostIncreasingSequence(sequence) = true`.

  You can remove `3` from the array to get the strictly increasing sequence `[1, 2]`. Alternately, you can remove `2` to get the strictly increasing sequence `[1, 3]`.

## Input/Output

* [**execution time limit**] 4 seconds (py3)
* [**input**] array.integer `sequence`
    * Guaranteed constraints:
      * `2 ≤ sequence.length ≤ 100,000`.
      * `-100,000 ≤ sequence[i] ≤ 100,000`.
* [**output**] boolean
    
    Return `true` if it is possible to remove one element from the array in order to get a strictly increasing sequence, otherwise return `false`.

---

`almostIncreasingSequence.py`
---
```python
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
```


>* [**input**] array.integer `sequence`
>    * Guaranteed constraints:
>      * `2 ≤ sequence.length ≤ 100,000`.
>      * `-100,000 ≤ sequence[i] ≤ 100,000`.

`sequence.length` is very long. 

**execution time limit exceeded:** when using O(n<sup>2</sup>) algorithm

`almostIncreasingSequence` is always `true`. when `sequence.length` is 2