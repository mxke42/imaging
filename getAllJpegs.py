import os
from convertTiffToJpeg import convertTiffToJpeg


## create new folders in 'allJpegs' that matches allTiffs, but is a lower quality jpeg
allJpegsDirectory = '/home/m/PycharmProjects/mapsProject/allJpegs/'
allTiffsDirectory = '/home/m/PycharmProjects/mapsProject/allTiffs'
directoryStates = sorted(os.listdir(allTiffsDirectory))


for file in directoryStates:
    stateToScan = str(file)
    isDir = os.path.isdir(allJpegsDirectory + stateToScan)
    if isDir == True:
        print(stateToScan + " already scanned")
    else:
        os.mkdir(allJpegsDirectory + stateToScan)  ## makes new folder for jpegs
        #continue  # go back to for loop
    print("converting " + stateToScan)

    directoryToScan = allTiffsDirectory + '/' + stateToScan
    #os.mkdir(allJpegsDirectory+stateToScan)  ## makes new folder for jpegs
    tiffsInStateDirectory = sorted(os.listdir(directoryToScan))  ##gets list of tiffs from directoryToScan
    length = len(tiffsInStateDirectory)
    for item in tiffsInStateDirectory:
        #print(item)
        tiffPath = directoryToScan+'/'+item
        name = item.replace('pdf.tiff', 'pdf.jpg')
        jpegPath = allJpegsDirectory + stateToScan + '/'
        isFile = os.path.exists(jpegPath + name)
        if isFile == True:

            print("skipped image already transferred")
            continue #  go back to for loop
        print("converting" + item)
        convertTiffToJpeg(tiffPath, jpegPath)



