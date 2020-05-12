

##Function to split dates ("MM/DD/YYYY", etc.) into multiple columns

import pandas as  pd # importing pandas library to create a dataframe

def split_dates_col(new_df):

    # TODO:selecting column  that i want to split
    ## then making a list with new column names
    ### using split method of pandas
    # it normally takes string and returns list
    # but assiging the TRUE to 'expand' instead of a list it returns us dataframe

    col='date_time',
    name_cols =['year','month','day']
    split_cols = new_df['date_time'].str.split(pat='-', n=3, expand=True)

    # unpacking dictionary with ' ** ' syntax while using assign method
    
    return new_df.assign(
        **dict(
            zip(name_cols, [split_cols.iloc[:, x]for x in range(split_cols.shape[1])])
        )
    )
    

if __name__ == "__main__":

    # df with one column
 df = pd.DataFrame({'date_time':['2019-01-01', '2018-02-04', '2019-02-06', '2020-01-03']})

 print(df.head())

 df2 = split_dates_col(df) # printing new dataframe addition to new columns along old ones
 print(df2.head())



