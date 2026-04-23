from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import joblib
import os

def extract_features(jobs_texts, users_texts):
    """
    Extract TF-IDF features for jobs and users.
    """
    vectorizer = TfidfVectorizer(max_features=5000)
    all_texts = jobs_texts + users_texts
    tfidf_matrix = vectorizer.fit_transform(all_texts)
    
    jobs_tfidf = tfidf_matrix[:len(jobs_texts)]
    users_tfidf = tfidf_matrix[len(jobs_texts):]
    
    # Save vectorizer
    os.makedirs('../models', exist_ok=True)
    joblib.dump(vectorizer, '../models/tfidf_vectorizer.pkl')
    
    return jobs_tfidf, users_tfidf, vectorizer

def compute_similarity(jobs_tfidf, users_tfidf):
    """
    Compute cosine similarity between jobs and users.
    """
    similarity_matrix = cosine_similarity(users_tfidf, jobs_tfidf)
    return similarity_matrix

if __name__ == "__main__":
    from data_loader import load_jobs, load_users
    from data_preprocessing import preprocess_jobs, preprocess_users
    
    jobs = load_jobs()
    users = load_users()
    jobs = preprocess_jobs(jobs)
    users = preprocess_users(users)
    
    jobs_texts = jobs['processed_text'].tolist()
    users_texts = users['processed_skills'].tolist()
    
    jobs_tfidf, users_tfidf, _ = extract_features(jobs_texts, users_texts)
    similarity = compute_similarity(jobs_tfidf, users_tfidf)
    
    print("Jobs TF-IDF shape:", jobs_tfidf.shape)
    print("Users TF-IDF shape:", users_tfidf.shape)
    print("Similarity shape:", similarity.shape)
    print("Sample similarity for user 0:", similarity[0][:5])