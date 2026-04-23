import pandas as pd

def load_jobs():
    """
    Load job dataset.
    """
    jobs_df = pd.read_csv('../data/jobs.csv')
    return jobs_df

def load_users():
    """
    Load user dataset.
    """
    users_df = pd.read_csv('../data/users.csv')
    return users_df

if __name__ == "__main__":
    jobs = load_jobs()
    users = load_users()
    print("Jobs shape:", jobs.shape)
    print("Users shape:", users.shape)
    print("Jobs sample:")
    print(jobs.head())
    print("Users sample:")
    print(users.head())