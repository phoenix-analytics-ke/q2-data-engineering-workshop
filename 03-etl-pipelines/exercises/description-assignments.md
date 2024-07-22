### Module 3 Assignments - ETL Pipelines

---

In the directory `phoenix-etl-workshop-q2 > 03-etl-pipelines >exercises`, you will find  the exercises in the folders.

- In the `clevelandart-api-exercise` , your ability to ingest data from APIs is tested. There is a `.py` in the folder with the instructions as docstrings. In your submission, write the code to ingest the relevant data as per the instructions.

- In the `car-accidents-supabase` assignment, you proficiency in ingesting data from databases is tested. In the folder, their is a text file called `supabase-credentials.txt` where you will find the necessary credentials. 
  
  The data hosted in the postgres instance is not cleaned, your task is to *write a pipeline that ingests data from the supabase instance, transform and aggregate the data, and load it into your supabase instance in a table called `aggregated-car-accidents`.

- In the `financial-data-exercise`  you are to pull the daily historical stock price for Microsoft since it went public up to July 12 2024. You can choose to use `yfinance` or `alphavantage website` as your data source. 

##### Deliverables

- `cleveland-api-exercise` -> a python file which outputs json format of the required output. Write clean and well documented functions. 

- `car-accidents-supabase` -> a `markdown file` or a `text file` that contains supabase credentials. These credentials will be used to ingest the aggregated data which is supposed to be hosted in your remote database. Also a `python` file containing the code for your data pipeline.

- `financial-data-exercise` -> `a python file` containing code from your data pipeline. 
  
  A `parquet` file that contains the historical daily financial data for Microsoft.

#### Additional resources

In the Google Drive link that hosts the ebooks, there is a folder called `datacamp-introduction-to-data-pipelines`.  Go through the first and second modules.