import pandas as pd
import re

# def use_regex(input_text):
#     pattern = re.compile("हिंदी", re.IGNORECASE)
#     a = pattern.search(input_text)

#     if a:
#         print(True)
#     else:
#         print(False)


def findClass(input_text):
    string = "(?<=class )[0-9]+", "(?<=कक्षा )[0-9]+"
    i = 0
    num = string.__len__()
    while i != num:
        pattern = re.compile(string[i], re.IGNORECASE)
        srh = pattern.search(input_text)
    
        if srh == None:
            pass
            i+=1
        else:
            print(i)
            print(srh[0])
            i+=1


def findMedium(input_text):
    string = "[\u0900-\u097F]+(?= medium)", "\w+(?= medium)", "(?<= medium)\w+", "(?<= medium )[\u0900-\u097F]+"
    medium = "hindi", "english", "हिंदी", "अंग्रेज़ी", "एन्ग्लिश्"
    num = string.__len__()
    i = 0
    while i != num:
        pattern = re.compile(string[i], re.IGNORECASE)
        srh = pattern.search(input_text)
        
        for med in medium:
            if srh == None:
                i+=1
                pass
            elif med == srh[0]:
                print(True, med, srh[0])
                i+=1
            else:
                print(False, med, srh[0])
                i+=1    
    
def findSubject(input_text):
    string = "(?<=class )[0-9]+ [A-Z][a-z]+", "(?<=class )[0-9]+[A-Z][a-z]+ [A-Z][a-z]+", "(?<=class )[0-9]+[A-Z][a-z]+ [\u0900-\u097F]+", "(?<=class )[0-9]+ [\u0900-\u097F]+"
    subject ="Political"
    i = 0
    num = string.__len__()
    while i != num:
        pattern = re.compile(string[i], re.IGNORECASE)
        srh = pattern.search(input_text)

        if srh == None:
            i+=1
            pass
        elif srh[0].split()[1].lower() == subject.lower():
            i+=1
            print(srh[0].split()[1] + ' Science')
        else:
            i+=1
            print(srh[0].split()[1])

def findAuthor(input_text):
    pattern = re.compile("(?<=by )[A-Z][a-z]+ [A-Z][a-z]+", re.IGNORECASE)
    srh = pattern.search(input_text)

    if srh == None:
        pass
    else:
        print(srh[0])

file = "magnet_brain_hindi.xlsx"
data = pd.read_excel(file, usecols=['playlist_name', 'asset_title', 'description'])

for i in data.itertuples():
    print(i[0])
    # print(i[2])
    #findMedium(i[1])
    #findClass(i[1])
    #findSubject(i[1])
    #findAuthor(i[3])
