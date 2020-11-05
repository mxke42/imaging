import cv2
import pytesseract
import os

img = cv2.imread('cropped.jpeg')

# Adding custom options
custom_config = r'--oem 3 --psm 6'
stateInfo = pytesseract.image_to_string(img, config=custom_config)
print(stateInfo)
os.remove('cropped.jpeg')
os.remove('cropped.pdf')