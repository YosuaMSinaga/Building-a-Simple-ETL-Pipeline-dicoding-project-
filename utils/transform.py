import pandas as pd


def transform_to_Dataframe(data):
    return pd.DataFrame(data)


def transform(df):
    try:

        df = df.copy()

        df.drop_duplicates(inplace=True)

        df.dropna(inplace=True)

        df = df[
            df["Title"] != "Unknown Product"
        ]

        df = df[
            df["Price"] != "Price Unavailable"
        ]

        df["Price"] = (
            df["Price"]
            .str.replace("$", "", regex=False)
            .astype(float)
            * 16000
        )

        df["Rating"] = (
            df["Rating"]
            .str.extract(r'(\d+\.\d+)')[0]
        )

        df = df[
            df["Rating"].notna()
        ]

        df["Rating"] = (
            df["Rating"]
            .astype(float)
        )

        df["Colors"] = (
            df["Colors"]
            .str.extract(r'(\d+)')[0]
            .astype(int)
        )

        df["Size"] = (
            df["Size"]
            .str.replace(
                "Size:",
                "",
                regex=False
            )
            .str.strip()
        )

        df["Gender"] = (
            df["Gender"]
            .str.replace(
                "Gender:",
                "",
                regex=False
            )
            .str.strip()
        )

        return df

    except Exception as e:
        print(f"Transform Error: {e}")
        return pd.DataFrame()