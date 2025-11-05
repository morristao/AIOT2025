import os
import pandas as pd
from sklearn.model_selection import train_test_split

DATA_URL = "https://raw.githubusercontent.com/PacktPublishing/Hands-On-Artificial-Intelligence-for-Cybersecurity/refs/heads/master/Chapter03/datasets/sms_spam_no_header.csv"


def download_and_load(csv_path="data/sms_spam_no_header.csv", force=False):
    """Download the dataset if not present and return a DataFrame with columns ['label','text']"""
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    if not os.path.exists(csv_path) or force:
        df = pd.read_csv(DATA_URL, header=None, encoding='latin-1')
        df.to_csv(csv_path, index=False, header=False)
    df = pd.read_csv(csv_path, header=None, encoding='latin-1')
    df = df.iloc[:, :2]
    df.columns = ["label", "text"]
    return df


def train_test_split_df(df, test_size=0.2, random_state=42):
    X = df["text"]
    y = df["label"].map({"ham": 0, "spam": 1})
    return train_test_split(X, y, test_size=test_size, random_state=random_state)
