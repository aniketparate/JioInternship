# from translate import Translator
# translator= Translator(to_lang="english")
# translation = translator.translate("Class 12 Hindi (Core) हिंदी Medium | सभी State Boards के लिए। सभी पाठ उपलब्ध")
# print (translation)

# हिंदी सभी के लिए सभी पाठ उपलब्ध
# Class 12 Hindi (Core) हिंदी Medium | सभी State Boards के लिए। सभी पाठ उपलब्ध


# import re
# pattern = re.compile('हिंदी')
# str = 'Class 12 Hindi (Core) हिंदी Medium | सभी State Boards के लिए। सभी पाठ उपलब्ध'
# a = pattern.search(str)
# print(a)
# print(a[0])


# import re
# pattern = re.compile("[A-Z][a-z]+(?= medium)","(?<= medium)[A-Z][a-z]+", re.IGNORECASE)
# str = 'Class 12 Hindi (Core) Hindi Medium Hello सभी State Boards के लिए। सभी पाठ उपलब्ध'
# print(pattern.search(str))
# import re
# pattern = re.compile("[A-Z][a-z]+(?= medium)", re.IGNORECASE)
# str = 'Class 12 Hindi (Core) Hindi Medium Hello सभी State Boards के लिए। सभी पाठ उपलब्ध'
# a=pattern.search(str)
# print(a[0])


# import re
# pattern = re.compile("[\u0900-\u097F]+(?= medium)", re.IGNORECASE)
# pattern = re.compile("(?<= medium)[\u0900-\u097F]+", re.IGNORECASE)
# str = 'Class 12 Hindi (Core) Hindi हिंदी Medium लिए सभी पाठ उपलब्ध'
# a = pattern.search(str)
# print(a[0])
# Class 12 Hindi (Core) Hindi हिंदी Medium लिए । सभी पाठ उपलब्ध

import re
# pattern = re.compile("(?<= medium )[\u0900-\u097F]+", re.IGNORECASE)
# str = 'Class 12 Hindi (Core) हिंदी Medium  | सभी State Boards के लिए। सभी पाठ उपलब्ध'
# print(pattern.search(str))  


pattern1 = re.compile("[0-9]+|\w+(?= कक्षा)", re.IGNORECASE)
str1 = "Class 10th Maths हिंदी Medium | UP Boards के लिए उपयोगी | सभी पाठ उपलब्ध हैं"
a = pattern1.search(str1)
print(a)

# Thinkers, Beliefs and Buildings - One Shot Revision | Class 12 History Ch 4 in Hindi |UP/Bihar Board"