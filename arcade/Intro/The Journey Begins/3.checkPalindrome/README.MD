# checkPalindrome

Given the string, check if it is a [<ins>palindrome<ins/>](./PALINDROME.MD).

## Example

* For `inputString = "aabaa"`, the output should be 
  
    `checkPalindrome(inputString) = true`;

* For `inputString = "abac"`, the output should be 
  
    `checkPalindrome(inputString) = false`;

* For `inputString = "a"`, the output should be
  
    `checkPalindrome(inputString) = true.`

## Input/Output

* [**execution time limit**] 4 seconds (py3)
* [**input**] string `inputString` 
    
    A non-empty string consisting of lowercase characters.

    * Guaranteed constraints:
      * `1 ≤ inputString.length ≤ 105`.
* [**output**] boolean
    
    `true` if `inputString` is a palindrome, `false` otherwise.


---

`checkPalindrome.py`
---
```python
def checkPalindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            return False
    return True
```
From [<ins>palindrome<ins/>](./PALINDROME.MD)
> A string that doesn't changed when reversed (it reads the same backward and forward).

just check for each character from the string against the reverse string. But unnecessary to check the whole string because half of the string is the same as the other half
string

**ex.**

**length is even**

`inputString = "abccba"` 

inputString has length is 6. So half of the length is 3. 


At the first check. Check between the first element (first a) and the last element (second a). Second check. Check between the 2nd element (first b) and the 5th element (second b).Third check. Check between the 3rd element (first c) and the 4th element (second c). Now the whole string is already check (Why?). If stay continues to check. the fourth check will check between the 4th element (second c) and the 3rd element (first c). It's the same as the third check.

**length is odd**

`inputString = "abcdcba"` 

inputString has length is 7. So half of the length is 3. 

Not 4? Because 4 is the middle character in the string. It's always the same as itself. In this case `'d' == 'd'`. Then check three time same as **length is even**


`checkPalindrome2.py`


---
```python
def checkPalindrome(s):
    for i in range(len(s)):
        if s[i] != s[-i - 1]:
            return False
    return True
```

bad time complexity than `checkPalindrome.py`

`checkPalindrome3.py`
---
```python
def checkPalindrome(s):
    return s == s[::-1]
```