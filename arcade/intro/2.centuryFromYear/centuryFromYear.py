def centuryFromYear(year):
    res = year // 100
    if year % 100 != 0:
        res += 1
    return res 