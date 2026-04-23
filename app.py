
import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Try to import matplotlib, use fallback if not available
try:
    import matplotlib.pyplot as plt
    import seaborn as sns
    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False

# Set page config
st.set_page_config(page_title="Job Recommendation System", page_icon="💼", layout="wide")

# Load data
@st.cache_data
def load_data():
    jobs_df = pd.read_csv('/home/abdulkerim/Documents/job_recommendation/data/jobs.csv')
    jobs_df['required_skills'] = jobs_df['required_skills'].str.lower().str.split(', ')
    jobs_df['skills_str'] = jobs_df['required_skills'].apply(lambda x: ' '.join(x))
    jobs_df['category'] = jobs_df['category'].str.title()
    return jobs_df

jobs_df = load_data()

# Preprocess
vectorizer = CountVectorizer()
job_vectors = vectorizer.fit_transform(jobs_df['skills_str'])

def recommend_jobs(user_skills, preferred_category='Any', top_n=5):
    skill_list = [skill.strip().lower() for skill in user_skills.split(',') if skill.strip()]
    if len(skill_list) == 0:
        return pd.DataFrame(columns=['job_title', 'description', 'category', 'match_score'])

    user_text = ' '.join(skill_list)
    user_vector = vectorizer.transform([user_text])
    similarities = cosine_similarity(user_vector, job_vectors).flatten()

    results = jobs_df.copy()
    results['match_score'] = (similarities * 100).round(1)
    if preferred_category != 'Any':
        results['category_bonus'] = (results['category'].str.lower() == preferred_category.lower()).astype(int) * 10
        results['match_score'] = results['match_score'] + results['category_bonus']
    else:
        results['category_bonus'] = 0

    results = results.sort_values(['match_score'], ascending=False)
    return results[results['match_score'] > 0][['job_title', 'description', 'category', 'match_score']].head(top_n)

# Sidebar
st.sidebar.title("💼 Job Recommendation Dashboard")
st.sidebar.markdown("---")

# Dataset stats in sidebar
st.sidebar.subheader("📊 Dataset Overview")
st.sidebar.metric("Total Jobs", len(jobs_df))
st.sidebar.metric("Categories", jobs_df['category'].nunique())

if MATPLOTLIB_AVAILABLE:
    # Category distribution
    category_counts = jobs_df['category'].value_counts()
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.pie(category_counts.values, labels=category_counts.index, autopct='%1.1f%%', startangle=90)
    ax.set_title("Job Categories Distribution")
    st.sidebar.pyplot(fig)
else:
    st.sidebar.info("📈 Charts will be available once matplotlib is installed")

# Main content
st.title("🎯 Job Recommendation System")
st.markdown("Enter your skills and get personalized job recommendations powered by AI!")

# Input section
col1, col2 = st.columns([2, 1])

with col1:
    skills_input = st.text_input(
        'Enter your skills (comma-separated)',
        'python, sql, machine learning',
        help="Example: python, sql, communication"
    )

with col2:
    category_options = ['Any'] + sorted(jobs_df['category'].unique().tolist())
    preferred_category = st.selectbox('Preferred Category', category_options)

# Recommend button
if st.button('🔍 Find My Perfect Jobs', type='primary'):
    with st.spinner('Analyzing your skills...'):
        recommendations = recommend_jobs(skills_input, preferred_category, top_n=10)

    if recommendations.empty:
        st.error('❌ No matching jobs found. Try adding more skills or selecting "Any" category.')
        st.info("💡 Tip: Include common skills like 'python', 'sql', 'communication', 'marketing'")
    else:
        st.success(f"✅ Found {len(recommendations)} job recommendations!")

        # Display recommendations
        st.subheader("🎉 Your Top Job Matches")

        # Create a nice table
        st.dataframe(
            recommendations.style.highlight_max(axis=0, subset=['match_score']),
            use_container_width=True
        )

        # Charts section
        if MATPLOTLIB_AVAILABLE:
            st.markdown("---")
            st.subheader("📈 Insights")

            col_chart1, col_chart2 = st.columns(2)

            with col_chart1:
                # Match score distribution
                fig, ax = plt.subplots(figsize=(8, 4))
                top_5 = recommendations.head(5)
                bars = ax.barh(top_5['job_title'], top_5['match_score'], color='skyblue')
                ax.set_xlabel('Match Score (%)')
                ax.set_title('Top 5 Match Scores')
                ax.set_xlim(0, 100)
                for bar, score in zip(bars, top_5['match_score']):
                    ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2, f'{score}%', va='center')
                st.pyplot(fig)

            with col_chart2:
                # Category breakdown of recommendations
                rec_category_counts = recommendations['category'].value_counts()
                fig, ax = plt.subplots(figsize=(6, 4))
                ax.pie(rec_category_counts.values, labels=rec_category_counts.index, autopct='%1.1f%%', startangle=90)
                ax.set_title("Recommended Jobs by Category")
                st.pyplot(fig)
        else:
            st.info("📊 Charts are not available. Install matplotlib to see visualizations.")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit, Scikit-learn" + (" and Matplotlib" if MATPLOTLIB_AVAILABLE else ""))
st.markdown("Dataset: 40+ jobs across multiple industries")
