import cv2
import pytesseract
import os
import re
import shutil


def use_ocr(jpeg, path):
    img = cv2.imread(jpeg)

    # Adding custom options
    custom_config = r'--oem 3 --psm 6'
    stateInfo = pytesseract.image_to_string(img, config=custom_config)
    stateName = re.search(".{1,20}", stateInfo).group()
    shutil.rmtree(path)
    return stateName

def ocr_get_file_key(jpeg):
    img = cv2.imread(jpeg)

    # Adding custom options
    custom_config = r'--oem 3 --psm 6'
    fileKey = pytesseract.image_to_string(img, config=custom_config).replace('\n', ' ').replace('\x0c', '').strip()

    shutil.rmtree('/home/m/PycharmProjects/mapsProject/Images/Temp')
    return fileKey


def bulk_use_ocr(jpeg1,
                 jpeg2,
                 jpeg3,
                 jpeg4,
                 jpeg5,
                 jpeg6,
                 jpeg7,
                 jpeg8,
                 jpeg9, ):
    img = cv2.imread(jpeg1)
    custom_config = r'--oem 3 --psm 6'
    gridName1 = pytesseract.image_to_string(img, config=custom_config).replace('\n', ' ').replace('\x0c', '').strip()
    # print(gridName1)

    img = cv2.imread(jpeg2)
    custom_config = r'--oem 3 --psm 6'
    gridName2 = pytesseract.image_to_string(img, config=custom_config).replace('\n', ' ').replace('\x0c', '').strip()
    # print(gridName2)

    img = cv2.imread(jpeg3)
    custom_config = r'--oem 3 --psm 6'
    gridName3 = pytesseract.image_to_string(img, config=custom_config).replace('\n', ' ').replace('\x0c', '').strip()
    # print(gridName3)

    img = cv2.imread(jpeg4)
    custom_config = r'--oem 3 --psm 6'
    gridName4 = pytesseract.image_to_string(img, config=custom_config).replace('\n', ' ').replace('\x0c', '').strip()
    # print(gridName4)

    img = cv2.imread(jpeg5)
    custom_config = r'--oem 3 --psm 6'
    gridName5 = pytesseract.image_to_string(img, config=custom_config).replace('\n', ' ').replace('\x0c', '').strip()
    # print(gridName5)

    img = cv2.imread(jpeg6)
    custom_config = r'--oem 3 --psm 6'
    gridName6 = pytesseract.image_to_string(img, config=custom_config).replace('\n', ' ').replace('\x0c', '').strip()

    # print(gridName6)

    img = cv2.imread(jpeg7)
    custom_config = r'--oem 3 --psm 6'
    gridName7 = pytesseract.image_to_string(img, config=custom_config).replace('\n', ' ').replace('\x0c', '').strip()
    # print(gridName7)

    img = cv2.imread(jpeg8)
    custom_config = r'--oem 3 --psm 6'
    gridName8 = pytesseract.image_to_string(img, config=custom_config).replace('\n', ' ').replace('\x0c', '').strip()
    # print(gridName8)

    img = cv2.imread(jpeg9)
    custom_config = r'--oem 3 --psm 6'
    gridName9 = pytesseract.image_to_string(img, config=custom_config).replace('\n', ' ').replace('\x0c', '').strip()
    # print(gridName9)
    # shutil.rmtree(path)
    # return stateName

    gridMatrix = [gridName1, gridName2, gridName3,
                  gridName4, gridName5, gridName6,
                  gridName7, gridName8, gridName9]
    # print(gridMatrix)
    shutil.rmtree('/home/m/PycharmProjects/mapsProject/Images/Temp')
    return gridMatrix

def bulk_use_ocr2(jpeg1,
                 jpeg2,
                 jpeg3,
                 jpeg4,
                 jpeg5,
                 jpeg6,
                 jpeg7,
                 jpeg8,
                 jpeg9, ):
    img = cv2.imread(jpeg1)
    custom_config = r'--oem 3 --psm 6'
    gridName1 = pytesseract.image_to_string(img, config=custom_config).replace('\n', ' ').replace('\x0c', '').strip()
    # print(gridName1)

    img = cv2.imread(jpeg2)
    custom_config = r'--oem 3 --psm 6'
    gridName2 = pytesseract.image_to_string(img, config=custom_config).replace('\n', ' ').replace('\x0c', '').strip()
    # print(gridName2)

    img = cv2.imread(jpeg3)
    custom_config = r'--oem 3 --psm 6'
    gridName3 = pytesseract.image_to_string(img, config=custom_config).replace('\n', ' ').replace('\x0c', '').strip()
    # print(gridName3)

    img = cv2.imread(jpeg4)
    custom_config = r'--oem 3 --psm 6'
    gridName4 = pytesseract.image_to_string(img, config=custom_config).replace('\n', ' ').replace('\x0c', '').strip()
    # print(gridName4)

    img = cv2.imread(jpeg5)
    custom_config = r'--oem 3 --psm 6'
    gridName5 = pytesseract.image_to_string(img, config=custom_config).replace('\n', ' ').replace('\x0c', '').strip()
    # print(gridName5)

    img = cv2.imread(jpeg6)
    custom_config = r'--oem 3 --psm 6'
    gridName6 = pytesseract.image_to_string(img, config=custom_config).replace('\n', ' ').replace('\x0c', '').strip()

    # print(gridName6)

    img = cv2.imread(jpeg7)
    custom_config = r'--oem 3 --psm 6'
    gridName7 = pytesseract.image_to_string(img, config=custom_config).replace('\n', ' ').replace('\x0c', '').strip()
    # print(gridName7)

    img = cv2.imread(jpeg8)
    custom_config = r'--oem 3 --psm 6'
    gridName8 = pytesseract.image_to_string(img, config=custom_config).replace('\n', ' ').replace('\x0c', '').strip()
    # print(gridName8)

    img = cv2.imread(jpeg9)
    custom_config = r'--oem 3 --psm 6'
    gridName9 = pytesseract.image_to_string(img, config=custom_config).replace('\n', ' ').replace('\x0c', '').strip()
    # print(gridName9)
    # shutil.rmtree(path)
    # return stateName

    gridMatrix = [gridName1, gridName2, gridName3,
                  gridName4, gridName5, gridName6,
                  gridName7, gridName8, gridName9]
    # print(gridMatrix)

    shutil.rmtree('/home/m/PycharmProjects/mapsProject/Images/Temp2')
    return gridMatrix