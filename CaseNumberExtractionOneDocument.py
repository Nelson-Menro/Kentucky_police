#SEE README FOR HELP WITH LIBRARY INSTALLATION
#First version of a one document case number grab
from PIL import Image
import pytesseract
import sys
from pdf2image import convert_from_path
import os
import cv2
import re
from tqdm import tqdm

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

#See framework
filePath = 'C:/Users/steel/Documents/NACDL/Suits_10.pdf'
doc = convert_from_path(filePath)
path, fileName = os.path.split(filePath)
fileBaseName, fileExtension = os.path.splitext(fileName)


for page_number, page_data in tqdm(enumerate(doc)):
    txt = pytesseract.image_to_string(page_data).encode("utf-8")
    
    #Optional print line
    #print("Page # {} - {}".format(str(page_number),txt))

    allText=("Page # {} - {}".format(str(page_number),txt))
    #Regex designed to find case number on given page
    x = re.findall("....-cv[^\s]+", allText)
    
    #Continues the loop if case number not found or if tesseract grabs number wrong
    if not x or len(x[0])!=17:
        continue
    else:
        #Outputs case number and ends search
        print(x)
        break