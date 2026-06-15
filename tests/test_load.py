import pandas as pd
from unittest.mock import MagicMock, patch

from utils.load import (
    store_to_csv,
    store_to_spreadsheet,
    create_database,
    store_to_postgre
)


def test_store_to_csv():
    df = pd.DataFrame({
        "name": ["Laptop"],
        "price": [10000]
    })

    with patch.object(df, "to_csv") as mock_to_csv:
        store_to_csv(df)

        mock_to_csv.assert_called_once_with(
            "products.csv",
            index=False
        )


@patch("utils.load.build")
@patch("utils.load.Credentials")
def test_store_to_spreadsheet(
    mock_credentials,
    mock_build
):
    df = pd.DataFrame({
        "name": ["Laptop"],
        "price": [10000]
    })

    mock_creds = MagicMock()
    mock_credentials.from_service_account_file.return_value = mock_creds

    mock_service = MagicMock()
    mock_build.return_value = mock_service

    store_to_spreadsheet(
        df,
        "spreadsheet_id"
    )

    mock_credentials.from_service_account_file.assert_called_once_with(
        "google-sheets-api.json",
        scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )

    mock_build.assert_called_once_with(
        "sheets",
        "v4",
        credentials=mock_creds
    )

    mock_service.spreadsheets.return_value.values.return_value.update.assert_called_once()


@patch("utils.load.create_engine")
def test_create_database_if_not_exists(
    mock_create_engine
):
    mock_conn = MagicMock()
    mock_engine = MagicMock()

    mock_engine.connect.return_value.__enter__.return_value = mock_conn
    mock_create_engine.return_value = mock_engine

    mock_result = MagicMock()
    mock_result.scalar.return_value = False

    mock_conn.execute.return_value = mock_result

    create_database(
        "postgres",
        "password",
        "localhost",
        "5432",
        "testdb"
    )

    assert mock_conn.execute.call_count == 2


@patch("utils.load.create_engine")
def test_create_database_if_exists(
    mock_create_engine
):
    mock_conn = MagicMock()
    mock_engine = MagicMock()

    mock_engine.connect.return_value.__enter__.return_value = mock_conn
    mock_create_engine.return_value = mock_engine

    mock_result = MagicMock()
    mock_result.scalar.return_value = True

    mock_conn.execute.return_value = mock_result

    create_database(
        "postgres",
        "password",
        "localhost",
        "5432",
        "testdb"
    )

    assert mock_conn.execute.call_count == 1


@patch("utils.load.create_engine")
def test_store_to_postgre(
    mock_create_engine
):
    df = pd.DataFrame({
        "name": ["Laptop"],
        "price": [10000]
    })

    mock_engine = MagicMock()
    mock_create_engine.return_value = mock_engine

    with patch.object(df, "to_sql") as mock_to_sql:

        store_to_postgre(
            df,
            "postgresql://user:password@localhost/testdb"
        )

        mock_create_engine.assert_called_once_with(
            "postgresql://user:password@localhost/testdb"
        )

        mock_to_sql.assert_called_once_with(
            "products",
            mock_engine,
            if_exists="replace",
            index=False
        )