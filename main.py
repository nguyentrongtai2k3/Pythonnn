import nltk,re
from urllib import request

from gensim.utils import unicode

myurl = "https://e.vnexpress.net/news/travel/stranded-in-vietnam-foreign-tourists-find-silver-lining-4339108.html"
html = request.urlopen(myurl).read().decode('utf8')
from bs4 import BeautifulSoup
getHTML = BeautifulSoup(html, 'html.parser')
getContent = getHTML.find('div', {'class': 'fck_detail'}).get_text(strip=True)
# with open(r'D:\Python\mytext.txt',"w",encoding='utf-8') as file :
#     file.write(getContent)
#     file.close()
###############################################################################################################
with open(r'D:\Python\mytext.txt','r',encoding='utf-8') as file:
	documents= [s.strip() for s in file.readlines()]
s2 = nltk.RegexpTokenizer(r'\w+|\$[\d\.]+|\S+')
tokens = s2.tokenize(documents[0])
from nltk.corpus import stopwords
clean_tokens = [word for word in tokens if not word in stopwords.words('english')]
print(clean_tokens)
###############################################################################################################
from spellchecker import SpellChecker
spell = SpellChecker(language='en')
misspelled = spell.unknown(clean_tokens)
###############################################################################################################
from spellchecker import SpellChecker
# for word in misspelled :
#     print(spell.correction(word))
#     print(spell.candidates(word))
###############################################################################################################
from nltk import sent_tokenize
sen = sent_tokenize(documents[0])
###############################################################################################################
from nltk.tokenize import word_tokenize
word = []
for p in sen :
    w= word_tokenize(p)
    word.append(w)
# print(word)
###############################################################################################################
with open(r'D:\Python\mytext.txt','r',encoding='utf-8') as file:
    documents = [s.strip() for s in file.readlines()]
def vocabulary(documents):
    processed_docs = [doc.lower().replace(".","") for doc in documents]
    vocab = {}
    count = 0
    for doc in processed_docs:
        for word in doc.split() :
            if word not in vocab :
                count = count+1
                vocab[word] = count
    return vocab
from nltk.stem import PorterStemmer
ps = PorterStemmer()
# for w in clean_tokens:
#     print(w," : ",ps.stem(w))
###############################################################################################################
from nltk import pos_tag
from nltk.tokenize import word_tokenize
with open(r'D:\Python\mytext.txt','r',encoding='utf-8') as file:
	documents= [s.strip() for s in file.readlines()]
word = []
for p in documents:
    w = word_tokenize(p)
    word.append(w)
    tagged = nltk.pos_tag(w)
    # print(tagged)
# print(word[0])
tagged = nltk.pos_tag(word[0])
# print(tagged)
###############################################################################################################
for p in documents:
    sen = p.lower()
    print(sen)
###############################################################################################################
text = "ur dream will come true$&$&$&$&$$&$&"
text1 = re.sub(r'[<| >| .| ,| !| (|)|#|^|&|*|+|=|$|]',r' ',text)
###############################################################################################################
from unidecode import unidecode
# unidecode("Hoàng Sa,Trường Sa là của Việt Nam")
# unidecode("VÌ TỔ QUỐC XÃ HỘI CHỦ NGHĨA VÌ LÍ TƯỞNG CỦA BÁC HỒ VĨ ĐẠI")
###############################################################################################################
# from numpy import unicode
def no_accent_vietnamese(utf8_str) :
    INTAB = "ạảãàáâậầấẩẫăắằặẳẵóòọõỏôộổỗồốơờớợởỡéèẻẹẽêếềệểễúùụủũưựữửừứíìịỉĩýỳỷỵỹđẠẢÃÀÁÂẬẦẤẨẪĂẮẰẶẲẴÓÒỌÕỎÔỘỔỖỒỐƠỜỚỢỞỠÉÈẺẸẼÊẾỀỆỂỄÚÙỤỦŨƯỰỮỬỪỨÍÌỊỈĨÝỲỶỴỸĐ"
    INTAB = [ch.encode('utf8') for ch in unicode(INTAB, 'utf8')]

    OUTTAB = "a" * 17 + "o" * 17 + "e" * 11 + "u" * 11 + "i" * 5 + "y" * 5 + "d" + \
             "A" * 17 + "O" * 17 + "E" * 11 + "U" * 11 + "I" * 5 + "Y" * 5 + "D"
    r = re.compile("|".join(INTAB))
    replaces_dict = dict(zip(INTAB, OUTTAB))
a = '''Hoàng Sa,Trường Sa là của Việt Nam'''
b = '''VÌ TỔ QUỐC XÃ HỘI CHỦ NGHĨA VÌ LÍ TƯỞNG CỦA BÁC HỒ VĨ ĐẠI'''
c = '''Welcome to Việt Nam'''
no_accent_vietnamese(a)
no_accent_vietnamese(b)
no_accent_vietnamese(c)
###############################################################################################################
