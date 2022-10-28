"""Lottery data API to fetch data from NY Lottery database"""

from request import request  # import our request function.


async def get_lottery_data(game_name: str, start_date: str, limit: int = 2500):
    """Gets lottery data from NY Lottery database"""

    # Api database id
    if game_name == 'Powerball':
        api_id = 'd6yy-54nr'
    elif game_name == 'Mega Millions':
        api_id = '5xaw-6ayf'
    else:
        return    
    
    # Query strings
    limit_query = f'$limit={limit}'
    date_query = f'$where=draw_date >= "{start_date}"'
    # Request url
    url = f'https://data.ny.gov/resource/{api_id}.json?{limit_query}&{date_query}'
    
    # GET
    headers = {"Content-type": "application/json"}
    response = await request(url, method="GET", headers=headers)

    return response
