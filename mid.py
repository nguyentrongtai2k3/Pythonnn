import re
from unidecode import unidecode
from nltk.stem import PorterStemmer
import nltk
from nltk.stem import WordNetLemmatizer
text = "= + Sau khi & & được GIẢI PHÓNG VÀO ( ) < > . , & * = + NGÀY 10 THÁNG  10 NĂM 1954, Hà  NỘI TRỞ THÀNH thủ đô của ! # $ ^ Việt Nam Dân chủ Cộng hòa & +."
#xoa ki tu dac biet
text1 = re.sub(r'[<|_|  |>| .| ,| !| (|)|#|^|&|*|+|=|$|{1:9}|0|]',r' ',text)
# xoa dau tieng viet
text2 = (unidecode(text.lower()))
print(text1,end="\n")
lemmatizer = WordNetLemmatizer()
lemmatized_output = ' '.join([lemmatizer.lemmatize(w) for w in text2])
print(lemmatized_output)
