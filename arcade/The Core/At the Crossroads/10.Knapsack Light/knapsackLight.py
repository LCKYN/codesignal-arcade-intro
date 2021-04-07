def knapsackLight(value1, weight1, value2, weight2, maxW):
    c_1 = value1 if maxW >= weight1 else 0
    c_2 = value2 if maxW >= weight2 else 0
    c_both = value1 + value2 if maxW >= weight1 + weight2 else 0
    return max(c_1, c_2, c_both)