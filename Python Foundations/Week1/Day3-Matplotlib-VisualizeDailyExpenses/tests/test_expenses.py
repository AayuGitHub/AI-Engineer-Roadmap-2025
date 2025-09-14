import pandas as pd
from pathlib import Path


def test_processed_file_exits():
    assert Path("../data/processed/daily_expenses.csv").exists()


def test_processed_file_content():
    df = pd.read_csv("../data/processed/daily_expenses.csv")
    assert set(df.columns) == {"Date", "TotalExpenses"}
    assert not df.empty
    assert pd.api.types.is_datetime64_any_dtype(pd.to_datetime(df["Date"]))
    assert pd.api.types.is_float_dtype(
        df["TotalExpenses"]
    ) or pd.api.types.is_integer_dtype(df["TotalExpenses"])
    assert (df["TotalExpenses"] >= 0).all()


def test_plot_file_exists():
    assert Path("../data/processed/daily_expenses_plot.png").exists()


def test_plot_file_content():
    fig_path = Path("../data/processed/daily_expenses_plot.png")
    assert fig_path.stat().st_size > 0

    from PIL import Image

    try:
        img = Image.open(fig_path)
        img.verify()  # Verify that it is, in fact, an image
    except (IOError, SyntaxError) as e:
        assert False, f"File is not a valid image: {e}"


if __name__ == "__main__":
    test_processed_file_exits()
    test_processed_file_content()
    test_plot_file_exists()
    test_plot_file_content()
    print("All tests passed!")
