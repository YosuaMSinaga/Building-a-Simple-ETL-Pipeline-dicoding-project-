from sqlalchemy import create_engine, text
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build


def store_to_csv(df):
    try:
        df.to_csv("products.csv", index=False)
        print("CSV berhasil disimpan.")
    except Exception as e:
        print(f"Gagal menyimpan CSV: {e}")


def store_to_spreadsheet(df, spreadsheet_id):
    try:
        creds = Credentials.from_service_account_file(
            "google-sheets-api.json",
            scopes=["https://www.googleapis.com/auth/spreadsheets"]
        )

        service = build(
            "sheets",
            "v4",
            credentials=creds
        )

        values = [df.columns.tolist()] + df.astype(str).values.tolist()

        body = {
            "values": values
        }

        service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id,
            range="Sheet1!A1",
            valueInputOption="RAW",
            body=body
        ).execute()

        print("Spreadsheet berhasil diperbarui.")

    except Exception as e:
        print(f"Gagal ke Spreadsheet: {e}")


def create_database(
    db_user,
    db_password,
    db_host,
    db_port,
    db_name
):
    try:
        admin_url = (
            f"postgresql+psycopg2://"
            f"{db_user}:{db_password}"
            f"@{db_host}:{db_port}/postgres"
        )

        engine = create_engine(
            admin_url,
            isolation_level="AUTOCOMMIT"
        )

        with engine.connect() as conn:

            query_check = text(
                "SELECT 1 FROM pg_database "
                "WHERE datname = :db_name"
            )

            check_db = conn.execute(
                query_check,
                {"db_name": db_name}
            )

            if not check_db.scalar():

                query_create = text(
                    f'CREATE DATABASE "{db_name}"'
                )

                conn.execute(query_create)

                print(
                    f"Database '{db_name}' berhasil dibuat."
                )

            else:
                print(
                    f"Database '{db_name}' sudah ada."
                )

    except Exception as e:
        print(f"Gagal membuat database: {e}")


def store_to_postgre(df, db_url):
    try:
        engine = create_engine(db_url)

        df.to_sql(
            "products",
            engine,
            if_exists="replace",
            index=False
        )

        print("Data berhasil masuk ke PostgreSQL.")

    except Exception as e:
        print(f"Gagal ke PostgreSQL: {e}")