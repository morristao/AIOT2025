## ADDED Requirements

### Requirement: Streamlit demo for spam-classification
The system SHALL provide a simple Streamlit demo page that allows a user to input a short message and receive a spam/ham prediction and probability.

#### Scenario: Local demo runs and predicts
- **GIVEN** the model artifact `aiot_hw3/artifacts/spam_baseline.joblib` exists
- **WHEN** the user runs `streamlit run aiot_hw3/streamlit_app.py`
- **THEN** the page SHALL render an input box and a Predict button and SHALL display `label` and `probability` for the entered message
