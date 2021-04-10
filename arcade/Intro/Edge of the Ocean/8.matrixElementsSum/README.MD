# matrixElementsSum

After becoming famous, the CodeBots decided to move into a new building together. Each of the rooms has a different cost, and some of them are free, but there's a rumour that all the free rooms are haunted! Since the CodeBots are quite superstitious, they refuse to stay in any of the free rooms, **or any of the rooms below any of the free rooms**.

Given `matrix`, a rectangular matrix of integers, where each value represents the cost of the room, your task is to return the total sum of all rooms that are suitable for the CodeBots (ie: add up all the values that don't appear below a `0`).

## Example

- For

  ```python
  matrix = [[0, 1, 1, 2],
            [0, 5, 0, 0],
            [2, 0, 3, 3]]
  ```

  the output should be

  `matrixElementsSum(matrix) = 9.`

  ![ ](./picture/example1.png)

  There are several haunted rooms, so we'll disregard them as well as any rooms beneath them. Thus, the answer is `1 + 5 + 1 + 2 = 9`.

- For

  ```python
  matrix = [[1, 1, 1, 0],
            [0, 5, 0, 1],
            [2, 1, 3, 10]]
  ```

  the output should be

  `matrixElementsSum(matrix) = 9.`

  ![ ](./picture/example2.png)

  Note that the free room in the final column makes the full column unsuitable for bots (not just the room directly beneath it). Thus, the answer is `1 + 1 + 1 + 5 + 1 = 9`.

## Input/Output

- [**execution time limit**] 4 seconds (py3)

- [**input**] array.array.integer `matrix`

  A 2-dimensional array of integers representing the cost of each room in the building. A value of `0` indicates that the room is haunted.

  - Guaranteed constraints:
    - `1 ≤ matrix.length ≤ 5`.
    - `1 ≤ matrix[i].length ≤ 5`.
    - `0 ≤ matrix[i][j] ≤ 10`.

- [**output**] integer

  The total price of all the rooms that are suitable for the CodeBots to live in.

---

## `matrixElementsSum.py`

```python
def matrixElementsSum(matrix):
    result = 0

    for x in range(len(matrix[0])):
        for y in range(len(matrix)):

            if(matrix[y][x] == 0):
                break
            result += matrix[y][x]

    return result
```

Find the sum of the values in the elements, column by column, from top to bottom. And stop when the value is equal to zero or all characters in that column

In the first loop, check the column.
In the inner loop, check the row. break the loop when the value is equal to zero

ex.
```python
matrix = [[a, c, b],
          [d, e, f],
          [g, h, i]]
```
The order is as follows. `a d g c e h b f i`

🥳🥳 Now, get the result 🥳🥳

