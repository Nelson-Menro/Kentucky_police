
#For iterating over local docs
import glob
#For using PDF functions
from PyPDF2 import PdfFileReader
#For progress bar
from tqdm import tqdm
import os
import re
#For the csv
import pandas as pd

#reads in csv from template
df = pd.read_csv(r'C:\Users\steel\Documents\NACDL\data_structure_template.csv')

toStore=[]
total=0
counter=0
currentPage=""
#Uses the glob library to iterate over files on local device like one would in a stored array
#The tqdm in front of the body of the loop here will cause a progress bar output
#Make sure you adjust the file path to match your machine
for filepath in tqdm(glob.iglob(r'C:\Users\steel\Documents\NACDL\*.pdf')):
    num=[]
    print(filepath)
    #Makes sure pdf reader closes when we are done with it
    with open(filepath, "rb") as f:
        counter+=1    
        #Sets and opens current pdf based on the filepath variable in the loop
        pdf = PdfFileReader(f, "rb")
            
        #Little test to assure page numbers are printed correctly
        #print(pdf.getNumPages())
        pageNum=pdf.getNumPages()
        
        for page in range (pageNum):
            currentPage=pdf.getPage(page).extractText()
            #print (currentPage)
            x = re.findall("....-c.[^\s]+", currentPage)
            y = re.findall("Case.\d[^\s]+",currentPage)
            z = re.findall("Case No[^\s]+\d[^\s]+",currentPage)
            a = re.findall("Case..\d[^\s]+",currentPage)
            b = re.findall("Case#[^\s]\d.[^\s]+\d[^\s]",currentPage)
            #print(a)
            #print(b)
            #print(x)
            #print(y)
            #print(z)
            if (not x or not(len(x[0])>=16 and len(x[0])<=17)) and not y:
                continue
            else:
                if b:
                    df.loc[counter,'Case_Number']=b[0]
                    df.loc[counter,'Document_filename']=filepath
                    print(b[0])
                    break
                elif y:
                    df.loc[counter,'Case_Number']=y[0]
                    df.loc[counter,'Document_filename']=filepath
                    y[0]=y[0].split("Case ",1)[1]
                    print(y[0])
                    break
                elif z:
                    df.loc[counter,'Case_Number']=z[0]
                    df.loc[counter,'Document_filename']=filepath
                    print(z[0])
                    break
                elif a:
                    df.loc[counter,'Case_Number']=a[0]
                    df.loc[counter,'Document_filename']=filepath
                    print(a[0])
                    break
                elif x:
                    df.loc[counter,'Case_Number']=x[0]
                    df.loc[counter,'Document_filename']=filepath
                    print(x[0])
                    break
            
        for page in range (pageNum):
                    currentPage=pdf.getPage(page).extractText()
                    #print(currentPage)
                    #Regex designed to find case date
                    date = re.findall("Filed: (.*)", currentPage)
                    #Alternate regex for other format for date
                    date2 = re.findall("Filed (.*)", currentPage, )
                    date3 = re.findall("iled (.*)", currentPage)
                    date4 = re.findall("filed on(.*)", currentPage)
                    #print(date, date2, date3, date4)
                    #Removes trailing characters from Date
                    if date:
                        date[0]=date[0].split(" ",1)[0]
                        date[0]=date[0].split("Date",1)[0]
                    elif date2:
                        date2[0]=date2[0].split(" ")[0]
                    elif date3:
                        date3[0]=date3[0].split(" ")[0]
                    elif date4:
                        date4[0]=date4[0].split(" ")[0]

                    #Prints the Date Filled
                    if date:
                        df.loc[counter,'Filing Date']=date[0]
                        print(date[0])
                        break
                    elif date2:
                        df.loc[counter,'Filing Date']=date2[0]
                        print(date2[0])
                        break
                    elif date3:
                        df.loc[counter,'Filing Date']=date3[0]
                        print(date3[0])
                        break
                    elif date4:
                        df.loc[counter,'Filing Date']=date4[0]
                        print(date4[0])
                        break
        for page in range (pageNum):
                    currentPage=pdf.getPage(page).extractText()   
                    court = re.findall("(DISCRICT OF COLUMBIA COURT OF APPEALS )\w", currentPage, re.IGNORECASE)
                    court2 = re.findall("(UNITED STATES DISTRICT COURT FOR THE DISTRICT OF COLUMBIA )\w", currentPage, re.IGNORECASE)
                    court3 = re.findall("(U.S. DISTRICT COURT )\w", currentPage, re.IGNORECASE)
                    court3_5 = re.findall("(U.S. DISTRICT COURT)\w", currentPage, re.IGNORECASE)
                    court4 = re.findall("(SUPERIOR COURT OF THE DISTRICT OF COLUMBIA)\w", currentPage, re.IGNORECASE)
                    court5 = re.findall("(United States Bankruptcy Court for the District of Columbia )\w", currentPage, re.IGNORECASE)

                    if court:
                        df.loc[counter,'Court_Name']=court[0]
                        print(court[0])
                        break
                    elif court2:
                        df.loc[counter,'Court_Name']=court2[0]
                        print(court2[0])
                        break
                    elif court3:
                        df.loc[counter,'Court_Name']="UNITED STATES DISTRICT COURT FOR THE DISTRICT OF COLUMBIA"
                        print("UNITED STATES DISTRICT COURT FOR THE DISTRICT OF COLUMBIA")
                        break
                    elif court3_5:
                        df.loc[counter,'Court_Name']="UNITED STATES DISTRICT COURT FOR THE DISTRICT OF COLUMBIA"
                        print("UNITED STATES DISTRICT COURT FOR THE DISTRICT OF COLUMBIA")
                    elif court4:
                        df.loc[counter,'Court_Name']=court4[0]
                        print(court4[0])
                        break
                    elif court5:
                        df.loc[counter,'Court_Name']=court5[0]
                        print(court5[0])
                        break
        for page in range (pageNum):
            currentPage=pdf.getPage(page).extractText()
            #regex gets two names
            x = re.findall("Judge\s[0-9a-zA-Z_]+\s[0-9a-zA-Z_]+", currentPage)
            #print(x)
            x = remove_prefix(x)
            if(len(x) > 0):
                different_judges.update(x)
                df.loc[counter,'Judge_Name']=x[0]
                print(x[0])
                break

#exports csv

df.to_csv('test_output.csv')
