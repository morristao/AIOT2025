## ADDED Requirements

### Requirement: Spam classification capability
The system SHALL provide a `spam-classification` capability that can be trained on a labeled short-message dataset and used to classify incoming messages as `spam` or `ham`.

#### Scenario: Train baseline model
- **GIVEN** the baseline dataset is available at the configured URL and the training script is executed
- **WHEN** the training completes successfully
- **THEN** a model artifact (serialized classifier) and evaluation report (precision, recall, f1, accuracy) SHALL be produced and stored in the project's artifacts directory

#### Scenario: Inference for a single message
- **GIVEN** a serialized model artifact exists
- **WHEN** the inference CLI is invoked with a message text
- **THEN** the CLI SHALL return JSON containing `label` ("spam" or "ham") and `probability` (float between 0 and 1)

#### Scenario: Baseline evaluation reporting
- **GIVEN** the baseline evaluation script is executed on a hold-out test set
- **THEN** the script SHALL output a machine-readable report (JSON or CSV) with keys `precision`, `recall`, `f1`, `accuracy` and save it to `aiot_hw3/artifacts/` or `aiot_hw3/reports/` for review
