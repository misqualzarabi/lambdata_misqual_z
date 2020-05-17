import pandas as pd  # importing pandas library to create a dataframe
class NewFeature():
    def __init__(self, df):
        self.df = df

    def split_dates_col(self):
        col = 'date_time',
        name_cols = ['year', 'month', 'day']
        split_cols = self.df['date_time'].str.split(pat='-', n=3, expand=True)

        return self.df.assign(
            **dict(
                zip(name_cols, [split_cols.iloc[:, x]
                                for x in range(split_cols.shape[1])])
            )
        )

   
    
    


    


if __name__ == "__main__":

    # df with one column
    df = pd.DataFrame(
        {'date_time': ['2019-01-01', '2018-02-04', '2019-02-06', '2020-01-03']})

    new_feature = NewFeature(df)
    print(new_feature.df.head())

    # printing new dataframe addition to new columns along old ones
    print(new_feature.split_dates_col())