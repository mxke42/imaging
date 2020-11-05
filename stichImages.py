import PIL
from PIL import Image
from appendImages import append_images
from unequalSegmentHandler import handleUnequalSegments
import re
import os

PIL.Image.MAX_IMAGE_PIXELS = 933120000


#  input is a list of file names
list = ['Oyster Lake', 'Big Marvine Peak', 'Lost Park', 'Ripple Creek', 'Devils Causeway', 'Trappers Lake',
        'Blair Mountain', 'Deep Lake'] #, 'Sweetwater Lake', 'Orno Peak', 'Dome Peak', 'Sugarloaf Mountain', 'Adams Lake', 'Carbonate', 'Broken Rib Creek']

#  a location dictionary file is used for mapping
txtDictFile = '/home/m/PycharmProjects/mapsProject/gridSections/COLORADO*/dict1(length,638.txt'
locationDictionary = open(txtDictFile, 'r').read()
locationDictionary = eval(locationDictionary)

# a sectionDict is created that holds coordinates and paths to files requested
sectionDict = {}
for key in locationDictionary:
    path = locationDictionary[key]
    pathTrim = path.split('/')[-1]
    pathTrim = pathTrim[:-25]
    pathTrim = re.split("\d{1,}", pathTrim)[1]
    pathTrim = pathTrim.replace('_', " ")
    if pathTrim in list:
        sectionDict[key] = path
        print(key + path)

# organize by x
coordList = []
for key in sectionDict:
    xy = key.split(',')
    x = int(xy[0])
    y = int(xy[1])
    coordList.append([x, y])
coordList = sorted(coordList, key=lambda k: [k[1], k[0]])

strCoordList = []
for elem in coordList:
    x = elem[0]
    y = elem[1]
    coordStr = str(x) + ',' + str(y)
    strCoordList.append(coordStr)
xMin = strCoordList[0][0]  # to be used later if needed for unequal segment sizes

# group by y
yDict = {}
for elem in strCoordList:
    xy = elem.split(',')
    y = int(xy[1])
    if str(y) in yDict:
        yDict[str(y)].append(elem)
    else:
        yDict[str(y)] = []
        yDict[str(y)].append(elem)
print(yDict)

#  check y dict for unequal segments
keyLengthList = []  # will be length of 1 unless there are unequal segment sizes
for key in yDict:
    length = len(yDict[key])
    keyLengthList.append(length) if length not in keyLengthList else keyLengthList
count = 0
print(keyLengthList)
if len(keyLengthList) > 1:  # process unequal segments
    print("Error, unequal segment sizes")
    yDict = handleUnequalSegments(yDict, keyLengthList)
    print(yDict)

#  creating horizontal stacks
for key in yDict:
    yList = yDict[key]
    print(yList)
    horizontalImages = []
    for elem in yList:
        if elem == 'mbm':
            jpegPath = '/home/m/PycharmProjects/mapsProject/Images/mapsbymaxdefault.jpg'
        else:
            pdfPath = locationDictionary[elem]
            jpegPath = pdfPath.replace('f.pdf', 'f.jpg')
            jpegPath = jpegPath.replace('allPdfs', 'allJpegs')
        horizontalImages.append(jpegPath)
    images = [Image.open(x) for x in horizontalImages]
    append_images(images, count)
    count = count + 1

tempJpegDirectory = '/home/m/PycharmProjects/mapsProject/Images/TempJpegImages'
horizontalStacks = sorted(os.listdir(tempJpegDirectory))
hStckList = []
count = count + 1

#  combining horizontal stacks vertically
for item in horizontalStacks:
    path = tempJpegDirectory + '/' + item
    hStckList.append(path)
hStckList.reverse()  # must reverse list because 1 on top of 2 on top of 3 is incorrect, need 3,2,1
print(hStckList)
hStackImages = []
for item in hStckList:
    hStackImages.append(Image.open(item))
print(hStackImages)

append_images(hStackImages, count, direction='vertical')
