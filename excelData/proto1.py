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

# import re
# pattern = re.compile("(?<= medium )[\u0900-\u097F]+", re.IGNORECASE)
# str = 'Class 12 Hindi (Core) हिंदी Medium  | सभी State Boards के लिए। सभी पाठ उपलब्ध'
# print(pattern.search(str))  


# pattern1 = re.compile("(?<=by )[A-Z][a-z]+", re.IGNORECASE)
# str1 = "?Previous Video : https://www.youtube.com/watch?v=l5LtyBPbHUE ?Next Video : https://www.youtube.com/watch?v=mCynkD574l0 ✔️?? Watch Full Free Course: https://www.magnetbrains.com ✔️?? Get All Subjects Playlists: ​https://www.pabbly.com/out/all-videos-playlist ✔️?? Let's Collaborate With Magnet Brains For Content Sharing https://www.magnetbrains.com/out/collaboration ======================================================= ? Full Playlist Link: https://www.youtube.com/playlist?list=PL4BZMEV0Q77jigz-fOj1fg0nChC-CGkfX ✅ In this video, ✔️ Class: 12th ✔️ Subject: Hindi/हिंदी - NCERT (आरोह भाग 2) ✔️ Chapter: Atma Parichay, Ek Geet/आत्म-परिचय, एक गीत (Chapter 1) ✔️ Topic Name: Atma Parichay, Ek Geet - One Shot Revision/आत्म-परिचय, एक गीत - One Shot Revision ✔️ Topics Covered In This Video (By Lali Mam): In this video, One Shot Revision of &quot;Class 12 Hindi Aroh Chapter 1&quot; named Atma Parichay, Ek Geet/आत्म-परिचय, एक गीत have been discussed. ======================================================= 00:00 Atma Parichay, Ek Geet/आत्म-परिचय, एक गीत - Introduction 02:44 हरिवंश राय बच्चन - जीवन परिचय 15:03 Atma Parichay - Explanation 21:31 एक गीत - Explanation 39:57 Website Slider ======================================================= Why study from Magnet Brains Hindi? Magnet Brains Hindi is an online education platform that helps gives you NCERT/CBSE curriculum-based free full courses from Kindergarten to Class 12th so that you can perform well in any and all exams you give in your academic career. ? Contact us ?? ➡️ Connect with us : magnetbrainsbhopal@gmail.com ➡️ Website : https://www.magnetbrains.com/ ➡️ Subscribe to us on YouTube: https://www.youtube.com/channel/UCwO6AYOIRYgyP1KJ5aPbDlw?sub_confirmation=1 ➡️ Subscribe to Magnet Brains English Medium : https://www.youtube.com/channel/UC3HS6gQ79jjn4xHxogw0HiA?sub_confirmation=1 ➡️ Subscribe to Magnet Brains IIT JEE &amp; NEET: https://www.youtube.com/channel/UC-PZSEHaQOcJiSTsbJMohZQ?sub_confirmation=1 ➡️ Subscribe to Magnet Brains Competition : https://www.youtube.com/channel/UC0PA9wn-FAXk0HsiCmg9gSA?sub_confirmation=1 ➡️Facebook-: https://www.magnetbrains.com/out/facebook ➡️Telegram-: https://www.magnetbrains.com/out/telegram ➡️Instagram:-https://www.magnetbrains.com/out/instagram_main #atmaparichay #ekgeet #class12hindi #ncert #aarohclass12 #magnetbrainshindi #hindimedium #stateboards #ncertclass12 #inhindi #class12hindi #mpboard #upboard #biharboard #ncertsolutions #ncertsolutionsinhindi #class12 #cbseclass12 class 12 hindi chapter 1 class 12 hindi aroh chapter 1 question answer class 12 hindi aroh chapter 1 summary class 12 hindi aroh chapter 1 vyakhya class 12 hindi aroh chapter 1 question answer pdf hindi chapter 1 class 12 pdf class 12 hindi antra chapter 1 question answer class 12 hindi aroh chapters summary"
# a = pattern1.search(str1)
# print(a)

# Thinkers, Beliefs and Buildings - One Shot Revision | Class 12 History Ch 4 in Hindi |UP/Bihar Board"

# Chapter: Atma Parichay, Ek Geet/आत्म-परिचय, एक गीत (Chapter 1) 

import re
pattern = re.compile("(?<=Chapter:\s)(.*?)\(", re.IGNORECASE)
str = 'Chapter: Atma Parichay, Ek Geet/आत्म-परिचय, एक गीत (Chapter 1)'
srh = pattern.search(str)

print(srh[0].strip().split('(')[0])

# "(?<=Chapter:\s).*(?=\s()"
#  
# ha try kar
# (?<= Chapter: ) [A-Z]+[\u0900-\u097F]+
# bc toh (chapte yetoyea
# aplayala baher chi matlab na chapter gela bhosadyat
# ajun ek aahe thamb
# bc mi v4 karat hoto ha chapter kasa yetoye lol hahahah
#bc split marun kiti marshil asa
# zala
# print(aniket is sexy boy)
#  hahahahcaahhahal
# chal re lavkar kar
