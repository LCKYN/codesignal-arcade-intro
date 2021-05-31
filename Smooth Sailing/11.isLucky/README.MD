# isLucky

Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number `n`, determine if it's lucky or not.

## Example

* For `n = 1230`, the output should be
    
    `isLucky(n) = true;`

* For `n = 239017`, the output should be

    `isLucky(n) = false.`

## Input/Output

* [**execution time limit**] 3 seconds (py3)

* [**input**]  integer `n`

    A ticket number represented as a positive integer with an even number of digits.

  * Guaranteed constraints:
    * `1 ≤ s1.length < 15`.

* [**input**] string `s2`

    A string consisting of lowercase English letters.

  * Guaranteed constraints:
    * `10 ≤ n < 1e6`.

* [**output**] boolean

    `true` if `n` is a lucky ticket number, `false` otherwise.

---

`isLucky.py`
---
```python
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
```

🥳🥳 Now, get the result 🥳🥳

`isLucky2.py`
---
```python
def isLucky(n):
    n = str(n)
    
    l = n[:len(n)//2]
    r = n[len(n)//2:]
    
    l = sum([int(i) for i in l])
    r = sum([int(i) for i in r])
    
    return not (l - r)
```

🥳🥳 Now, get the result 🥳🥳