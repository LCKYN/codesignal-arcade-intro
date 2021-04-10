# commonCharacterCount

Given two strings, find the number of common characters between them.

## Example

* For `s1 = "aabcc"` and `s2 = "adcaa"`, the output should be

    `commonCharacterCount(s1, s2) = 3`.

Strings have `3` common characters - `2` "a"s and `1` "c".

## Input/Output

* [**execution time limit**] 3 seconds (java)

* [**input**] string `s1`

    A string consisting of lowercase English letters.

  * Guaranteed constraints:
    * `1 ≤ s1.length < 15`.

* [**input**] string `s2`

    A string consisting of lowercase English letters.

  * Guaranteed constraints:
    * `1 ≤ s2.length < 15`.

[**output**] integer

---

`commonCharacterCount.py`
---
```python
def commonCharacterCount(s1, s2):
    ch = [False] * len(s2)
    result = 0
    
    for i in s1:
        for j in range(len(s2)):
            if(i == s2[j] and not ch[j]):
                result += 1
                ch[j] = True
                break
    return result
```

🥳🥳 Now, get the result 🥳🥳

`commonCharacterCount2.py`
---
```python
def commonCharacterCount(s1, s2):
    result = 0
    for x in set(s1):
        result += min(s1.count(x), s2.count(x))
    return result
```

using count function

🥳🥳 Now, get the result 🥳🥳