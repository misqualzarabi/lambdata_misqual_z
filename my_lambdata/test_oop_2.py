
import pandas as pd
import unittest
from my_lambdata.OOP_2 import AddList


class TestAddList(unittest.TestCase):
    def test_add_new_col(self):
        data = {'Name':['Tom', 'nick', 'krish', 'jack'], 'Age':[20, 21, 19, 18]}
        df1 = pd.DataFrame(data)
        list_data = AddList(df1)

        self.assertEqual(list(list_data.df1.columns), ['Name', 'Age'])

        list_data = list_data.add_new_col()
        self.assertEqual(list(list_data.columns), ['Name', 'Age', 'Class'])

if __name__ == "__main__":
    unittest.main()
    
    


