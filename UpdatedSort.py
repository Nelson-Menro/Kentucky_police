###SCRIPT FOR ITERATING THROUGH FILES AND MOVING OUT FILES LARGER THAN A GIVEN PAGE LIMIT###
#For iterating over local docs
import glob
#For using PDF functions
from PyPDF2 import PdfFileReader
#For progress bar
from tqdm import tqdm
import os
import re

#Constant representing max pages we want to work with for now
TARGET=50

#Array of files to push to side for now
toStore=[]
total=0
currentPage=""
#Uses the glob library to iterate over files on local device like one would in a stored array
#The tqdm in front of the body of the loop here will cause a progress bar output
#Make sure you adjust the file path to match your machine
for filepath in tqdm(glob.iglob(r'C:\Users\steel\Documents\NACDL\*.pdf')):
    num=[]
    print(filepath)
    #Makes sure pdf reader closes when we are done with it
    with open(filepath, "rb") as f:
        
            
        #Sets and opens current pdf based on the filepath variable in the loop
        pdf = PdfFileReader(f, "rb")
            
        #Little test to assure page numbers are printed correctly
        #print(pdf.getNumPages())
        pageNum=pdf.getNumPages()
        
        for page in range (pageNum):
            currentPage=pdf.getPage(page).extractText()
            x = re.findall("....-c.[^\s]+", currentPage)
            y = re.findall("Case No..............",currentPage)
            if x:
                x[0]=x[0].split("\\n",1)[0]
            elif y:
                print(y)
                try:
                    y[0]=y[0].split(": ",1)[1]
                except IndexError:
                    y[0]=y[0].split(". ",1)[1]
            if (not x or not(len(x[0])>=16 and len(x[0])<=17)) and not y:
                continue
            else:
                if not x:
                    print(y[0])
                    num.append(y[0])
                    break
                else:
                    print(x[0])
                    num.append(x[0])
                    break
