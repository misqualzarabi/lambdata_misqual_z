
import pandas as pd

class AddList():
    def __init__(self, df1):
        self.df1 = df1

    def add_new_col(self):
        Class_list = ['a_levels', 'o_levels', 'a_levels', 'a_levels']
        column_values = pd.Series(Class_list)
        self.df1.insert(loc=2, column='Class',value=column_values)
        return self.df1

    






if __name__ == "__main__":

    # only run the code below if executing otherwise don't run it+

    data = {'Name':['Tom', 'nick', 'krish', 'jack'], 'Age':[20, 21, 19, 18]}
    
    df1 = pd.DataFrame(data)
    print(df1.head())

    list_data = AddList(df1)
    print(list_data.df1.head())

    print(list_data.add_new_col())