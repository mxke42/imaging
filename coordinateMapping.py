from processRemainingFiles import review_leftover_files
x1=0
y1=0
x2=1
y2=0
x3=2
y3=0
x4=0
y4=-1
x5=1
y5=-1
x6=2
y6=-1
x7=0
y7=-2
x8=1
y8=-2
x9=2
y9=-2

x0= [0,1,2,0,1,2,0,1,2]
y0= [0,0,0,-1,-1,-1,-2,-2,-2]


def identify_transform2(nextSection, gridMatrix):
    transform = gridMatrix.index(nextSection)

    if transform == 1: #x+1
        xNew = [i + 1 for i in x0]
        yNew = y0
    elif transform == 2:
        xNew = [i + 1 for i in x0]
        yNew = y0
    elif transform == 3: #x-2, y-1
        xNew = [i - 2 for i in x0]
        yNew = [i - 1 for i in y0]
    elif transform == 4:
        xNew = [i + 1 for i in x0]
        yNew = y0
    elif transform == 5:
        xNew = [i + 1 for i in x0]
        yNew = y0
    elif transform == 6:#x-2, y-1
        xNew = [i - 2 for i in x0]
        yNew = [i - 1 for i in y0]
    elif transform == 7:
        xNew = [i + 1 for i in x0]
        yNew = y0
    elif transform == 8:
        xNew = [i + 1 for i in x0]
        yNew = y0
    else:
        print("error")
        exit()
    return xNew, yNew


## needs to find the space between the first file key and the second file key on the grid matrix
def identify_transform(initialSection, nextSection, gridMatrix):

    transform = gridMatrix.index(nextSection)-gridMatrix.index(initialSection)
    if transform == -4: #x-1, y-1
        xNew= [i -1 for i in x0]
        yNew = [i -1 for i in y0]
    elif transform == -3: #y-1
        xNew = x0
        yNew = [i -1 for i in y0]
    elif transform == -2: #x+1, y-1
        xNew = [i +1 for i in x0]
        yNew = [i -1 for i in y0]
    elif transform == 1:  #x+1
        xNew = [i + 1 for i in x0]
        yNew = y0
    elif transform == 4: # x + 1, y-1
        xNew = [i + 1 for i in x0]
        yNew = [i - 1 for i in y0]
    elif transform == 3: #y-1
        xNew = x0
        yNew = [i - 1 for i in y0]
    elif transform == 2:#x-1, y-1
        xNew = [i  - 1 for i in x0]
        yNew = [i - 1 for i in y0]
    elif transform == -1: #x-1
        xNew = [i - 1 for i in x0]
        yNew = y0
    else:
        print("error" +str(transform) + "=transform")
        exit()
    # x0 = xNew
    # y0 = yNew
    return xNew, yNew



def transform_coordinate_system(xValues, yValues):
    xV = xValues
    yV = yValues
    x1 = xV[0]
    y1 = yV[0]
    x2 = xV[1]
    y2 = yV[1]
    x3 = xV[2]
    y3 = yV[2]
    x4 = xV[3]
    y4 = yV[3]
    x5 = xV[4]
    y5 = yV[4]
    x6 = xV[5]
    y6 = yV[5]
    x7 = xV[6]
    y7 = yV[6]
    x8 = xV[7]
    y8 = yV[7]
    x9 = xV[8]
    y9 = yV[8]

    coordinateSystem = [str(x1)+','+str(y1),  str(x2)+','+str(y2),  str(x3)+','+str(y3),
                        str(x4)+','+str(y4),  str(x5)+','+str(y5),  str(x6)+','+str(y6),
                        str(x7)+','+str(y7),  str(x8)+','+str(y8),  str(x9)+','+str(y9)]
    return coordinateSystem

def transform_coordinate_system2(xValues, yValues):

    coordinateSystem = [str(xValues[0])+','+str(yValues[0]),  str(xValues[1])+','+str(yValues[1]),  str(xValues[2])+','+str(yValues[2]),
                        str(xValues[3])+','+str(yValues[3]),  str(xValues[4])+','+str(yValues[4]),  str(xValues[5])+','+str(yValues[5]),
                        str(xValues[6])+','+str(yValues[6]),  str(xValues[7])+','+str(yValues[7]),  str(xValues[8])+','+str(yValues[8])]
    return coordinateSystem


def transform_get_new_grid_pattern(matchingCount, anchorCoordinates):
    split = anchorCoordinates.split(',')
    x0 = int(split[0])
    y0 = int(split[1])
    if matchingCount == 0:
       xNew = [x0, x0+1, x0+2, x0, x0+1, x0+2, x0, x0+1, x0+2]
       yNew = [y0, y0, y0, y0-1, y0-1, y0-1, y0-2, y0-2, y0-2]
    elif matchingCount == 1:
        xNew = [x0-1, x0, x0+1, x0-1, x0, x0+1, x0-1, x0, x0+1]
        yNew = [y0, y0, y0, y0-1, y0-1, y0-1, y0-2, y0-2, y0-2]
    elif matchingCount == 2:
        xNew = [x0-2, x0-1, x0, x0-2, x0-1, x0, x0-2, x0-1, x0]
        yNew = [y0, y0, y0, y0-1, y0-1, y0-1, y0-2, y0-2, y0-2]
    elif matchingCount == 3:
        xNew = [x0, x0+1, x0+2, x0, x0+1, x0+2, x0, x0+1, x0+2]
        yNew = [y0+1, y0+1, y0+1, y0, y0, y0, y0-1, y0-1, y0-1]
    # elif matchingCount == 4:
    #     xNew = [x0-1, x0, x0-1, x0-1, x0, x0-1, x0-1, x0, x0-1]
    #     yNew = [y0+1, y0+1, y0+1, y0, y0, y0, y0-1, y0-1, y0-1]
    elif matchingCount == 5:
        xNew = [x0-2, x0-1, x0, x0-2, x0-1, x0, x0-2, x0-1, x0]
        yNew = [y0+1, y0+1, y0+1, y0, y0, y0, y0-1, y0-1, y0-1]
    elif matchingCount == 6:
        xNew = [x0, x0+1, x0+2, x0, x0+1, x0+2, x0, x0+1, x0+2]
        yNew = [y0+2, y0+2, y0+2, y0+1, y0+1, y0+1, y0, y0, y0]
    elif matchingCount == 7:
        xNew = [x0-1, x0, x0+1, x0-1, x0, x0+1, x0-1, x0, x0+1]
        yNew = [y0+2, y0+2, y0+2, y0+1, y0+1, y0+1, y0, y0, y0]
    elif matchingCount == 8:
        xNew = [x0-2, x0-1, x0, x0-2, x0-1, x0, x0-2, x0-1, x0]
        yNew = [y0+2, y0+2, y0+2, y0+1, y0+1, y0+1, y0, y0, y0]
    return xNew, yNew

##this function searches locationDict for values in grid Matrix (grid matrix is list of name strings [place1, place2,..]
def get_new_grid_pattern(locationDict, nextFileGridMatrix, fileDict, fileDictList):
    pathGridMatrix = []

    ##invert Location Dictionary for easy searching
    invLocationDict = dict(zip(locationDict.values(), locationDict.keys()))
    status = "GOOD"
    #print("invLocationDict: "+str(invLocationDict))

    #creates a Matrix based on nextFileGridMatrix, that shows PDF locations of files in nextFileGridMatrix
    #   nextFileGridMatrix looks like [gridSectionName1, gridSectionName2, gridSectionName3,...] gridSectionNames
    #   may not have corresponding PDFs, and could look like [pdfPathtoGridSection1, "", "", pdfPathtoGridSection4, ...]
    for i in nextFileGridMatrix:
        if i in fileDict:
            pathGridMatrix.append(fileDict[i])
        else:
            pathGridMatrix.append("")
    print('pathGridMatrix: '+str(pathGridMatrix))

    # uses pdfPaths from pathGridMatrix, searches for them in locationDict, gets coordinate.
    # 'matchingCount' is the position on the grid(3x3) where the coordinate is. 0 for upper left, 8 for lower right
    count1 = 0
    for i in pathGridMatrix:
        #print("searching for " + str(i) + ' in pathGridMatrix' )
        if i in invLocationDict:

            matchingCount = pathGridMatrix.index(i)
            anchorCoordinates = invLocationDict[i]
            print("anchor coordinate for transform= " + str(anchorCoordinates))
            print("position of coordinates on grid: " + str(matchingCount))
            count1 = count1 + 1
            break
        else:
            count1 = count1 + 1
            continue
    if count1 > 8:
        ##this creates a problem because the next file uses the previous coordinate system
        print("ERROR OCCURRED: no matching grid sections recorded yet")
        status = "BAD"
        matchingCount = -1
        anchorCoordinates = " , "
        return matchingCount, anchorCoordinates, status
    return matchingCount, anchorCoordinates, status

