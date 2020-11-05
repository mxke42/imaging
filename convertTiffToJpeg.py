import cv2, os

def convertTiffToJpeg(tiffPath, otherPath):

    # convert pdfPath to tiffPath
    name = tiffPath.split('/')[-1]
    name = name.replace('pdf.tiff', 'pdf.jpg')


    newPath = otherPath

    read = cv2.imread(tiffPath)
    outfile = newPath + name
    cv2.imwrite(outfile,read,[int(cv2.IMWRITE_JPEG_QUALITY), 50])
