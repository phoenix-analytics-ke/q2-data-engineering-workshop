#loading the necessary libraries
import pandas as pd
import numpy as np
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s-%(levelname)s-%(message)s')

#function for loading data
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        logging.info("Successfully loaded")
        return data
    except Exception as e:
        logging.error(f"Unsuccessful: {e}")
        raise

#cleaning data
def clean_data(data):
    try:
        data = data.dropna()
        data = data.drop_duplicates()

        #conversion of columns
        data['id'] = data['id'].astype(int)
        data['wholesale'] = pd.to_numeric(data['wholesale'], errors='coerce')
        data['retail'] = pd.to_numeric(data['retail'], errors='coerce')
        data['supply_volume'] = pd.to_numeric(data['supply_volume'], errors='coerce')
        data['date'] = pd.to_datetime(data['date'], errors='coerce')

        logging.info("Data cleaned successfully")
        return data
    except Exception as e:
        logging.error(f"Unsuccessful clean: {e}")
        raise

#the main program
def main():
    file_path = "D:/pythonProject/Data Engineering Workshop/q2-data-engineering-workshop/04-data-warehousing/data/sample_agric_commodities.csv"
    data = load_data(file_path)
    cleaned_data = clean_data(data)
    cleaned_data.to_csv("D:/pythonProject/Data Engineering Workshop/q2-data-engineering-workshop/04-data-warehousing/data/cleaned_data.csv", index=False)
    logging.info("Cleaned data saved successfully")

if __name__ == "__main__":
    main()
