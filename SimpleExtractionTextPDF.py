#Super simple script for extracting all text from a single PDF document
from PIL import Image
import pytesseract
import sys
from pdf2image import convert_from_path
import os
import cv2

#Needed to run tesseract, is based on your set path
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

#your filepath to the desired doc
filePath = 'C:/Users/steel/Documents/NACDL/Suits_2.pdf'

#Loads document

#Grabs file data for cleaner output
doc = convert_from_path(filePath)
path, fileName = os.path.split(filePath)
fileBaseName, fileExtension = os.path.splitext(fileName)

#Extracts all text from each page and outputs to standard out
for page_number, page_data in enumerate(doc):
    txt = pytesseract.image_to_string(page_data).encode("utf-8")
    print("Page # {} - {}".format(str(page_number),txt))