import os
import shutil

from createNewLocationDictionary import getNewLocationDictionary

allPdfsDirectory = '/home/m/PycharmProjects/mapsProject/gridSections'
directoryStates = sorted(os.listdir(allPdfsDirectory))
count = 0
for file in directoryStates:
    if count == 10:
        exit()
    count = count + 1
    stateToScan = str(file)
    stateMapDirectory = '/home/m/PycharmProjects/mapsProject/gridSections/' + stateToScan
    stateName = stateMapDirectory.split('/')[-1]
    print(stateName)
    directory = sorted(os.listdir(stateMapDirectory))
    txtItems = []
    for item in directory:
        #print(item)
        if item.endswith('.txt'):  #'newdict' in item:    #
            #print(item)
            #os.remove(stateMapDirectory + '/' + item)
            txtItems.append(stateMapDirectory+'/'+item)
        else:
            continue
    for elem in txtItems:
        locationDictionary = open(elem, 'r').read()
        locationDictionary = eval(locationDictionary)
        length = str(len(locationDictionary))
        newLocationDictionary = getNewLocationDictionary(locationDictionary)

        f = open(stateMapDirectory + '/newdict' + '(length,' + length + '.txt', "w")
        f.write(str(newLocationDictionary))
        f.close()

