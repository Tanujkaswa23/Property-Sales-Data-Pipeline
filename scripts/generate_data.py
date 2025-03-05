import pandas as pd
import random
import os
from faker import Faker

fake = Faker()

output_dir = "c:/Users/tanuj/property_sales_pipeline/data"
os.makedirs(output_dir, exist_ok=True)  

csv_path = os.path.join(output_dir, "property_sales_data.csv")

SELECTED_COUNTY = "Kings County"
STATE_ABBR = "NY"

def generate_property_data(num_rows=50):
    data = []
    for _ in range(num_rows):
        property_id = fake.uuid4()[:8]
        address = fake.street_address()
        city = fake.city()
        county = SELECTED_COUNTY
        state = STATE_ABBR
        zipcode = fake.zipcode()
        sale_price = round(random.uniform(50000, 1000000), 2)
        sale_date = fake.date_between(start_date="-2y", end_date="today")
        buyer = fake.name()
        seller = fake.name()
        status = random.choice(["New", "Updated", "Deleted"])

        data.append([property_id, address, city, county, state, zipcode, sale_price, sale_date, buyer, seller, status])

    df = pd.DataFrame(data, columns=["property_id", "address", "city", "county", "state", "zipcode", "sale_price", "sale_date", "buyer", "seller", "status"])

    df.to_csv(csv_path, index=False)

    print(f"Fake property sales data (for {SELECTED_COUNTY}, {STATE_ABBR}) saved to: {csv_path}")

if __name__ == "__main__":
    generate_property_data()
