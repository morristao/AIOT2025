import os
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_recall_fscore_support, accuracy_score
import joblib
import json


def build_pipeline():
    pipe = Pipeline([
        ("tfidf", TfidfVectorizer(max_features=5000)),
        ("clf", LogisticRegression(max_iter=1000))
    ])
    return pipe


def train(X_train, y_train):
    pipe = build_pipeline()
    pipe.fit(X_train, y_train)
    return pipe


def evaluate(pipe, X_test, y_test):
    preds = pipe.predict(X_test)
    probs = pipe.predict_proba(X_test)[:, 1] if hasattr(pipe, "predict_proba") else None
    p, r, f, _ = precision_recall_fscore_support(y_test, preds, average='binary', zero_division=0)
    acc = accuracy_score(y_test, preds)
    return {"precision": float(p), "recall": float(r), "f1": float(f), "accuracy": float(acc)}


def save_model(pipe, path="artifacts/spam_baseline.joblib"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    joblib.dump(pipe, path)
    return path


def load_model(path="artifacts/spam_baseline.joblib"):
    return joblib.load(path)


def predict(pipe, text):
    prob = float(pipe.predict_proba([text])[:, 1]) if hasattr(pipe, "predict_proba") else None
    label = int(pipe.predict([text])[0])
    return {"label": "spam" if label == 1 else "ham", "probability": prob}
