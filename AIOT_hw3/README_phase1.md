# Phase1 — Spam classification baseline

Quick start:

1. Create a virtual environment and install dependencies:

```zsh
python -m venv .venv
source .venv/bin/activate
pip install -r aiot_hw3/requirements.txt
```

2. Run training (this will download dataset, train logistic regression, save artifact):

```zsh
python aiot_hw3/src/train.py
```

3. Evaluate or run prediction:

```zsh
python aiot_hw3/src/evaluate.py
python aiot_hw3/src/predict.py "Free entry in 2 a wkly comp to win FA Cup final tkts"
```
