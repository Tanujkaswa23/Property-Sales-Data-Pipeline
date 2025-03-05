import pandas as pd
import sqlalchemy
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config import DB_CONFIG

db_url = f"mysql+pymysql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
engine = sqlalchemy.create_engine(db_url)

def upsert_data():
    df = pd.read_csv("data/property_sales_data.csv")

    df["sale_date"] = pd.to_datetime(df["sale_date"], errors="coerce")

    with engine.begin() as conn:
        sql = """
        INSERT INTO property_sales (property_id, address, city, county, state, zipcode, sale_price, sale_date, buyer, seller, status)
        VALUES (:property_id, :address, :city, :county, :state, :zipcode, :sale_price, :sale_date, :buyer, :seller, :status)
        ON DUPLICATE KEY UPDATE 
            sale_price = VALUES(sale_price), 
            sale_date = VALUES(sale_date),
            buyer = VALUES(buyer), 
            seller = VALUES(seller),
            status = VALUES(status);
        """
        
        conn.execute(sqlalchemy.text(sql), df.to_dict(orient="records"))

        conn.execute(sqlalchemy.text("""
            CREATE TEMPORARY TABLE temp_property_ids AS 
            SELECT DISTINCT property_id FROM property_sales;
        """))

        conn.execute(sqlalchemy.text("""
            UPDATE property_sales 
            SET status = 'Deleted' 
            WHERE property_id NOT IN (SELECT property_id FROM temp_property_ids);
        """))

        conn.execute(sqlalchemy.text("DROP TEMPORARY TABLE temp_property_ids;"))

    print("Data successfully upserted into MySQL.")

if __name__ == "__main__":
    upsert_data()
