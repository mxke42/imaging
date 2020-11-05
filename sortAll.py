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


allPdfsDirectory = '/home/m/PycharmProjects/mapsProject/allPdfs'
#directoryStates = sorted(os.listdir(allPdfsDirectory))
sortAllPath = '/home/m/PycharmProjects/mapsProject/sortAll'
## make master file Dict
masterFileDict = {}
masterFileDictList = []
masterGridDictionary = {}

## master file dict creation
directoryStates = ['COLORADO', 'COLORADO-KANSAS', 'COLORADO-UTAH', 'COLORADO-WYOMING']
# insert list of state folders to scan together

for file in directoryStates:
    stateToScan = str(file)
    stateMapDirectory = '/home/m/PycharmProjects/mapsProject/allPdfs/' + stateToScan
    stateName = stateMapDirectory.split('/')[-1]
    directory = sorted(os.listdir(stateMapDirectory))
    fileDict = {}
    fileDictList = []
    locationDict = {}
    alreadyIndexed = []
    filesAddedList = []
    allSectionsList = []
    listOfLocationDictionaries=[]
    gridDictionary = {}

    ## create file dictionary: {'file key' : 'path to file'} FORMAT OF fileDict  ####
    for file in directory:
        path = stateMapDirectory + '/' + file
        fileKey = read_file_keyV2(file)
        fileDict[fileKey] = path

    fileDictList = list(fileDict)



    txtDictFile = '/home/m/PycharmProjects/mapsProject/gridMatrixFolder/'+ stateToScan +'.txt'

    gridDictionary = open(txtDictFile, 'r').read()
    gridDictionary = eval(gridDictionary)
    print('masterFileDict=' + str(masterFileDict))
    print(fileDict)



    masterFileDict.update(fileDict)
    print('masterFileDict2=' + str(masterFileDict))
    masterGridDictionary.update(gridDictionary)
    masterFileDictList = fileDictList + masterFileDictList

f = open(sortAllPath + '/masterFileDict' + '.txt', "w")
f.write(str(masterFileDict))
f.close()

f = open(sortAllPath + '/masterGridDictionary' + '.txt', "w")
f.write(str(masterGridDictionary))
f.close()

f = open(sortAllPath + '/masterFileDictList' + '.txt', "w")
f.write(str(masterFileDictList))
f.close()


