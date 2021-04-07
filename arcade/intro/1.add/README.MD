# add

Write a function that returns the sum of two numbers.

## Example

* For `param1 = 1` and `param2 = 2`, the output should be 

  `add(param1, param2) = 3`.
  

## Input/Output
* [**execution time limit**] 4 seconds (py3)
* [**input**] integer `param1`
  * Guaranteed constraints:
    * `-1000 ≤ param1 ≤ 1000`.
* [**input**] integer `param2`
  * Guaranteed constraints:
    * `-1000 ≤ param1 ≤ 1000`.
* [**output**] integer
  * The sum of the two inputs.

---

`add.py`
```python
def add(param1, param2):
    res = param1 + param2
    return res
```
`add2.py`
```python
def add(param1, param2):
    return param1 + param2
```
Just sum param1 and param2 and return.