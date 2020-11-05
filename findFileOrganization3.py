from readGrid import read_grid
from readGrid import read_grid2
import time
from readGrid import read_file_keyV2
from coordinateMapping import transform_get_new_grid_pattern
from coordinateMapping import transform_coordinate_system2
from coordinateMapping import get_new_grid_pattern
import os
from errorFunction import error_function3
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

gridPattern = ['0,0', '1,0', '2,0', '0,-1', '1,-1', '2,-1', '0,-2', '1,-2', '2,-2']
allPdfsDirectory = '/home/m/PycharmProjects/mapsProject/allPdfs'
directoryStates = sorted(os.listdir(allPdfsDirectory))


#for file in directoryStates:
# stateToScan = str(file)
# stateMapDirectory = '/home/m/PycharmProjects/mapsProject/allPdfs/' + stateToScan
# stateName = stateMapDirectory.split('/')[-1]
# directory = sorted(os.listdir(stateMapDirectory))
stateName = 'COLORADO-ALL'
fileDict = {}
locationDict = {}
alreadyIndexed = []
filesAddedList = []
allSectionsList = []
listOfLocationDictionaries=[]
gridDictionary = {}

## create file dictionary: {'file key' : 'path to file'} FORMAT OF fileDict  ####
# for file in directory:
#     path = stateMapDirectory + '/' + file
#     fileKey = read_file_keyV2(file)
#     fileDict[fileKey] = path
# print('file dict:' + str(fileDict))
# print('#####')
# fileDictList = list(fileDict)
# print(fileDictList)
# print('#####')

txtDictFile = '/home/m/PycharmProjects/mapsProject/sortAll/masterFileDict.txt'
fileDict = open(txtDictFile, 'r').read()
fileDict = eval(fileDict)

fileDictList = list(fileDict)



#txtDictFile = '/home/m/PycharmProjects/mapsProject/gridMatrixFolder/'+ stateToScan +'.txt'
txtDictFile = '/home/m/PycharmProjects/mapsProject/sortAll/masterGridDictionary.txt'
gridDictionary = open(txtDictFile, 'r').read()
gridDictionary = eval(gridDictionary)





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
        if gridSection not in allSectionsList:  #allSectionsList will contain some items not in the file dictionary, but most will be in the file dictionary
            allSectionsList.append(gridSection)
        if gridSection in alreadyIndexed:  # skip over already indexed
            coordinateCount = coordinateCount + 1
            continue
        if gridSection in fileDict:  ## check if gridsection exists in file dictionary
            try:
                locationDict[gridPattern[coordinateCount]] = fileDict[gridSection]
            except TypeError:
                print("fileDict=" + str(fileDict))
                print('locationDict='+str(locationDict))
                print('gridPattern=' + str(gridPattern))
                print('coordinateCount=' + str(coordinateCount))
                exit()
            locationDict[gridPattern[coordinateCount]] = fileDict[gridSection]   ##adds to grid
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
    #time.sleep(1)
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
        gridDictionary[fileDictList[0]]
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
        break
        exit()
    fileToScan = fileDictList[0]
    nextFileGridMatrix = gridDictionary[fileToScan] #gets 9 names for next image
    print(str(fileToScan) + " has grid matrix: " + str(nextFileGridMatrix))
    values = get_new_grid_pattern(locationDict, nextFileGridMatrix, fileDict, fileDictList)
    status = values[2]
    if status == "GOOD":
        newCoordinates = transform_get_new_grid_pattern(values[0], values[1])
        gridPattern = transform_coordinate_system2(newCoordinates[0], newCoordinates[1])
        fileToScan = fileDictList[0]
    else:  # when status = 'BAD'
        errorCount = 1
        info = error_function3(fileDictList,  fileDict, locationDict, values, allSectionsList, listOfLocationDictionaries, alreadyIndexed, nextFileGridMatrix, gridDictionary)
        gridPattern = info[0]
        fileToScan = info[1]
        locationDict = info[2]
        allSectionsList = info[3]
    print('#####')
    print('#####')
    print('#####')

# gridMatrix = read_grid('/home/m/PycharmProjects/mapsProject/allPdfs/KANSAS/37101Elkhart_NE_370710145_FSTopo.pdf.pdf')
# fileKey = gridMatrix[1][1]
