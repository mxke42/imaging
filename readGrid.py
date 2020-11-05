from cropPdf import crop_pdf_grid
from cropPdf import crop_pdf_grid2
from cropPdf import crop_file_key
from convertPdfToJpegFunction2 import bulkPdf2jpeg
from convertPdfToJpegFunction2 import bulkPdf2jpeg2
from convertPdfToJpegFunction2 import pdf2jpeg
from useOcrFunction import bulk_use_ocr
from useOcrFunction import bulk_use_ocr2
from useOcrFunction import ocr_get_file_key
import os
import re



def read_grid(pdfPath):
    crop_pdf_grid(pdfPath)
    path = '/home/m/PycharmProjects/mapsProject/Images/Temp/'
    bulkPdf2jpeg(path + 'cropped1.pdf',
                 path + 'cropped2.pdf',
                 path + 'cropped3.pdf',
                 path + 'cropped4.pdf',
                 path + 'cropped5.pdf',
                 path + 'cropped6.pdf',
                 path + 'cropped7.pdf',
                 path + 'cropped8.pdf',
                 path + 'cropped9.pdf')

    gridMatrix = bulk_use_ocr(path + 'cropped1.jpg',
                              path + 'cropped2.jpg',
                              path + 'cropped3.jpg',
                              path + 'cropped4.jpg',
                              path + 'cropped5.jpg',
                              path + 'cropped6.jpg',
                              path + 'cropped7.jpg',
                              path + 'cropped8.jpg',
                              path + 'cropped9.jpg',
                              )
    return gridMatrix

def read_file_keyV2(pdfPath):
    fileKey = re.split("_\d{9}", pdfPath)[0]
    fileKey = fileKey[5:]
    fileKey = fileKey.replace("_", " ")
    return fileKey


def read_grid2(pdfPath, item):
    crop_pdf_grid2(pdfPath)
    path = '/home/m/PycharmProjects/mapsProject/Images/Temp2/'
    bulkPdf2jpeg2(path + 'cropped1.pdf',
                 path + 'cropped2.pdf',
                 path + 'cropped3.pdf',
                 path + 'cropped4.pdf',
                 path + 'cropped5.pdf',
                 path + 'cropped6.pdf',
                 path + 'cropped7.pdf',
                 path + 'cropped8.pdf',
                 path + 'cropped9.pdf')

    gridMatrix = bulk_use_ocr2(path + 'cropped1.jpg',
                              path + 'cropped2.jpg',
                              path + 'cropped3.jpg',
                              path + 'cropped4.jpg',
                              path + 'cropped5.jpg',
                              path + 'cropped6.jpg',
                              path + 'cropped7.jpg',
                              path + 'cropped8.jpg',
                              path + 'cropped9.jpg',
                              )

    gridMatrix[4] = item
    return gridMatrix


def read_file_key(pdfPath):
    crop_file_key(pdfPath)
    path = '/home/m/PycharmProjects/mapsProject/Images/Temp/cropped.pdf'
    pdf2jpeg(path)
    path = path.replace('.pdf', '.jpg')
    fileKey = ocr_get_file_key(path)
    return fileKey


