from readGrid import read_grid
from readGrid import read_grid2
from coordinateMapping import get_new_grid_pattern

from coordinateMapping import transform_get_new_grid_pattern

from coordinateMapping import transform_coordinate_system2
from processRemainingFiles import review_leftover_files

gridPattern0 = ['0,0', '1,0', '2,0', '0,-1', '1,-1', '2,-1', '0,-2', '1,-2', '2,-2']
x0= [0,1,2,0,1,2,0,1,2]
y0= [0,0,0,-1,-1,-1,-2,-2,-2]


def error_function(fileDictList, fileDict, errorCount,
                   locationDict, values, allSectionsList, listOfLocationDictionaries, gridDictionary):
    print("error function has been called")
    stop = len(fileDictList)
    status = values[2]

    while status == "BAD":

        try:
            fileDictList[errorCount]
        except IndexError: ## program reaches end of fileDictList without finding any matches
            print("process may have completed")
            review_leftover_files(fileDictList, allSectionsList)
            print("complete location dictionary segment, length=" + str(len(locationDict)) + str(locationDict))
            listOfLocationDictionaries.append(locationDict)
            return gridPattern0, fileDictList[0], errorCount, {}
            print("location dictionary:" + str(locationDict))
            exit()
        fileToScan = fileDictList[errorCount]
        pdfPath = fileDict[fileToScan]
        nextFileGridMatrix = gridDictionary[fileToScan]
        values = get_new_grid_pattern(locationDict, nextFileGridMatrix, fileDict, fileDictList)
        status = values[2]
        # errorCount = errorCount + 1
        if status == "GOOD":
            newCoordinates = transform_get_new_grid_pattern(values[0], values[1])
            gridPattern = transform_coordinate_system2(newCoordinates[0], newCoordinates[1])
            fileToScan = fileDictList[errorCount]
            return gridPattern, fileToScan, errorCount, locationDict
        errorCount = errorCount + 1
    return gridPattern, fileToScan, errorCount, locationDict


def error_function2(fileDictList, fileDict,
                    locationDict, values, allSectionsList, listOfLocationDictionaries, alreadyIndexed, nextFileGridMatrix):
    status = values[2]
    count = 1
    grid = nextFileGridMatrix
    while status == "BAD":
        for item in grid:
            if item in fileDictList:
                values = get_new_grid_pattern(locationDict, grid, fileDict, fileDictList)
                status = values[2]
                if status == "GOOD":
                    newCoordinates = transform_get_new_grid_pattern(values[0], values[1])
                    gridPattern = transform_coordinate_system2(newCoordinates[0], newCoordinates[1])
                    fileToScan = fileDictList[fileDictList.index(item)]
                    return gridPattern, fileToScan, locationDict, allSectionsList
                else:  # status = "BAD", meaning this file needed to be indexed, but no hook was found
                    try:
                        fileDictList[count]
                    except IndexError:  ## program reaches end of fileDictList without finding any matches
                        print("process may have completed")
                        allSectionsList = review_leftover_files(fileDictList, allSectionsList)
                        print("complete location dictionary segment, length=" + str(len(locationDict)) + str(locationDict))
                        listOfLocationDictionaries.append(locationDict)
                        return gridPattern0, fileDictList[0], {}, allSectionsList
                    fileToScan = fileDictList[count]  # try next file in fileDictList
                    grid = read_grid2(fileDict[fileToScan])
                    values2 = get_new_grid_pattern(locationDict, grid, fileDict, fileDictList)
                    status = values2[2]  # can be ""GOOD" or "BAD"
                    if status == "GOOD":
                        newCoordinates = transform_get_new_grid_pattern(values2[0], values2[1])
                        gridPattern = transform_coordinate_system2(newCoordinates[0], newCoordinates[1])
                        return gridPattern, fileToScan, locationDict, allSectionsList
                    count = count + 1



                    #break  # returns to while statement
            else:
                continue
    return gridPattern, fileToScan, locationDict, allSectionsList


def error_function3(fileDictList, fileDict,
                    locationDict, values, allSectionsList, listOfLocationDictionaries, alreadyIndexed, nextFileGridMatrix, gridDictionary):
    status = values[2]
    count = 1
    grid = nextFileGridMatrix
    while status == "BAD":
        for item in grid:
            if item in fileDictList:
                values = get_new_grid_pattern(locationDict, grid, fileDict, fileDictList)
                status = values[2]
                if status == "GOOD":
                    newCoordinates = transform_get_new_grid_pattern(values[0], values[1])
                    gridPattern = transform_coordinate_system2(newCoordinates[0], newCoordinates[1])
                    fileToScan = fileDictList[fileDictList.index(item)]
                    return gridPattern, fileToScan, locationDict, allSectionsList
                else:  # status = "BAD", meaning this file needed to be indexed, but no hook was found
                    try:
                        fileDictList[count]
                    except IndexError:  ## program reaches end of fileDictList without finding any matches
                        print("process may have completed")
                        allSectionsList = review_leftover_files(fileDictList, allSectionsList)
                        print("complete location dictionary segment, length=" + str(len(locationDict)) + str(locationDict))
                        listOfLocationDictionaries.append(locationDict)
                        return gridPattern0, fileDictList[0], {}, allSectionsList
                    fileToScan = fileDictList[count]  # try next file in fileDictList
                    grid = gridDictionary[fileToScan]
                    values2 = get_new_grid_pattern(locationDict, grid, fileDict, fileDictList)
                    status = values2[2]  # can be ""GOOD" or "BAD"
                    if status == "GOOD":
                        newCoordinates = transform_get_new_grid_pattern(values2[0], values2[1])
                        gridPattern = transform_coordinate_system2(newCoordinates[0], newCoordinates[1])
                        return gridPattern, fileToScan, locationDict, allSectionsList
                    count = count + 1



                    #break  # returns to while statement
            else:
                continue
    return gridPattern, fileToScan, locationDict, allSectionsList

