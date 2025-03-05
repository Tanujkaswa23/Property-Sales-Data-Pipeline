# Property Sales Data Pipeline

This project is a data pipeline that generates fake property sales data, creates a MySQL database, and loads the data into it. The pipeline consists of three main scripts:

1. **generate_data.py** - Generates fake property sales data and saves it as a CSV file.
2. **create_db.py** - Creates the MySQL database (`property_db`) and the required table (`property_sales`).
3. **etl_pipeline.py** - Loads the CSV data into MySQL using SQLAlchemy and performs an upsert operation.

## Installation

### 1. Clone the repository:
```bash
git clone https://github.com/yourusername/property_sales_pipeline.git
cd property_sales_pipeline
2. Create a Virtual Environment (Recommended):
bash
Copy
Edit
python -m venv myvenv
3. Activate the Virtual Environment:
Windows:
bash
Copy
Edit
myvenv\Scripts\activate
Mac/Linux:
bash
Copy
Edit
source myvenv/bin/activate
4. Install Dependencies:
bash
Copy
Edit
pip install -r requirements.txt
Configuration
Update the config.py file with your MySQL database credentials:

python
Copy
Edit
DB_CONFIG = {
    "database": "property_db",
    "user": "root",
    "password": "yourpassword",
    "host": "localhost",
    "port": "3306",
}
Usage
Run the pipeline using the shell script:

bash
Copy
Edit
bash run_pipeline.sh
Or manually execute each script:

bash
Copy
Edit
python scripts/generate_data.py
python scripts/create_db.py
python scripts/etl_pipeline.py
Project Structure
graphql
Copy
Edit
property_sales_pipeline/
│-- data/                   # Stores the generated CSV file
│-- scripts/
│   ├── generate_data.py    # Generates fake data
│   ├── create_db.py        # Creates the MySQL database and table
│   ├── etl_pipeline.py     # Loads data into MySQL
│-- config.py               # Database configuration
│-- requirements.txt        # Project dependencies
│-- run_pipeline.sh         # Shell script to run the pipeline
│-- README.md               # Project documentation
Troubleshooting
Common Issues & Fixes:
MySQL Database Not Found

Run python scripts/create_db.py manually and ensure the database property_db exists.
ModuleNotFoundError

Ensure dependencies are installed: pip install -r requirements.txt
Activate the virtual environment before running any script.
Permission Issues (Linux/Mac)

Use chmod +x run_pipeline.sh before executing.
