# def createNewLocationDictionary(locationDictionary):
#     newLocationDict = {}
#     for key in locationDictionary:
import re



#locationDictionary = {'0,0': '/home/m/PycharmProjects/mapsProject/allPdfs/COLORADO/37105San_Isabel_375210500_FSTopo.pdf.pdf', '0,1': '/home/m/PycharmProjects/mapsProject/allPdfs/COLORADO/33085Choccolocco_333708537_FSTopo.pdf.pdf'}

def getNewLocationDictionary(locationDictionary):
    newDict = {}
    for key in locationDictionary:
        path = locationDictionary[key]
        print(path)
        trimPath = path[:-25]
        print('trimpath=' + trimPath)
        trimPath = re.split("\d{1,}", trimPath)[1]
        trimPath = trimPath.replace('_', " ")
        newDict[key] = trimPath
    return newDict
