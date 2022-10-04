import os
import sqlite3

import pandas as pd
from dotenv import load_dotenv

import lottery_data_api as api

load_dotenv()


def formatGameData(game_data_df: pd.DataFrame, game_name: str) -> pd.DataFrame:
    data_list = []

    for row in game_data_df.iterrows():
        draw_date = row[1]['draw_date']
        if game_name == 'mega_millions':
            field_numbers = row[1]['winning_numbers']
            bonus_ball = row[1]['mega_ball']
        elif game_name == 'powerball':
            field_numbers = row[1]['winning_numbers'][0:14]
            bonus_ball = row[1]['winning_numbers'][2:None:-1]
        multiplier = row[1]['multiplier']
        # Append row to data_list
        data_list.append({
            'draw_date': draw_date,
            'field_numbers': field_numbers,
            'bonus_ball': bonus_ball,
            'multiplier': multiplier})

    return pd.DataFrame(data=data_list)


def insertDrawingsHistory(game_data_df: pd.DataFrame, game_name: str) -> None:
    # Format game data for table
    formatted_df = formatGameData(game_data_df, game_name)

    # Connect to db and create cursor
    db_connection = sqlite3.connect(os.environ['DB_FILENAME'])

    num_inserted = formatted_df.to_sql(
        f'{game_name}_drawings',
        db_connection,
        if_exists='replace',
        index=False)

    if num_inserted is not None:
        print(f'{num_inserted} {game_name} rows inserted.')
        print(f'{game_name} database load complete.')
    else:
        print(f'{game_name} database did not update.')


def updateDrawingsHistory(games: list[str]) -> None:
    for game in games:
        # get lates draw date from db
        latest_drawing_date_in_db = getLatestDrawDate(game)

        # get latest draw date from data api
        latest_drawing_date = api.getLotteryData(
            game, 1)['draw_date'].values[0]

        # if latest draw date not in db update db
        if (latest_drawing_date_in_db != latest_drawing_date):
            data_df = api.getLotteryData(game)
            insertDrawingsHistory(data_df, game)
        else:
            print(f'{game} database is up to date.')


def getLatestDrawDate(game_name: str) -> str:
    # Connect to db
    db_connection = sqlite3.connect(os.environ['DB_FILENAME'])

    # Try to select table, if not exists return None
    try:
        result_df = pd.read_sql_query(
            f'SELECT MAX(draw_date) FROM {game_name}_drawings',
            db_connection)
    except BaseException:
        return None
    latest_date = result_df.to_numpy()[0][0]

    return latest_date


def getFieldNumbers(game_name: str) -> pd.DataFrame:
    # Create connection
    db_connection = sqlite3.connect(os.environ['DB_FILENAME'])

    # Get all field numbers
    field_numbers_df = pd.read_sql(
        f'SELECT field_numbers FROM {game_name}_drawings',
        db_connection)

    return field_numbers_df
