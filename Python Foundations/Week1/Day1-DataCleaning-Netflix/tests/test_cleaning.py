import pandas as pd


def test_no_null_titles():
    df = pd.read_csv("../data/processed/netflix_clean.csv")
    assert df["title"].notnull().all()


def test_duration_parsed():
    df = pd.read_csv("../data/processed/netflix_clean.csv")
    # at least some durations parsed to ints
    assert df["duration_int"].dropna().shape[0] > 0
