#For iterating over local docs
import glob

#For using PDF functions
from PyPDF2 import PdfFileReader

#For progress bar
from tqdm import tqdm



#Uses the glob library to iterate over files on local device like one would in a stored array
#The tqdm in front of the body of the loop here will cause a progress bar output
#Make sure you adjust the file path to match your machine
for filepath in tqdm(glob.iglob(r'C:\Users\steel\Documents\NACDL\*.pdf')):
    
    #Sets and opens current pdf based on the filepath variable in the loop
    pdf = PdfFileReader(open(filepath,'rb'))
    
    #Little test to assure page numbers are printed correctly
    print(pdf.getNumPages())