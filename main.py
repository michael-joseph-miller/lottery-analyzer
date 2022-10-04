# %%
import os

from dotenv import load_dotenv

import FieldNumbers as fn
import lottery_analyzer_db as db
import lottery_data_api as api

load_dotenv()  # Get environment variables from .env file


def main():
    # db.updateDrawingsHistory(['powerball', 'mega_millions'])
    pb_field_nums_df = db.getFieldNumbers('powerball')
    # print(pb_field_nums_df)
    field_nums = fn.FieldNumbers(pb_field_nums_df)
    # print('num_drawings:', field_nums.num_drawings)
    # print('num_hits_df:\n', field_nums.num_hits_df)
    field_nums.num_hits_df.plot.bar(figsize=(12, 3))


if __name__ == '__main__':
    main()

# %%
