# checkPalindrome

Given the string, check if it is a [<ins>palindrome<ins/>](./PALINDROME.MD).

## Example

* For `inputString = "aabaa"`, the output should be 
  
    `checkPalindrome(inputString) = true`;

* For `inputString = "abac"`, the output should be 
  
    `checkPalindrome(inputString) = false`;

* For `inputString = "a"`, the output should be
  
    `checkPalindrome(inputString) = true.`

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


`checkPalindrome2.py`
---
```python
def checkPalindrome(s):
    for i in range(len(s)):
        if s[i] != s[-i - 1]:
            return False
    return True
```

`checkPalindrome3.py`
---
```python
def checkPalindrome(s):
    return s == s[::-1]
```