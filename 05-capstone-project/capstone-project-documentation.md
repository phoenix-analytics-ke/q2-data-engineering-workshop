#### Capstone Project

---

The capstone project will be a culmination of all the concepts learned through out this workshop. It will involve `data exctaction from APIs`, `data wrangling`, `dimensional modelling` , `ETL` ,and `workflow orchestration`. Upon successful completion of the project, you will be awarded a certificate indicating you have successfully completed the intended learning objectives for the workshop.

#### Overview

The project entails ingesting financial data and loading it to a cloud datawarehouse - Snowflake. 

The workflow for the capstone project is as follows:

- Data Sources - `polygon API`, `yfinance`

- Data Cleaning - `Pandas Dataframes`

- Data Warehouse - `Snowflake`

- Workflow Orchestration - `Mage AI`

#### Architecture Diagram

#### 



##### Extraction

The first stage is to extract `all reference tickers supported by Polygon API`. You can refer to the documentation from the website. 

Find the link below:

https://polygon.io/docs/stocks/get_v3_reference_tickers

The second stage will be to fetch the historical daily data from yfinance. One way of achieving this is to have the list of supported tickers from polygon API in a linear data structure like an array or a linked list. You will then use that to fetch the daily stock prices of the company. Ingest the data of the specified date range below.

Date Range : `31-12-2010` to `31-12-2020`, date format : dd-Mm-Yyyy

NOTE: Use the python wrapper called `yfinance` to get the daily stock price data.

Make sure you have it installed in your local working environment, if not you can do a pip install of the requirements.txt file in the capstone project folder.

OUTPUT: If your extraction stage is successful, you should have a dataframe with the `ohlcv` as the columns, and the stock prices for each company on each trading day as the columns.

#### Transformation

The data ingested from the sources is not cleaned, you are to use pandas to clean and wrangle the data accordingly before loading to your target system.

Additionally, you can use pandas to generate a dataframe which will serve as the date dimension. A sample of the date dimension can be found in the capstone project folder.

#### Data Modelling

Your data model is to have three tables - `fact table`, `date dimension`, and `companies dimension`. 

- The `date dimension` should have been sucessfully generated in the transformation phase and does not need any cleaning. The only modification to the date dimension is to select the primary key, you can use a surrogate key, or the date as the unique identifier.

- The `companies dimension` table was generated in the first step during the extraction phase. You need to select the primary key for this table.**NOTE** : You can add additional dimensions from yfinance, this is not mandatory.

- The `fact table` was also generated in the extraction phase. This is the data that contains the stock prices. You need to add the primary key for this table, as well as the foreign keys of the corresponding dimension tables

#### Loading

You are to create your fact and dimension tables in snowflake and then load your data into the datawarehouse.

#### Orchestration

Use  Mage AI to orchestrate your entire pipeline.

#### Evaluation Points

Implement best practices when writing your data pipeline.

- Modularlize your code.

- Document your code using docstrings and add comments where necessary

- Implement logging.

- Write robust code, using try and except blocks for error handling.
