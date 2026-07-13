from src.extract import extract_data
from src.transform import clean_data
from src.crud import insert_data
from src.export_json import export_json
from src.upload_s3 import upload_to_s3

# Extract data from the Police API
df = extract_data()

# Clean and transform the data
clean_df = clean_data(df)

# Store the cleaned data in MongoDB
insert_data(clean_df)
export_json()
upload_to_s3()

# Show the first 5 cleaned records
print(clean_df.head())

print("\nDataset Information\n")
print(clean_df.info())