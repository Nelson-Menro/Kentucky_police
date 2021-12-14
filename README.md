# DMV_police
The files include both the main extraction and several frameworks for future extraction.  They are as follows:

CaseName.py: A framework for Case caption that is in progress and can be expanded upon

CaseNumberExtractionOneDocument.py: A framework script utilizing a deepscan (see below) for case number extraction

Final_Output_NACDL.csv: The final error checked csv file made from the master extractor

MasterExtractor.py: The main program that, when ran, will collect and output case number, filename, judge, court name, and filing date to a csv

PsuedoDocumentPages.py: Basic proof of concept to get page numbers from a set of documents

ScanLater.txt: A collection of documents unable to be properly parsed or outliers to the dataset

SimpleExtractionTextPDF.py: Demonstration of text extraction using a deep scan method (see below)

UpdatedSort.py: Framework for extracting a documents case number more efficiently than deep scan

brennanextraction: Demonstration of date extraction via deep scan (see below)

date_and_court: The date and court name script that was combined with MasterExtractor.py

dateforloop: The date script that was added to MasterExtractor.py

findjudgeName.py: The script for finding judge name that was added to MasterExtractor.py

removeFiles.py: Script for removing outlier files from a filepath given target files







# FOR UTILIZING ANY SCRIPTS THAT USE PYTESSERACT DEEP SCAN
# HOW TO PREPARE TO EXTRACT TEXT FROM IMAGES

1. First prepare use of tesseract  
   
            1 - You need to have Tesseract OCR installed on your computer.

            get it from here. https://github.com/UB-Mannheim/tesseract/wiki

            Download the suitable version.

        2 - Add Tesseract path to your System Environment. i.e. Edit system variables.

        3 - Run pip install pytesseract and pip install tesseract

        4 - Add this line to your python script every time
        
        pytesseract.pytesseract.tesseract_cmd = 'C:/OCR/Tesseract-OCR/tesseract.exe'  # your path 
        Guide via https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i
        


2. Ensure Poppler is installed in environment variables

2.1 Download the following https://github.com/oschwartz10612/poppler-windows/releases



2.2 Extract to C:/Program Files



2.3 Add C://Program Files/poppler-21.10.0/Library/bin to environment variables

Then script will be able to be run as normal

3. Restart your PC
