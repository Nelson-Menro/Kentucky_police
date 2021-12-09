from PIL import Image
import pytesseract
import sys
from pdf2image import convert_from_path
import os
import re
from tqdm import tqdm
import cv2

####


#change this to use in your local machine
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'


#left blank so you can choose any file
filePath = ''
doc = convert_from_path(filePath)
path, fileName = os.path.split(filePath)
fileBaseName, fileExtension = os.path.splitext(fileName)


import glob
#For using PDF functions
from PyPDF2 import PdfFileReader
#For progress bar
from tqdm import tqdm
import os
import re

#represents max pages
TARGET=50

#Array of files to push to side for now
toStore=[]
total=0
currentPage=""
different_judges = set()
def remove_prefix(x):
    to_return = []
    for i in x:
        for j in x:
            to_return.append(j[6:])
    return to_return
    
    
#Uses the glob library to iterate over files on local device like one would in a stored array
#The tqdm in front of the body of the loop here will cause a progress bar output
#Make sure you adjust the file path to match your machine
for filepath in tqdm(glob.iglob('/Users/nelson/Downloads/Suits_1002.pdf')):
    num=[]
    print('file path is ' + filepath)
    #Makes sure pdf reader closes when we are done with it
    with open(filepath, "rb") as f:


        #Sets and opens current pdf based on the filepath variable in the loop
        pdf = PdfFileReader(f, "rb")

        #Little test to assure page numbers are printed correctly
        #print(pdf.getNumPages())
        pageNum=pdf.getNumPages()
        for page in range (pageNum):
            currentPage=pdf.getPage(page).extractText()
            #regex gets two names
            x = re.findall("Judge\s[0-9a-zA-Z_]+\s[0-9a-zA-Z_]+", currentPage)
            #print(x)
            x = remove_prefix(x)
            if(len(x) > 0):
                different_judges.update(x)
            
            
            
            
            
            
            
            
            
            
            
print(different_judges)
