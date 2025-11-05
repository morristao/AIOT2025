"""Evaluate saved model on test split and write report"""
from spamclf.data import download_and_load, train_test_split_df
from spamclf.model import load_model, evaluate
import json


def main():
    df = download_and_load(csv_path="AIOT_hw3/data/sms_spam_no_header.csv")
    X_train, X_test, y_train, y_test = train_test_split_df(df)
    pipe = load_model(path="AIOT_hw3/artifacts/spam_baseline.joblib")
    metrics = evaluate(pipe, X_test, y_test)
    with open("AIOT_hw3/artifacts/baseline_report.json", "w") as f:
        json.dump(metrics, f, indent=2)
    print(json.dumps(metrics, indent=2))


if __name__ == "__main__":
    main()
