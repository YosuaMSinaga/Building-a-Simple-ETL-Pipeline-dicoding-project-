from sqlalchemy import create_engine, text
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build


def store_to_csv(df):

    try:
        df.to_csv(
            "products.csv",
            index=False
        )

        print("CSV berhasil")

    except Exception as e:
        print(e)


def store_to_spreadsheet(
        df,
        spreadsheet_id
):

    try:

        creds = Credentials.from_service_account_file(
            "google-sheets-api.json",
            scopes=[
                "https://www.googleapis.com/auth/spreadsheets"
            ]
        )

        service = build(
            "sheets",
            "v4",
            credentials=creds
        )

        values = [
            df.columns.tolist()
        ] + df.astype(str).values.tolist()

        body = {
            "values": values
        }

        service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id,
            range="Sheet1!A1",
            valueInputOption="RAW",
            body=body
        ).execute()

        print("Spreadsheet berhasil")

    except Exception as e:
        print(e)


def create_database(db_name):

    try:

        engine = create_engine(
            "postgresql+psycopg2://developer:supersecretpassword@localhost/postgres"
        )

        with engine.connect() as conn:

            conn.execute(
                text(
                    f"commit; create database {db_name}"
                )
            )

        print("Database dibuat")

    except Exception:
        print("Database sudah ada")


def store_to_postgre(
        df,
        db_url
):

    try:

        engine = create_engine(db_url)

        df.to_sql(
            "products",
            engine,
            if_exists="replace",
            index=False
        )

        print("PostgreSQL berhasil")

    except Exception as e:
        print(e)