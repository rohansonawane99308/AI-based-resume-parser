from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_similarity_score(resume_text, jd_text):
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform([resume_text, jd_text])
    return cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
