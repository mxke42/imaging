from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path
import os
import random


def crop_pdf(pdfPath):
    ## trim and save pdf
    # pdfPath = '/home/m/PycharmProjects/mapsProject/Images/newTest2.pdf'
    pdf = PdfFileReader(pdfPath)
    page = pdf.getPage(0)
    page.mediaBox.lowerLeft = (1322, 1894)
    page.mediaBox.upperRight = (1496, 1905.8)
    pdfWriter = PdfFileWriter()
    pdfWriter.addPage(page)
    path = '/home/m/PycharmProjects/mapsProject/Images/Temp'
    os.mkdir(path)
    with Path(path + "/cropped.pdf").open(mode="wb") as outputFile:
        pdfWriter.write(outputFile)
    return path

def crop_pdf_region(pdfPath):
    ## trim and save pdf
    # pdfPath = '/home/m/PycharmProjects/mapsProject/Images/newTest2.pdf'
    pdf = PdfFileReader(pdfPath)
    page = pdf.getPage(0)
    page.mediaBox.lowerLeft = (1031.3, 126.7)
    page.mediaBox.upperRight = (1141.2, 202.1)
    pdfWriter = PdfFileWriter()
    pdfWriter.addPage(page)
    path = '/home/m/PycharmProjects/mapsProject/Images/Temp'
    os.mkdir(path)
    with Path(path + "/cropped.pdf").open(mode="wb") as outputFile:
        pdfWriter.write(outputFile)
    return path


def crop_pdf_grid(pdfPath):
    pdf = PdfFileReader(pdfPath)

    path = '/home/m/PycharmProjects/mapsProject/Images/Temp'
    os.mkdir(path)
    page = pdf.getPage(0)

    pdfWriter1 = PdfFileWriter()
    page1 = page
    page1.mediaBox.lowerLeft = (1051.2, 97.9)
    page1.mediaBox.upperRight = (1077.8, 123.8)
    pdfWriter1.addPage(page1)
    with Path(path + "/cropped1.pdf").open(mode="wb") as outputFile:
        pdfWriter1.write(outputFile)

    pdfWriter2 = PdfFileWriter()
    page2 = page
    page2.mediaBox.lowerLeft = (1079.3, 97.9)
    page2.mediaBox.upperRight = (1105.9, 123.8)
    pdfWriter2.addPage(page2)
    with Path(path + "/cropped2.pdf").open(mode="wb") as outputFile:
        pdfWriter2.write(outputFile)

    pdfWriter3 = PdfFileWriter()
    page3 = page
    page3.mediaBox.lowerLeft = (1107.4, 97.9)
    page3.mediaBox.upperRight = (1133.3, 123.8)
    pdfWriter3.addPage(page3)
    with Path(path + "/cropped3.pdf").open(mode="wb") as outputFile:
        pdfWriter3.write(outputFile)

    pdfWriter4 = PdfFileWriter()
    page4 = page
    page4.mediaBox.lowerLeft = (1051.2, 69.1)
    page4.mediaBox.upperRight = (1077.8, 95.8)
    pdfWriter4.addPage(page4)
    with Path(path + "/cropped4.pdf").open(mode="wb") as outputFile:
        pdfWriter4.write(outputFile)

    pdfWriter5 = PdfFileWriter()
    page5 = page
    page5.mediaBox.lowerLeft = (1079.3, 69.1)
    page5.mediaBox.upperRight = (1105.9, 95.8)
    pdfWriter5.addPage(page5)
    with Path(path + "/cropped5.pdf").open(mode="wb") as outputFile:
        pdfWriter5.write(outputFile)

    pdfWriter6 = PdfFileWriter()
    page6 = page
    page6.mediaBox.lowerLeft = (1107.4, 69.1)
    page6.mediaBox.upperRight = (1133.3, 95.8)
    pdfWriter6.addPage(page6)
    with Path(path + "/cropped6.pdf").open(mode="wb") as outputFile:
        pdfWriter6.write(outputFile)

    pdfWriter7 = PdfFileWriter()
    page7 = page
    page7.mediaBox.lowerLeft = (1051.2, 41.8)
    page7.mediaBox.upperRight = (1077.8, 67)
    pdfWriter7.addPage(page7)
    with Path(path + "/cropped7.pdf").open(mode="wb") as outputFile:
        pdfWriter7.write(outputFile)

    pdfWriter8 = PdfFileWriter()
    page8 = page
    page8.mediaBox.lowerLeft = (1079.3, 41.8)
    page8.mediaBox.upperRight = (1105.9, 67)
    pdfWriter8.addPage(page8)
    with Path(path + "/cropped8.pdf").open(mode="wb") as outputFile:
        pdfWriter8.write(outputFile)

    pdfWriter9 = PdfFileWriter()
    page9 = page
    page9.mediaBox.lowerLeft = (1107.4, 41.8)
    page9.mediaBox.upperRight = (1133.3, 67)
    pdfWriter9.addPage(page9)
    with Path(path + "/cropped9.pdf").open(mode="wb") as outputFile:
        pdfWriter9.write(outputFile)


def crop_file_key(pdfPath):
    pdf = PdfFileReader(pdfPath)

    path = '/home/m/PycharmProjects/mapsProject/Images/Temp'
    os.mkdir(path)
    page = pdf.getPage(0)
    pdfWriter = PdfFileWriter()
    page.mediaBox.lowerLeft = (1079.3, 69.1)
    page.mediaBox.upperRight = (1105.9, 95.8)
    pdfWriter.addPage(page)
    with Path(path + "/cropped.pdf").open(mode="wb") as outputFile:
        pdfWriter.write(outputFile)

    # return path
def crop_pdf_grid2(pdfPath):
    pdf = PdfFileReader(pdfPath)

    path = '/home/m/PycharmProjects/mapsProject/Images/Temp2'
    os.mkdir(path)
    page = pdf.getPage(0)

    pdfWriter1 = PdfFileWriter()
    page1 = page
    page1.mediaBox.lowerLeft = (1051.2, 97.9)
    page1.mediaBox.upperRight = (1077.8, 123.8)
    pdfWriter1.addPage(page1)
    with Path(path + "/cropped1.pdf").open(mode="wb") as outputFile:
        pdfWriter1.write(outputFile)

    pdfWriter2 = PdfFileWriter()
    page2 = page
    page2.mediaBox.lowerLeft = (1079.3, 97.9)
    page2.mediaBox.upperRight = (1105.9, 123.8)
    pdfWriter2.addPage(page2)
    with Path(path + "/cropped2.pdf").open(mode="wb") as outputFile:
        pdfWriter2.write(outputFile)

    pdfWriter3 = PdfFileWriter()
    page3 = page
    page3.mediaBox.lowerLeft = (1107.4, 97.9)
    page3.mediaBox.upperRight = (1134, 123.8)
    pdfWriter3.addPage(page3)
    with Path(path + "/cropped3.pdf").open(mode="wb") as outputFile:
        pdfWriter3.write(outputFile)

    pdfWriter4 = PdfFileWriter()
    page4 = page
    page4.mediaBox.lowerLeft = (1051.2, 69.1)
    page4.mediaBox.upperRight = (1077.8, 95.8)
    pdfWriter4.addPage(page4)
    with Path(path + "/cropped4.pdf").open(mode="wb") as outputFile:
        pdfWriter4.write(outputFile)

    pdfWriter5 = PdfFileWriter()
    page5 = page
    page5.mediaBox.lowerLeft = (1079.3, 69.1)
    page5.mediaBox.upperRight = (1105.9, 95.8)
    pdfWriter5.addPage(page5)
    with Path(path + "/cropped5.pdf").open(mode="wb") as outputFile:
        pdfWriter5.write(outputFile)

    pdfWriter6 = PdfFileWriter()
    page6 = page
    page6.mediaBox.lowerLeft = (1107.4, 69.1)
    page6.mediaBox.upperRight = (1134, 95.8)
    pdfWriter6.addPage(page6)
    with Path(path + "/cropped6.pdf").open(mode="wb") as outputFile:
        pdfWriter6.write(outputFile)

    pdfWriter7 = PdfFileWriter()
    page7 = page
    page7.mediaBox.lowerLeft = (1051.2, 41.8)
    page7.mediaBox.upperRight = (1077.8, 67)
    pdfWriter7.addPage(page7)
    with Path(path + "/cropped7.pdf").open(mode="wb") as outputFile:
        pdfWriter7.write(outputFile)

    pdfWriter8 = PdfFileWriter()
    page8 = page
    page8.mediaBox.lowerLeft = (1079.3, 41.8)
    page8.mediaBox.upperRight = (1105.9, 67)
    pdfWriter8.addPage(page8)
    with Path(path + "/cropped8.pdf").open(mode="wb") as outputFile:
        pdfWriter8.write(outputFile)

    pdfWriter9 = PdfFileWriter()
    page9 = page
    page9.mediaBox.lowerLeft = (1107.4, 41.8)
    page9.mediaBox.upperRight = (1134, 67) #1133.3
    pdfWriter9.addPage(page9)
    with Path(path + "/cropped9.pdf").open(mode="wb") as outputFile:
        pdfWriter9.write(outputFile)