import requests
import pandas as pd
import time


def extract_data():
    """
    Download crime data from major UK cities using the UK Police API.
    """

    cities = [
        ("Manchester", 53.4808, -2.2426),
        ("London", 51.5074, -0.1278),
        ("Birmingham", 52.4862, -1.8904),
        ("Liverpool", 53.4084, -2.9916),
        ("Leeds", 53.8008, -1.5491)
    ]

    all_data = []

    headers = {
        "User-Agent": "Police-ETL-Pipeline/1.0"
    }

    for city, lat, lng in cities:

        print(f"Downloading {city}...")

        url = (
            f"https://data.police.uk/api/crimes-street/all-crime"
            f"?lat={lat}&lng={lng}"
        )

        try:
            response = requests.get(url, headers=headers, timeout=30)

            if response.status_code == 429:
                print("Rate limit reached. Waiting 10 seconds...")
                time.sleep(10)
                response = requests.get(url, headers=headers, timeout=30)

            response.raise_for_status()

            crimes = response.json()

            print(f"Found {len(crimes)} crimes in {city}")

            for crime in crimes:
                crime["city"] = city

            all_data.extend(crimes)

            # Wait before next request
            time.sleep(2)

        except Exception as e:
            print(f"Skipping {city}: {e}")

    df = pd.DataFrame(all_data)

    print("\n==============================")
    print(f"Downloaded {len(df)} total crime records.")
    print("==============================\n")

    return df