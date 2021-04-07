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

From the example which some results are less than the answer by 1 century. When two last digit, not equal zero

that why I added

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

Now, all correct

`centuryFromYear2.py`

```python
def centuryFromYear(year):
    return (year + 99) // 100
```

Same problem as `centuryFromYear.py` but in this solve. Just shift the year to the correct answer.

"The 1st century AD began with 1 AD and ended with 100 AD"

The first years divide by 100 equal 1 is 100 and last years divide by 100 equal 1 is 199 but, 1st century began with 1 AD and ended with 100 AD

```
	year	divide by 100	  century		 (year +  99) divide by 100
	   1                0 ❌   	   1                 (1 + 99) / 100 = 1 ✅
	   2                0 ❌   	   1                 (2 + 99) / 100 = 1 ✅
	   3                0 ❌ 	   1                 (3 + 99) / 100 = 1 ✅
	[...]
	  97                0 ❌   	   1                (97 + 99) / 100 = 1 ✅
	  98                0 ❌   	   1                (97 + 99) / 100 = 1 ✅
	  99                0 ❌   	   1                (97 + 99) / 100 = 1 ✅
	 100                1 ✅   	   1               (100 + 99) / 100 = 1 ✅
```

|year	|divide by 100	  |century		| (year +  99) divide by 100|
|:---|:---|:---|:---|
|1|0 ❌|1|(1 + 99) / 100 = 1 ✅|
|2|0 ❌|1|(2 + 99) / 100 = 1 ✅|
|3|0 ❌|1|(3 + 99) / 100 = 1 ✅|
	[...]
	  97                0 ❌   	   1                (97 + 99) / 100 = 1 ✅
	  98                0 ❌   	   1                (97 + 99) / 100 = 1 ✅
	  99                0 ❌   	   1                (97 + 99) / 100 = 1 ✅
	 100                1 ✅   	   1               (100 + 99) / 100 = 1 ✅