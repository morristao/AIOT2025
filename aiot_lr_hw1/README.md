# HW1: Linear Regression — Streamlit (CRISP‑DM)

> **Goal**: Write Python to solve a simple linear regression problem following **CRISP‑DM**.  
> Include **prompt** and **process**, allow users to modify `a` and `b` in `y = a·x + b`, noise, number of points, and deploy as a simple web app.

## 1) Prompt (老師需求 → 我方任務)
- 「做一個示範 `y = a·x + b + ϵ` 的線性回歸，並讓使用者可以調整 `a,b`、**noise**、**number of points**，同時呈現模型擬合結果與評估指標；以 **Streamlit** 部署；整份作業需依 **CRISP‑DM** 交付從需求到部署的流程。」

## 2) Process (CRISP‑DM)
### A. Business Understanding
- 學習目標：掌握線性回歸的基本概念（資料生成、最小平方法擬合、MSE/R² 評估），理解雜訊/離群值對模型的影響。
- 交付物：互動式網站（Streamlit）、可下載資料、報告說明。

### B. Data Understanding
- 以亂數產生 `x ~ U(x_min, x_max)`，`ϵ ~ N(0, σ)`，得到 `y = a·x + b + ϵ`。
- 透過散佈圖檢視線性關係；可選擇加入離群點觀察影響。

### C. Data Preparation
- 參數化資料產生器（`n_points`, `a`, `b`, `noise_std`, `x_range`）。
- 可選「加離群點」：隨機挑選一定比例樣本，拉大偏移量（`outlier_scale×σ`）。

### D. Modeling
- 採 **最小平方法**（`np.linalg.lstsq`）估計係數：  
  $$\min\_{a,b}\ \|Xa - y\|^2,\quad X=[x,\ 1]$$
- 亦可用 `numpy.polyfit` 或 `scikit-learn`；為避免額外依賴，這裡用 `numpy` 閉式解。

### E. Evaluation
- 指標：**MSE**, **R²**。
- 視覺化：資料散佈＋擬合直線；觀察噪音/離群點如何影響係數與評分。

### F. Deployment
- 以 Streamlit 製作互動網頁（側欄控制參數、主區顯示圖表/指標/資料表）。
- 可在 **Streamlit Community Cloud** 零設定部署：只要把本專案推上 GitHub 並在 Streamlit 連結該倉庫即可。

## 3) 專案結構
```
.
├── app.py              # Streamlit 主程式
├── README.md           # 本說明
└── requirements.txt    # 依賴（streamlit、numpy、matplotlib、pandas）
```

## 4) 本地執行
```bash
# 建議使用 Python 3.10+
pip install -r requirements.txt
streamlit run app.py
```

## 5) 部署（Streamlit Community Cloud）
1. 建一個 GitHub repo，加入本三個檔案。
2. 進入 [share.streamlit.io](https://share.streamlit.io) 連結 GitHub。
3. 選 `app.py` 為主檔；第一次部署約 1–2 分鐘完成。
4. 推上新 commit 即自動重新部署。

## 6) 評分重點對應
- ✅ **CRISP‑DM**：README 逐步呈現。
- ✅ **可互動**：側欄參數 `a, b, noise, n_points, x_range, outliers`。
- ✅ **結果與說明**：顯示方程、MSE、R²、散佈圖、資料表、可下載 CSV/JSON。
- ✅ **部署**：與 Streamlit/Flask 二選一，本案採 Streamlit。

---

若需 Flask 版本或加入殘差圖、置信區間、正規化等擴充，可在 `Issues` 提出。  
作者：陶亮清（7113056099）
