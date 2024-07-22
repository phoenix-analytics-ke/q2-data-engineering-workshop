# -*- coding: utf-8 -*-

import requests
import logging
import pandas as pd
import duckdb
import datetime

# configure the logger
logging.basicConfig(
    level=logging.INFO,
    filename="ETL_log.log",
    format="%(asctime)s %(levelname)s %(message)s",
)


def extract_ticker_daily(function: str = "TIME_SERIES_DAILY", ticker: str = "IBM"):
    """Extract daily time series(date, daily, open, high, low, volume)
      of the global equity specified

    Parameters:
        function : time series of your choice, defaults to TIME_SERIES_DAILY
        symbol : ticker symbol of equity of choice, defaults to IBM

    Returns:
        json data of the specified equity
    """
    ENDPOINT = "https://www.alphavantage.co/query"
    KEY = "08QEH6LPOHADA7VX"
    params = {
        "function": function,
        "symbol": ticker,
        "outputsize": "full",
        "apikey": KEY,
    }
    try:
        res = requests.get(ENDPOINT, params=params)
        logging.info(f"Extracting data from {ENDPOINT}......")
        data = res.json()
        logging.info(f"Successfully extracted data from {ENDPOINT}")
    except Exception as e:
        logging.error(f"Error {e} while fetching data from {ENDPOINT}")
        data = pd.DataFrame()

    return data


def transform(extracted_data):
    """Perform transformation on json file and load to a dataframe

    Parameters:
      data : input data in json format

    Output:
      df : pandas dataframe of transformed data

    """

    filtered_json = extract_ticker_daily()["Time Series (Daily)"]

    logging.info("Starting data transformation......")

    # Extract and store dates in an array
    dates_arr = []
    for dates in filtered_json.keys():
        dates_arr.append(dates)

    # Flatten the json file
    transformed = []
    for date in dates_arr:
        transformed.append(
            {
                "date": dates_arr,
                "open": filtered_json[date]["1. open"],
                "high": filtered_json[date]["2. high"],
                "low": filtered_json[date]["3. low"],
                "close": filtered_json[date]["4. close"],
            }
        )

    # load the data to a pandas dataframe
    df = pd.DataFrame(transformed)

    # convert date column from object to datatime
    df["date"] = pd.to_datetime(dates_arr)

    # set the datetime column as the index
    df = df.set_index("date")

    # cast all the columns as floats
    for col in df.columns:
        df[f"{col}"] = df[f"{col}"].astype(float)

    logging.info(
        f"Transformations complete, DataFrame has {df.shape[0]} rows, {df.shape[1]} columns"
    )

    return df


def load_to_sql(dataframe, db_name, table_name):
    """Load the cleaned dataframe into a duckdb database

    Parameters:
      dataframe : input dataframe
      db_name   : name of target database
      table_name : name of target table
    """

    logging.info(f"Loading {dataframe} into {db_name}")
    # connect to duckdb
    con = duckdb.connect(db_name)

    # write the dataframe to duckdb
    dataframe.to_sql(name=table_name, con=con, if_exists="replace", index="False")
    print(f"Data succesfully written to {db_name}")

    # read the data from sql
    loaded_df = pd.read_sql(f"SELECT * FROM {table_name}", con=con)

    logging.info(
        f"Load successful, dataframe has {loaded_df.shape[0]} rows and {loaded_df.shape[1]} columns"
    )


def load_to_csv(transformed_df, filename):
    """Load dataframe into a csv file

    Parameters:
      transformed_df : dataframe to be loaded to csv
      filename : name of the output csv
    """
    cur_date = datetime.datetime.now()
    formatted_date = cur_date.strftime("%Y-%m-%d")

    transformed_df.to_csv(f"{filename}_{formatted_date}.csv")


def load_to_parquet(transformed_df, filename):
    """Load dataframe into a parquet file

    Parameters:
      transformed_df : dataframe to be loaded to parquet file
      filename : name of output parquet file
    """
    cur_date = datetime.datetime.now()
    formatted_date = cur_date.strftime("%Y-%m-%d")

    transformed_df.to_parquet(f"{filename}_{formatted_date}")


def run_pipeline():
    """
    Run the data pipeline
    """

    extract_df = extract_ticker_daily("TIME_SERIES_DAILY", "IBM")
    transformed_df = transform(extract_df)
    load_to_csv(transformed_df, "IBM")
    load_to_sql(transformed_df, "IBM_data.db", "historical_data")

    print("ETL successful")


if __name__ == "__main__":
    run_pipeline()
