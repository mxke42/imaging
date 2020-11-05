from readGrid import read_grid
from readGrid import read_file_keyV2
from coordinateMapping import transform_get_new_grid_pattern
from coordinateMapping import transform_coordinate_system2
from coordinateMapping import get_new_grid_pattern
import os
from errorFunction import error_function
from createVisualGrid import store_grid_images

x1 = 0
y1 = 0
x2 = 1
y2 = 0
x3 = 2
y3 = 0
x4 = 0
y4 = -1
x5 = 1
y5 = -1
x6 = 2
y6 = -1
x7 = 0
y7 = -2
x8 = 1
y8 = -2
x9 = 2
y9 = -2

x0 = [0, 1, 2, 0, 1, 2, 0, 1, 2]
y0 = [0, 0, 0, -1, -1, -1, -2, -2, -2]
# half1 = ['ALABAMA', 'ALABAMA-FLORIDA', 'ALABAMA-GEORGIA', 'ARIZONA', 'ARIZONA-NEW MEXICO', 'ARIZONA-SONORA', 'ARKANSAS', 'ARKANSAS-LOUISIANA', 'ARKANSAS-MISSISSIPPI', 'ARKANSAS-MISSOURI', 'ARKANSAS-OKLAHOMA', 'CALIFORNIA', 'CALIFORNIA-NEVADA', 'CALIFORNIA-OREGON', 'CAROLINA-SOUTH CAROL', 'COLORADO', 'COLORADO-KANSAS', 'COLORADO-UTAH', 'COLORADO-WYOMING', 'FLORIDA', 'FLORIDA-ALABAMA', 'FLORIDA-GEORGIA', 'GEORGIA', 'GEORGIA-FLORIDA', 'GEORGIA-NORTH CAROLI', 'GEORGIA-SOUTH CAROLI', 'GEORGIA-TENNESSEE', 'IDAHO', 'IDAHO-MONTANA', 'IDAHO-NEVADA', 'IDAHO-OREGON', 'IDAHO-UTAH', 'IDAHO-WASHINGTON', 'IDAHO-WYOMING', 'ILLINOIS', 'ILLINOIS-KENTUCKY', 'ILLINOIS-MISSOURI', 'INDIANA', 'INDIANA-KENTUCKY', 'KANSAS', 'KANSAS-OKLAHOMA', 'KENTUCKY', 'KENTUCKY-ILLINOIS', 'KENTUCKY-INDIANA', 'KENTUCKY-OHIO', 'KENTUCKY-TENNESSEE', 'KENTUCKY-VIRGINIA', 'LOUISIANA', 'LOUISIANA-TEXAS', 'MAINE', 'MARYLAND-WEST VIRGIN', 'MASSACHUSETTS-VERMON', 'MICHIGAN', 'MICHIGAN-WISCONSIN', 'MINNESOTA', 'MISSISSIPPI', 'MISSISSIPPI-ARKANSAS', 'MISSISSIPPI-TENNESSE', 'MISSOURI', 'MISSOURI-ILLINOIS', 'MONTANA', 'MONTANA-IDAHO', 'MONTANA-NORTH DAKOTA', 'MONTANA-SOUTH DAKOTA', 'MONTANA-WYOMING', 'NEBRASKA', 'NEBRASKA-COLORADO', 'NEVADA', 'NEVADA-CALIFORNIA', 'NEVADA-IDAHO', 'NEVADA-OREGON', 'NEVADA-UTAH']
#
# mainPath = '/home/m/PycharmProjects/mapsProject/allPdfs/'
# for item in half1:

gridPattern = ['0,0', '1,0', '2,0', '0,-1', '1,-1', '2,-1', '0,-2', '1,-2', '2,-2']
stateMapDirectory = '/home/m/PycharmProjects/mapsProject/allPdfs/ARKANSAS'
#stateMapDirectory = mainPath + item
stateName = stateMapDirectory.split('/')[-1]
directory = sorted(os.listdir(stateMapDirectory))
fileDict = {}
locationDict = {}
alreadyIndexed = []
filesAddedList = []
allSectionsList = []
listOfLocationDictionaries=[]

txtDictFile = '/home/m/PycharmProjects/mapsProject/gridMatrixFolder/ARKANSAS.txt'

gridDictionary = open(txtDictFile, 'r').read()
gridDictionary = eval(gridDictionary)


## create file dictionary: {'file key' : 'path to file'} FORMAT OF fileDict  ####
for file in directory:
    path = stateMapDirectory + '/' + file
    fileKey = read_file_keyV2(file)
    fileDict[fileKey] = path
print('file dict:' + str(fileDict))
print('#####')
fileDictList = list(fileDict)
print(fileDictList)
print('#####')

## (2) Get grid
errorCount = 1
fileToScan = fileDictList[0]
fileAddedCount = 0
while len(fileDictList) > 0:
    pdfPath = fileDict[fileToScan]
    print("pdf being scanned: " + str(pdfPath))
    gridMatrix = gridDictionary[fileToScan]  # list of 9 strings that are the grid from pdf
    print("grid matrix: " + str(gridMatrix))
    print('#####')
    coordinateCount = 0

    for elem in gridMatrix:
        gridSection = str(elem)
        if gridSection not in allSectionsList:
            allSectionsList.append(gridSection)  #adding every section (some not in dictList
        if gridSection in alreadyIndexed:  # skip over already indexed
            coordinateCount = coordinateCount + 1
            continue
        if gridSection in fileDict:  ## check if gridsection exists in file dictionary
            locationDict[gridPattern[coordinateCount]] = fileDict[gridSection]  ##adds to grid
            fileAddedCount = fileAddedCount + 1
            alreadyIndexed.append(gridSection)
            fileDictList.remove(gridSection)  # removes from file dictionary
            filesAddedList.append(gridSection)
            coordinateCount = coordinateCount + 1
        else:
            coordinateCount = coordinateCount + 1
            continue
    print("# of files appended to location dictionary=" + str(fileAddedCount))
    print("error count= " + str(errorCount))
    print('files appended: ' + str(filesAddedList))
    filesAddedList = []
    print('#####')
    print("location dict size=" + str(len(locationDict)))
    print('#####')
    print("location dict:" + str(locationDict))
    print('#####')

    print('gridPattern used for location dictionary above:' + str(gridPattern))
    print('#####')
    print("remaining # files to scan=" + str(len(fileDictList)))
    print('#####')
    print('remaining files to scan: ' + str(fileDictList))
    print('#####')
    try:
        read_grid(fileDict[fileDictList[0]])
    except IndexError:
        print("process may have completed")
        print(str(len(locationDict)) + "=size of ""location dictionary:" + str(locationDict))
        listOfLocationDictionaries.append(locationDict)
        print(listOfLocationDictionaries)
        for elem in listOfLocationDictionaries:
            print(str(len(elem)) + ' files')
            print(elem)
        store_grid_images(listOfLocationDictionaries, stateName)
        exit()
    nextFileGridMatrix = gridDictionary[fileDictList[0]]
    print(str(fileDictList[0]) + " has grid matrix: " + str(nextFileGridMatrix))
    values = get_new_grid_pattern(locationDict, nextFileGridMatrix, fileDict, fileDictList)
    status = values[2]
    if status == "GOOD":
        newCoordinates = transform_get_new_grid_pattern(values[0], values[1])
        gridPattern = transform_coordinate_system2(newCoordinates[0], newCoordinates[1])
        fileToScan = fileDictList[0]
    else:  # when status = 'BAD'
        errorCount = 1
        info = error_function(fileDictList,  fileDict, errorCount, locationDict, values, allSectionsList, listOfLocationDictionaries, gridDictionary)
        gridPattern = info[0]
        fileToScan = info[1]
        errorCount = info[2]
        locationDict = info[3]
    print('#####')
    print('#####')
    print('#####')

# gridMatrix = read_grid('/home/m/PycharmProjects/mapsProject/allPdfs/KANSAS/37101Elkhart_NE_370710145_FSTopo.pdf.pdf')
# fileKey = gridMatrix[1][1]
