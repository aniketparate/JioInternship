import pandas as pd
import re

class findColumnData: 
    def findClass(self, id, input_text):
        string = "(?<=class )[0-9]+", "(?<=CBSE )[0-9]+[a-z]+", "(?<=class )[0-9]+[a-z]+", "(?<=CBSE )[0-9]+", "[0-9]+[a-z]+(?= class)", "[0-9]+[a-z]+(?= CBSE)" 
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

    # def findMedium(self, id, input_text):
    #     string = "[\u0900-\u097F]+(?= medium)", "[A-Z][a-z]+(?= medium)", "(?<= medium)[A-Z][a-z]+", "(?<= medium )[\u0900-\u097F]+"
    #     medium = "hindi", "english", "हिंदी", "अंग्रेज़ी"
    #     num = string.__len__()
    #     i = 0
    #     while i != num:
    #         pattern = re.compile(string[i], re.IGNORECASE)
    #         srh = pattern.search(input_text)
            
    #         for med in medium:
    #             if srh == None:
    #                 i+=1
    #                 pass
    #             elif med == srh[0]:
    #                 data.loc[id, ['medium']] = [srh[0]]
    #                 i+=1
    #             else:
    #                 i+=1
        
    def findSubject(self, id, input_text1 , input_text2):
        subject = "Economics", "Physics", "Maths", "Chemistry", "Biology", "Hindi", "Psychology", "Arts", "English"
        i = 0
        num = subject.__len__()
        while i != num:
            string = "("+subject[i]+")"
            
            pattern = re.compile(string, re.IGNORECASE)
            srh1 = pattern.search(input_text1)
            srh2 = pattern.search(input_text2)

            if srh1 == None:
                if srh2 == None:
                    i+=1
                    pass
                else:
                    i+=1
                    data.loc[id, ['subject']] = [srh2[0]]
            else:
                i+=1
                data.loc[id, ['subject']] = [srh1[0]]


    def findAuthor(self, id, input_text):
        pattern = re.compile("(?<=by )[A-Z]{1}[a-z]+ [A-Z][a-z]+", re.IGNORECASE)
        pattern2 = re.compile("[A-Z][a-z]+")
        srh = pattern.search(input_text)

        if srh == None:
            pass
        else:
            str = pattern2.search(srh[0])
            if str == None:
                pass
            elif srh[0].split()[0] == str[0]:
                data.loc[id, ['author_name']] = [srh[0]]

if __name__ == '__main__':
    file = "usp_studio.xlsx"
    newUpdatedFile = "update_" + file

    data = pd.read_excel(file)

    colData = findColumnData()

    for i in data.itertuples():
        colData.findClass(i[0], i[8])
        # colData.findMedium(i[0], i[8])
        colData.findSubject(i[0], i[7] ,i[8])
        colData.findAuthor(i[0], i[15])

    data.to_excel(newUpdatedFile, index=False)
