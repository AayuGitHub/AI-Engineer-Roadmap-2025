
# Day 3 — Matplotlib: Visualize Daily Expenses

**Raw file:** `data/raw/sales_data_sample.csv`
**Processed files:**

* `data/processed/daily_expenses.csv`
* `data/processed/daily_expenses_plot.png`

---

## 📌 What I did

1. Loaded **Sample Sales Data** from Kaggle.
2. Parsed `ORDERDATE` column into proper datetime format.
3. Aggregated sales by day → created **daily expenses dataset**.
4. Saved cleaned snapshot to `daily_expenses.csv`.
5. Built **line chart** to visualize expenses over time.
6. Built **bar chart** for last 10 days of expenses.
7. Exported final plot as `daily_expenses_plot.png`.

---

## Example Outputs

**Line Chart:**

* Shows daily total expenses across time.
* Useful for identifying peaks & dips.

**Bar Chart (last 10 days):**

* Clearer snapshot of short-term spending pattern.

---

## ✅ Next steps

* Add **moving averages** to smooth trends.
* Compare **daily expenses vs monthly/weekly totals**.
* Extend with anomaly detection (flag unusually high/low days).

---

## How to Run

```bash
# Activate environment
conda activate ai-roadmap

# Open notebook
jupyter notebook expenses_visualization.ipynb

# Run tests
pytest -q
```

---

## Deliverables

* Clean dataset → `daily_expenses.csv`
* Visualizations → `daily_expenses_plot.png`
* Notebook → `expenses_visualization.ipynb`
* Unit tests → `tests/test_expenses.py`

---