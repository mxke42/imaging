from cropPdf import crop_pdf
from cropPdf import crop_pdf_region
from convertPdfToJpegFunction2 import pdf2jpeg
from convertPdfToJpegFunction2 import pdf2jpeglowRes
from useOcrFunction import use_ocr
from PIL import Image
import shutil
def identify_state(pdfPath):

    ## trim and save pdf
    path = crop_pdf(pdfPath)

    tempPdfPath = path + "/cropped.pdf"
    tempJpegPath = path + "/cropped.jpg"
    # ##convert to jpeg
    pdf2jpeg(
         tempPdfPath
     )

    # ##OCR
    stateName = use_ocr(tempJpegPath, path)
    return stateName

#returns a list of pixel information
def identify_regions(pdfPath):
    ## trim and save pdf
    path = crop_pdf_region(pdfPath)

    tempPdfPath = path + "/cropped.pdf"
    tempJpegPath = path + "/cropped.jpg"
    # ##convert to jpeg
    pdf2jpeglowRes(
        tempPdfPath
    )
    im = Image.open(tempJpegPath, 'r')
    pxVal = list(im.getdata())
    shutil.rmtree('/home/m/PycharmProjects/mapsProject/Images/Temp')
    return pxVal

def identify_regions2(pdfPath):
    ## trim and save pdf
    path = crop_pdf_region(pdfPath)

    tempPdfPath = path + "/cropped.pdf"
    tempJpegPath = path + "/cropped.jpg"
    # ##convert to jpeg
    pdf2jpeglowRes(
        tempPdfPath
    )
    im = Image.open(tempJpegPath, 'r')
    pxVal = list(im.getdata())
    shutil.rmtree('/home/m/PycharmProjects/mapsProject/Images/Temp2')
    return pxVal











