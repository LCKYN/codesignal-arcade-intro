`centuryFromYear.py`

```python
def centuryFromYear(year):
    res = year // 100
    if year % 100 != 0:
       res += 1
    return res
```

from: https://en.wikipedia.org/wiki/Century

- A century is a period of 100 years
- The 1st century AD began with 1 AD and ended with 100 AD, with the same pattern continuing onward.

"The 1st century AD began with 1 AD and ended with 100 AD" but divide years by 100 is not right at all.

ex.

```
    years divide by 100 equal century
   (1 to 99) / 100 = 0 ❌
        100  / 100 = 1 ✅
(101 to 199) / 100 = 1 ❌
```

From the example which some result is less than answer by 1 century when two last digit not equal zero

that why I add

```python
if year % 100 != 0:
    res += 1
```

if two last digit is not zero add result by 1

`centuryFromYear2.py`

```python
def centuryFromYear(year):
    return (year + 99) // 100
```
