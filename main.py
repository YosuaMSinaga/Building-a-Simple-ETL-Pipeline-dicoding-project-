import pandas as pd
from utils.extract import scrape_collection_data
from utils.transform import transform, transform_to_Dataframe
from utils.load import store_to_postgre, create_database, store_to_csv, store_to_spreadsheet

def main():
    url = "https://fashion-studio.dicoding.dev"
    collection_data = scrape_collection_data(url)

    if not collection_data:
        print("Tidak ada data ditemukan")
        return

    products_df = transform_to_Dataframe(collection_data)
    products_df = transform(products_df)

    print(f"Total data setelah transformasi: {len(products_df)}")

    store_to_csv(products_df)

    spreadsheet_id = "[MASUKKAN_SPREADSHEET_ID_ANDA]"
    store_to_spreadsheet(products_df, spreadsheet_id)

    db_user = "developer"        
    db_password = "supersecretpassword"    
    db_host = "localhost"
    db_port = "5433" #<-- Sesuaikan dengan port PostgreSQL Anda
    db_name = "fashion_etl"#<-- Sesuaikan dengan nama database yang Anda inginkan

    db_url = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

    create_database(db_name) 
    store_to_postgre(products_df, db_url)

    print("ETL selesai")

if __name__ == "__main__":
    main()