"""Simple CLI to predict a single message"""
import argparse
import json
from spamclf.model import load_model, predict as model_predict


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("text", help="Message text to classify")
    args = parser.parse_args()
    pipe = load_model(path="aiot_hw3/artifacts/spam_baseline.joblib")
    out = model_predict(pipe, args.text)
    print(json.dumps(out))


if __name__ == "__main__":
    main()
