from sklearn.feature_extraction.text import TfidfVectorizer
#
d = "He wants to become a great inventor."
documents= [d.strip()]
processed_docs = [doc.lower().replace("."," ") for doc in documents]
print(processed_docs)
tfidf = TfidfVectorizer()
bow_rep_tfidf = tfidf.fit_transform((processed_docs))
print(tfidf.idf_)
print("TFIDF representation for all documents in our corpus\n",bow_rep_tfidf.toarray())
print("-"*10)