def createDict(keys,values):
    res = {}
    border = len(values)

    for i in range(len(keys)):
        if (i >= border):
            res.update({keys[i]: None})
        else:
            res.update({keys[i] : values[i]})

    return res