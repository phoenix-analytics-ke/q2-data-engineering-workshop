#loading the necessary libraries
import pandas as pd
import numpy as np
import logging
import snowflake.connector

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

#loading data inot snowflake
def load_to_snowflake(data, conn_params, table_name):
    try:
        #connection
        conn = snowflake.connector.connect(
            user=conn_params['user'],
            password=conn_params['password'],
            account=conn_params['account'],
            warehouse=conn_params['warehouse'],
            database=conn_params['database'],
            schema=conn_params['schema']
        )
        cur=conn.cursor()
        # Create a table if not exists
        create_table_query =""" 
        CREATE TABLE IF NOT EXISTS AGRIC_COMMODITIES (
            id INT,
            commodity STRING,
            grade STRING,
            sex STRING,
            market STRING,
            wholesale FLOAT,
            retail FLOAT,
            supply_volume FLOAT,
            county STRING,
            date DATE,
            PRIMARY KEY (id)
        );
        """
        cur.execute(create_table_query)

        # Insert data into the table
        for index, row in data.iterrows():
            insert_query = f"""
            INSERT INTO AGRIC_COMMODITIES (id, commodity, grade, sex, market, wholesale, retail, supply_volume, county, date) VALUES
            ({row['id']}, '{row['commodity']}', '{row['grade']}', '{row['sex']}', '{row['market']}', {row['wholesale']}, {row['retail']}, {row['supply_volume']}, '{row['county']}', '{row['date']}');
            """
            cur.execute(insert_query)

        conn.commit()
        cur.close()
        conn.close()
        logging.info("Data loaded to Snowflake successfully")
    except Exception as e:
        logging.error(f"Error loading data to Snowflake: {e}")
        raise

#the main program
def main():
    file_path = "D:/pythonProject/Data Engineering Workshop/q2-data-engineering-workshop/04-data-warehousing/data/sample_agric_commodities.csv"
    
    conn_params = {
        'user': 'Gichuru',
        'password': 'Kidsnextdoor01',
        'account': 'RGZGUTT.KA63834',
        'warehouse': 'COMPUTE_WH',
        'database': 'ETLTUTORIALS',
        'schema': 'PUBLIC'
    }
    table_name = 'AGRIC_COMMODITIES'

    data = load_data(file_path)
    cleaned_data = clean_data(data)
    cleaned_data.to_csv("D:/pythonProject/Data Engineering Workshop/q2-data-engineering-workshop/04-data-warehousing/data/cleaned_data.csv", index=False)
    logging.info("Cleaned data saved successfully")

if __name__ == "__main__":
    main()
