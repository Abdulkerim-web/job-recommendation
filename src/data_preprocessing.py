import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import pandas as pd

# Download required NLTK data
nltk.download('stopwords')
nltk.download('wordnet')

def preprocess_text(text):
    """
    Preprocess text: lowercase, remove punctuation, stopwords, lemmatize.
    """
    if pd.isna(text):
        return ""
    # Lowercase
    text = str(text).lower()
    # Remove punctuation and numbers
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)
    # Tokenize
    words = text.split()
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    # Lemmatize
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    return ' '.join(words)

def preprocess_jobs(jobs_df):
    """
    Combine job fields into processed text.
    """
    jobs_df['combined_text'] = jobs_df['job_title'] + ' ' + jobs_df['description'] + ' ' + jobs_df['required_skills']
    jobs_df['processed_text'] = jobs_df['combined_text'].apply(preprocess_text)
    return jobs_df

def preprocess_users(users_df):
    """
    Process user skills.
    """
    users_df['processed_skills'] = users_df['skills'].apply(preprocess_text)
    return users_df

if __name__ == "__main__":
    from data_loader import load_jobs, load_users
    jobs = load_jobs()
    users = load_users()
    jobs = preprocess_jobs(jobs)
    users = preprocess_users(users)
    print(jobs[['job_title', 'processed_text']].head())
    print(users[['user_id', 'processed_skills']].head())