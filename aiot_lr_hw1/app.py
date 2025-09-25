import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="HW1: Linear Regression — CRISP‑DM Demo", layout="wide")

st.title("HW1: Linear Regression")
st.caption("CRISP‑DM demo • synthetic data y = a·x + b + noise • modify parameters and inspect the fit")

# --- Sidebar controls ---
with st.sidebar:
    st.header("Data generator")
    seed = st.number_input("Random seed", value=42, step=1)
    n_points = st.slider("Number of points", 10, 500, 60, 5)
    a_true = st.slider("True slope (a)", -5.0, 5.0, 2.0, 0.1)
    b_true = st.slider("True intercept (b)", -20.0, 20.0, 5.0, 0.5)
    x_min, x_max = st.slider("x range", -50.0, 50.0, (-10.0, 10.0), 0.5)
    noise_std = st.slider("Noise std. deviation", 0.0, 10.0, 2.0, 0.1)
    add_outliers = st.checkbox("Add outliers", value=False)
    outlier_frac = st.slider("Outlier fraction", 0.0, 0.5, 0.1, 0.05, disabled=not add_outliers)
    outlier_scale = st.slider("Outlier noise scale (×σ)", 1.0, 10.0, 6.0, 0.5, disabled=not add_outliers)

# --- Data generation ---
rng = np.random.default_rng(int(seed))
x = rng.uniform(x_min, x_max, int(n_points))
eps = rng.normal(0.0, noise_std, int(n_points))
y = a_true * x + b_true + eps

if add_outliers and outlier_frac > 0:
    m = int(np.floor(outlier_frac * n_points))
    if m > 0:
        idx = rng.choice(np.arange(n_points), size=m, replace=False)
        y[idx] += rng.normal(0, noise_std * outlier_scale, size=m)

# --- Fit a linear model (closed-form least squares) ---
X = np.vstack([x, np.ones_like(x)]).T  # [x, 1]
# Solve min ||Xa - y|| using lstsq
coef, *_ = np.linalg.lstsq(X, y, rcond=None)
a_hat, b_hat = coef[0], coef[1]

# Predictions and metrics
y_pred = a_hat * x + b_hat
mse = float(np.mean((y - y_pred) ** 2))
# R^2
ss_res = float(np.sum((y - y_pred) ** 2))
ss_tot = float(np.sum((y - np.mean(y)) ** 2))
r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else float("nan")

left, right = st.columns([2, 1], gap="large")

with left:
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.scatter(x, y, alpha=0.7, label="data")
    # Draw fitted line on full range
    xs = np.linspace(min(x_min, x.min()), max(x_max, x.max()), 200)
    ax.plot(xs, a_hat * xs + b_hat, label=f"fit: y = {a_hat:.3f}x + {b_hat:.3f}")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    ax.grid(True, alpha=0.3)
    st.pyplot(fig, clear_figure=True)

with right:
    st.subheader("Model & Metrics")
    st.markdown(
        f"""
**True function:** :blue[`y = {a_true:.3f}·x + {b_true:.3f} + ϵ`],  ϵ ~ 𝓝(0, {noise_std:.2f})  
**Fitted model:** :green[`y = {a_hat:.3f}·x + {b_hat:.3f}`]

- MSE: **{mse:.4f}**
- R²: **{r2:.4f}**
- Points: **{n_points}**
- Outliers: **{add_outliers}** (fraction **{outlier_frac:.2f}**)
"""
    )
    st.download_button(
        "Download parameters (JSON)",
        data=bytes(
            str(
                {
                    "seed": int(seed),
                    "n_points": int(n_points),
                    "a_true": float(a_true),
                    "b_true": float(b_true),
                    "x_min": float(x_min),
                    "x_max": float(x_max),
                    "noise_std": float(noise_std),
                    "add_outliers": bool(add_outliers),
                    "outlier_frac": float(outlier_frac),
                    "outlier_scale": float(outlier_scale),
                    "fit": {"a_hat": float(a_hat), "b_hat": float(b_hat), "mse": mse, "r2": r2},
                }
            ),
            "utf-8",
        ),
        file_name="params_and_fit.json",
        mime="application/json",
    )

    st.divider()
    # Data preview & CSV download
    import pandas as pd
    df = pd.DataFrame({"x": x, "y": y, "y_pred": y_pred})
    st.dataframe(df.head(20), use_container_width=True)
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("Download dataset (CSV)", data=csv, file_name="synthetic_linear_data.csv", mime="text/csv")

st.markdown("""---
### How this works (CRISP‑DM mapping)
- **Business Understanding** → simulate a simple regression task and let users explore data and noise
- **Data Understanding** → inspect scatter plot/table; adjust noise/outliers
- **Data Preparation** → generator builds `x`, `y` and optionally injects outliers
- **Modeling** → ordinary least squares using `np.linalg.lstsq`
- **Evaluation** → MSE and R² displayed; visual residuals via scatter vs. fitted line
- **Deployment** → this Streamlit app (can be hosted on Streamlit Community Cloud)
""")
