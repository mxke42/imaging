
def handleUnequalSegments(yDict, keyLengthList):
    # find model list
    shortList = []
    xOrderList = []
    modelLength = max(keyLengthList)
    for key in yDict:
        if len(yDict[key]) == modelLength:
            modelXList = yDict[key]
        else:
            shortList.append(key)
    for elem in modelXList:
        x = int(elem.split(',')[0])
        xOrderList.append(x)
    stop = len(xOrderList)
    for item in shortList:
        key = item
        listToScan = yDict[key]
        print(listToScan)
        count = 0
        while count < stop:
            try:
                listToScan[count]
            except IndexError:
                listToScan.insert(count, 'mbm')
                count = count + 1
                continue
            x = int(listToScan[count].split(',')[0])
            xCorrect = xOrderList[count]
            if x == xCorrect:
                count = count + 1
                continue
            else:
                listToScan.insert(count, 'mbm')
                count = count + 1
        yDict[item] = listToScan

    return yDict

# newDict = handleUnequalSegments({'1':['0,1','1,1'], '2': ['1,2']}, [2,1])
#
# print(newDict)