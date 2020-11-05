import re
from readGrid import read_file_keyV2
fileName = 'Storm Mountain'
target = '<id = "gridSection" area shape="circle" coords="1065,1107,21" alt="testRect" onclick="myFunction()">'
base2 = 'https://data.fs.usda.gov/geodata/rastergateway/data3/'
# base = '<area shape="circle" coords= ' + '"0,0,21" ' + 'alt="'+ 'fileName' +'" onclick="myFunction()">'

base = ' area shape="rect" coords= '
fileName = 'alt="' + fileName
end = " onclick=" + '"' + "myFunction('"
end2 = "')" + '"' + ">"
full = base + '"0,0,21" ' + fileName + end

locationDictPath = '/home/m/PycharmProjects/mapsProject/gridSections/IDAHO/dict3(length,719.txt'

locationDictionary = open(locationDictPath, 'r').read()
locationDictionary = eval(locationDictionary)

# $('[id="San Isabel"]').click(function(e) {
#             e.preventDefault();
#             var data = $(this).data('maphilight') || {};
#             data.alwaysOn = !data.alwaysOn;
#             $(this).data('maphilight', data).trigger('alwaysOn.maphilight');
#         });
one = "$('"
two = "[id=" + fileName + '"]'
three = "').click(function(e) {e.preventDefault();var data = $(this).data('maphilight') || {};data.alwaysOn = !data.alwaysOn;$(this).data('maphilight', data).trigger('alwaysOn.maphilight');});"

#  enter origin
TL = [1490, 2601]
xStart =TL[0] + 21.5
yStart =TL[1] + 28

xMultiplier = 45
#xMultiplier = 47
#yMultiplier = 58
#yMultiplier = 61  ##sometimes works better for arranging y  #colorado
yMultiplier = 65

count = 0
for key in locationDictionary:
    x = int(key.split(',')[0])
    y = int(key.split(',')[1])

    x = x * (-x/50+xMultiplier) + xStart
    y = y * (-1) * (yMultiplier) + yStart
    # x = x*(-x/50+xMultiplier) + xStart     #colorado
    # y = y*(-1)*( y/30+yMultiplier) + yStart
    # x1 = x -21.5     ##  may only work for colorado
    # y1 = y -28
    # x2 = x + 21.5
    # y2 = y + 28
    x1 = x - 21.5  ##  may only work for colorado
    y1 = y - 28
    x2 = x + 21.5
    y2 = y + 33
    path = locationDictionary[key]

    targetTrim = path.split('/')[-1]
    fiveCode = targetTrim[:5]
    name = targetTrim[5:]
    name = name.replace('f.pdf', 'f')
    fsTopo = '/fstopo/'
    link = base2 + fiveCode + fsTopo + name



    #fileName = path[53:]
    #print(fileName)
    fileName = path.split('/')[-1]

    fileName = read_file_keyV2(fileName)
    href = ' href = "' + link + '"'
    fileNameFull = ' alt="' + fileName
    areaId = '<area id=' + '"'+ fileName + '"'
    className = ' class = "mapArea"'
    full = areaId + className+ base + '"'+str(x1)+','+str(y1)+','+str(x2)+','+str(y2) + '"' + fileNameFull+'"' + end  + link + "'" + ','+"'"+fileName + end2
    two = "[id="  +'"'+fileName + '"]'
    #full = one + two + three

    print(full)


















