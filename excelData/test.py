import re
# from openpyxl import load_workbook
import pandas as pd


def findClass(input_text):
    string = "(?<=class )[0-9]+", "(?<=कक्षा )[0-9]+"
    i = 0
    num = string.__len__()
    update = data['class'] = ('')
    while i != num:
        pattern = re.compile(string[i], re.IGNORECASE)
        srh = pattern.search(input_text)
        if srh == None:
            pass
            i+=1
        else:
            # print(i)
            print(srh[0])
            i+=1
        # data.loc[update, 'class']  = srh[0]
            

file = "test1.xlsx"
data = pd.read_excel(file)

for i in data.itertuples():
    # print(i[2])
    # findClass(i[1])
    findClass(i[2])
 

# update = data['class'] = ''
# data.loc[update, 'class']  = output
# print(data)

