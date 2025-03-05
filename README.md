# Property Sales Data Pipeline

## Overview
This project is an ETL (Extract, Transform, Load) pipeline for generating and managing property sales data. It uses Python to create synthetic real estate transaction data, store it in a MySQL database, and provides a streamlined process for data generation and database management.

## Features
- Generate synthetic property sales data
- Create MySQL database and table schema
- Upsert data with handling for new, updated, and deleted records
- Shell script for easy pipeline execution

## Prerequisites
- Python 3.8+
- MySQL Server
- pip package manager

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/property-sales-pipeline.git
cd property-sales-pipeline
```

2. Create a virtual environment:
```bash
python -m venv myvenv
source myvenv/bin/activate  # On Windows use: myvenv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure Database
- Open `config.py`
- Update MySQL connection details:
  - `database`: Database name
  - `user`: MySQL username
  - `password`: MySQL password
  - `host`: Database host
  - `port`: Database port

## Environment Setup
Recommended: Use environment variables for sensitive credentials
- Create a `.env` file in the project root
- Add your database credentials:
```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_PORT=3306
```

## Running the Pipeline

### Using Shell Script
```bash
chmod +x run_pipeline.sh
./run_pipeline.sh
```

### Manual Execution
```bash
python scripts/generate_data.py
python scripts/create_db.py
python scripts/etl_pipeline.py
```

## Pipeline Steps
1. `generate_data.py`: Creates synthetic property sales data
   - Generates 50 random property records
   - Saves data to CSV in `data/` directory

2. `create_db.py`: Sets up MySQL database
   - Creates `property_db` database
   - Creates `property_sales` table

3. `etl_pipeline.py`: Loads data into MySQL
   - Reads generated CSV
   - Upserts data into `property_sales` table
   - Handles record updates and deletions

## Data Model
- `property_id`: Unique identifier
- `address`: Property street address
- `city`: City name
- `county`: County name
- `state`: State abbreviation
- `zipcode`: Postal code
- `sale_price`: Transaction price
- `sale_date`: Date of sale
- `buyer`: Buyer's name
- `seller`: Seller's name
- `status`: Record status (New/Updated/Deleted)

## Testing
Run tests using pytest:
```bash
pytest tests/
```

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
Distributed under the MIT License. See `LICENSE` for more information.

## Contact
Your Name - your.email@example.com

Project Link: [https://github.com/yourusername/property-sales-pipeline](https://github.com/yourusername/property-sales-pipeline)
