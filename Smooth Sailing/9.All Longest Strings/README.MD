# All Longest Strings

Given an array of strings, return another array containing all of its longest strings.

## Example

* For `inputArray = ["aba", "aa", "ad", "vcd", "aba"]`, the output should be

    `allLongestStrings(inputArray) = ["aba", "vcd", "aba"]`.

## Input/Output

* [**execution time limit**] 4 seconds (py3)

* [**input**] array.string `inputArray`

    A non-empty array.

  * Guaranteed constraints:
    * `1 ≤ inputArray.length ≤ 10`,
    * `1 ≤ inputArray[i].length ≤ 10`.

* [**output**] array.string

    Array of the longest strings, stored in the same order as in the `inputArray`.

---

`allLongestStrings.py`
---
```python
def allLongestStrings(inputArray):
    longestLen = max(len(i) for i in inputArray)
    allLongest = [i for i in inputArray if longestLen == len(i)]
    return allLongest
```
All of the longest strings. First of all, find the longest length first. Next, select all string are length equal to the longest length 

🥳🥳 Now, get the result 🥳🥳

`allLongestStrings2.py`
---
```python 
def allLongestStrings(inputArray):
    return (list(filter(lambda x: len(x) == len(max(inputArray, key=len)), inputArray)))
```

same as `allLongestStrings.py` 

`longestLen` = `len(max(inputArray, key=len)`
`allLongest` = `list(filter(lambda x: len(x) == len(max(inputArray, key=len)), inputArray))`

🥳🥳 Now, get the result 🥳🥳