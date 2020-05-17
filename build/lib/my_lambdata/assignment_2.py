
# Single function to take a list, turn it into a series and add it to a dataframe as a new column

import pandas as pd

def add_new_col(new_col):
    
    #TODO:making a list to add into existing dataframe

    Class_list = ['a_levels', 'o_levels', 'a_levels', 'a_levels']

    # First converting that list into series

    column_values = pd.Series(Class_list)

     # using an insert function to add this into dataframe

    new_col.insert(loc=2, column='Class',value=column_values)
 

    return new_col





if __name__ == "__main__":

    # only run the code below if executing otherwise don't run it+

    data = {'Name':['Tom', 'nick', 'krish', 'jack'], 'Age':[20, 21, 19, 18]}
    
    df1 = pd.DataFrame(data)
    print(df1.head())

    df2 = add_new_col(df1)
    print(df2.head())