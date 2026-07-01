from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# --------------------------------------
# ATS Score Function
# --------------------------------------

def calculate_ats_score(resume_text, job_description):

    # Create TF-IDF Vectorizer
    vectorizer = TfidfVectorizer()


    # Convert text into vectors
    vectors = vectorizer.fit_transform(
        [resume_text, job_description]
    )


    # Calculate cosine similarity
    similarity = cosine_similarity(
        vectors[0:1],
        vectors[1:2]
    )[0][0]


    # Convert into percentage
    ats_score = round(similarity * 100, 2)

    return ats_score