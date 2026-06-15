import os
import pandas as pd
from utils.extract import scrape_collection_data


def test_extract():
    data = scrape_collection_data(
        "https://fashion-studio.dicoding.dev"
    )

    assert isinstance(data, list)

    df = pd.DataFrame(data)

    test_file = "tests/test_extract_output.csv"

    df.to_csv(
        test_file,
        index=False
    )

    assert os.path.exists(test_file)

    if os.path.exists(test_file):
        os.remove(test_file)