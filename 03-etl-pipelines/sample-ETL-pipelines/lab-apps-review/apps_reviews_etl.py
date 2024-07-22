import logging
import pandas as pd
import duckdb

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="app-review-etl.log",
)


def extract(file_path):
    """
    Description:
        This function extracts data from a CSV for the path passed in, and prints
        some basic information about the data that is extracted

    Parameters:
        file_path (str)

    Returns:
        pd.DataFrame
    """

    try:
        logging.info("Extraction in progress.........")
        data = pd.read_csv(file_path)

        logging.info(
            f"Here is a little bit of information about the data stored {file_path}:"
        )
        logging.info(
            f"\nThere are {data.shape[0]} rows and {data.shape[1]} columns in this DataFrame."
        )

    except FileNotFoundError:
        logging.exception(f"{file_path} does not exist")
    except Exception as e:
        logging.exception(f"Error {e} while extracting data from {file_path}")

    return data


def transform(apps, reviews, category, min_rating, min_reviews):
    """
    Description:
        Transform the apps and reviews data to only include reviews in the specified category,
        find the most common sentiment, and average sentiment polarity. Keep a subset of columns, and
        filter out less popular apps. Return the sorted DataFrame

    Parameters :
        apps(pandas.DataFrame)
        reviews(pd.DataFrame)
        category(str)
        min_rating(float)
        min_reviews(int)

    Returns:
        transformed (pd.DataFrame)
    """

    # Print statement for observability
    logging.info(
        f"Transforming data to curate a dataset with all {category} apps and their "
        f"corresponding reviews with a rating of at least {min_rating} and "
        f" {min_reviews} reviews\n"
    )

    # Drop any duplicates from both DataFrames (also have the option to do this in-place)
    apps = apps.drop_duplicates(["App"])
    reviews = reviews.drop_duplicates()

    # Find all of the apps and reviews in the food and drink category
    subset_apps = apps.loc[apps["Category"] == category, :]
    subset_reviews = reviews.loc[
        reviews["App"].isin(subset_apps["App"]), ["App", "Sentiment_Polarity"]
    ]

    # Aggregate the subset_reviews DataFrame
    aggregated_reviews = subset_reviews.groupby(by="App").mean()

    # Join it back to the subset_apps table
    joined_apps_reviews = subset_apps.join(aggregated_reviews, on="App", how="left")

    # Keep only the needed columns
    filtered_apps_reviews = joined_apps_reviews.loc[
        :, ["App", "Rating", "Reviews", "Installs", "Sentiment_Polarity"]
    ]

    # Convert reviews, keep only values with an average rating of at least 4 stars, and at least 1000 reviews
    filtered_apps_reviews = filtered_apps_reviews.astype({"Reviews": "int32"})
    top_apps = filtered_apps_reviews.loc[
        (filtered_apps_reviews["Rating"] > min_rating)
        & (filtered_apps_reviews["Reviews"] > min_reviews),
        :,
    ]

    # Sort the top apps, replace NaN with 0, reset the index
    top_apps.sort_values(by=["Rating", "Reviews"], ascending=False, inplace=True)
    top_apps.reset_index(drop=True, inplace=True)

    # Persist this DataFrame as .csv file
    top_apps.to_csv("top_apps.csv")
    print(
        f"The transformed DataFrame, which includes {top_apps.shape[0]} rows "
        f"and {top_apps.shape[1]} columns has been persisted, and will now be "
        f"returned"
    )

    logging.info("Transformation complete...................")

    # Return the transformed DataFrame
    return top_apps


def load(dataframe, database_name, table_name):
    """
    Description:
        Loads the DataFrame into a specified database and table.

    Parameters:
        dataframe (pd.DataFrame)
        database_name (str)
        table_name (str)

    Returns:
        pd.DataFrame
    """
    try:
        logging.info("Loading in progress...........")

    # Connect to the database
        con = duckdb.connect(database_name)

        # Write the DataFrame to the database
        dataframe.to_sql(table_name, con, if_exists="replace", index=False)

        # Validate the data was loaded correctly
        loaded_dataframe = con.execute(f"SELECT * FROM {table_name}").fetchdf()
        assert dataframe.shape == loaded_dataframe.shape
    
    except Exception as e:
        logging.exception("Error {e} while loading data")

    # Return the loaded DataFrame
    return loaded_dataframe


def run_pipeline():
    """
    Run the data pipeline
    """

    logging.info("Starting data pipeline...")
    # extract the data
    # NOTE - use OS module to get path, this is UGLY!!!
    apps_data = extract(
        "/home/c99/Desktop/data-projects/phx-etl-workshop/03-ETL-pipelines/lab-apps-review/data/apps_data.csv"
    )
    reviews_data = extract(
        "/home/c99/Desktop/data-projects/phx-etl-workshop/03-ETL-pipelines/lab-apps-review/data/review_data.csv"
    )

    # Transform the data
    top_apps_data = transform(
        apps=apps_data,
        reviews=reviews_data,
        category="FOOD_AND_DRINK",
        min_rating=4.0,
        min_reviews=1000,
    )

    # load the data
    loaded_apps_data = load(
        dataframe=top_apps_data, database_name="market_data.db", table_name="top_apps"
    )

    logging.info("Pipeline successful")


if __name__ == "__main__":
    run_pipeline()
