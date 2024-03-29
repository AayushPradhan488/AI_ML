'''import cv2
import pytesseract
import numpy as np

path = 'C:\\Users\\Amruta\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages'
pytesseract.pytesseract.tesseract_cmd = path

img = cv2.imread('Intro.png')
#Alternatively: can be skipped if you have a Blackwhite image
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
gray, img_bin = cv2.threshold(gray,128,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
gray = cv2.bitwise_not(img_bin)

kernel = np.ones((2, 1), np.uint8)
img = cv2.erode(gray, kernel, iterations=1)
img = cv2.dilate(img, kernel, iterations=1)
out_below = pytesseract.pytesseract.image_to_string(img)
print("OUTPUT:", out_below)

print("Success!")'''

import pytesseract
from PIL import Image

path = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = path

def perform_ocr(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text

print(perform_ocr('Intro.png'))