

### Instructions

For the walmart ETL pipeline, you have been provided a notebook containing code to the ETL pipeline. 

Make the following modifications to the code

- rewrite the code in a static `.py` file instead of a notebook, the the file `walmart_ecommerce_etl.py`

- Implement best practices. Make the code robust by handling exceptions in each of the functions. Implement logging for observability.  Ensure you also document your code.

- Modify the load function to write data to a `duckdb` database. Load the `clean_data.csv` and `aggregated_data.csv` into seperate tables, in the same duckdb database.

- Orchestrate the entire process using `Prefect`.  NOTE : Check out the workflow orchestration section.


