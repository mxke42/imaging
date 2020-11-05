from PyPDF2 import PdfFileReader
pdfPath = '/home/m/PycharmProjects/mapsProject/cropped.pdf'

pdf = PdfFileReader(pdfPath)

page = pdf.getPage(0)
print(page.extractText())