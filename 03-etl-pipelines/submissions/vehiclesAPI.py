import requests
import pprint

def extract_vehicle_data(endpoint, search_param=None, format="json"):
    """Description:
    Ingest data from API endpoint
    Parameters:
        endpoint : API endpoint hosting data
        search_param : string to query endpoint e.g model name - "mercedes"
        format : data format for response - Options are json, csv, xml, defaults to json
    Returns:
        JSON data
    """
    params = {"format": format}

    if search_param is None:
        uri = f"https://vpic.nhtsa.dot.gov/api/vehicles/{endpoint}"
    else:
        uri = f"https://vpic.nhtsa.dot.gov/api/vehicles/{endpoint}/{search_param}"

    print(f"Extracting data from {uri}")

    try:
        res = requests.get(uri, params=params)
        res.raise_for_status()
        data = res.json()
    except Exception as e:
        print(f"Exception {e} occurred while extracting data from {uri}")
        data = {}

    return data

# Exercise 1 - Get all models for the make Toyota
toyota_models = extract_vehicle_data("getmodelsformake", "toyota")

# Print the result
pprint.pprint(toyota_models)

# Exercise 2 - Get all the manufacturer details for the model Ford
ford_manufacturer_details = extract_vehicle_data("getmanufacturerdetails", "ford")

# Print the result
pprint.pprint(ford_manufacturer_details)