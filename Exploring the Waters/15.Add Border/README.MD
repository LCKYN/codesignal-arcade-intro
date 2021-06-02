# Add Border

Given a rectangular matrix of characters, add a border of asterisks(`*`) to it.

## Example

- For
    ```python
    picture = ["abc",
               "ded"]
    ```

    the output should be
    ```python
        addBorder(picture) = ["*****",
                              "*abc*",
                              "*ded*",
                              "*****"]
    ```
## Input/Output

- [execution time limit] 4 seconds (py3)

- [input] array.string `picture`

    A non-empty array of non-empty equal-length strings.

    Guaranteed constraints:
    - `1 ≤ picture.length ≤ 100`.
    - `1 ≤ picture[i].length ≤ 100`.

- [output] array.string

    The same matrix of characters, framed with a border of asterisks of width 1.

---

## `addBorder.py`

```python
def addBorder(p):
    return ["*" * (len(p[0]) + 2)] + ["*" + i + "*" for i in p] + ["*" * (len(p[0]) + 2)]
```

🥳🥳 Now, get the result 🥳🥳

---
## `addBorder2.py`
```python
def addBorder(p):
    temp = len(p[0]) + 2
    return ["*" * temp] + ["*" + i + "*" for i in p] + ["*" * temp]
```

🥳🥳 Now, get the result 🥳🥳

---