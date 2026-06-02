from utils.extract import scrape_collection_data


def test_extract():

    data = scrape_collection_data(
        "https://fashion-studio.dicoding.dev"
    )

    assert isinstance(data, list)
