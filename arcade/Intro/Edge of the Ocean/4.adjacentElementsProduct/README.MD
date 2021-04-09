# adjacentElementsProduct

Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

## Example

* For `inputArray = [3, 6, -2, -5, 7, 3]`, the output should be
  
  `adjacentElementsProduct(inputArray) = 21.`

  `7` and `3` produce the largest product.

## Input/Output

* [**execution time limit**] 4 seconds (py3)
* [**input**] array.integer `inputArray`
    
    An array of integers containing at least two elements.

    * Guaranteed constraints:
      * `2 ≤ inputArray.length ≤ 10`.
      * `-1000 ≤ inputArray[i] ≤ 1000`.
* [**output**] integer
    
    The largest product of adjacent elements.

---

`adjacentElementsProduct.py`
---
```python
def adjacentElementsProduct(a):
    res = a[0] * a[1]
    
    for i in range(1,len(a) - 1):
        if res < a[i] * a[i+1]:
            res = a[i] * a[i+1]
    
    return res
```