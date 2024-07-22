import pandas as pd
import logging
import duckdb

logging.basicConfig(level=logging.INFO, filename="e-commerce.log", format="%(asctime)s-%(levelname)s-%(message)s")


def extract_csv(path : str) -> pd.DataFrame:
    """Ingest data from a csv file
    
    Parameters:
        path : file path containing the csv file
    
    Returns:
    """
    try:
        logging.INFO("Starting data ingestion of {path}")
        df = pd.read_csv(path)
        logging.INFO("Data Ingestion successful")
    except FileNotFoundError as e:
        logging.error(f"File {path} is missing")
    except Exception as e:
        logging.error(f"Error {e}, while ingesting data")
        df = pd.DataFrame()

    return df

def clean_data(df: object) -> object:
    """
       ECommerce Transformation Function in Python with Error Handling
       :param df: pandas dataframe, extracted ecommerce data 1
       :output: pandas dataframe, transformed data
    """

    # drop duplicate rows
    df = df.drop_duplicates()

    # replace missing values in numeric columns with the mean
    df = df.fillna(df.mean(), inplace=True)

    # drop rows with any remaining null values
    df = df.dropna()

    return df

# transform data
def transform_data(orders_df: object, products_df: object, customers_df: object) -> object:
    """
       ECommerce Transformation Function in Python with Error Handling
       :param orders_df: pandas dataframe, extracted ecommerce data 1
       :param products_df: pandas dataframe, extracted ecommerce data 1
       :param customers_df: pandas dataframe, extracted ecommerce data 1
       :output: pandas dataframe, transformed data
    """

    # Merge the orders and products DataFrames
    product_orders_df = pd.merge(orders_df, products_df, on='product_id')

    # Calculate the total price for each order
    product_orders_df['total_price'] = product_orders_df['quantity'] * product_orders_df['price']

    # Merge the resulting DataFrame with the customers DataFrame
    ecommerce_df = pd.merge(product_orders_df, customers_df, on='customer_id')

    return ecommerce_df

def load_data(ecommerce_df : object):
    """Load transformed data into duckdb database
    
    Parameters:
        ecommerce_df :
    Return:
        None
    """
    duckdb.from_df(ecommerce_df, 'ecommerce')

