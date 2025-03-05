import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config import DB_CONFIG
import pymysql

conn = pymysql.connect(
    host=DB_CONFIG["host"],
    user=DB_CONFIG["user"],
    password=DB_CONFIG["password"],
)

cur = conn.cursor()

cur.execute("CREATE DATABASE IF NOT EXISTS property_db;")
cur.execute("USE property_db;")

cur.execute("""
    CREATE TABLE IF NOT EXISTS property_sales (
        property_id VARCHAR(50) PRIMARY KEY,
        address TEXT,
        city VARCHAR(100),
        county VARCHAR(100),
        state VARCHAR(50),
        zipcode VARCHAR(10),
        sale_price DECIMAL(12,2),
        sale_date DATE,
        buyer TEXT,
        seller TEXT,
        status ENUM('New', 'Updated', 'Deleted')
    );
""")

conn.commit()
cur.close()
conn.close()

print("MySQL Database and table created successfully!")
