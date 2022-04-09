from gensim.models import Word2Vec
import re
from nltk import word_tokenize
import numpy as np
import warnings
warnings.filterwarnings('ignore')
with open(r'D:\Python\mytext.txt','r',encoding='utf-8') as file:
	documents= [s.strip() for s in file.readlines()]
corpus = []
for sentence in documents:
    text1 = re.sub(r'[?|`|!|,|:|;|"|&|/|(|)|\|<|>|]',r'',sentence)
    word = word_tokenize(text1.lower())
    corpus.append(word)
model_cbow = Word2Vec(corpus,min_count=1,sg= 0)
print(model_cbow)

words = list(model_cbow.wv.key_to_index)
print(model_cbow.wv.get_vector("since",norm = True))
print("teaching and collect", model_cbow.wv.similarity('teaching','collects'))
print(" collect only ", model_cbow.wv.similarity('only','collects'))
print(model_cbow.wv.most_similar('teaching'))
print(model_cbow.wv.most_similar('collects'))
print(model_cbow.wv.most_similar('only'))
