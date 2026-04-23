# Job Recommendation System

An AI-powered job recommendation system that matches users to jobs based on their skills. Features a simple machine learning model (cosine similarity), Prolog rule-based reasoning, and an interactive web dashboard.

## Features

- **Skill-Based Matching**: Enter your skills and get personalized job recommendations
- **Category Filtering**: Filter by job categories (Tech, Business, HR, etc.)
- **Interactive Dashboard**: Visualize job categories, match scores, and recommendations
- **Prolog Integration**: Rule-based reasoning for logical job matching
- **40+ Job Listings**: Comprehensive dataset across multiple industries

## Project Structure

- `data/`: Datasets (jobs.csv with 40+ jobs, users.csv)
- `src/`: Source code modules
  - `data_loader.py`: Load and preprocess datasets
  - `data_preprocessing.py`: Text cleaning and normalization
  - `feature_extraction.py`: Vectorize skills using CountVectorizer
  - `evaluation.py`: Evaluate recommendation accuracy
  - `model_training.py`: Simple similarity-based model
- `models/`: Saved model artifacts
- `app.py`: Streamlit web application with dashboard
- `job_recommendation.pl`: Prolog facts and rules for logical reasoning

## Quick Start

1. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Web App**:

   ```bash
   streamlit run app.py
   ```

3. **Explore Prolog Rules**:
   - Install SWI-Prolog
   - Load `job_recommendation.pl`
   - Query: `recommend(1, Job).`

## How It Works

### Machine Learning Model

- Uses CountVectorizer to create skill vectors
- Computes cosine similarity between user skills and job requirements
- Ranks jobs by match score (0-100%)
- Adds category bonus for preferred categories

### Prolog Rules

- Declarative facts for jobs and user skills
- Logical rules for skill-based recommendations
- Example: `recommend(User, Job) :- user_skill(User, Skill), job(Job, Skill).`

### Dashboard Features

- Skill input with comma-separated values
- Category dropdown (Any, Tech, Business, etc.)
- Interactive table of recommendations with match scores
- Bar chart of job categories in dataset
- Pie chart of top matching categories
- Dataset statistics and summary

## Dataset

- **Jobs**: 40+ job listings across 10+ categories
- **Users**: Sample user profiles with skills and preferences
- **Skills**: Common tech and business skills (Python, SQL, Marketing, etc.)

## Requirements

- Python 3.8+
- Streamlit
- Pandas
- Scikit-learn
- Plotly (for charts)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests and documentation
4. Submit a pull request

## License

MIT License - feel free to use and modify!
