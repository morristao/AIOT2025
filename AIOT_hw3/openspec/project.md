# Project Context

## Purpose
This subproject implements a lightweight spam (SMS/email) classification capability. The goal is to provide a reproducible baseline for short-message spam detection using classical ML (logistic regression), with training, evaluation, and a small inference CLI. Outputs (models and evaluation reports) are stored under `aiot_hw3/artifacts/`.

## Tech Stack
- Python 3.10+ (3.10/3.11 recommended)
- pandas, numpy
- scikit-learn (modeling & pipeline)
- nltk (optional preprocessing)
- joblib (model artifact serialization)
- streamlit (optional UI in `streamlit_app.py`)

## Project Conventions

### Code Style
- Follow PEP8 where practical. Use black/flake8 in CI if added later.
- Python modules live under `aiot_hw3/src/` and package namespace `spamclf`.

### Architecture Patterns
- Simple single-repo, single-package layout for experiments.
- Pipeline pattern: data loader -> preprocessing -> training -> evaluation -> inference.

### Testing Strategy
- Start with minimal unit tests for data loading and inference behavior.
- Keep tests fast and deterministic (use small fixtures or subset of data).

### Git Workflow
- Use feature branches `feature/<short-desc>` and PRs to `main`.

## Domain Context
- Input data are short text messages labeled `ham` or `spam`.
- Preprocessing uses TF-IDF features for the baseline; future phases may add embeddings.

## Important Constraints
- No PII exfiltration. Data used for training is the public Packt dataset referenced in the spec.
- Model artifacts are small and stored in `aiot_hw3/artifacts/`.

## External Dependencies
- Baseline dataset URL: https://raw.githubusercontent.com/PacktPublishing/Hands-On-Artificial-Intelligence-for-Cybersecurity/refs/heads/master/Chapter03/datasets/sms_spam_no_header.csv
- No external APIs required for Phase 1.

## Source & References
- Source code and inspiration: Packt — "Hands-On Artificial Intelligence for Cybersecurity" Chapter 3 dataset and patterns
- Packt repo: https://github.com/PacktPublishing/Hands-On-Artificial-Intelligence-for-Cybersecurity.git

## Project Links
- GitHub repository (this project): https://github.com/huanchen1107/2025ML-spamEmail
- Demo site (Streamlit): https://2025spamemail.streamlit.app/
- Tutorial / walkthrough (optional reference): https://www.youtube.com/watch?v=ANjiJQQIBo0

## How to work with the AI assistant (quick)
- Use the Copilot prompts in `openspec/copilot_prompts.md` to populate context, create proposals, or ask for workflow guidance.
- When requesting a change, prefer the OpenSpec phrasing: choose a verb-led `change-id` (e.g., `add-spam-classification`) and ask to scaffold `proposal.md`, `tasks.md`, and spec deltas under `openspec/changes/`.

## Developer utilities
- Copilot prompts: `openspec/copilot_prompts.md`
