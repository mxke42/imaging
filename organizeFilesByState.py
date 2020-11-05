from identifyStateFunction import identify_state
import os
import shutil
from shutil import copyfile

mapDirectory = '/media/m/_mk_/MapsByMax/MapPDFs'
tiffDirectory = '/home/m/PycharmProjects/mapsProject/allTiffs'
directory = os.listdir(mapDirectory)
# print(directory)
# for entry in os.scandir(mapDirectory):
#     pdfPath= mapDirectory + '/' + entry;
#     print(pdfPath)
count = 0
for item in directory:
    pdfPath = mapDirectory + '/' + item
    if pdfPath == "/media/m/_mk_/MapsByMax/MapPDFs/.DS_Store" or pdfPath == "/media/m/_mk_/MapsByMax/MapPDFs/._.DS_Store":
        print(count)
        count = count + 1
        continue
    print(pdfPath)
    stateName = identify_state(pdfPath)
    newPath = '/home/m/PycharmProjects/mapsProject/allPdfs/' + stateName
    newTiffDirectory = tiffDirectory + '/' + stateName
    newPdf = newPath + '/' + item
    tiffElem = item.replace("pdf.pdf", "pdf.tiff")
    tiffPath = tiffDirectory + '/' + tiffElem
    newTiffPath = newTiffDirectory + '/' + tiffElem

    # pdf organization
    if os.path.isdir(newPath):
        copyfile(pdfPath, newPdf)
    else:
        os.mkdir(newPath)
        copyfile(pdfPath, newPdf)

    #tiff organization
    if os.path.isfile(tiffPath):
        if os.path.isdir(newTiffDirectory):
            os.rename(tiffPath, newTiffPath)
        else:
            os.mkdir(newTiffDirectory)
            os.rename(tiffPath, newTiffPath)
    else:
        print(count)
        count = count + 1
        continue
    print(stateName)
    print(count)
    count = count + 1

# identify_state('/media/m/_mk_/MapsByMax/MapPDFs/30084Sumatra_300008452_FSTopo.pdf.pdf')
