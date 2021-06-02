def addBorder(p):
    temp = len(p[0]) + 2
    return ["*" * temp] + ["*" + i + "*" for i in p] + ["*" * temp]