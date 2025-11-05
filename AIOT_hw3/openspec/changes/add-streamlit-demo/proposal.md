# Change: add-streamlit-demo

## Why
Provide a simple interactive demo for the spam-classification baseline so stakeholders can try predictions without running local scripts. A Streamlit app simplifies sharing a live demo and helps validate model behavior on real inputs.

## What Changes
- Add a Streamlit demo page `aiot_hw3/streamlit_app.py` that loads the baseline model artifact and exposes a text input for live prediction.
- Add a small OpenSpec proposal and tasks to track implementation and testing.

## Impact
- Affected code: `aiot_hw3/streamlit_app.py`, `aiot_hw3/artifacts/` (reads `spam_baseline.joblib`), `aiot_hw3/requirements.txt` (streamlit already included)
- No breaking changes.

## Acceptance Criteria
- A Streamlit app can load the model artifact and show prediction label + probability for arbitrary text input.
- The app displays baseline metrics (if `aiot_hw3/artifacts/baseline_report.json` exists).

## References
- Project GitHub repo: https://github.com/huanchen1107/2025ML-spamEmail
- Demo site target: https://2025spamemail.streamlit.app/
