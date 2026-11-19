# Senior Data Engineer Technical Assignment

## 1. Project Overview

This project implements an ETL pipeline using Python and SQL to extract data from the JSONPlaceholder API, transform the data, and load it into a local SQLite database.

The pipeline processes user and post information from the following API endpoints:

- https://jsonplaceholder.typicode.com/users
- https://jsonplaceholder.typicode.com/posts

## 2. Technologies Used

- Python
- SQL
- SQLite
- REST API
- Requests library
- Pytest

## 3. Project Structure

## 3. Project Structure

```text
SeniorDataEngineerTechTaskSuvarna/
│
├── _evidence/
│   ├── evidence.txt
│   ├── unit_tests.png
│   ├── etl_execution.png
│   └── sql_results.png
│
├── etl_pipeline/
│   ├── api_client.py
│   ├── transform_data.py
│   ├── load_to_database.py
│   ├── main.py
│   ├── verify_database.py
│   ├── test_api.py
│   ├── test_transform.py
│   ├── test_load.py
│   └── requirements.txt
│
├── sql/
│   ├── analysis_queries.sql
│   ├── run_sql.py
│   ├── schema.sql
│   └── sql_answers.md
│
├── senior_data.db
├── README.md
└── .gitignore
```


*Adjust the structure if your actual database or files are stored in different folders.*

## 4. ETL Process

### Extract

- Connect to JSONPlaceholder API using Python Requests.
- Fetch all posts from the `/posts` endpoint.
- Fetch all users from the `/users` endpoint.
- Retrieve JSON responses and convert them into Python objects.

### Transform

- Calculate the length of each post body.
- Add a status field:
  - If body length is greater than 150 characters, status is `lengthy`.
  - Otherwise, status is `concise`.
- Preserve the original post data.

### Load

- Use SQLite as the local database.
- Create two tables:
  - `KS_users`
  - `KS_posts`
- Insert user and post records into their respective tables.
- Maintain the relationship between posts and users using `userId`.

## 5. Database Details

Database name: `senior_data.db`

Tables:

**KS_users**
- id
- name
- username
- email
- city
- zipcode
- company_name

**KS_posts**
- id
- userId
- title
- body
- status

## 6. Execution Instructions

### Prerequisites

- Python 3
- pip

### Setup

Create a virtual environment:

```bash
python -m venv venv
```

Activate on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r etl_pipeline/requirements.txt
```

### Run the ETL pipeline

From the project root directory:

```bash
python etl_pipeline/main.py
```

### Verify database records

```bash
python etl_pipeline/verify_database.py
```

## 7. SQL Analysis

The SQL analysis is available in `sql/analysis_queries.sql`.

The assignment covers:

1. Top five users based on average post body length, excluding titles.
2. Average post length, including title and body, for those five users.
3. Weekday with the highest number of lengthy posts, using post IDs as day offsets from the UNIX epoch.

## 8. Data Validation

The database verification script checks:

- Total number of users and posts.
- Duplicate user and post IDs.
- Missing user names and email addresses.
- Posts without matching users.
- Lengthy and concise post counts.

## 9. Testing

Unit tests are included for the API extraction, transformation and database loading components.

Run tests using:

```bash
python -m pytest -v
```

## 10. Execution Results

The ETL pipeline was executed successfully during development.

Observed extraction and loading counts:

- Users fetched and loaded: 10
- Posts fetched and loaded: 100
- Lengthy posts: 62
- Concise posts: 38

## 11. Error Handling and Assumptions

- HTTP errors are checked using `raise_for_status()`.
- The pipeline uses SQLite for local data storage.
- Post status is calculated using the specified 150-character threshold.
- Post and user records are related using `posts.userId = users.id`.

## 12. Conclusion

This project demonstrates an end-to-end Python and SQL ETL pipeline, including API extraction, data transformation, SQLite loading, data validation and SQL analysis. 