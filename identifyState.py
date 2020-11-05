from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path

tracking = 0
     ##1) trim and save new pdf 2) convert to high quality jpeg 3) OCR 4) Organize

     ## trim and save pdf
pdfPath = '/home/m/PycharmProjects/mapsProject/Images/newTest2.pdf'
pdf = PdfFileReader(pdfPath)
page = pdf.getPage(0)
page.mediaBox.lowerLeft = (1322, 1894)
page.mediaBox.upperRight = (1496, 1905.8)
     #print(page.mediaBox)
pdfWriter = PdfFileWriter()
pdfWriter.addPage(page)

with Path("cropped.pdf").open(mode="wb") as outputFile:
          pdfWriter.write(outputFile)

##convert to jpeg
import convertPdfToJpeg
convertPdfToJpeg
tracking = tracking + 1
##OCR
import useOcr
useOcr









