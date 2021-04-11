# shapeArea

Below we will define an `n`-interesting polygon. Your task is to find the area of a polygon for a given `n`.

A `1`-interesting polygon is just a square with a side of length `1`. An `n`-interesting polygon is obtained by taking the `n - 1`-interesting polygon and appending `1`-interesting polygons to its rim, side by side. You can see the `1`-, `2`-, `3`- and `4`-interesting polygons in the picture below.

![pic-shape-area](./picture/area.png)

## Example

* For `n = 2`, the output should be
 
  `shapeArea(n) = 5;`

* For `n = 3`, the output should be

  `shapeArea(n) = 13`.

## Input/Output

* [**execution time limit**] 4 seconds (py3)
* [**input**] integer `n`
    * Guaranteed constraints:
      * `1 ≤ n < 10,000`.
* [**output**] integer
    
    The area of the `n`-interesting polygon.

---

`shapeArea.py`
---

```python
def shapeArea(n):
    return 2 * n * n - 2 * n + 1
```

For every n (1 ≤ n <10,000). Middle takes 1 square.
```python 
result = 1
```
`Horizontal` take 2 (right and left) slots for every n that it increases. 

`Vertical` take 2 (top and bottom) slots for every n that it increases. 

when `n ≥ 2`

```python 
result = 1 + 4 * (n - 1)
```

`Diagonal`

`n` = `3` take `(1 * 4)` slots

`n` = `4` take `(1 * 4) + (2 * 4)` slots

`n` = `5` take `(1 * 4) + (2 * 4) + (3 * 4)` slots

simplify

`n` = `3` take `4 * (1)` slots

`n` = `4` take `4 * (1 + 2)` slots

`n` = `5` take `4 * (1 + 2 + 3)` slots

therefore

`n` = `i` take `4 * (1 + 2 + 3 + ... + (i - 2))` slots

from summation formula

`4 * (1 + 2 + 3 + ... + (i - 2))`

equal 

`4 * ((i - 2) * (i - 1) / 2)`

let `i` = `n`

`4 * ((n - 2) * (n - 1) / 2)`

```python 
result = 1 + 4 * (n - 1) + 4 * ((n - 2) * (n - 1) / 2)
```

🥳🥳 Now, get the result 🥳🥳

❗️❗️❗️ but ❗️❗️❗️

😡😡 but the formula is not perfect. 😡😡

😊😊 More simplify. more satisfying 😊😊

Easy way go to [wolframalpha (click here!!)](https://www.wolframalpha.com/input/?i=1+%2B+4+*+%28n-1%29+%2B+4+*+%28%28n+-+2%29+*+%28n+-+1%29+%2F+2%29) see in `Alternate forms:` or do it yourself

```
1   +   4 * (n - 1)   +   4 * ((n - 2) * (n - 1) / 2)

1   +       4n - 4    +   4 * ((n - 2) * (n - 1) / 2)

1   +       4n - 4    +   2 * ((n - 2) * (n - 1))

1   +       4n - 4    +   2 *((n * n) - (3 * n) + 2)

1   +       4n - 4    +   (2 * n * n) - (6 * n) + 4

:Groping like terms:

(2 * n * n)   +   (4 * n - 6 * n)   +   (1 - 4 + 4)

2 * n * n - 2 * n + 1
```

`2 * n * n - 2 * n + 1`

🥳🥳 Now, get satisfied result 🥳🥳