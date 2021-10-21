###SCRIPT FOR ITERATING THROUGH FILES AND MOVING OUT FILES LARGER THAN A GIVEN PAGE LIMIT###



#For iterating over local docs
import glob
#For using PDF functions
from PyPDF2 import PdfFileReader
#For progress bar
from tqdm import tqdm

#Libraries for moving our files
import os
import re

#Constant representing max pages we want to work with for now
TARGET=50

#Array of files to push to side for now
toStore=[]

#Uses the glob library to iterate over files on local device like one would in a stored array
#The tqdm in front of the body of the loop here will cause a progress bar output
#Make sure you adjust the file path to match your machine
for filepath in tqdm(glob.iglob(r'C:\Users\steel\Documents\NACDL\*.pdf')):
    
    #Makes sure pdf reader closes when we are done with it
    with open(filepath, "rb") as f:
    
        #Sets and opens current pdf based on the filepath variable in the loop
        pdf = PdfFileReader(f, "rb")
    
        #Little test to assure page numbers are printed correctly
        #print(pdf.getNumPages())
        pageNum=pdf.getNumPages()
    
        #stores files too large in a separate array to help sort later
        if pageNum>TARGET:
            
            #Gets only the file name in the full path for moving purposes
            filepathslice=(filepath[31:len(filepath)])
            toStore.append(filepathslice)

#Be sure the files are not open elsewhere on the pc as this will cause error from the program
for names in toStore:
    
    #Should match your normal path
    toName="C:/Users/steel/Documents/NACDL/" + names
    
    #change this to desired target path
    toReplace="C:/Users/steel/Documents/NACDL/ToUseLater/" + names
    
    #Moves each unneeded file to target path
    os.rename(toName,toReplace)
