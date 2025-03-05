# Property Sales Data Pipeline  

This project is a **data pipeline** that generates fake property sales data, creates a MySQL database, and loads the data into it. The pipeline consists of three main scripts:  

1. **`generate_data.py`** - Generates fake property sales data and saves it as a CSV file.  
2. **`create_db.py`** - Creates a MySQL database (`property_db`) and the required table (`property_sales`).  
3. **`etl_pipeline.py`** - Loads the CSV data into MySQL using SQLAlchemy and performs an **upsert operation** (insert or update existing records).  

---

## 📌 Features  

✅ Generates **realistic fake** property sales data using `Faker`.  
✅ Uses **MySQL** for database storage.  
✅ Implements **ETL (Extract, Transform, Load)** operations efficiently.  
✅ Supports **upsert operations** to update existing records.  
✅ Automates the entire pipeline with a **bash script**.  

---

## 📦 Installation  

### 1️ Clone the Repository  
```bash
  git clone https://github.com/yourusername/property_sales_pipeline.git
  cd property_sales_pipeline

### 2 Create a Virtual Environment (Recommended)

