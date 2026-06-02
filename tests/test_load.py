import pandas as pd
import os

from utils.load import store_to_csv


def test_load():

    df = pd.DataFrame({
        "A": [1]
    })

    store_to_csv(df)

    assert os.path.exists(
        "products.csv"
    )
