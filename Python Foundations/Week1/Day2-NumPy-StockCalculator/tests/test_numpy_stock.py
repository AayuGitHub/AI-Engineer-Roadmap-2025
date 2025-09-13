import pandas as pd


def test_value_and_allocation_exist():
    df = pd.read_csv("../data/Portfolio_Processed.csv")
    assert "value" in df.columns
    assert "allocation" in df.columns


def test_total_alloc_near_100():
    df = pd.read_csv("../data/Portfolio_Processed.csv")
    total_alloc = df["allocation"].sum()
    assert abs(total_alloc - 100) < 0.5
