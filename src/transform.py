import pandas as pd


def clean_data(df):
    """
    Clean and transform the Police API data.
    """

    # Extract latitude
    df["latitude"] = df["location"].apply(
        lambda x: x.get("latitude") if isinstance(x, dict) else None
    )

    # Extract longitude
    df["longitude"] = df["location"].apply(
        lambda x: x.get("longitude") if isinstance(x, dict) else None
    )

    # Extract street name
    df["street_name"] = df["location"].apply(
        lambda x: x.get("street", {}).get("name") if isinstance(x, dict) else None
    )

    # Keep only useful columns
    df = df[
        [
            "id",
            "city",
            "category",
            "street_name",
            "latitude",
            "longitude",
            "month",
        ]
    ]

    # Remove duplicate records
    df = df.drop_duplicates()

    # Remove rows with missing coordinates
    df = df.dropna(subset=["latitude", "longitude"])

    # Standardise city names
    df["city"] = df["city"].str.title()

    print(f"Cleaned dataset contains {len(df)} records.")

    return df