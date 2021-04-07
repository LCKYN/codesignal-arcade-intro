# centuryFromYear

Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100, the second - from the year 101 up to and including the year 200, etc.

## Example

* For `year = 1905`, the output should be 
  
    `centuryFromYear(year) = 20`;

* For `year = 1700`, the output should be 
  
    `centuryFromYear(year) = 17`;

## Input/Output
* [**execution time limit**] 4 seconds (py3)
* [**input**] integer `year` 

    A positive integer, designating the year.

  * Guaranteed constraints:
    * `1 ≤ year ≤ 2005`.
* [**output**] integer

    The number of the century the `year` is in.

---

`centuryFromYear.py`
---
```python
def centuryFromYear(year):
    res = year // 100
    if year % 100 != 0:
       res += 1
    return res
```

from: <https://en.wikipedia.org/wiki/Century>

>- A century is a period of 100 years
>- The 1st century AD began with 1 AD and ended with 100 AD, with the same pattern continuing onward.

"The 1st century AD began with 1 AD and ended with 100 AD" but divide years by 100 is not right at all.

**ex.**

```
    years divide by 100 equal century
   (1 to 99) / 100 = 0 ❌
        100  / 100 = 1 ✅
(101 to 199) / 100 = 1 ❌
```

From the example which some results are less than the answer by 1 century. When last two digit, not equal zero. That why I add 

```python
if year % 100 != 0:
    res += 1
```

If the last two digits are not zero then add the result by 1.

then

```
   (1 to 99) / 100 = 0 + 1 ✅
        100  / 100 = 1     ✅
(101 to 199) / 100 = 1 + 1 ✅
```

🥳🥳 Now, all correct 🥳🥳

`centuryFromYear2.py`
---
```python
def centuryFromYear(year):
    return (year + 99) // 100
```

Same problem as `centuryFromYear.py` but in this solve. Just shift the year to the correct answer.

"The 1st century AD began with 1 AD and ended with 100 AD"

The first years divide by 100 equal 1 is 100 and last years divide by 100 equal 1 is 199 but, 1st century began with 1 AD and ended with 100 AD

|year	|divide by 100	  |century		| (year +  99) divide by 100|
|---:|---:|---:|---:|
|1|0 ❌|1|(1 + 99) / 100 = 1 ✅|
|2|0 ❌|1|(2 + 99) / 100 = 1 ✅|
|3|0 ❌|1|(3 + 99) / 100 = 1 ✅|
|[. . .]||||
|97|0 ❌|1|(97 + 99) / 100 = 1 ✅|
|98|0 ❌|1|(97 + 99) / 100 = 1 ✅|
|99|0 ❌|1|(97 + 99) / 100 = 1 ✅|
|100|1 ✅|1|(100 + 99) / 100 = 1 ✅|

That why I shifted year by 99.

🥳🥳 Now, all correct 🥳🥳