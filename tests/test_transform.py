import os
import pandas as pd

from utils.transform import (
    transform_to_Dataframe,
    transform
)


def test_transform_to_dataframe():
    sample_data = [
        {
            "Title": "T-Shirt",
            "Price": "$10",
            "Rating": "Rating: 4.5",
            "Colors": "3 Colors",
            "Size": "Size: M",
            "Gender": "Gender: Men"
        }
    ]

    df = transform_to_Dataframe(sample_data)

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 1


def test_transform():
    sample_data = [
        {
            "Title": "T-Shirt",
            "Price": "$10",
            "Rating": "Rating: 4.5",
            "Colors": "3 Colors",
            "Size": "Size: M",
            "Gender": "Gender: Men"
        }
    ]

    df = transform_to_Dataframe(sample_data)

    result = transform(df)

    assert not result.empty

    test_file = "tests/test_transform_output.csv"

    result.to_csv(
        test_file,
        index=False
    )

    assert os.path.exists(test_file)

    if os.path.exists(test_file):
        os.remove(test_file)