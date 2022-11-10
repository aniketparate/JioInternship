import pandas as pd
import re

def use_regex(input_text):
    pattern = re.compile("हिंदी", re.IGNORECASE)
    a = pattern.search(input_text)

    if a:
        print(True)
    else:
        print(False)


def findClass(input_text):
    pattern1 = re.compile("class [0-9]+", re.IGNORECASE)
    pattern2 = re.compile("कक्षा [0-9]+", re.IGNORECASE)

    srh1 = pattern1.search(input_text)
    srh2 = pattern2.search(input_text)

    if srh1:
        print(srh1[0].split()[1])
    elif srh2:
        print(srh2[0].split()[1])
    else:
        print(None)
        # print(input_text)


def findMedium(input_text):
    string = "[A-Z][a-z]+(?= medium)", "(?<= medium)[A-Z][a-z]+"
    medium = "hindi", "english", "हिंदी"
    num = string.__len__()
    i = 0
    while i != num:
        pattern = re.compile(string[i], re.IGNORECASE)
        srh = pattern.search(input_text)
        if srh:
            print(True)
            i+=1
        else:
            print(False)
            i+=1

    # str = 'Class 12 Hindi (Core) Hindi Medium Hello सभी State Boards के लिए। सभी पाठ उपलब्ध'
    

    # a = pattern1.search(input_text)

    

def findSubject():
    pass

def findAuthor():
    pass

file = "magnet_brain_hindi.xlsx"
data = pd.read_excel(file, usecols=['playlist_name'])


for i in data.itertuples():
    print(i[0])
    findMedium(i[1])
