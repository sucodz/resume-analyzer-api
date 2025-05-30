# semantic_matcher.py
from sentence_transformers import SentenceTransformer, util

# Load the model once globally (this is expensive so do it once)
model = SentenceTransformer('all-MiniLM-L6-v2')  # lightweight & fast

def get_similarity(text1, text2):
    # Encode texts to dense vectors
    embeddings1 = model.encode(text1, convert_to_tensor=True)
    embeddings2 = model.encode(text2, convert_to_tensor=True)

    # Compute cosine similarity using util.pytorch_cos_sim
    cosine_score = util.cos_sim(embeddings1, embeddings2).item()

    return round(cosine_score * 100, 2)





# # semantic_matcher.py
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

# def get_similarity(text1, text2):
#     vectorizer = TfidfVectorizer()
#     tfidf = vectorizer.fit_transform([text1, text2])
#     cosine_sim = cosine_similarity(tfidf[0:1], tfidf[1:2])
#     return round(cosine_sim[0][0] * 100, 2)




# from sentence_transformers import SentenceTransformer, util

# model = SentenceTransformer('all-MiniLM-L6-v2')

# def get_similarity(text1, text2):
#     emb1 = model.encode(text1, convert_to_tensor=True)
#     emb2 = model.encode(text2, convert_to_tensor=True)
#     score = util.pytorch_cos_sim(emb1, emb2).item()
#     return round(score * 100, 2)
