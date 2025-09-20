import pandas as pd

def test_processed_file_exists():
    df = pd.read_csv("../data/processed/houses_processed.csv")
    assert "Predicted" in df.columns
    assert "Actual" in df.columns

def test_predictions_reasonable():
    df = pd.read_csv("../data/processed/houses_processed.csv")
    assert df["Predicted"].mean() > 50000  # sanity check
    assert df["Predicted"].mean() < 1e7