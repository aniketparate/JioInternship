import pandas as pd
import re

class findColumnData:
    def findClass(self, id, input_text):
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
                i+=1

    def findMedium(self, id, input_text):
        string = "[\u0900-\u097F]+(?= medium)", "[A-Z][a-z]+(?= medium)", "(?<= medium)[A-Z][a-z]+", "(?<= medium )[\u0900-\u097F]+"
        medium = "hindi", "english", "हिंदी", "अंग्रेज़ी"
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
                    data.loc[id, ['medium']] = [srh[0]]
                    i+=1
                else:
                    i+=1    
        
    def findSubject(self, id, input_text):
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
                str = srh[0].split()[1] + ' Science'
                data.loc[id, ['subject']] = [str]
            else:
                i+=1
                str = srh[0].split()[1]
                data.loc[id, ['subject']] = [str]

    def findAuthor(self, id, input_text):
        pattern = re.compile("(?<=by )[A-Z][a-z]+ [A-Z][a-z]+", re.IGNORECASE)
        srh = pattern.search(input_text)

        if srh == None:
            pass
        else:
            data.loc[id, ['author_name']] = [srh[0]]

    def findChapter(self, id, input_text):
        pattern = re.compile("(?<=Chapter:\s)(.*?)\(", re.IGNORECASE)
        srh = pattern.search(input_text)
        if srh == None:
            pass
        else:
            data.loc[id, ['chapter_name']] = [srh[0].split(r'/')[0].split('(')[0].split('-')[0]]

if __name__ == '__main__':
    file = "magnet_brain_hindi.xlsx"
    newUpdatedFile = "update_" + file

    data = pd.read_excel(file)

    colData = findColumnData()

    for i in data.itertuples():
        colData.findClass(i[0], i[8])
        colData.findMedium(i[0], i[8])
        colData.findSubject(i[0], i[8])
        colData.findChapter(i[0], i[17])
        colData.findAuthor(i[0], i[17])

    data.to_excel(newUpdatedFile, index=False)
    print(data)
