import numpy as np
from sklearn.metrics import precision_score, recall_score
import matplotlib.pyplot as plt
import seaborn as sns

def evaluate_recommendations(similarity_matrix, users_df, jobs_df, k=3):
    """
    Evaluate recommendations using precision@K.
    For simplicity, assume users prefer jobs in their category.
    """
    precisions = []
    for i, user in users_df.iterrows():
        user_category = user['preferred_category']
        # Get top k similar jobs
        top_k_indices = np.argsort(similarity_matrix[i])[::-1][:k]
        recommended_jobs = jobs_df.iloc[top_k_indices]
        # Check if any recommended job matches user's category
        matches = recommended_jobs['category'] == user_category
        precision = np.mean(matches)
        precisions.append(precision)
    
    avg_precision = np.mean(precisions)
    print(f"Average Precision@{k}: {avg_precision:.2f}")
    return avg_precision

def plot_similarity_heatmap(similarity_matrix, users_df, jobs_df):
    """
    Plot similarity heatmap for first few users and jobs.
    """
    plt.figure(figsize=(10, 8))
    sns.heatmap(similarity_matrix[:5, :5], annot=True, xticklabels=jobs_df['job_title'][:5], yticklabels=users_df['user_id'][:5])
    plt.title('User-Job Similarity Heatmap')
    plt.savefig('../models/similarity_heatmap.png')
    plt.show()

if __name__ == "__main__":
    import joblib
    from data_loader import load_jobs, load_users
    from data_preprocessing import preprocess_jobs, preprocess_users
    from feature_extraction import extract_features, compute_similarity
    
    jobs = load_jobs()
    users = load_users()
    jobs = preprocess_jobs(jobs)
    users = preprocess_users(users)
    
    jobs_texts = jobs['processed_text'].tolist()
    users_texts = users['processed_skills'].tolist()
    
    jobs_tfidf, users_tfidf, _ = extract_features(jobs_texts, users_texts)
    similarity = compute_similarity(jobs_tfidf, users_tfidf)
    
    evaluate_recommendations(similarity, users, jobs)
    plot_similarity_heatmap(similarity, users, jobs)