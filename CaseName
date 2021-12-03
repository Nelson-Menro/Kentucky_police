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
for filepath in tqdm(glob.iglob(r'/Users/edwardaloba/Documents/CaseNumber/*.pdf')):
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
            x =re.findall("(PITTS et al v. DISTRICT OF COLUMBIA et al )\w", currentPage)
            y = re.findall("(KATZ, MITCHELL A. Vs. DISTRICT OF COLUMBIA et al )\w", currentPage)
            z = re.findall("(QUEEN et al v. DISTRICT OF COLUMBIA et al )\w", currentPage)
            a = re.findall("(A.B. et al v. DISTRICT OF COLUMBIA et al )\w", currentPage)
            b = re.findall("(BRIGGS et al v. DISTRICT OF COLUMBIA et al )\w", currentPage)
            c = re.findall("(Collis V. Timlick )\w", currentPage)
            d = re.findall("(QUEEN et al v. DISTRICT OF COLUMBIA et al )\w", currentPage)
            if x:
                x[0]=x[0]
                print(x[0])
            if y:
                y[0]=y[0]
                print(y[0])
            if z:
                z[0]=z[0]
                print(z[0])
            if a:
                a[0]=a[0]
                print(a[0])
            if b:
                b[0]=b[0]
                print(b[0])
            if c:
                c[0]=c[0]
                print(c[0])
            if d:
                d[0]=d[0]
                print(d[0])
   
