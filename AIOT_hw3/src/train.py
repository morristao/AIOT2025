"""Train baseline logistic regression spam classifier"""
from spamclf.data import download_and_load, train_test_split_df
from spamclf.model import train, evaluate, save_model
import json


def main():
    df = download_and_load(csv_path="aiot_hw3/data/sms_spam_no_header.csv")
    X_train, X_test, y_train, y_test = train_test_split_df(df)
    pipe = train(X_train, y_train)
    metrics = evaluate(pipe, X_test, y_test)
    save_model(pipe, path="aiot_hw3/artifacts/spam_baseline.joblib")
    out = {"metrics": metrics}
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
