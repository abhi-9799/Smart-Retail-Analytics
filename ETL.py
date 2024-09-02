import pandas as pd
import numpy as np
from sqlalchemy import create_engine

# Replace with your database credentials
db_username = 'your_username'
db_password = 'your_password'
db_host = 'localhost'
db_port = '3306'
db_name = 'retail_db'

# Create a database connection
engine = create_engine(f'mysql+pymysql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}')

# Example: Load sales data from a CSV file
sales_data = pd.read_csv('sales_data.csv')

# Clean and preprocess data
sales_data['Date'] = pd.to_datetime(sales_data['Date'])
sales_data.dropna(inplace=True)

# Load data into the database
sales_data.to_sql('sales', con=engine, if_exists='replace', index=False)

print("Data loaded successfully!")
