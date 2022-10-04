import pandas as pd


class FieldNumbers():

    def __init__(self, fn_df: pd.DataFrame) -> None:
        self.num_drawings = fn_df.values.__len__()
        self.num_hits_df = self.__calcNumHits(fn_df)
        # self.num_freq_df = self.__calcNumFreq()

    def __calcNumHits(self, field_numbers_df: pd.DataFrame) -> pd.DataFrame:
        field_numbers_list = []
        # Split field number strings and add to field_numbers_list
        for row in field_numbers_df.iterrows():
            field_numbers_list.extend(row[1]['field_numbers'].split(' '))
        # Count number of hits for each field number
        num_hits_dict = {}
        for num in field_numbers_list:
            if num in num_hits_dict:
                num_hits_dict[num] += 1
            else:
                num_hits_dict[num] = 1
        # Convert to DataFrame, sort by index and return
        return pd.DataFrame.from_dict(
            num_hits_dict,
            orient='index',
            columns=['Num Hits']).sort_index()

    # def __calcNumFreq(self) -> pd.DataFrame:
