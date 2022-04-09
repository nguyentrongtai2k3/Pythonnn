

with open(r'D:\Python\mytext.txt','r',encoding='utf-8') as file:
	documents= [s.strip() for s in file.readlines()]
def get_one_hot_vct(string):
    processed_docs = [doc.lower().replace("."," ") for doc in documents]
    vocab = {}
    count = 0
    for doc in processed_docs:
        for word in doc.split():
            if word not in vocab :
                count = count +1
                vocab[word] = count
    onehot_encode = []
    for word in string.split():
        temp = [0]*len(vocab)
        if word in vocab:
            temp[vocab[word]-1] = 1
        onehot_encode.append(temp)
    return onehot_encode
    print(processed_docs[1])
from sklearn.feature_extraction.text import CountVectorizer

processed_docs = [doc.lower().replace("."," ")for doc in documents]
count_vect = CountVectorizer()
bow_rep = count_vect.fit_transform(processed_docs)
print("Our vocab:",count_vect.vocabulary_)
bow_rep[0].toarray()
temp = count_vect.transform(["nothing impossible"])
temp.toarray()
#####################################
from sklearn.feature_extraction.text import CountVectorizer
with open(r'D:\Python\mytext.txt','r',encoding='utf-8') as file:
	documents= [s.strip() for s in file.readlines()]
processed_docs = [doc.lower().replace("."," ") for doc in documents]
count_vect = CountVectorizer(ngram_range=(1,3))
bow_rep = count_vect.fit_transform(processed_docs)
print("our vocab : ",count_vect.vocabulary_)
print(bow_rep[0].toarray())
#####################################
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer()
bow_rep_tfidf = tfidf.fit_transform((processed_docs))
print("TF IDF :",tfidf.idf_)
print("All word in vocab",tfidf.get_feature_names())
print("TF IDF for all docs in our corpus\n",bow_rep_tfidf.toarray())
temp = tfidf.transform(["nothing impossible"])
print("TFIDF for temp:\n",temp.toarray())
#####################################
from gensim.models import Word2Vec
import re
from nltk import word_tokenize
import warnings
warnings.filterwarnings('ignore')
with open(r'D:\Python\mytext.txt','r',encoding='utf-8') as file:
	documents= [s.strip() for s in file.readlines()]
corpus = []
for sentence in documents:
    text1 = re.sub(r'[?|~|!|@|#|$|%|^|&|*|(|)|\|<|>|]',r'',sentence)
    word = word_tokenize(text1.lower())
    corpus.append(word)
model_cbow = Word2Vec(corpus,min_count=1,sg= 0)
print(model_cbow)

words = list(model_cbow.wv.key_to_index)
print(model_cbow.wv.get_vector("since",norm = True))