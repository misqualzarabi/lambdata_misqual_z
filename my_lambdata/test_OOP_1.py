import pandas as pd
from my_lambdata.OOP_1 import NewFeature 
import unittest

class TestNewFeature(unittest.TestCase):

    def test_split_dates_col(self):
        df = pd.DataFrame(
        {'date_time': ['2019-01-01', '2018-02-04', '2019-02-06', '2020-01-03']})
        new_feature = NewFeature(df)
        self.assertEqual(list(new_feature.df.columns), ['date_time'])

        
        new_feature = new_feature.split_dates_col()
        self.assertEqual(list(new_feature.columns), ["date_time", "year", "month", "day"])

        self.assertEqual(new_feature.iloc[0] ["year"], "2019")



if __name__ == "__main__":
    unittest.main()


