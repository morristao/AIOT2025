def test_pipeline_predict():
    from spamclf.model import train, predict

    # tiny training data
    X = ["hello friend", "win money now", "free prize offer"]
    y = [0, 1, 1]

    pipe = train(X, y)
    out = predict(pipe, "free entry to win a prize")

    assert isinstance(out, dict)
    assert "label" in out and "probability" in out
    assert out["label"] in ("spam", "ham")
