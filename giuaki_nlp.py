from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

d = "He wants to become a great inventor."
processed_docs= [d.strip()]

tfidf = TfidfVectorizer()
bow_rep_tfidf = tfidf.fit_transform(processed_docs)
#
# print("IDF for all words in the vocabulary",tfidf.idf_)
#
# print("All words in the vocabulary",tfidf.get_feature_names())
#
# print("TFIDF representation for all documents in our corpus\n",bow_rep_tfidf.toarray())
count_vect = CountVectorizer(ngram_range=(1,3))
bow_rep = count_vect.fit_transform(processed_docs)
print("our vocab : ",count_vect.vocabulary_)
print(bow_rep[0].toarray())