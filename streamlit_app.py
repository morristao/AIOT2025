"""Simple Streamlit demo for spam-classification baseline

This demo attempts to load the artifact `AIOT_hw3/artifacts/spam_baseline.joblib` and
provides an input box for live prediction. If the artifact is missing, the page shows
instructions to run `python AIOT_hw3/src/train.py` first.
"""
import json
import os
import streamlit as st

from joblib import load


ARTIFACT_PATH = "AIOT_hw3/artifacts/spam_baseline.joblib"
REPORT_PATH = "AIOT_hw3/artifacts/baseline_report.json"


@st.cache_resource
def load_model(path=ARTIFACT_PATH):
	if not os.path.exists(path):
		return None
	return load(path)


def load_report(path=REPORT_PATH):
	if not os.path.exists(path):
		return None
	with open(path, "r") as f:
		return json.load(f)


def main():
	st.title("Spam Classification — Demo")

	st.write("Enter a short message and click Predict. This demo uses the baseline logistic regression model.")

	pipe = load_model()
	report = load_report()

	if report:
		st.subheader("Baseline evaluation")
		st.json(report)

	if pipe is None:
		st.warning("Model artifact not found at `AIOT_hw3/artifacts/spam_baseline.joblib`. Run `python AIOT_hw3/src/train.py` to create it.")
		st.stop()

	text = st.text_area("Message text", value="Free entry in 2 a wkly comp to win FA Cup final tkts")
	if st.button("Predict"):
		try:
			prob = float(pipe.predict_proba([text])[:, 1]) if hasattr(pipe, "predict_proba") else None
			label = int(pipe.predict([text])[0])
			st.metric("Label", "spam" if label == 1 else "ham")
			if prob is not None:
				st.metric("Probability (spam)", f"{prob:.3f}")
		except Exception as e:
			st.error(f"Prediction failed: {e}")


if __name__ == "__main__":
	main()

