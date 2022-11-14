import re
# from openpyxl import load_workbook
import pandas as pd


def findClass(id, input_text):
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
            data.loc[id, ['class']] = [srh[0]]
            print(srh[0])
            i+=1
            

file = "test1.xlsx"
newUpdatedFile = "update_" + file
data = pd.read_excel(file)

for i in data.itertuples():
    print(i[0])
    # print(i[1])
    findClass(i[0], i[2])
    

data.to_excel(newUpdatedFile, index=False)
print(data)
