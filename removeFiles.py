#For iterating over local docs
import glob
#For using PDF functions
from PyPDF2 import PdfFileReader
#For progress bar
from tqdm import tqdm
import os
import re

toStore=[]

#change to where ScanLater is stored
f = open("C:\\Users\steel\Desktop\ScanLater.txt", "r")
for lines in tqdm(f):
    filepath=f.readline()
    filepathslice=(filepath[42:len(filepath)-1])
    toStore.append(filepathslice)
for names in toStore:
    
    #Should match your normal path
    toName="C:/Users/steel/Documents/NACDL/" + names
    
    #change this to desired target path
    toReplace="C:/Users/steel/Documents/NACDL/ToUseLater/" + names
    
    #Moves each unneeded file to target path
    os.rename(toName,toReplace)