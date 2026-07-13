from src.mongodb import collection

def insert_data(df):

    records = df.to_dict("records")

    collection.delete_many({})

    collection.insert_many(records)

    print(f"{len(records)} records inserted into MongoDB.")