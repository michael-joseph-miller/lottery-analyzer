
import os

import pandas as pd
from dotenv import load_dotenv
from sodapy import Socrata

load_dotenv()  # Get environment variables from .env file


def getLotteryData(game_name: str, limit: int = 2500) -> pd.DataFrame:
    # Unauthenticated client only works with public data sets. Note 'None'
    # in place of application token, and no username or password:
    client = Socrata(os.environ['API_URL'], os.environ['API_TOKEN'])

    # First 2500 results, returned as JSON from API / converted to Python list of
    # dictionaries by sodapy.
    api_id = os.environ[f'{game_name.upper()}_API_ID']
    results = client.get(api_id, limit=limit)

    # Convert to pandas DataFrame
    results_df = pd.DataFrame.from_records(results)

    return results_df
