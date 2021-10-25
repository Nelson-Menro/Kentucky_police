# Kentucky_police


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
   2.3 Add C://Program Files/poppler-21.10.1/Library/bin to environment variables

Then script will be able to be run as normal
