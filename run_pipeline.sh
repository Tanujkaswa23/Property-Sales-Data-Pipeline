source myvenv/Scripts/activate

python scripts/generate_data.py
python scripts/create_db.py
python scripts/etl_pipeline.py
