# Change: add-spam-classification

## Why
Spam (unsolicited or malicious messages) harms user experience and can enable phishing or other attacks. We need a lightweight, testable capability to classify short messages (SMS / email) as spam vs. ham so downstream systems can filter or escalate suspicious messages.

## What Changes
- Add a new capability `spam-classification` that provides model training, evaluation, and inference for short-message spam detection.
- Add a baseline ML pipeline (data ingest, preprocessing, training, evaluation) using logistic regression as the first baseline model. An SVM variant may be evaluated as an alternative.
- Add a minimal inference endpoint (CLI/script) that returns label + probability for a given message.

**BREAKING:** none.

## Impact
- Affected specs: none existing; new capability `spam-classification` will be added under `openspec/changes/add-spam-classification/specs/spam/spec.md` (delta: ADDED Requirements).
- Affected code (suggested): `aiot_hw3/src/train.py`, `aiot_hw3/src/predict.py`, `aiot_hw3/src/evaluate.py`, `aiot_hw3/src/spamclf/` (new module), and top-level `requirements.txt` updates for scikit-learn, pandas.
- Data: baseline dataset will be fetched from: https://raw.githubusercontent.com/PacktPublishing/Hands-On-Artificial-Intelligence-for-Cybersecurity/refs/heads/master/Chapter03/datasets/sms_spam_no_header.csv

## References & Links
- Packt source dataset & patterns: https://github.com/PacktPublishing/Hands-On-Artificial-Intelligence-for-Cybersecurity.git (Chapter 3)
- Project GitHub repo: https://github.com/huanchen1107/2025ML-spamEmail
- Demo site (Streamlit): https://2025spamemail.streamlit.app/

## Acceptance Criteria
- A baseline model (logistic regression) is trained and a test evaluation report (precision, recall, f1, accuracy) is produced and checked in under `aiot_hw3/artifacts/` or `aiot_hw3/reports/`.
- An inference script `predict.py` accepts a text input and prints JSON with fields: `label` (spam/ham) and `probability` (float 0..1).

## Notes / Assumptions
- The user originally mentioned logistic regression; an earlier note mentioned SVM. This proposal uses logistic regression as the canonical baseline; SVM can be added as an experimental variant in a follow-up phase.
- The dataset above is a CSV of short messages. Preprocessing will include text normalization and TF-IDF or simple bag-of-words features.
