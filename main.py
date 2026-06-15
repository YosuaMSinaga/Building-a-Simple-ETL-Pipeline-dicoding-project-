import pandas as pd
from utils.extract import scrape_collection_data
from utils.transform import transform, transform_to_Dataframe
from utils.load import (
    store_to_postgre,
    create_database,
    store_to_csv,
    store_to_spreadsheet
)


def main():
    url = "https://fashion-studio.dicoding.dev"

    collection_data = scrape_collection_data(url)

    if not collection_data:
        print("Tidak ada data ditemukan")
        return

    products_df = transform_to_Dataframe(collection_data)
    products_df = transform(products_df)

    print(
        f"Total data setelah transformasi: "
        f"{len(products_df)}"
    )

    # Simpan ke CSV
    store_to_csv(products_df)

    # Simpan ke Google Spreadsheet
    spreadsheet_id = (
        "1fM5gTCmhkmEBY783m7FW4B1lWc7oSj3jQxvpDff8oyk"
    )

    store_to_spreadsheet(
        products_df,
        spreadsheet_id
    )

    # Konfigurasi PostgreSQL
    db_user = "postgres"
    db_password = "supersecretpassword"
    db_host = "localhost"
    db_port = "5433"

    # Nama database PostgreSQL
    db_name = "fashion_etl"

    db_url = (
        f"postgresql+psycopg2://"
        f"{db_user}:{db_password}"
        f"@{db_host}:{db_port}/{db_name}"
    )

    # Membuat database jika belum ada
    create_database(
        db_user,
        db_password,
        db_host,
        db_port,
        db_name
    )

    # Menyimpan data ke PostgreSQL
    store_to_postgre(
        products_df,
        db_url
    )

    print("ETL selesai")


if __name__ == "__main__":
    main()