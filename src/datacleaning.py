import pandas as pd

from .dataloading import Data

obj = Data()
df = obj.loader(r'artifacts\Train.csv')

class Cleaner:
    def __init__(self):
        pass

    def clean(df = df):
        print(df.shape)
        x = df.drop('Item_Outlet_Sales', axis = 1)
        y=df['Item_Outlet_Sales']
        df = df.drop_duplicates()
        df = df.drop.na()
        print(df.shape)
        return df 
        x.drop(['Item_Identifier', 'Outlet_Identifier'], axis=1, inplace=True)
        return x,y


c = Cleaner()
c.clean()