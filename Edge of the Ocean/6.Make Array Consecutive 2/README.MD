# Make Array Consecutive 2

Ratiorg got `statues` of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size. Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by `1`. He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.

## Example

* For `statues = [6, 2, 3, 8]`, the output should be
  
  `makeArrayConsecutive2(statues) = 3.`
  
  Ratiorg needs statues of sizes `4`, `5` and `7`.

## Input/Output

* [**execution time limit**] 4 seconds (py3)
* [**input**] array.integer `statues`

  An array of distinct non-negative integers.

    * Guaranteed constraints:
      * `1 ≤ statues.length ≤ 10`.
      * `0 ≤ statues[i] ≤ 20`.
* [**output**] integer
    
    The minimal number of statues that need to be added to existing `statues` such that it contains every integer size from an interval `[L, R]` (for some `L, R`) and no other sizes.

---

`makeArrayConsecutive2.py`
---

```python
def makeArrayConsecutive2(s):
    return max(s) - min(s) - len(s) + 1 ;
```
<br />

`s = [min, min + 1, min + 2,..., max - 2, max - 1, max]`

therefore

`length = max - min + 1`

ex.
```
min = 3
max = 5
s = [3, 4, 5]

length = 3 (5 - 3 + 1)
```

The number of missing numbers will affect the length of the array.

ex.
|attribute|ex.1|ex.2|ex.3|
|:-- | :--: | :--: | :--: |
|min|`3`|`3`|`1`|
|max|`5`|`6`|`4`|
|missing numbers|`[4]`|`[4, 5]`|`[2]`|
|s|`[3, 5]`|`[3, 6]`|`[1, 3, 4, 5]`|
|||||
|calculated length|`3`|`4`|`5`|
|actual length|`2`|`2`|`4`|
|||||
|difference|`1`|`2`|`1`|
<br />

`difference` is equal to the length of `missing numbers` 

therefore

`difference = calculated length - actual length`.

`calculated length = (Minimum value of s) - (Maximum value of s) + 1`.

`actual length = (Length of s)`.

`difference = (Minimum value of s) - (Maximum value of s + 1) - (Length of s)`.


🥳🥳 Now, get the result 🥳🥳