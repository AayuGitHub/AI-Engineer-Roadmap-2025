import pandas as pd

def test_processed_files_exists():
    df = pd.read_csv("../data/processed/houses_processed.csv")
    assert "Predicted" in df.columns
    assert "Actual" in df.columns
    assert not df["Predicted"].isnull().any()
    assert not df["Actual"].isnull().any()
    assert len(df) > 0
    assert df["Predicted"].dtype in [float, int]
    assert df["Actual"].dtype in [float, int]
    assert (df["Predicted"] >= 0).all()

def test_predictions_reasonable():
    df = pd.read_csv("../data/processed/houses_processed.csv")
    assert (df["Predicted"] > 0).all()