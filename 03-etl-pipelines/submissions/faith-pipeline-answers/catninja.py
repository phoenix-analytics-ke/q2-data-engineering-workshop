import requests
import logging

# Create a logger
logger = logging.getLogger('cat_ninjas_logger')
logger.setLevel(logging.INFO)

# Create a file handler to log messages to a file
file_handler = logging.FileHandler('cat_ninjas_log.log')

# Create a formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Add the formatter to the handler
file_handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(file_handler)

def extract_cat_breeds(api_url):
    """Extracts cat breeds from the given API endpoint."""
    logger.info(f"Extracting data from {api_url}")
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()
        logger.info("Data extraction successful")
        return data
    except Exception as e:
        logger.error(f"Exception {e} occurred while extracting data")
        return None
if __name__ == "__main__":
    breeds_api_url = "https://catfact.ninja/breeds"
    cat_breeds_data = extract_cat_breeds(breeds_api_url)
    
    if cat_breeds_data:
        print(cat_breeds_data)
def extract_random_cat_fact(api_url):
    """Extracts a random cat fact from the given API endpoint."""
    logger.info(f"Extracting random cat fact from {api_url}")
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()
        logger.info("Random cat fact extraction successful")
        return data
    except Exception as e:
        logger.error(f"Exception {e} occurred while extracting random cat fact")
        return None

if __name__ == "__main__":
    fact_api_url = "https://catfact.ninja/fact"
    random_cat_fact = extract_random_cat_fact(fact_api_url)
    
    if random_cat_fact:
        print(random_cat_fact)
