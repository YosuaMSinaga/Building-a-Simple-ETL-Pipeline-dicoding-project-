import pandas as pd

from utils.transform import (
    transform,
    transform_to_Dataframe
)


def test_transform():

    sample = [{
        "Title": "T-Shirt",
        "Price": "$10",
        "Rating": "4.5 / 5",
        "Colors": "3 Colors",
        "Size": "Size: M",
        "Gender": "Gender: Men",
        "timestamp": "2026"
    }]

    df = transform_to_Dataframe(sample)

    result = transform(df)

    assert result["Price"].iloc[0] == 160000
    assert result["Rating"].iloc[0] == 4.5
    assert result["Colors"].iloc[0] == 3
