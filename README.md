# 🚔 UK Police Crime ETL Pipeline

## Project Overview

This project demonstrates a complete ETL (Extract, Transform, Load) pipeline using Python, MongoDB, AWS EC2 and Amazon S3.

The application downloads crime data from the UK Police API, cleans the data, stores it in MongoDB running on an AWS EC2 instance, exports it as a JSON file and finally uploads the JSON file to an Amazon S3 bucket.

---

# ETL Workflow

```
UK Police API
       │
       ▼
Extract Data
       │
       ▼
Transform (Clean Data)
       │
       ▼
Load into MongoDB (EC2)
       │
       ▼
Export to JSON
       │
       ▼
Upload to Amazon S3
```
<img width="2880" height="1704" alt="Screenshot 2026-07-13 233946" src="https://github.com/user-attachments/assets/a7f9bb9b-38a7-41e7-804b-eda486ddce74" />
# Running the ETL Pipeline

---

# Technologies Used

- Python
- Requests
- Pandas
- MongoDB
- PyMongo
- AWS EC2
- Amazon S3
- Boto3
- MongoDB Compass
- VS Code

---

# Project Structure

```
Police-ETL-Pipeline/

│
├── data/
│
├── exports/
│     └── police_crimes.json
│
├── src/
│     ├── extract.py
│     ├── transform.py
│     ├── mongodb.py
│     ├── crud.py
│     ├── export_json.py
│     └── upload_s3.py
│
├── tests/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Step 1 - Create the Project

Created a new project folder called

```
Police-ETL-Pipeline
```

Created the following folders

```
src
exports
data
tests
```

Created the following files

```
main.py
requirements.txt
README.md
.gitignore
```

---

# Step 2 - Create Virtual Environment

Created a virtual environment.

```
python -m venv .venv
```

Activated it.

PowerShell

```
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned

.\.venv\Scripts\Activate.ps1
```

---

# Step 3 - Install Packages

Installed the required Python libraries.

```
pip install pandas requests pymongo boto3 python-dotenv
```

Saved them.

```
pip freeze > requirements.txt
```

---

# Step 4 - Extract Data

Created

```
src/extract.py
```

Downloaded crime data from the UK Police API.

Data was collected from several major UK cities:

- Manchester
- London
- Birmingham
- Liverpool
- Leeds

Total records downloaded

```
9153
```

---

# Step 5 - Transform Data

Created

```
src/transform.py
```

The raw Police API contains many nested fields.

The data was cleaned by:

- Keeping only useful columns
- Removing unnecessary nested JSON
- Extracting street names
- Keeping latitude
- Keeping longitude
- Keeping city
- Keeping crime category
- Keeping month

Final columns

```
id
city
category
street_name
latitude
longitude
month
```

---

# Step 6 - Configure MongoDB

MongoDB was installed on an AWS EC2 Ubuntu instance.

MongoDB service was started.

Verified MongoDB was running using

```
sudo systemctl status mongod
```

Allowed my laptop to connect using Security Group rules.

Opened port

```
27017
```

Connected using MongoDB Compass.

---

# Step 7 - Connect Python to MongoDB

Created

```
src/mongodb.py
```

Connected Python to MongoDB.

Created database

```
police_etl
```

Created collection

```
crimes
```



---

# Step 8 - Load Data into MongoDB

Created

```
src/crud.py
```

Converted the cleaned dataframe into Python dictionaries.

Inserted all records into MongoDB.

```
9153 records inserted
```

Verified inside MongoDB Shell.

```
show dbs

use police_etl

show collections

db.crimes.countDocuments({})
```

Result

```
9153
```
<img width="2240" height="1704" alt="Screenshot 2026-07-13 234349" src="https://github.com/user-attachments/assets/4ba2457c-846c-4193-9e8e-fe74393fb3c1" />

---

# Step 9 - Export JSON

Created

```
src/export_json.py
```

Exported all MongoDB documents to

```
exports/police_crimes.json
```

Result

```
9153 records exported
```

---

# Step 10 - Upload to Amazon S3

Created

```
src/upload_s3.py
```

Used the AWS SDK (Boto3).

Uploaded

```
exports/police_crimes.json
```

to

```
Amazon S3 Bucket

se-data-with-ai-etl-project
```

Stored inside

```
alina/

police_crimes.json
```

Verified upload successfully inside AWS Console.

---
<img width="2877" height="1479" alt="Screenshot 2026-07-13 235145" src="https://github.com/user-attachments/assets/aff2d814-e444-4a0d-b1f4-65ce12fe83c7" />
# Final Output

The complete ETL pipeline works successfully.

```
Police API

↓

Extract

↓

Transform

↓

MongoDB (AWS EC2)

↓

JSON Export

↓

Amazon S3
```

---

# Example Output

```
Downloaded 9153 crime records.

↓

Cleaned dataset contains 9153 records.

↓

9153 records inserted into MongoDB.

↓

Exported 9153 records to JSON.

↓

JSON uploaded successfully to Amazon S3.
```

---

# Future Improvements

This project can be extended by adding:

- CRUD menu
- Logging
- Unit tests
- Scheduled ETL jobs
- AI semantic search
- Vector embeddings
- RAG chatbot
- Interactive dashboard
- Crime trend analysis
- Machine Learning predictions
